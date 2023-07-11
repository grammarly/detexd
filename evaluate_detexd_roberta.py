from transformers import pipeline
from datasets import load_dataset
from sklearn.metrics import precision_recall_fscore_support
from tqdm.auto import tqdm
from transformers.pipelines.pt_utils import KeyDataset


BINARY_THRESHOLD = 0.72496545


def predict_binary_scores(classifier, texts):
    # get multiclass probability scores
    all_scores = tqdm(classifier(texts, top_k=None, truncation=True), total=len(texts))

    # convert to a single score by summing the probability scores
    # for the higher-index classes
    return [sum(score['score']
                for score in scores
                if score['label'] in ('LABEL_3', 'LABEL_4', 'LABEL_5'))
            for scores in all_scores]


def predict_delicate(classifier, texts, threshold=BINARY_THRESHOLD):
    return [result > threshold for result in predict_binary_scores(classifier, texts)]


if __name__ == '__main__':
    dataset = load_dataset("grammarly/detexd-benchmark", split='test')
    classifier = pipeline("text-classification", model="grammarly/detexd-roberta-base", device=0)
    predictions = predict_delicate(classifier, KeyDataset(dataset, 'text'))

    precision, recall, f_score, _ = precision_recall_fscore_support(y_true=dataset['label'], y_pred=predictions, average='binary')
    print(f'precision = {precision:.1%}')  # 81.4%
    print(f'recall = {recall:.1%}')  # 78.3%
    print(f'f_score = {f_score:.1%}')  # 79.8%

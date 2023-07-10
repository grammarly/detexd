# DeTexD: A Benchmark Dataset for Delicate Text Detection

This is the official repository for [DeTexD paper](TODO). Here you can find scripts used in the paper to evaluate models.

See also: [DeTexD dataset](https://huggingface.co/datasets/grammarly/detexd-benchmark), [detexd-roberta-base model](https://huggingface.co/grammarly/detexd-roberta-base).

## Install

```sh
pip install -r requirements.txt
```

## Usage

Run `evaluate_detexd_roberta.py` to get the published model (grammarly/detexd-roberta-base) results on published dataset (grammarly/detexd-benchmark).

Run `founta_basile_comparison.ipynb` to reproduce results for models comparison from the paper. Note that you need to acquire the datsets because they have separate licences.

Run `country_bias.ipynb` to reproduce country bias analysis.

Run `compare_hatebert.ipynb` to reproduce hatebert models comparison.

## Citation Information

```
@inproceedings{chernodub-etal-2023-detexd,
    title = "{D}e{T}ex{D}: A Benchmark Dataset for Delicate Text Detection",
    author = "Yavnyi, Serhii and Sliusarenko, Oleksii  and Razzaghi, Jade  and Mo, Yichen  and Hovakimyan, Knar and Chernodub, Artem",
    booktitle = "The 7th Workshop on Online Abuse and Harms (WOAH)",
    month = jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.woah-1.2",
    pages = "14--28",
    abstract = "Over the past few years, much research has been conducted to identify and regulate toxic language. However, few studies have addressed a broader range of sensitive texts that are not necessarily overtly toxic. In this paper, we introduce and define a new category of sensitive text called {``}delicate text.{''} We provide the taxonomy of delicate text and present a detailed annotation scheme. We annotate DeTexD, the first benchmark dataset for delicate text detection. The significance of the difference in the definitions is highlighted by the relative performance deltas between models trained each definitions and corpora and evaluated on the other. We make publicly available the DeTexD Benchmark dataset, annotation guidelines, and baseline model for delicate text detection.",
}
```

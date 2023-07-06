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

DeTexD: A Benchmark Dataset for Delicate Text Detection. Serhii Yavnyi, Oleksii Sliusarenko, Jade Razzaghi, Yichen Mo, Knar Hovakimyan, Artem Chernodub // [Accepted for publication at The 7th Workshop on Online Abuse and Harms (WOAH) at ACL 2023 in Toronto](https://www.workshopononlineabuse.com/)

# P7

Research Project

## Abstract

This project aims to test use of early-stage research results regarding use of transformers for time-series forecasting.

Usually, this field is covered with other kind of machine learning neural networks (LSTM, RNN). Also, transformers have proven their efficiency in NLP.

This project is based on a [research paper](https://arxiv.org/abs/2202.07125) "Transformers in Time Series: A Survey" (Qingson et al.) which makes a survey on using different kinds of transformers and attentipon-based networks, applied to time series forecasting, compare them and provide some conclusions.

This module will implement one of them on a realistic use case, and compare with a standard LSTM/RNN network.

The use case choosen is a predictive analysis of crypto currencies and DeFi. Especially, the prediction for decentralised exchanges (DEX) where liquidity providers (LP) will provide or withdraw liquidity (liquidity events).

We are trying to predict these movements that affects the total value lock (TVL), and try to find some correlations with other data, for instance the movement made on traditional finance (TradFi), i.e. US tresury bonds.

## Paper

[White paper](docs/2202.07125.pdf), from <https://arxiv.org/abs/2202.07125>

## Links

<https://ml-cheatsheet.readthedocs.io/en/latest/index.html>

<https://medium.com/towards-data-science/how-not-to-use-machine-learning-for-time-series-forecasting-avoiding-the-pitfalls-19f9d7adf424>



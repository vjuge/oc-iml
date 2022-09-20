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

## Dataset

We use [dune analytics](https://dune.com/browse/dashboards) to extract events and function calls from blocks in ethereum blockchain.

Specifically, we extract the frequency and amount of liquidity deposited/withdraw on Uniswap V2 pool.

> Uniswap is a decentralized, Automated Market Maker (AMM) which allows to trade pairs of crypto currencies. 
> an AMM is a kind of decentralized version of a traditional order book, and requires Liquidity Providers to fill a pool

Our goal is to try to predict what will be the amount of Total Value Locked (TVL) in the pool 
(which is the cumulative sum of deposits and withdraws)

## Predictive Models

We compare two models for prediction: popular ARIMA and new Transformer-based one.

### ARIMA

Different kinds of ARIMA exists :

* autoregressive models: AR(p)
* moving average models: MA(q)
* mixed autoregressive moving average models: ARMA(p, q)
* integration models: ARIMA(p, d, q)
* seasonal models: SARIMA(P, D, Q, s)
* regression with errors that follow one of the above ARIMA-type models

_source: <https://www.statsmodels.org/devel/generated/statsmodels.tsa.arima.model.ARIMA.html>_

### Transformer

## Links

<https://ml-cheatsheet.readthedocs.io/en/latest/index.html>

<https://medium.com/towards-data-science/how-not-to-use-machine-learning-for-time-series-forecasting-avoiding-the-pitfalls-19f9d7adf424>

ARIMA : <https://towardsdatascience.com/forecast-with-arima-in-python-more-easily-with-scalecast-35125fc7dc2e#:~:text=An%20Autoregressive%20Integrated%20Moving%20Average,statistical%20properties%20of%20the%20data.>

Statsmodels: <https://www.statsmodels.org/devel/index.html>

ScaleCast (ARMIA): <https://scalecast-examples.readthedocs.io/en/latest/arima/arima.html>

Article: <https://towardsdatascience.com/attention-for-time-series-classification-and-forecasting-261723e0006d>

Research paper: <https://www.researchgate.net/publication/347999026_A_Transformer_Self-Attention_Model_for_Time_Series_Forecasting>

TensorFlow using Transformers tutorial: <https://www.tensorflow.org/text/tutorials/transformer#attention_plots>


# Educational Material

Autocorrelation, partial autocorrelation: <https://machinelearningmastery.com/gentle-introduction-autocorrelation-partial-autocorrelation/>

Seasonality decomposition: <https://machinelearningmastery.com/decompose-time-series-data-trend-seasonality/>

Augmented Dickey Fuller test (ADF Test): <https://medium.com/@cmukesh8688/why-is-augmented-dickey-fuller-test-adf-test-so-important-in-time-series-analysis-6fc97c6be2f0>


first article to read: <https://towardsdatascience.com/time-series-forecasting-with-deep-learning-and-attention-mechanism-2d001fc871fc>

a complete overview an tutorial : <https://arxiv.org/pdf/2004.10240.pdf>

tensorflow appliled to timeseries: <https://keras.io/examples/timeseries/timeseries_transformer_classification/>
# Module P3

This Module is about to estimate the Green House Gas Emissions of Seattle's Buildings.

Raw data are available [here](https://www.kaggle.com/city-of-seattle/sea-building-energy-benchmarking#2015-building-energy-benchmarking.csv)


We will also evaluate the interest of [Energy Star](https://www.energystar.gov/buildings/facility-owners-and-managers/existing-buildings/use-portfolio-manager/interpret-your-results/what) Score




## Reading List

### SkLearn

Train Error vs Test Error : <https://scikit-learn.org/stable/auto_examples/model_selection/plot_train_error_vs_test_error.html>

Validation Curves: <https://scikit-learn.org/stable/auto_examples/model_selection/plot_validation_curve.html#sphx-glr-auto-examples-model-selection-plot-validation-curve-py>

All Together: <https://scikit-learn.org/stable/tutorial/statistical_inference/putting_together.html>

Linear Models: <https://scikit-learn.org/stable/modules/linear_model.html#linear-model>


### Kaggle example

<https://www.kaggle.com/michaelfumery/seattle-building-energy-cleaning#Sommaire>

<https://www.kaggle.com/michaelfumery/sea-building-energy-and-ghg-prediction#Sommaire>

### XGBoost 

<https://towardsdatascience.com/from-zero-to-hero-in-xgboost-tuning-e48b59bfaf58>

<https://xgboost.readthedocs.io/en/stable/get_started.html>

<https://machinelearningmastery.com/avoid-overfitting-by-early-stopping-with-xgboost-in-python/#:~:text=XGBoost%20supports%20early%20stopping%20after,which%20no%20improvement%20is%20observed>

<https://towardsdatascience.com/https-medium-com-vishalmorde-xgboost-algorithm-long-she-may-rein-edd9f99be63d#:~:text=What%20is%20XGBoost%3F,all%20other%20algorithms%20or%20frameworks>


### Variance Inflation Factor

Permet de connaitre pour chaque feature la multicolinéarité
> Des scores VIF supérieur à 5 indiquent généralement une forte multicolinéarité. Ces variables fortement corrélées  risquent d'impacter nos modèles.

> Les features suffixées EUI(kBtu/sf), sont des variables dont les valeurs sont ramenées à la surface par étage. Nous allons les supprimer car nous avons créer des variables pouvant permettre de ramener nos données à l'étage ou au  building. Idem pour la variable GHGEmissionsIntensity

```python
from statsmodels.stats.outliers_influence import variance_inflation_factor
```

--> aller voir dans le kaggle pour son usage. TODO à implenter 

https://www.wikiwand.com/en/Variance_inflation_factor

### Overfitting

https://dataaspirant.com/handle-overfitting-with-regularization/

https://towardsdatascience.com/ridge-regression-for-better-usage-2f19b3a202db


### Misc

https://towardsdatascience.com/how-to-differentiate-between-scaling-normalization-and-log-transformations-69873d365a94

https://en.wikipedia.org/wiki/Multicollinearity

https://en.wikipedia.org/wiki/Ordinary_least_squares

https://en.wikipedia.org/wiki/Occam%27s_razor

https://en.wikipedia.org/wiki/Minimum_description_length

https://towardsdatascience.com/features-correlations-data-leakage-confounded-features-and-other-things-that-can-make-your-deep-771bcaf84f9f

https://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables

https://machinelearningmastery.com/data-leakage-machine-learning/

https://towardsdatascience.com/what-are-rmse-and-mae-e405ce230383

https://towardsdatascience.com/guide-to-encoding-categorical-features-using-scikit-learn-for-machine-learning-5048997a5c79

https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html

very important article why to normalize features: https://towardsdatascience.com/how-to-differentiate-between-scaling-normalization-and-log-transformations-69873d365a94

### Personal Notes

data leakage, à cause de la corrélation entre features, le fait de bouger un peu une feature, va non seulement influencer le resultat mais aussi les features elles memes, donc la prédiction sera plus aléatoire

scaling, normalisation, : à ne faire que sur le train set

transformation : à faire sur train et test set

certaines features ne suivent pas des distributions normales, mais on peut les transformer pour y parvenir: 
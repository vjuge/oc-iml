# Module P3


## Reading List

### SkLearn

Train Error vs Test Error : https://scikit-learn.org/stable/auto_examples/model_selection/plot_train_error_vs_test_error.html

Validation Curves: https://scikit-learn.org/stable/auto_examples/model_selection/plot_validation_curve.html#sphx-glr-auto-examples-model-selection-plot-validation-curve-py

All Together: https://scikit-learn.org/stable/tutorial/statistical_inference/putting_together.html

Linear Models: https://scikit-learn.org/stable/modules/linear_model.html#linear-model


### Kaggle example

https://www.kaggle.com/michaelfumery/seattle-building-energy-cleaning#Sommaire

https://www.kaggle.com/michaelfumery/sea-building-energy-and-ghg-prediction#Sommaire

### XGBoost 

[https://towardsdatascience.com/from-zero-to-hero-in-xgboost-tuning-e48b59bfaf58]()

https://xgboost.readthedocs.io/en/stable/get_started.html

https://machinelearningmastery.com/avoid-overfitting-by-early-stopping-with-xgboost-in-python/#:~:text=XGBoost%20supports%20early%20stopping%20after,which%20no%20improvement%20is%20observed.

https://towardsdatascience.com/https-medium-com-vishalmorde-xgboost-algorithm-long-she-may-rein-edd9f99be63d#:~:text=What%20is%20XGBoost%3F,all%20other%20algorithms%20or%20frameworks.


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


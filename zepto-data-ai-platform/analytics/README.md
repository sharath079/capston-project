# Analytics Module

This module performs profiling, EDA, and predictive modeling on the Titanic dataset.

## Steps
1. Run `01_eda.ipynb` → loads Titanic dataset once, saves `titanic.csv`, profiles, cleans, and performs EDA with charts and interpretations.
2. Run `02_modeling.ipynb` → uses `titanic.csv`; its regression task imputes missing predictors within the training pipeline and excludes rows without a fare target.
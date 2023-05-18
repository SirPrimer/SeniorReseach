import pandas as pd
import xgboost as xgb
import openpyxl
from sklearn.model_selection import train_test_split
import shap
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'Tahoma'


data = pd.read_excel('NewDummyReadyXGB.xlsx')



data.drop(['jobTitle'], axis=1, inplace=True)

y = data['averageJobSalary']


X = data.iloc[:, 54:]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = xgb.XGBRegressor()
model.fit(X_train, y_train)
explainer = shap.Explainer(model, X_train)
shap_values = explainer(X_test)

shap.dependence_plot("frontend", shap_values.values, X_test, interaction_index="backend")

plt.show()

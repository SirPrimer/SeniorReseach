import pandas as pd
import xgboost as xgb
import openpyxl
from sklearn.model_selection import train_test_split
from hyperopt import hp, tpe, Trials, fmin
import shap
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel('NewDummyReadyXGB.xlsx')


data.drop(['jobTitle'], axis=1, inplace=True)

y = data['averageJobSalary']


X = data.iloc[:, 54:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = xgb.XGBRegressor()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

results['Difference'] = results['Predicted'] - results['Actual']


print(results.head(100))

from sklearn.metrics import mean_squared_error


mse = mean_squared_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)

print(f"Mean Squared Error: {mse:.2f}")
print(f"Root Mean Squared Error: {rmse:.2f}")

plt.rcParams['font.family'] = 'Tahoma'


explainer = shap.Explainer(model, X_train)
shap_values = explainer(X_test)


mean_abs_shap_values = np.mean(np.abs(shap_values.values), axis=0)


print("Mean Absolute SHAP Values:")
for feature, shap_value in zip(X_test.columns, mean_abs_shap_values):
    print(f"{feature}: {shap_value:.4f}")


shap.summary_plot(shap_values[:100], X_test[:100], plot_type='bar', color='#ff0e57', show=False, plot_size=(10, 6))

plt.show()

shap.plots.waterfall(shap_values[112])

shap.summary_plot(shap_values[:100], X_test[:100])

mean_abs_shap_df = pd.DataFrame({'Feature': X_test.columns, 'Mean Absolute SHAP': mean_abs_shap_values})


mean_abs_shap_df = mean_abs_shap_df.sort_values(by='Mean Absolute SHAP', ascending=False)

mean_abs_shap_df.to_excel('meanabshap.xlsx', index=False)
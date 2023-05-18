from sklearn.linear_model import LassoCV
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import cross_val_score
import pandas as pd
import numpy as np

data = pd.read_excel("NewDummyReadyLasso.xlsx")

X = data.iloc[:, 2:]
y = data.iloc[:, 1]

model = LassoCV(cv=10)
model.fit(X, y)

coefficients = model.coef_
intercept = model.intercept_

mse = -1 * cross_val_score(model, X, y, cv=10, scoring='neg_mean_squared_error').mean()
rmse = np.sqrt(mse) # calculate RMSE
mae = -1 * cross_val_score(model, X, y, cv=10, scoring='neg_mean_absolute_error').mean()
r2 = cross_val_score(model, X, y, cv=10, scoring='r2').mean()

coefficients_df = pd.DataFrame(coefficients.reshape(1, -1), columns=X.columns)
coefficients_df.insert(0, "R-squared", r2)
coefficients_df.insert(0, "MAE", mae)
coefficients_df.insert(0, "RMSE", rmse)
coefficients_df.insert(0, "Intercept", intercept)
coefficients_df.to_excel("Lasso Result.xlsx", index=True)

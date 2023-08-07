import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

data = pd.read_excel("data.xlsx")
df = pd.DataFrame(data)



y = data["Производство электроэнергии"]
x = df[["Инвестиции в основной капитал на душу населения","Численность рабочей силы"]]






model = LinearRegression().fit(x, y)

b1 = model.coef_[0]
b2 = model.coef_[1]
print(b2)




x_ = sm.add_constant(x)

smm = sm.OLS(y, x_).fit()

std_err_b2 = smm.bse[1]

t_statistic_b2 = b2 / std_err_b2

print("T-статистика для коэффициента b2:", t_statistic_b2)

summary = smm.summary()
print(summary)



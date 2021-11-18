import itertools

from statsmodels.tsa.arima_model import ARIMA

clear_time_series = [10, 15, 17, 20, 22, 17]

model = ARIMA(clear_time_series, order=(5,1,0))
model_fit = model.fit()
x = model_fit.forecast()
print(x[0])
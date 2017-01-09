from darksky import forecast
from secrets import key

fo = forecast(key, "Ljubljana", units="si")
print(fo.temperature)
print(fo.summary)
print(fo.daily.summary)

import exchange_rate
from datetime import datetime



data = exchange_rate.get_exchange_rate()
base = 1
usd = 1 / data["rates"]["EGP"]
eur = (1 / data["rates"]["EGP"]) * data["rates"]["EUR"]
epoch = data["timestamp"]
time_stamp = datetime.fromtimestamp(epoch)
print(base)
print(usd)
print(eur)
print(epoch)
print(time_stamp)












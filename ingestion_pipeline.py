import exchange_rate
from datetime import datetime
import os
import csv



data = exchange_rate.get_exchange_rate()
base = 1
usd = 1 / data["rates"]["EGP"]
eur = (1 / data["rates"]["EGP"]) * data["rates"]["EUR"]
epoch = data["timestamp"]
time_stamp = datetime.fromtimestamp(epoch)
#row = f"{base},{usd},{eur},{time_stamp}"
header = ["base_EGP", "USD", "EUR", "time_stamp"]
row = [base, usd, eur, time_stamp]

loc = "."
partition_folder = str(time_stamp.year) + "-" + str(time_stamp.month)
partition_file = str(time_stamp.month) + "-" + str(time_stamp.day) + ".csv"
partition_folder_path = os.path.join(loc, partition_folder)
partition_file_path = os.path.join(partition_folder_path, partition_file)
file_exist = os.path.isfile(partition_file_path)

os.makedirs(os.path.dirname(partition_folder_path), exist_ok=True)
with open(partition_file_path, "a+", encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    if not file_exist:
        writer.writerow(header)
    writer.writerow(row)






"""
https://stackoverflow.com/questions/46258499/how-to-read-the-last-line-of-a-file-in-python

with open('filename.txt') as f:
    for line in f:
        pass
    last_line = line


import os

with open('filename.txt', 'rb') as f:
    try:  # catch OSError in case of a one line file 
        f.seek(-2, os.SEEK_END)
        while f.read(1) != b'\n':
            f.seek(-2, os.SEEK_CUR)
    except OSError:
        f.seek(0)
    last_line = f.readline().decode()



"""



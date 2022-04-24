import api_configs
import requests
import argparse
from datetime import datetime
from decimal import Decimal, getcontext
import os
import sys
import csv
import json


def get_argument() -> argparse.Namespace:
    """function takes args from the user with the targeted directory for the partitioned data and has a default value for the cwd"""
    parser = argparse.ArgumentParser("exchange rate script")
    parser.add_argument("-d", "--dir", default=".", help="directory of the file for the exchange rates, default is current directory")
    args = parser.parse_args()
    return args


def get_exchange_rates() -> dict:
    """function to call the API and get the latest exchange rates for specific symbols(that are defined in the api_configs.py file)"""
    full_url = api_configs.URL + api_configs.TOKEN + "&base=" + api_configs.BASE + "&symbols=" + api_configs.SYMBOLS
    try:
        response = requests.get(full_url)
    except requests.exceptions.RequestException as e:
        print("Something went wrong with the api call, please check it")
        print(e)
        sys.exit(1)
    json_payload = response.text
    dict_payload = json.loads(json_payload)
    return dict_payload


def convert_rates(data: dict) -> tuple:
    """function to work-around the currency conversion as the free API subscription doesn't allow to change the base"""
    data = get_exchange_rates()
    base = "1"
    usd = str(1 / Decimal(data["rates"]["EGP"])) #EGP to USD
    eur = str((1 / Decimal(data["rates"]["EGP"])) * Decimal(data["rates"]["EUR"])) #EGP to EUR
    epoch = data["timestamp"]
    time_stamp = datetime.fromtimestamp(epoch)
    str_time_stamp = str(datetime.fromtimestamp(epoch))
    header = ["base_EGP", "USD", "EUR", "time_stamp"]
    row = [base, usd, eur, str_time_stamp]
    return(header, row, time_stamp)


def write_partitioned_data(partition_folder_path: str, partition_file_path: str, header: list, row: list) -> None:
    """function to check first if the folder/file does not exist and create them, then write the header for the 1st time and append any new row of data"""
    file_exist = os.path.isfile(partition_file_path)
    os.makedirs(partition_folder_path, exist_ok=True)
    if not file_exist:
        with open(partition_file_path, "a+", encoding='UTF8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(header)
            csv_writer.writerow(row)
    else:
        with open(partition_file_path, "r+", encoding='UTF8', newline='') as f:
            for line in f:
                pass
            last_line = line
            str_row = ','.join(row)
            if(last_line.strip() != str_row):
                csv_writer = csv.writer(f)
                csv_writer.writerow(row)


def main():
    args = get_argument()
    dir = args.dir
    getcontext().prec = api_configs.PRECISION
    exchange_rates = get_exchange_rates()
    header, row, time_stamp = convert_rates(exchange_rates)
    partition_folder = str(time_stamp.year) + "-" + str(time_stamp.month)
    partition_file = str(time_stamp.month) + "-" + str(time_stamp.day) + ".csv"
    partition_folder_path = os.path.join(dir, partition_folder)
    partition_file_path = os.path.join(partition_folder_path, partition_file)
    write_partitioned_data(partition_folder_path, partition_file_path, header, row)


if __name__ == "__main__":
    main()


import api_config
import requests
import json



def get_exchange_rate():
    #response_API = requests.get('https://openexchangerates.org/api/latest.json?app_id=a8bbcddd31004b9dbdc7786662dae3ad&base=USD&symbols=USD,EUR,EGP')
    full_url = api_config.URL + api_config.TOKEN + "&base=" + api_config.BASE + "&symbols=" + api_config.SYMBOLS
    response = requests.get(full_url)
    json_payload = response.text
    dict_payload = json.loads(json_payload)
    return dict_payload









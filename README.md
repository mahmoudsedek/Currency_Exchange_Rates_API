# Currency_Exchange_Rates_API

This repo aims to retrieve some currencies exchange rates from the "openexchangerate" API.

# Architecture Description
    1.api_configs.py contains some configs related the API, base currency, symbols, and decimal precision for saved data
    2.exchange_rates.py contains the actual magic where: 
      -Taking arguments from the user to specify where the targeted dir for the data is going to (there's a default for that as well)
      -Calling the API
      -Converting the retrieved exchanges rates
      -Write the data (in a partitioned way: month/day) after checking & validating the dir/file exists
      
# Steps
>>> put your tokens/app_id from the  "openexchangerate" API websites in the api_configs.py
>>> 
That's it! you see how easy that repo works xD

# Currency_Exchange_Rates_API

This repo aims to retrieve some currencies exchange rates from the "https://openexchangerates.org/" API.

# Architecture Description
    1.api_configs.py contains some configs related the API, base currency, symbols, and decimal precision for saved data
    2.exchange_rates.py contains the actual magic where: 
      -Taking arguments from the user to specify where the targeted dir for the data is going to (there's a default for that as well)
      -Calling the API
      -Converting the retrieved exchanges rates
      -Write the data (in a partitioned way: month/day) after checking & validating the dir/file exists
      
# Steps
    1. put your tokens/app_id from the  "openexchangerate" API websites in the api_configs.py
    2. python exchange_rates.py (without passing any arguments will create the partioned_data folder in the cwd
    3. if you wanna pass sepcific directory use: python exchange_rates.py --dir directory_path
    4. or you can run it this way as well: pytohn exchange_rates.py -d directory_path <br />
    <B>Note that if you passed (if you passed any number/letter it'll create a directory with that name and within this directory you'll have your data in our format: YYYY-M)
>>> That's it! you see how easy that repo works xD

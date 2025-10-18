from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
from datetime import datetime
import time 



def automated_crypto_pull():
    # Getting the url of the website we want to scrape.
    url = 'https://coinmarketcap.com/currencies/bitcoin/'
    # Making sure the respinse is good.
    page = requests.get(url)
    # getting text from the website.
    soup = BeautifulSoup(page.text, 'html')

    # Retrieving the title 'Bitcoin' from html script.
    crypto_name = soup.find('span', class_ = 'sc-65e7f566-0 lsTl').contents[0]
    # Retrieving the crypto price from html script.
    crypto_price = soup.find('span', attrs={"data-test": "text-cdp-price-display"}).text
    # Removing '$' sign from the crypto price.
    final_crypto_price = crypto_price.replace('$', '')

    # Current date and time.
    date_time = datetime.now()

    # Creating a dictionary to structure information.
    dict = {'Crypto Name': crypto_name, 
            'Price' : final_crypto_price,
            'TimeStamp': date_time}

    # Converting dictonary to dataframe
    df = pd.DataFrame([dict])

    # If file exists in file path add info to existing file, else create csv. 
    if os.path.exists(r'C:\Users\YourName\Documents\bitcoin_prices.csv'):
        df.to_csv(r'C:\Users\YourName\Documents\bitcoin_prices.csv', mode='a', header= False, index = False)
    else:
        df.to_csv(r'C:\Users\YourName\Documents\bitcoin_prices.csv', index = False)
    # So we can have tab open without it erroring out
    print(df)


# While function is true keeping looping every hour.
while True: 
    automated_crypto_pull()
    # Run cell after a certain amount of seconds
    time.sleep(3600)







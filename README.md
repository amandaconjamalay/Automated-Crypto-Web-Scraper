# Automated-Web-Scraper
Automatically scrapes the latest Bitcoin price from CoinMarkCap every hour and stores it in a CSV file for analysis or tracking purposes.

## Features 
* Automatically scrapes Bitcoin's current price from CoinMarketCap.
* Logs data with timestamps into a CSV file.
* Runs continuously every hour (3600 seconds).
* Simple and lightweight - Uses **Requests**, **BeautifulSoup** and **Pandas**.

## How It Works
1. The script fetches the Bitcoin page HTML using the requests library.
2. It parses the page with BeautifulSoup to extract:
   - Crypto Name
   - Current Price (USD)
   - Time Stamp
3. The data is structured into a Pandas DataFrame.
4. The DataFrame is appended to a local CSV file.
5. The process repeats every hour automatically.

## Imports
Libraries used:
   - BeautifulSoup - Reads and extracts information from HTML web pages.
   - Requests - sends HTTP requests to fetch the web page data.
   - Pandas - Used for organising the scraped data into a table (DataFrame) and exporting it to CSV.
   - os - checks if file exists.
   - datetime - gets the current data and time.
   - time - controls how long the script waits between each run.

```Python
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
from datetime import datetime
import time
```
## 1. Defining the Function
Defining a function that contains all the logic for pulling and storing the crypto price data.
```Python
def automated_crypto_pull():
```

## 2. Fetching the  Web Page
Defines the URL of the page that is going to be scraped.
**requests.get(url)** downloads the page content, which contains the HTML source code of that webpage.
```Python
url = 'https://coinmarketcap.com/currencies/bitcoin/'
page = requests.get(url)
```

## 3. Parsing the HTML
Converts the raw HTML text into a BeautifulSoup object that can be searched easily, so its easy to find tags or elements.
```Python
soup = BeautifulSoup(page.text, 'html')
```

## 4. Extracting the Data
- **soup.find(...)** locates HTML elements that contain the data you want.
- **crypto_name** = 'Bitcoin', **crypto_price** = (e.g. 107,237.67)
- **final_crypto_price** removes the dollar sign.
```Python
crypto_name = soup.find('span', class_ = 'sc-65e7f566-0 lsTl').contents[0]
crypto_price = soup.find('span', attrs={"data-test": "text-cdp-price-display"}).text
final_crypto_price = crypto_price.replace('$', '')
  ```

## 5. Organising the Data
  Creates a dictionary to store the data in a structured way.
  Converts it into a pandas dataframe (table).
  ```Python
  dict = {'Crypto Name': crypto_name, 
           'Price' : final_crypto_price,
           'TimeStamp': date_time}
  ```
## 6. Saving to CSV
  Checks if CSV file already exists at your chosen file path.
  If it exists it will append new data, if it doesn't it creates a new file with headers.
  ```Python
  if os.path.exists(r'</FilePath/'):
     df.to_csv(r'</FilePath/', mode='a', header= False, index = False)
  else:
     df.to_csv(r'</FilePath/', index = False)
  ```

## 7. Automating the process
This loop:
   - Runs the **automated_crypto_pull()** function.
   - Waits 3600 seconds (1 hour).
   - Repeats forever (when not true).
```Python
while True: 
   automated_crypto_pull()
   time.sleep(3600)
```


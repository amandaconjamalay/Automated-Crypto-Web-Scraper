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

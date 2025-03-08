# Create virtual environment
# python -m venv venv
# source venv/bin/activate



# Install packages into virtual environment
# pip3 install httpx (allows to send http requests, similar to requests but with async possibilities)
# pip3 install selectolax (similar to BeautifulSoup)
# pip3 install beautifulsoup4 (HTML parser)
# pip3 install pandas
# pip3 install numpy

# Create requirement.txt
# pip3 freeze > requirements.txt

# Install from requirements.txt
# pip3 install -r requirements.txt


#-----Check installed packages
# pip3 list

# Create files
# touch main.py


# Import modul
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import re


url = "https://suchen.mobile.de/fahrzeuge/search.html?dam=false&isSearchRequest=true&ref=quickSearch&s=Car&sb=rel&vc=Car"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}

resp = requests.get(url, headers = headers)
print(resp.status_code)


class crawledCar():
    def __init__(self, hp: str, km: float, year: str, date: date, price: float)  -> None:
        self.hp = hp
        self.km = km
        self.year = year
        self.date = date
        self.price = price


class carFetcher():
    def extract_info(self, html, selector: str) -> str | None:
        try:
            return BeautifulSoup.find('a', attrs={'data-testid': 'price-and-procure-title'})
        except AttributeError:
            return None

    def fetch(self, url: str) -> list[object]:
        #url = 'https://www.kaggle.com/datasets?search=Data+Visualization'
        print("fetching from: %s" %url)
        driver = webdriver.Firefox()
        driver.get(url)
        time.sleep(5)
        page = driver.page_source
        driver.quit()
        soup = BeautifulSoup(page, 'html.parser')
        # Using regex to match any number at the end
        pattern = re.compile(r'price-and-procure-title\d+$')

        # Finding the div
        div = soup.find('a', attrs={'data-testid': pattern})

        cars = []
        for car in soup.select():
            hp = self.extract_info(car,'h1')
            km = self.extract_info(car,'h1')
            year =
            date =
            price =
            crawled_object = crawledCar(hp, float(km), year, date, price)
            cars.append(crawled_object)

        return cars
# search page vs product page

def main():
    pass


if __name__ == '__main__':
    main()
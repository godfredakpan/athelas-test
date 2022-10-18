import requests
import json
import csv
import datetime
import time
import os
import sys
import pandas as pd

def get_stock_price(symbol):
    url = "https://finnhub.io/api/v1/quote?symbol=" + symbol + "&token=cd76miaad3i47lmpns50cd76miaad3i47lmpns5g"
    response = requests.get(url)
    data = response.json()
    return data


def get_latest_price():
    apple = get_stock_price("AAPL")
    amazon = get_stock_price("AMZN")
    netflix = get_stock_price("NFLX")
    facebook = get_stock_price("FB")
    google = get_stock_price("GOOGL")
    return apple, amazon, netflix, facebook, google


def get_most_volatile_stock():
    apple, amazon, netflix, facebook, google = get_latest_price()
    apple_change = apple["c"] - apple["pc"]
    amazon_change = amazon["c"] - amazon["pc"]
    netflix_change = netflix["c"] - netflix["pc"]
    facebook_change = facebook["c"] - facebook["pc"]
    google_change = google["c"] - google["pc"]
    most_volatile_stock = max(apple_change, amazon_change, netflix_change, facebook_change, google_change)
    if most_volatile_stock == apple_change:
        return apple
    elif most_volatile_stock == amazon_change:
        return amazon
    elif most_volatile_stock == netflix_change:
        return netflix
    elif most_volatile_stock == facebook_change:
        return facebook
    elif most_volatile_stock == google_change:
        return google


def save_to_csv():
    most_volatile_stock = get_most_volatile_stock()
    stock_symbol = most_volatile_stock["symbol"]
    percentage_change = (most_volatile_stock["c"] - most_volatile_stock["pc"]) / most_volatile_stock["pc"] * 100
    current_price = most_volatile_stock["c"]
    last_close_price = most_volatile_stock["pc"]
    with open("stock.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["stock_symbol", "percentage_change", "current_price", "last_close_price"])
        writer.writerow([stock_symbol, percentage_change, current_price, last_close_price])


if __name__ == "__main__":
    save_to_csv()


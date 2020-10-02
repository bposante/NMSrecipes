# Author: Bailey Posante & Katie Long
# Date: 10/02/2020
# Description: a program to scrape the web for No Man's Sky recipes, ingredients, and prices. Outputs information as
# text file for now.

import requests
from bs4 import BeautifulSoup

def scraper():
    url = input("> ")
    page = requests.get(url)
    #print(page.content)
    soup = BeautifulSoup(page.content, 'html.parser')
    refiner_recipes = soup.find(id='tablepress-36')
    print(refiner_recipes.prettify())
    return

scraper()

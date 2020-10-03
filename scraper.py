# Author: Bailey Posante & Katie Long
# Date: 10/02/2020
# Description: a program to scrape the web for No Man's Sky recipes, ingredients, and prices. Outputs information as
# text file for now.

import requests
from bs4 import BeautifulSoup

def scraper():
    recipes_output = []
    # recipe_qty, recipe_val, intput_1, inputjasdlkfja etc

    url = input("> ")
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    refiner_recipes = soup.find(id='tablepress-36')
    rows = refiner_recipes.findChildren(['th', 'tr'])
    for row in rows:
        cells = row.findChildren('td')
        if len(cells) != 0:
            value = cells[0].string
            recipes_output.append(value)

    print(recipes_output)
    return

scraper()

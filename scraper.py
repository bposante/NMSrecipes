# Author: Bailey Posante & Katie Long
# Date: 10/02/2020
# Description: a program to scrape the web for No Man's Sky recipes, ingredients, and prices. Outputs information as
# nothing for now.

import requests
from bs4 import BeautifulSoup

def scraper(url):
    """scraper.py: takes url, looks for specific table, parses table into No Man's Sky recipe outputs, values, inputs,
    and quantities, etc.

    Parameters
    ----------
    url : str
          URL to scrape data from

    Returns
    ----------
    Nothing
    """
    recipe_output = []
    recipe_qty = []
    recipe_val = []
    input_1 = []
    input_1_qty = []
    input_2 = []
    input_2_qty = []
    input_3 = []
    input_3_qty = []

    #url = input("> ")
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    refiner_recipes = soup.find(id='tablepress-36')
    rows = refiner_recipes.findChildren(['th', 'tr'])
    for row in rows:
        cells = row.findChildren('td')
        if len(cells) != 0:
            recipe_output.append(cells[0].string)
            recipe_qty.append(cells[1].string)
            recipe_val.append(cells[2].string)
            input_1.append(cells[3].string)
            input_1_qty.append(cells[4].string)
            input_2.append(cells[5].string)
            input_2_qty.append(cells[6].string)
            input_3.append(cells[7].string)
            input_3_qty.append(cells[8].string)
    return recipe_output, recipe_qty, recipe_val, input_1, input_1_qty, input_2, input_2_qty, input_3, input_3_qty

recipes = scraper("https://www.xainesworld.com/all-refiner-recipes-in-no-mans-sky-origins-3-02/")
print(recipes)

import argparse
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def scrape(url):
    try:
        html = urlopen(url)
    except HTTPError:
        return None
    soup = BeautifulSoup(html.read())
    content = {}
    content['title'] = get_title(soup)
    content['url'] = url
    content['img_url'] = get_img_url(soup)
    content['ingredients'] = get_ingredients(soup)
    content['directions'] = get_directions(soup)
    content['servings'] = get_servings(soup)
    content['total_time'] = get_total_time(soup)
    content['cooking_time'] = get_cooking_time(soup)
    content['notes'] = get_notes(soup)
    return content

def get_title(soup):
    try:
        title = soup.find('h3', {'class': 'recipe-title'})
        return title.text
    except AttributeError:
        return ''

def get_img_url(soup):
    try:
        img_url = soup.find('meta', {'property': 'og:image'})
        return img_url.attrs['content']
    except AttributeError:
        return ''

def get_ingredients(soup):
    try:
        ingredients = []
        for ingredient in soup.findAll('span', {'class': 'ingredient'}):

            quantity = ingredient.find('span', {'class': 'quantity'}).text
            unit = ingredient.find('span', {'class': 'unit'}).text
            name = ingredient.find('span', {'class': 'name'}).text
            ingredient_str = ''
            if quantity:
                ingredient_str += quantity
            if unit:
                ingredient_str += " " + unit
            if name:
                name = name.replace('\u2028\t', '')
                ingredient_str += " " + name
            ingredients.append(ingredient_str)
        return ingredients
    except AttributeError:
        return ''

def get_directions(soup):
    try:
        directions = []
        for direction in soup.findAll('div', {'itemprop': 'recipeInstructions'}):
            directions.append(direction.text)
        return directions
    except AttributeError:
        return ''

def get_servings(soup):
    try:
        servings = soup.find('span', {'class': 'total-servings'}).text
        if servings:
            return servings.split('Servings: ')[1]
    except AttributeError:
        return ''

def get_cooking_time(soup):
    try:
        cooking_time = soup.find('span', {'class': 'active-time',
                                          'itemprop': ''}).text
        if cooking_time:
            return cooking_time.split('active: ')[1]
    except AttributeError:
        return ''

def get_total_time(soup):
    try:
        total_time = soup.find('span', {'class': 'active-time',
                                        'itemprop': 'totalTime'}).text
        if total_time:
            return total_time.split('total: ')[1]
    except AttributeError:
        return ''

def get_notes(soup):
    try:
        notes = soup.find('div', {'class': 'content-intro'}).h2.text
        return notes
    except AttributeError:
        return ''

def parse_args():
    pass

if __name__ == '__main__':
    args = parse_args()

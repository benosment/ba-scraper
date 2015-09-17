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
    return content


def get_title(soup):
    try:
        title = soup.body.h1
    except AttributeError:
        return None

def get_img_url(soup):
    try:
        title = soup.body.h1
    except AttributeError:
        return None

def get_ingredients(soup):
    try:
        title = soup.body.h1
    except AttributeError:
        return None

def get_directions(soup):
    try:
        title = soup.body.h1
    except AttributeError:
        return None

def get_servings(soup):
    try:
        title = soup.body.h1
    except AttributeError:
        return None

def get_cooking_time(soup):
    try:
        title = soup.body.h1
    except AttributeError:
        return None

def get_total_time(soup):
    try:
        title = soup.body.h1
    except AttributeError:
        return None


def parse_args():
    pass

if __name__ == '__main__':
    args = parse_args()

from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = requests.get(PACKT).text

Book = namedtuple('Book', 'title description image link')


def get_book() -> Book:
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup   = Soup(CONTENT, 'html.parser')
    title   = soup.find("div",id="deal-of-the-day").find("h2").contents[0].strip()
    desc    = soup.find("div",class_="dotd-title").findNext('div').contents[0].strip()
    image   = soup.find("div",class_="dotd-main-book-image float-left").find("img")['src']
    link    = soup.find("div",class_="dotd-main-book-image float-left").find("a")["href"]
    return Book(title,desc,image,link)
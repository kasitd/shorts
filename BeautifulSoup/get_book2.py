from collections import Counter

import requests
from bs4 import BeautifulSoup

AMAZON = "amazon.com"
# static copy
TIM_BLOG = ('https://bites-data.s3.us-east-2.amazonaws.com/'
            'tribe-mentors-books.html')
MIN_COUNT = 3


def load_page() -> Any:
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(TIM_BLOG).content.decode("utf-8")


def get_top_books(content: Any = None) -> list[tuple[Any, int]]:
    """Make a BeautifulSoup object loading in content,
       find all links that contain AMAZON, extract the book title
       (stripping spacing characters), and count them.
       Return a list of (title, count) tuples where
       count is at least MIN_COUNT
    """
    if content is None:
        content = load_page()

    soup = BeautifulSoup(content, "html.parser")

    books = [link.text.strip() for link in soup.find_all("a")
             if AMAZON in link["href"]]

    return [book for book in Counter(books).most_common()
            if book[1] >= MIN_COUNT]
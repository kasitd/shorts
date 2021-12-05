from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup as Soup


# prep data
tmp = os.getenv("TMP", "/tmp")
page = 'us_holidays.html'
holidays_page = os.path.join(tmp, page)
urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{page}',
    holidays_page
)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content: str = content) -> defaultdict[Any, list]:
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""

    soup = Soup(content, 'html.parser')
    
    times= soup.find('table', class_='list-table').find_all('time')
    holidays_names=soup.find('table', class_='list-table').find_all('a')

    times_list = [(t.contents[0].split('-')[1], elem.contents[0].strip() )for t, elem in zip(times, holidays_names)]
    for tt in times_list:
        holidays[tt[0]].append(tt[1])
        
    
    return holidays
import requests
from bs4 import BeautifulSoup as Soup
import re

cached_so_url = 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'


def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    with requests.Session() as session:
        content = session.get(cached_so_url).content.decode('utf-8')
    
    soup = Soup(content, 'html.parser')
    
    all_questions = [question.contents for question in soup.find_all('a', class_="question-hyperlink") \
        if question['class']!=['js-gps-track', 'question-hyperlink', 'mb0']]
            
    all_views = [views.contents[0].strip('\r\n').strip() for views in soup.find_all('div', class_='views')]
    all_votes = [votes.string.strip() for votes in soup.find_all('span', class_='vote-count-post')]
    all_data = [(question[0], int(vote)) for question, view, vote in zip(all_questions, all_views, all_votes)\
        if 'm' in view]
    return sorted(all_data, key=lambda tup:tup[1], reverse=True)
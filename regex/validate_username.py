# nice snippet: https://gist.github.com/tonybruess/9405134
from collections import namedtuple
import re

social_platforms = """Twitter
  Min: 1
  Max: 15
  Can contain: a-z A-Z 0-9 _

Facebook
  Min: 5
  Max: 50
  Can contain: a-z A-Z 0-9 .

Reddit
  Min: 3
  Max: 20
  Can contain: a-z A-Z 0-9 _ -
"""

# note range is of type range and regex is a re.compile object
Validator = namedtuple('Validator', 'range regex')


def parse_social_platforms_string():
    """Convert the social_platforms string above into a dict where
       keys = social platformsname and values = validator namedtuples"""
    platforms = social_platforms.split('\n\n')
    return dict(_parse_platformstext(nw) for nw in platforms)


def _parse_platformstext(text):
    """Helper to parse a block of platformstext, returns platform name
       and Validator namedtuple"""
    lines = text.split('\n')
    name = lines[0].strip()

    min_ = int(lines[1].split(': ')[1])
    max_ = int(lines[2].split(': ')[1]) + 1  # upper range is exclusive

    char_classes = lines[3].split(': ')[1].replace(' ', '').replace('.', '\.')
    regex = f'^[{char_classes}]+$'  # one or more and make sure start to end

    return name, Validator(range(min_, max_), re.compile(regex))


def validate_username(platform, username):
    """Receives platforms(Twitter, Facebook or Reddit) and username string,
       raise a ValueError if the wrong platform is passed in,
       return True/False if username is valid for entered platform"""
    all_validators = parse_social_platforms_string()
    validator = all_validators.get(platform)

    if not validator:
        raise ValueError('Not a valid platform')

    if len(username) not in validator.range:
        return False

    return validator.regex.match(username)
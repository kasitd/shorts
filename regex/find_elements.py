import re


def has_timestamp(text):
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""
    t = re.findall(r'\d{4}-\d{2}-\d{2}\w\d{2}:\d{2}:\d{2}', text)
    return t


def is_integer(number):
    """Return True if number is an integer"""
    return (isinstance(number, int))


def has_word_with_dashes(text):
    """Returns True if text has one or more words with dashes"""
    for word in text.split():
        if re.findall(r'\d-\d', word) or re.findall(r'\w-\w', word):
            return True


def remove_all_parenthesis_words(text):
    """Return text but without any words or phrases in parenthesis:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""
    m = re.sub(r'\s\((.*?)\)', '', text)
    return m


def split_string_on_punctuation(text):
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
       ['hi', 'how are you doing', 'blabla']
       (make sure you strip trailing spaces)"""
    a = []
    pattern = re.compile(r'\s')
    t = re.split(r'[;\.!\?,]', text)
    for word in t:
        print(word)
        if word == '':
            continue
        if pattern.search(word, 0):
            a.append(word[1:])

        else:
            a.append(word)
    return a


def remove_duplicate_spacing(text):
    """Replace multiple spaces by one space"""
    return re.sub(re.compile(r'\s\s*'), ' ', text)


def has_three_consecutive_vowels(word):
    """Returns True if word has at least 3 consecutive vowels"""
    if re.findall(re.compile(r'[aeiouy]{3}'), word):
        return True


def convert_emea_date_to_amer_date(date):
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
       (AMER date format)"""
    if re.search(r'\d{2}/\d{2}/\d{4}', date):
        m = re.match(r'(\w{2})/(\w{2})/(\w{4})', date)
        return ('/'.join(m.group(2, 1, 3)))
    else:
        return date
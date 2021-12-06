import re

def get_sentences(text):
    """Return a list of sentences as extracted from the text passed in.
       A sentence starts with [A-Z] and ends with [.?!]"""
    
    no_lines = (re.sub('\n', ' ', text))
    return re.findall(r'[A-Z].*?[\.\!\?](?=\s[A-Z])|[A-Z].*?[\.\!\?]', no_lines)
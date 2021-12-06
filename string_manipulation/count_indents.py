import textwrap

def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""

    t = text.lstrip('\t')

    return len(t)-len(textwrap.dedent(t))
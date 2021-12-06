PYBITES = "pybites"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    new = ''
    for letter in text:
        if letter.lower() in PYBITES:
            new+=letter.swapcase()
        else:
            new+=letter
    return new

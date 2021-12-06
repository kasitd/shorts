import unicodedata

def normalize(text):
    try:
        text = unicode(text, 'utf-8')
    except NameError:
        pass
    text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode("utf-8")
    return str(text)

def filter_accents(text):
    
    no_accent = normalize(text)

    return [accent for accent, letter in zip(text.lower(), no_accent.lower()) if accent != letter]
import re

def split_words_and_quoted_text(text):
    """Split string text by space unless it is
       wrapped inside double quotes, returning a list
       of the elements.

       For example
       if text =
       'Should give "3 elements only"'

       the resulting list would be:
       ['Should', 'give', '3 elements only']
    """
    lista = []
    pattern = r'^\"'
    t = re.findall(r'(.*)(\".*")(.*)', text)

    for elem in t[0]:
        if re.match(pattern, elem):
            lista.append(re.sub('"', '', elem))
        else:
            for e in elem.split():
                lista.append(e)
    return lista
INDENTS = 4
import textwrap

def print_hanging_indents(poem):
    s_poem = poem.strip()
    split_poem = s_poem.split('\n\n')



    for paragraph in split_poem:
        n = 0
        for line in paragraph.splitlines():
            stripped_line = line.strip()
            n+=1
            if n == 1:
                wrapper = textwrap.indent(stripped_line, '')
            else:
                wrapper = textwrap.indent(stripped_line, (' '*INDENTS))
            print(wrapper)
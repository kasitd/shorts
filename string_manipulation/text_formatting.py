import itertools
import textwrap

COL_WIDTH = 20


def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""
    split_text = [ textwrap.wrap(col, width=COL_WIDTH) for col in text.split('\n\n') ]
    rearranged_text = itertools.zip_longest(*split_text, fillvalue=' ')
    return '\n'.join(' '.join(f'{chunk:20}' for chunk in chunks) for chunks in rearranged_text)
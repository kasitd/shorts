import re


def strip_comments(code):
    # [\s\S]*? to rm docstring -> https://stackoverflow.com/a/44532145
    # \s* = 0 or more spaces
    # ?: is non-capturing (not needed but best practice)
    # *? is not being 'greedy' (match shortest possible pattern)
    # carrying over the newline to fix indenting issue
    return re.sub(r'(?:\s*#\s.*|\s{2}#\s.*|\s*"""[\s\S]*?""")(\n)',
                  r'\1', code, re.MULTILINE)
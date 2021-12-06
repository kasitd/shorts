import pprint
from typing import Any


def pretty_string(obj: Any) -> str:
    # TODO: your code
    pp = pprint.pformat(obj, width=60, depth=2)
    print(pp)
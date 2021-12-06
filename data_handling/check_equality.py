from enum import Enum


class Equality(Enum):
    SAME_REFERENCE = 4
    SAME_ORDERED = 3
    SAME_UNORDERED = 2
    SAME_UNORDERED_DEDUPED = 1
    NO_EQUALITY = 0

def check_equality(list1, list2):

    if list1 is list2:
        return Equality.SAME_REFERENCE

    if list1 == list2:
        return Equality.SAME_ORDERED

    if sorted(list1) == sorted(list2):
        return Equality.SAME_UNORDERED

    if sorted(set(list1)) == sorted(set(list2)):
        return Equality.SAME_UNORDERED_DEDUPED

    if list1 is not list2 or ist1 != list2 or sorted(list1) != sorted(list2) or sorted(set(list1)) != sorted(set(list2)):
        return Equality.NO_EQUALITY
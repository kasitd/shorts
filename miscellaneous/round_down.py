import math
def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) round up, else round down.
       Return a new list of rounded values
    """
    return [math.floor(transaction) if up == False else math.ceil(transaction) for transaction in transactions]
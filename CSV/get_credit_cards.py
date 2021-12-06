import base64
import csv
from typing import List  # will remove with 3.9


def get_credit_cards(data: bytes) -> List[str]:
    """Decode the base64 encoded data which gives you a csv
    of "first_name,last_name,credit_card", from which you have
    to extract the credit card numbers.
    """
    credit_card = []
    
    message_bytes = base64.b64decode(data)
    message = message_bytes.decode('ascii')
    for line in message.splitlines()[1:]:
        credit_card.append(line.split(',')[-1])
    return credit_card
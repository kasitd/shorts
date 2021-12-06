import re


def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    if len(key)!= 38:
       return False
    if key.count('-') !=4:
        return False

    else:
        parts = key.split('-')
        if parts[0] !='PB':
            return False
        for part in parts[1:]:
            if len(part)!=8:
                return False
            if not part.isalnum():
                return False
            if not part.upper():
                return False
            else:
                return True
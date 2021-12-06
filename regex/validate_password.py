import string
import re

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())


def validate_password(password):
    
    if (len(password)<6 or 
    len(password)>12 or 
    len(re.findall(r'[0-9]', password))<1 or 
    len(re.findall(r'[A-Z]', password))<1 or 
    len(re.findall(r'[a-z]', password))<2 or 
    len([elem for elem in password if elem in PUNCTUATION_CHARS]) <1 or
    password in used_passwords):
        return False
    else:
        used_passwords.add(password)
        return True
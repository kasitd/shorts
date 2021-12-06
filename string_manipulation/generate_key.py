import secrets

def gen_key(parts=4, chars_per_part=8):
    new_part = ''
    for part in range(parts):
        part = secrets.token_hex(nbytes=(int(chars_per_part/2))).upper()

        new_part = (new_part[0:] + '-' + part[:]).lstrip('-')

    return new_part

from collections import namedtuple

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

name1 = User(name='name1', role=USER, expired=False)
name2 = User(name='name2', role=USER, expired=True)
name3 = User(name='name3', role=ADMIN, expired=False)
USERS = (name1, name2, name3)

class UserDoesNotExist(Exception):
    'raised when user is not in USERS'
    pass

class UserAccessExpired(Exception):
    'raises when asses is expired'
    pass

class UserNoPermission(Exception):
    'raises when there is no permission'
    pass


def get_secret_token(username):
    if username not in [x.name for x in USERS]:
        raise UserDoesNotExist
    if username in [x.name for x in USERS if x.expired]:
        raise UserAccessExpired
    if username in [x.name for x in USERS if x.role != "admin"]:
        raise UserNoPermission
    return SECRET
from functools import wraps



known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


def login_required(func):
    @wraps(func)
    def func_wrapper(user):
        if user in loggedin_users:
            return func(user)
        if user in known_users:
            return "please login"
        if user not in known_users or user =='anonymous':
            return 'please create an account'
    return func_wrapper

@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    return f'welcome back {user}'
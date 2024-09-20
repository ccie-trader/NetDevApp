from getpass import getpass

def get_input(prompt=''):
    try:
        username = raw_input(prompt)
    except NameError:
        username = input(prompt)
    return username
def get_credentials():
    '''Prompts for, and returns, a username and passowrd'''

    username = get_input('Enter Username: ')
    password = None

    while not password:
        password = getpass()
        password_verify = getpass('Confirm password: ')
        
        if password != password_verify:
            print('Password do not match. Try again.')
            password = None
    return username, password

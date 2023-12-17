import json
from getpass import getpass
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from commands import clear

def load_accounts():
    try:
        with open('./Code/Data/Accounts.json') as f:
            return json.load(f)
    except:
        return dict()
    finally:
        f.close()
    
def username_exists(username):
    accounts = load_accounts()
    return username in accounts

def add_account(username, password):
    if not username_exists(username):
        accounts = load_accounts()
        accounts[username] = password
        with open('./Code/Data/Accounts.json', 'w') as f:
            json.dump(accounts, f)
        return True
    else:
        return False

def match_password(username, password):
    accounts = load_accounts()
    return username in accounts and accounts[username] == password

def login():
    retry = True
    while retry:
        clear()
        username = input('Username: ').strip()
        if not username_exists(username):
            print("This username doesn't exist")
            retry = try_again()
        else:
            password = getpass('Password: ')
            if not match_password(username, password):
                print('Incorrect password')
                retry = try_again()
            else:
                return username
    return False

def create_account():
    retry = True
    while retry:
        clear()
        print('Your username must be between 4 and 16 characters long and can only contain letters, numbers, and underscores.')
        username = input('Username: ').strip()
        if not check_username(username):
            print('Invalid username')
            retry = try_again()
        elif username_exists(username):
            print('This username already exists')
            retry = try_again()
        else:
            print('Your password must be between 4 and 16 characters long')
            password = getpass('Password: ')
            if not check_password(password):
                print('Invalid password')
                retry = try_again()
            else:
                add_account(username, password)
                return username
    return False

def try_again():
    print('Would you like to try again?')
    retry = input('Retry? (y/n): ').strip().lower()
    if retry == 'y' or retry == 'yes':
        return True
    else:
        return False

def check_username(username):
    if len(username) < 4 or len(username) > 16:
        return False
    for char in username:
        if not char.isalnum() and char != '_':
            return False
    return True

def check_password(password):
    return len(password) >= 4 and len(password) <= 16

def account_main():
    clear()
    print('Welcome to PYTHON_RPG!')
    print('Would you like to login or create an account?')
    print('1. Login')
    print('2. Create an account')
    print('3. Exit')
    choice = input('Choice: ').strip()
    if choice == '1':
        username = login()
        if not username:
            print('Login failed')
        else:
            clear()
            print('You are logged in as', username)
            print('Enter anything to continue')
            input()
            return username
    elif choice == '2':
        new_account = create_account()
        if not new_account:
            print('Account creation failed')
        else:
            print('You created the account of', new_account)
    elif choice == '3':
        clear()
        print('Goodbye!')
        sys.exit()
    else:
        print('Invalid choice')
        account_main()

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), './Classes'))
sys.path.append(os.path.join(os.path.dirname(__file__), './Data'))

from User import User
from Account_manager import account_main
from Character_manager import character_main

from ORM_connector import engine, session

user = User()
while True:
    username = account_main()
    if username:
        try:
            loaded = user.load(username)
        except ValueError as e:
            print("An error occured: ", e)
            print("No idea what happened, restarting...")
            break
        character_main(user)
        break
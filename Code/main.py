import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), './Classes'))
sys.path.append(os.path.join(os.path.dirname(__file__), './Data'))

from User import User
from Account_manager import account_main
from Character_manager import character_main

user = User()
# Add if here
while True:
    username = account_main()
    if username:
        user.login(username)
        character_main(user)
        break
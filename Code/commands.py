import os
import platform

def clear():
    if platform.system() == "Windows":
        os.system('cls')
    elif platform.system() == "Linux":
        os.system('clear')
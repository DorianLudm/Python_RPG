import json
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Classes'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Character import Dragoon, Arbalist, Slaughterer, Guardian, Spellcaster, Bard, Seraph
from Account_manager import account_main
from commands import clear

def load_characters():
    try:
        with open('./Code/Data/Characters.json') as f:
            return json.load(f)
    except:
        return dict()
    finally:
        f.close()

def is_initialized(username):
    characters = load_characters()
    return username in characters

def owns_character(username):
    characters = load_characters()
    return username in characters and len(characters[username]) > 0

def character_name_taken(username, character_name):
    characters = load_characters()
    for character in characters[username]:
        if character_name.lower() == character.lower():
            return True
    return False

def initialize(username):
    characters = load_characters()
    characters[username] = dict()
    with open('./Code/Data/Characters.json', 'w') as f:
        json.dump(characters, f)

def get_characters_name(username):
    characters = load_characters()
    list_of_characters = list(characters[username].keys())
    string_return = ""
    for i in range(len(list_of_characters)):
        string_return += list_of_characters[i]
        string_return += ", "
    return string_return[:-2]

def check_name(name):
    if len(name) < 4 or len(name) > 16:
        return False
    for char in name:
        if not char.isalnum() and char != '_':
            return False
    return True

def add_character(username, character):
    characters = load_characters()
    characters[username][character.name] = character.to_dict()
    with open('./Code/Data/Characters.json', 'w') as f:
        json.dump(characters, f)

def remove_character(username, character_name):
    characters = load_characters()
    del characters[username][character_name]
    with open('./Code/Data/Characters.json', 'w') as f:
        json.dump(characters, f)

def view_character(username, name):
    os.system('cls')
    characters = load_characters()[username]
    character = characters[name]
    print("Name:", name)
    print("Profession:", character["prof"])
    print("Stats:", character["skill_points"])

def manual_skill_points(character):
    repartition_done = False
    error = []
    while not repartition_done:
        clear()
        print("You have 15 skill points to distribute")
        print("You can distribute them however you want between the following skills")
        print("Strength, Dexterity, Defense, Magic, Holiness, Charisma and Speed")
        print("Your characters current skill points are:", character.skill_points)
        print("Exemple: If you want to add 10 points to strength and 5 points to defense, type 'strength 10, defense 5'")
        if len(error) > 0:
            for i in range(len(error)):
                print(error[i])
            error = []
        point_given = 0
        repartition_points = {"strength": 0, "dexterity": 0, "defense": 0, "magic": 0, "holiness": 0, "charisma": 0, "speed": 0}
        input_string = input("Skill points repartition: ")
        try:
            repartition = input_string.split(",")
            for tuple in repartition:
                tuple = tuple.split(" ")
                tuple = [i for i in tuple if i != ""]
                skill = tuple[0].strip().lower()
                amount = tuple[1].strip()
                if skill in repartition_points and amount.isnumeric():
                    repartition_points[skill] += int(amount)
                    point_given += int(amount)
                else:
                    error = ["Invalid input"]
                    break
            if point_given != 15:
                error = ["You must give exactly 15 points"]
            else:
                repartition_done = True
        except:
            error = ["Invalid input"]
    character.add_skill_points(list(repartition_points.values()))
    clear()
    print("Your character's skill points are now:", character.skill_points)

def character_main(player):
    username = player.username
    clear()
    print("Welcome to Python RPG", username, "!")
    print("What would you like to do?")
    print("1. Play with a character")
    print("2. Manage characters")
    print("3. Logout")
    choice = input("Choice: ")
    if choice == "1":
        play(player)
    elif choice == "2":
        character_manager(player)
    elif choice == "3":
        player.logout()
        #account_main() Might need to re-add this??
    else:
        print("Invalid choice")
        character_main()

def character_manager(player):
    username = player.username
    clear()
    print("This is the character manager")
    print("What would you like to do?")
    print("1. Create a character")
    print("2. Delete a character")
    print("3. View characters")
    print("4. Go back")
    choice = input("Choice: ")
    if choice == "1":
        create_character(username)
    elif choice == "2":
        delete_character(username)
    elif choice == "3":
        view_characters(username)
    elif choice == "4":
        character_main(player)
    else:
        print("Invalid choice")
        character_manager(username)

def create_character(username):
    clear()
    if not is_initialized(username):
        initialize(username)
    if len(load_characters()[username]) >= 5:
        print("You already have 5 characters, delete one to create a new one")
        character_manager(username)
    else:
        print("Choose a profession")
        print("1. Dragoon")
        print("2. Arbalist")
        print("3. Slaughterer")
        print("4. Guardian")
        print("5. Spellcaster")
        print("6. Bard")
        print("7. Seraph")
        print("8. Go back")
        choice = input("Choice: ")
        match (choice):
            case "1":
                character = Dragoon()
            case "2":
                character = Arbalist()
            case "3":
                character = Slaughterer()
            case "4":
                character = Guardian()
            case "5":
                character = Spellcaster()
            case "6":
                character = Bard()
            case "7":
                character = Seraph()
            case "8":
                character_manager(username)
            case _:
                print("Invalid choice")
                create_character(username)
        if choice.isnumeric() and 1 <= int(choice) and int(choice) <= 7:
            name_good = False
            error = []
            while not name_good:
                clear()
                print("You chose", character.prof + "!", "Now give your character a name!")
                print('Your character name must be between 4 and 16 characters long and can only contain letters, numbers, and underscores.')
                if len(error) > 0:
                    for i in range(len(error)):
                        print(error[i])
                name = input("Name: ")
                if not check_name(name):
                    error = ["Invalid name"]
                elif character_name_taken(username, name):
                    error = ["That name is already taken", "Please choose a name different than " + get_characters_name(username)]
                else:
                    name_good = True
            character.name = name
            print("Your character's name is", character.name, "and their profession is", character.prof)
            manual_skill_points(character)
            add_character(username, character)
            print("Your character has been created!")
            print("Enter anything to go back")
            input()
            character_manager(username)

def delete_character(username):
    clear()
    if not owns_character(username):
        print("You don't have any characters yet!")
        print("Enter anything to go back")
        input()
        character_manager(username)
    else:
        answers = dict()
        print("Select a character to delete")
        characters = load_characters()[username]
        for i in range(len(characters)):
            print(i+1, ". ", list(characters.keys())[i], sep="")
            answers[str(i+1)] = list(characters.keys())[i]
        print(len(characters)+1, ". Go back", sep="")
        choice = input("Choice: ")
        if choice.isnumeric() and 1 <= int(choice) and int(choice) <= len(characters)+1:
            if choice == str(len(characters)+1):
                character_manager(username)
            else:
                clear()
                print("Are you sure you want to delete", answers[choice], "?")
                print("1. Yes")
                print("2. No")
                choice_valid = False
                while not choice_valid:
                    choice_validation = input("Choice: ")
                    clear()
                    if choice_validation == "1":
                        remove_character(username, answers[choice])
                        choice_valid = True
                        print("The character", answers[choice], "has been deleted")
                        print("Enter anything to go back")
                        input()
                        character_manager(username)
                    elif choice_validation == "2":
                        choice_valid = True
                        print("The deletion of", answers[choice], "has been cancelled")
                        print("Enter anything to go back")
                        input()
                        character_manager(username)
                    else:
                        print("Invalid choice")
                        delete_character(username)

def view_characters(username):
    if not owns_character(username):
        clear()
        print("You don't have any characters yet!")
        print("Enter anything to go back")
        input()
        character_manager(username)
    else:
        clear()
        print("Select a character to view")
        characters = load_characters()[username]
        for i in range(len(characters)):
            print(i+1, ". ", list(characters.keys())[i], sep="")
        print(len(characters)+1, ". Go back", sep="")
        choice = input("Choice: ")
        if choice.isnumeric() and 1 <= int(choice) and int(choice) <= len(characters)+1:
            if choice == str(len(characters)+1):
                character_manager(username)
            else:
                view_character(username, list(characters.keys())[int(choice)-1])
                print("Enter anything to go back")
                input()
                character_manager(username)

def play(*args):
    if len(args) == 1:
        player = args[0]
        username = player.username
        clear()
        if not owns_character(username):
            clear()
            print("You don't have any characters yet!")
            print("Enter anything to go back")
            input()
            character_main(username)
        else:
            print("Select a character to play with")
            characters = load_characters()[username]
            for i in range(len(characters)):
                print(i+1, ". ", list(characters.keys())[i], sep="")
            print(len(characters)+1, ". Go back", sep="")
            choice = input("Choice: ")
            if choice.isnumeric() and 1 <= int(choice) and int(choice) <= len(characters)+1:
                if choice == str(len(characters)+1):
                    character_main(username)
                else:
                    print("You are now playing with", list(characters.keys())[int(choice)-1])
                    play(username, list(characters.keys())[int(choice)-1])
    elif len(args) == 2:
        Player = args[0]
        username = Player.username
        character_name = args[1]
        print("Welcome to Python RPG", username, "!")
        print("You are playing with", character_name)
        print("Not yet implemented")
        import time
        time.sleep(5)
        character_main(username)
    else:
        raise Exception("Invalid number of arguments")

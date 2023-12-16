import json
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Classes'))

from Character import Dragoon, Arbalist, Slaughterer, Guardian, Spellcaster, Bard, Seraph

def load_characters():
    try:
        with open('./Code/Data/Characters.json') as f:
            return json.load(f)
    except:
        return dict()
    finally:
        f.close()

def has_character(username):
    characters = load_characters()
    return username in characters

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

def manual_skill_points(character):
    print("You have 15 skill points to distribute")
    print("You can distribute them however you want between the following skills")
    print("Strength, Dexterity, Defense, Magic, Holiness, Charisma and Speed")
    print("Your characters current skill points are:", character.skill_points)
    print("Exemple: If you want to add 10 points to strength and 5 points to defense, type 'strength 10, defense 5'")
    repartition_done = False
    while not repartition_done:
        point_given = 0
        repartition_points = {"strength": 0, "dexterity": 0, "defense": 0, "magic": 0, "holiness": 0, "charisma": 0, "speed": 0}
        input_string = input("Skill points repartition: ")
        if input_string.strip() == "":
            print("Invalid input")
        repartition = input_string.split(",")
        for tuple in repartition:
            tuple = tuple.split(" ")
            tuple = [i for i in tuple if i != ""]
            print(tuple)
            skill = tuple[0].strip().lower()
            amount = tuple[1].strip()
            if skill in repartition_points and amount.isnumeric():
                repartition_points[skill] = int(amount)
                point_given += int(amount)
            else:
                print("Invalid input")
                # break
        if point_given != 15:
            print("You must give exactly 15 points")
        else:
            repartition_done = True
    character.add_skill_points(list(repartition_points.values()))
    print("Your character's skill points are now:", character.skill_points)

def main(username):
    print("Welcome to Python RPG", username, "!")
    print("What would you like to do?")
    print("1. Play with a character")
    print("2. Manage characters")
    choice = input("Choice: ")
    if choice == "1":
        print("This feature is not yet implemented")
    elif choice == "2":
        character_manager(username)
    else:
        print("Invalid choice")
        main()

def character_manager(username):
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
        main(username)
    else:
        print("Invalid choice")
        character_manager(username)

def create_character(username):
    if not has_character(username):
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
            print("You chose", character.prof + "!", "Now give your character a name!")
            print('Your character name must be between 4 and 16 characters long and can only contain letters, numbers, and underscores.')
            name_good = False
            while not name_good:
                name = input("Name: ")
                if not check_name(name):
                    print("Invalid name")
                elif character_name_taken(username, name):
                    print("That name is already taken")
                    print("Please choose a name different than", get_characters_name(username))
                else:
                    name_good = True
            character.name = name
            print("Your character's name is", character.name, "and their profession is", character.prof)
            manual_skill_points(character)
            add_character(username, character)

def delete_character(username):
    if not has_character(username):
        print("You don't have any characters yet!")
        character_manager(username)
    else:
        print("Select a character to delete")
        for i in range(len(load_characters()[username])):
            print(i+1, ". ", list(load_characters()[username].keys())[i], sep="")
        print(len(load_characters()[username])+1, ". Go back", sep="")
    

def view_characters(username):
    print("This feature is not yet implemented")
    character_manager(username)

main("Pixa253lulu")
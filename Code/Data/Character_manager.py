import json
from ..Classes import Dragoon, Arbalist, Slaughterer, Guardian, Spellcaster, Bard, Seraph

def load_characters():
    try:
        with open('./Code/Data/Characters.json') as f:
            return json.load(f)
    except:
        return dict()
    finally:
        f.close()

def add_character(username, character):
    characters = load_characters()
    # if len(characters[username]) >= 5:
    #     return False
    characters[username].append(character)
    with open('./Code/Data/Characters.json', 'w') as f:
        json.dump(characters, f)

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
        if 1 <= choice and choice <= 7:
            print("You chose", character.profession, "!", "Now give your character a name!")
            character.name = input("Name: ")
            print("Your character's name is", character.name, "and their profession is", character.profession)
            print("Stats:", character.stats)

def delete_character(username):
    print("This feature is not yet implemented")
    character_manager(username)

def view_characters(username):
    print("This feature is not yet implemented")
    character_manager(username)

main()
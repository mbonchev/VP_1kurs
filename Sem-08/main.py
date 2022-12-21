from entities.character import Character
from entities.weapon import Weapon
from entities.item import Item
from errors import *

class Menu:
    def print_menu(self):
        print("1. Create a new character")
        print("2. Create a weapon")
        print("3. Create an item")
        print("4. Print all characters")
        print("5. Delete a character")
        print("6. Exit")

    def command_create_character(self):
        name = input("Enter the character name: \n")
        sex = input("Enter the character sex: \n")
        ch_class = input("Enter the character class: \n")
        newCharacter = Character(name, sex, ch_class)
        return newCharacter

    def command_create_weapon(self):
        name = input("Enter the weapon name: \n")
        attack = input("Enter the weapon attack: \n")
        newWeapon = Weapon(name, attack)
        return newWeapon

    def command_create_item(self):
        name = input("Enter the item name: \n")
        newItem = Item(name)
        return newItem

    def run(self):
        characters = []
        while True:
            Menu.print_menu()
            choice = input("Choose an item from the menu: \n")

            if choice == "1":
                characters.append(Menu.command_create_character())
            elif choice == "2":
                ch_name = input("Enter an existing character's name: \n")
                if ch_name in characters:
                    for i in range(len(characters)):
                        if ch_name == characters[i]:
                            characters[i].weapon = Menu.command_create_weapon()

                else:
                    raise CharacterNotFound()
            elif choice == "3":
                ch_name = input("Enter an existing character's name: \n")
                if ch_name in characters:
                    for i in range(len(characters)):
                        if ch_name == characters[i]:
                            characters[i].item = Menu.command_create_item()
                else:
                    raise CharacterNotFound()

Menu.run()
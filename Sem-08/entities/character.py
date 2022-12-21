from errors import *
from weapon import *
from item import *

class Character:
    def __init__(self, name, sex, ch_class, weapon = None, item = None):
        Character.set_name(name)
        Character.set_sex(sex)
        Character.set_ch_class(ch_class)
        self.weapon = weapon
        self.item = item

    def set_name(self, name):
        if len(name) >= 4:
            self.name = name
        else:
            raise InvalidFormat()

    def set_sex(self, sex):
        if len(sex) >= 4 and (chr.isdigit() for chr in sex):
            self.sex = sex
        else:
            raise InvalidFormat()

    def set_ch_class(self, ch_class):
        if len(ch_class) >= 4 and (chr.isdigit() for chr in ch_class):
            valid_ch_classed = {"Warrior", "Mage", "Priest", "Rogue"}
            if ch_class in valid_ch_classed:
                self.ch_class = ch_class
            else:
                raise InvalidCharacterClass()
        else:
            raise InvalidFormat()

    def print_character(self):
        print("Name: %s, sex: %s, character class: %s, weapon: [%s], item: %s" % (self.name, self.sex, self.ch_class, self.weapon.print_weapon(), self.item.print_item()))
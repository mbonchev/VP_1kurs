from entities import Item
from errors import *

class Weapon(Item):
    def __init__(self, name, durability, attack):
        super().__init__(self, name, durability)
        self.name = name
        self.durability = durability
        self.attack = attack

    def set_attack(self, attack):
        if attack > 0:
            self.attack = attack
        else:
            raise InvalidAttackValue()

    def print_weapon(self):
        print("Name: %s, durability: %s, attack: %s" % (self.name, self.durability, self.attack))
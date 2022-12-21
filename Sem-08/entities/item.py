class Item:
    def __init__(self, name, durability = 100):
        self.name = name
        self.durability = durability

    def print_item(self):
        print("Name: %s, durability: %s" % (self.name, self.durability))
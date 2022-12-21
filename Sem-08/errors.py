class InvalidCharacterClass(Exception):
    def __init__(self, message = "Invalid character class!"):
        super.__init__("Error: {message}")

class InvalidFormat(Exception):
    def __init__(self, message = "Invalid format!"):
        super.__init__("Error: {message}")

class CharacterNotFound(Exception):
    def __init__(self, message = "Character not found!"):
        super.__init__("Error: {message}")

class InvalidAttackValue(Exception):
    def __init__(self, message = "Invalid attack value!"):
        super.__init__("Error: {message}")
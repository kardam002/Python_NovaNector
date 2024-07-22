# character.py
class Character:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes
        self.inventory = Inventory()

    def __str__(self):
        return f"{self.name}: {self.attributes}"

# Define more methods for character actions

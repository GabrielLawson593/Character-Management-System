class Character:
    def __init__(self, name, health, level):
        # Protected attributes
        self._name = name
        self._health = health
        self._level = level
        self._inventory = []  #  List of items

    # Name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and value:
            self._name = value
        else:
            print("Invalid name.")

    # Health property
    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if isinstance(value, int) and value > 0:
            self._health = value
        else:
            print("Health must be a positive integer.")

    # Level property
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if isinstance(value, int) and value > 0:
            self._level = value
        else:
            print("Level must be a positive integer.")

    # Inventory property
    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, items):
        if isinstance(items, list):
            self._inventory = items
        else:
            print("Inventory must be a list.")

    # Method to add item to inventory
    def add_item(self, item):
        self._inventory.append(item)

    # Recursive display of inventory
    def display_inventory_recursive(self, index=0):
        if index >= len(self._inventory):
            return
        print(f"- {self._inventory[index]}")
        self.display_inventory_recursive(index + 1)

    # Display character info
    def display_info(self):
        print(f"Name: {self._name}")
        print(f"Health: {self._health}")
        print(f"Level: {self._level}")
        print("Inventory:")
        if self._inventory:
            self.display_inventory_recursive()
        else:
            print("Empty")
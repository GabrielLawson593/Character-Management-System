from Class import Character

def main():
    # Create Character objects
    hero = Character("Arin", 100, 1)
    mage = Character("Lyra", 80, 2)

    # Add items
    hero.add_item("Iron Sword")
    hero.add_item("Health Potion")

    mage.add_item("Magic Staff")
    mage.add_item("Mana Potion")

    print("=== Initial Characters ===\n")
    hero.display_info()
    print()
    mage.display_info()
    print()

    # Modify attributes using properties
    hero.health = 120
    mage.level = 3
    hero.name = "Arin the Brave"

    print("=== Updated Characters ===\n")
    hero.display_info()
    print()
    mage.display_info()


if __name__ == "__main__":
    main()
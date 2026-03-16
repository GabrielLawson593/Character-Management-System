from Class import Character

FILE_NAME = "characters.txt"


def load_characters():
    characters = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")

                name = data[0]
                health = int(data[1])
                level = int(data[2])

                inventory = []
                if len(data) > 3 and data[3]:
                    inventory = data[3].split("|")

                char = Character(name, health, level)

                for item in inventory:
                    char.add_item(item)

                characters.append(char)

    except FileNotFoundError:
        pass

    return characters


def save_characters(characters):
    with open(FILE_NAME, "w") as file:
        for char in characters:
            inventory = "|".join(char.inventory)
            line = f"{char.name},{char.health},{char.level},{inventory}\n"
            file.write(line)

    print("Characters saved successfully.\n")


def create_character(characters):
    name = input("Enter character name: ")
    health = int(input("Enter health: "))
    level = int(input("Enter level: "))

    new_char = Character(name, health, level)
    characters.append(new_char)

    print("Character created.\n")


def view_characters(characters):
    if not characters:
        print("No characters available.\n")
        return

    for i, char in enumerate(characters):
        print(f"\nCharacter #{i + 1}")
        char.display_info()


def choose_character(characters):
    view_characters(characters)

    if not characters:
        return None

    try:
        choice = int(input("\nSelect character number: ")) - 1
        return characters[choice]
    except:
        print("Invalid selection.")
        return None


def modify_character(characters):
    char = choose_character(characters)

    if not char:
        return

    print("\n1. Change Name")
    print("2. Change Health")
    print("3. Change Level")

    choice = input("Choose option: ")

    if choice == "1":
        char.name = input("New name: ")

    elif choice == "2":
        char.health = int(input("New health: "))

    elif choice == "3":
        char.level = int(input("New level: "))

    else:
        print("Invalid choice.")


def add_inventory_item(characters):
    char = choose_character(characters)

    if not char:
        return

    item = input("Enter item to add: ")
    char.add_item(item)

    print("Item added.\n")


def remove_inventory_item(characters):
    char = choose_character(characters)

    if not char:
        return

    if not char.inventory:
        print("Inventory empty.")
        return

    print("\nInventory:")
    for i, item in enumerate(char.inventory):
        print(f"{i + 1}. {item}")

    try:
        choice = int(input("Select item to remove: ")) - 1
        removed = char.inventory.pop(choice)
        print(f"{removed} removed.")
    except:
        print("Invalid choice.")


def main():

    characters = load_characters()

    while True:

        print("\n=== Character Management System ===")
        print("1. Create Character")
        print("2. View Characters")
        print("3. Modify Character")
        print("4. Add Inventory Item")
        print("5. Remove Inventory Item")
        print("6. Save Characters")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_character(characters)

        elif choice == "2":
            view_characters(characters)

        elif choice == "3":
            modify_character(characters)

        elif choice == "4":
            add_inventory_item(characters)

        elif choice == "5":
            remove_inventory_item(characters)

        elif choice == "6":
            save_characters(characters)

        elif choice == "7":
            save_characters(characters)
            print("Goodbye.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
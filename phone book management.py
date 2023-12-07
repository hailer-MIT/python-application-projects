class PhoneBookManager:
    def __init__(self):
        self.phone_book = {}

    def add_contact(self, name, number):
        self.phone_book[name] = number
        print(f"Contact '{name}' added.")

    def remove_contact(self, name):
        if name in self.phone_book:
            del self.phone_book[name]
            print(f"Contact '{name}' removed.")
        else:
            print(f"Contact '{name}' not found.")

    def search_contact(self, name):
        if name in self.phone_book:
            print(f"Contact '{name}': {self.phone_book[name]}")
        else:
            print(f"Contact '{name}' not found.")

# User Interactive Section
manager = PhoneBookManager()

print("Phone Book Management - User Interactive Version")
print("Commands:")
print("- 'add <name> <number>' to add a new contact")
print("- 'remove <name>' to remove a contact")
print("- 'search <name>' to search for a contact")
print("- 'quit' to exit the program")

while True:
    command = input("Enter a command: ")

    if command.startswith("add"):
        _, name, number = command.split(maxsplit=2)
        manager.add_contact(name, number)

    elif command.startswith("remove"):
        _, name = command.split(maxsplit=1)
        manager.remove_contact(name)

    elif command.startswith("search"):
        _, name = command.split(maxsplit=1)
        manager.search_contact(name)

    elif command == "quit":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid command. Please try again.")

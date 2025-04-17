def collect_contacts():

    contacts = {}

    while True:
        person = input("Name: ")
        if person == "":
            break
        phone = input("Number: ")
        contacts[person] = phone

    return contacts


def show_contacts(contacts):

    print("\nSaved Contacts:")
    for person in contacts:
        print(f"{person} -> {contacts[person]}")


def search_contacts(contacts):
    """
    Lets the user search for a contact by name.
    """
    print("\nSearch Contacts:")
    while True:
        name = input("Enter name to search: ")
        if name == "":
            break
        if name in contacts:
            print(f"{name}'s number is {contacts[name]}")
        else:
            print(f"{name} not found in contacts.")


def main():
    phonebook_data = collect_contacts()
    show_contacts(phonebook_data)
    search_contacts(phonebook_data)


if __name__ == "__main__":
    main()

class Person():
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.phone_number = ""

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, new_first_name):
        self.first_name = new_first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, new_last_name):
        self.last_name = new_last_name

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, new_phone_number):
        if len(new_phone_number) != 12:
            raise "Oopsie"
        for digit in new_phone_number:
            if digit not in "-0123456789":
                raise "Big Oopsie"
        self.phone_number = new_phone_number

    def get_info(self):
        person_info = self.first_name + " " + self.last_name + "\n"
        person_info = self.phone_number

        return person_info

class Friend(Person):
    def __init__(self):
        super().__init__()
        self.email = ""
        self.birth_date = ""

    def get_email(self):
        return self.email

    def set_email(self, new_email):
        self.email = new_email

    def get_birth_date(self):
        return self.birth_date

    def set_birth_date(self, new_birth_date):
        if len(new_birth_date) != 8:
            raise "Oopsie"
        for digit in new_phone_number:
            if digit not in "-0123456789":
                raise "Big Oopsie"
        self.birth_date = new_birth_date

    def get_info(self):
        friend_info = self.first_name + " " + self.last_name + "\n"
        friend_info = self.phone_number + "\n"
        friend_info = self.email + "\n"
        friend_info = self.birth_date

        return friend_info

def add_regular_person():
    new_person = Person()
    new_person.first_name = input("First Name -->")
    new_person.last_name = input("Last Name -->")
    new_person.phone_number = input("Phone Number 'xxx-xxx-xxxx' -->")

    return new_person

def add_friend():
    new_friend = Friend()
    new_friend.first_name = input("First Name -->")
    new_friend.last_name = input("Last Name -->")
    new_friend.phone_number = input("Phone Number 'xxx-xxx-xxxx' -->")
    new_friend.email = input("Email Address -->")
    new_friend.birth_date = input("Birth Date 'mm-dd-yy' -->")

    return new_friend

def look_up_contact_by_name():
    user_input = input("Enter Contact's Last Name -->")
    person_name = Person()
    friend_name = Friend()

    for name in person_name:
        if name == self.last_name:
            print(person_info)

    for name in friend_name:
        if name == self.last_name:
            print(friend_info)
            
        
def menu():
    print("1. Add Contact")
    print("2. Look up Contact by name")
    print("3. Exit")
            


def main():
    menu()
    menu_choice = 0
    while menu_choice != 3:
        print()
        menu_choice = int(input("Menu Choice (1-3) -->"))
        if menu_choice == 1:
            user_input = input("Do you want to add a regular person or a friend?")
            if user_input == "regular person":
                add_regular_person()
            elif user_input == "friend":
                add_friend()
            print()
            menu()
        elif menu_choice == 2:
            look_up_contact_by_name()
            print()
            menu()
        elif menu_choice == 3:
            print()

import math
import random


# Luhn algorithm for generating card number
def luhn_algorithm():
    luhn_number = [4, 0, 0, 0, 0, 0]
    luhn_number.extend(random.randint(0, 9) for i in range(9))
    # print(luhn_number)
    luhn_number_check = [j * 2 if i % 2 != 0 else j for i, j in enumerate(luhn_number, 1)]
    # print(luhn_number_check)
    luhn_number_check = [i - 9 if i > 9 else i for i in luhn_number_check]
    # print(luhn_number_check)
    check_sum = sum(luhn_number_check)
    x = 0
    while not (check_sum + x) % 10 == 0:
        x += 1
    luhn_number.append(x)
    return luhn_number


# class card database
class Database:
    name = None
    column_names = []
    attribute_data_types = []

    def __init__(self, name, column_names, attribute_data_types):
        self.name = name
        


# create a class card
class Card:
    def __init__(self):
        self.number = None
        self.pin = None
        self.balance = 0

    def create_number(self):
        self.number = ''.join(str(i) for i in luhn_algorithm())
        return self.number

    def create_password(self):
        self.pin = ''.join(str(random.randint(0, 9)) for i in range(4))
        return self.pin


# create main menu
while True:
    print()
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")
    choice = input()
    card_id = 0

    if choice == "1":
        print()
        card = Card()
        card.create_number()
        card.create_password()
        print("Your card has been created")
        print(f"Your card number:\n{card.number}")
        print(f"Your card PIN:\n{card.pin}")
    elif choice == "2":
        print()
        card_number = input("Enter your card number:\n")
        card_pin = input("Enter your pin:\n")
        if card_number == card.number and card_pin == card.pin:
            print("\nYou have successfully logged in!")

            # create a sub-menu when logged in
            while True:
                print()
                print("1. Balance")
                print("2. Log out")
                print("0. Exit")
                choice_2 = input()
                if choice_2 == "1":
                    print("Balance:", card.balance)
                elif choice_2 == "2":
                    print("\nYou have successfully logged out!")
                    break
                elif choice_2 == "0":
                    break
                else:
                    pass
            break
        else:
            print()
            print("Wrong card number or PIN")
    elif choice == "0":
        break
    else:
        pass

print("Bye!")

# card1 = Card()
# card1.create_number()
# card1.create_password()
# print(card1.number)
# print(card1.pin)




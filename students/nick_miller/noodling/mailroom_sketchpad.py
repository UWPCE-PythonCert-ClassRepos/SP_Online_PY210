# #!/usr/bin/env python3

import sys

donor_db = {
    "Jeff Staple": [20, 20],
    "Takashi Murakami": [10.50],
    "Virgil Abloh": [300, 40.33, 5.35],
    "Jan Chipchase": [1001.23, 400.87, 102]
}

# user_key = str(input("enter a name: "))
# user_key = user_key.title()
# if user_key in donor_db.keys():
#     print("tight")
# else:
#     print("no dice")


def y_or_n(u_input):
    try:
        u_input = str(u_input)
        u_input = u_input.strip().lower()
    except ValueError:
        return False
    while True:
        if u_input == "y":
            print("1")
        elif u_input == "n":
            print("2")
        elif u_input == "list":
            print(donor_db)
        elif u_input == "q":
            sys.exit()
        else:
            print("Invalid input.")
            break


def look_format(key, db):
    key = str(key)
    key = key.title()
    if key in db:
        return True
    else:
        return False


# def db_check():


def ask(question):
    question = input(question)
    return question


# user_key = input("enter a name or 'list': ")
#
# if look_format(user_key, donor_db) is True:
#     y_or_n()

q1 = "enter a name or type 'list': "
ans1 = ask(q1)
is_in = look_format(ans1, donor_db)
while is_in is True:
    q2 = "that name is in the list, do you want to send a thank you? (y/n): "
    ans2 = ask(q2)
    y_or_n(ans2)

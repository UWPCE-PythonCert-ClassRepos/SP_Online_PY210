#!/usr/bin/env python3

"""PY210_SP - mailroom part 4 - done
author: Nick Miller"""

import sys


donor_db = {
    "Jeff Staple": [20, 20],
    "Takashi Murakami": [10.50],
    "Virgil Abloh": [300, 40.33, 5.35],
    "Jan Chipchase": [1001.23, 400.87, 102]
}


def letter_prep(ver, db):
    """
    takes user input (name)
    :param ver: name (sanitized before being passed)
    :param db: a dict of donors and their donations
    :return: a list of their full name, first name, all donations, and a total
    """
    namer = ver.split(" ")
    firster = namer[0]
    monies = db[ver.title()]
    toters = sum(monies)
    toters = float(f"{toters:.2f}")
    return [firster, toters]


def letter_format(firster, toters):
    """
    takes in first name and totals and returns formatted Thank You message
    :param firster: first name, sanitized before passing
    :param toters: sum of donations, sanitized before passing
    :return: formatted, faux-personalized Thank You message
    """
    letter = ('\n'.join(['', 'Dearest {first_name},', '', 'Thank you for your generous support!',
                             'We appreciate your donation(s), which total ${donats:.2f} to date!', '',
                             'Sincerest regards,',
                             '',
                             'The Foundation'])).format(first_name=firster, donats=toters)
    return letter


def ask_user(q):
    """
    Asks a question, returns input
    :param q: a question/input request string
    :return: the user's returned input
    """
    answer = input(str(q))
    return answer


def input_prep(thanks_c):
    """
    formats user input for easier use
    :param thanks_c: a string
    :return: stripped, lowercase string
    """
    thanks_c = thanks_c.strip().lower()
    return thanks_c


def list_print(db=None):
    """
    prints the donors in a given db
    :param db: dictionary-based database of donors(key) and their donations(values)
    :return: a printed list of donors
    """
    if db is None:
        db = donor_db
    for item in db:
        print(item)


def list_check(thanks_c, db=None):
    """
    Checks the db to see if the entered donor is in it
    :param thanks_c: a sanitized/assumed donor name
    :param db: dictionary-based database of donors(key) and their donations(values)
    :return: if the thanks_c param is in the dict, it is returned for further use, otherwise, the str "not" is returned
    """
    if db is None:
        db = donor_db
    if thanks_c.title() in db.keys():
        return thanks_c
    elif thanks_c.title() not in db.keys():
        return "not"


def input_check(thanks_c):
    """
    Cleans up input when used against y/n situations
    :param thanks_c: user input
    :return: formatted user input
    """
    if thanks_c.strip().lower() == "q":
        return "q"
    elif thanks_c.strip().lower() == "y":
        return "y"
    elif thanks_c.strip().lower() == "y":
        return "n"
    elif thanks_c.strip().lower() == "list":
        return "list"
    else:
        return thanks_c


def don_add(thanks_c, db=None):
    """
    Adds a donation to existing donor, formats it
    :param thanks_c: a name to add to the db
    :param db: dictionary-based database of donors(key) and their donations(values)
    :return: updated db
    """
    if db is None:
        db = donor_db
    donats = donor_db[thanks_c.title()]
    while True:
        try:
            amount = "Add a donation amount: "
            add_donats = ask_user(amount)
            if add_donats.strip().lower() == "q":
                return
            else:
                add_donats = float(add_donats)
                donats.append(add_donats)
                break
        except ValueError:
            print("Sorry, that is not a valid amount.")


def db_update(new_item_key, new_item_value, db=None):
    """
    Updates db with new name and donations
    :param new_item_key: donor name to add
    :param new_item_value: donation to add (starts with one)
    :param db: dictionary-based database of donors(key) and their donations(values)
    :return: updated db
    """
    if db is None:
        db = donor_db
    db[new_item_key.title()] = [new_item_value]


def one_thanks(db=None):
    """
    This will generate a single thank you based on user input
    :param db: dictionary-based database of donors(key) and their donations(values)
    :return: formatted thank you text
    """
    if db is None:
        db = donor_db
    q = "Enter a name or type 'list': "
    ans = ask_user(q)
    if input_check(ans) == "list":
        list_print(donor_db)
    elif input_prep(ans) in list_check(ans):
        q = "That name is in the list, would you like to add a donation? (y/n): "
        add_or_no = input_check(ask_user(q))
        while add_or_no != "y" and add_or_no != "n" and add_or_no != "q":
            add_or_no = input("Please enter y or n: ").lower()
        if add_or_no == "y":
            don_add(ans, donor_db)
            letter = letter_prep(ans, donor_db)
            letter = letter_format(letter[0], letter[1])
            print(letter)
        elif add_or_no == "n":
            q = "Would you still like to create a thank you? (y/n): "
            answ = input_check(ask_user(q))
            while answ != "y" and answ != "n" and answ != "q":
                answ = input("Please enter y or n: ").lower()
            if answ == "y":
                letter = letter_prep(ans, donor_db)
                letter = letter_format(letter[0], letter[1])
                print(letter)
            elif ans == "n":
                return
            elif ans == "q":
                return
        elif add_or_no == "q":
            return
    elif list_check(ans) == "not":
        q = "That name is not in the list, would you like to add it? (y/n): "
        answ = input_check(ask_user(q))
        while answ != "y" and answ != "n" and answ != "q":
            answ = input("Please enter y or n: ").lower()
        if answ == "y":
            q = "Please enter a donation amount: "
            amount = float(ask_user(q))
            db_update(ans, amount, donor_db)
            letter = letter_prep(ans, donor_db)
            letter = letter_format(letter[0], letter[1])
            print(letter)
        elif answ == "n":
            return
        elif answ == "q":
            return
    elif input_check(ans) == "q":
        return


def save_file(file_name, letter_text):
    """
    borrowed from a totally diff assignment, needs re-tooled to save files for donation thank-yous
    :param file_name: name for file to be written
    :param letter_text: formatted text to be written to file
    :return: text file with Thank You letter
    """
    f = open(file_name, "w+")
    f.write(letter_text)
    f.close()


def thanks_all(db=None):
    """
    given a donor db, write thank-you files for each donor
    :param db: dictionary-based database of donors(key) and their donations(values)
    :return: a text file thank you for each donor
    """
    if db is None:
        db = donor_db
    for donor in donor_db:
        firster = letter_prep(donor, donor_db)[0]
        toters = letter_prep(donor, donor_db)[1]
        file_name = donor.lower().replace(" ", "") + ".txt"
        letter_text = letter_format(firster, toters)
        save_file(file_name, letter_text)


def confirm_all():
    """
    :return: prints an output to confirm the send-all action completed for the user
    """
    print("Individual Thank You files for each donor have been created in the same directory\n"
          "in which this programs lives/runs.")


def send_and_confirm(db=None):
    """
    Combines the send-all and confirm into a single function for call from a menu-dict
    :param db: dictionary-based database of donors(key) and their donations(values)
    :return: saves files and prints a message
    """
    if db is None:
        db = donor_db
    thanks_all(donor_db)
    confirm_all()


def report_sort_key(item):
    """
    defines a sorting key for database, stolen for part 1, might need fixed for proper dict sorting
    :param item: an index-able thing
    :return: returns index item 1 as the key to sort by
    """
    return item[1]


def get_report(db=None):
    """
    Gets/makes report based on orig dict
    :param db: dictionary-based database of donors(key) and their donations(values)
    :return: formatted dictionary with some math run on donations
    """
    if db is None:
        db = donor_db
    report_don = []
    [report_don.append((key, sum(db[key]), len(db[key]), float(sum(db[key])/len(db[key])))) for key in db]
    report_don.sort(key=report_sort_key, reverse=True)
    return report_don


def display_report(report_dict):
    """
    this functions takes in a donor database and returns a formatted report
    :param report_dict: input dict - formatted data from db
    :return: formatted report, based on db data; sum of donations, total num of donations, average donation/name
    """
    key = ["name", "total given", "num gifts", "average gift"]
    separator = "|"
    print(f"{key[0]:<18}",
          f"{separator:^3}",
          f"{key[1]:^18}",
          f"{separator:^3}",
          f"{key[2]:^10}",
          f"{separator:^3}",
          f"{key[3]:>15}")
    print("-" * 76)
    for row in report_dict:
        print("{:<18s}   {:>15.2f}   {:13.0f}   {:>20.2f}".format(*row))


def report():
    """
    Combines report visual formatting with report data formatting
    :return: a completed report
    """
    display_report(get_report(donor_db))


def quit_prog():
    """
    used to trigger program quit
    :return: ends program
    """
    return "exit menu"


def menu_selection(prompt, dispatch_dict):
    """
    :param prompt: requests user input for a given prompt
    :param dispatch_dict: a dispatch dict of functions corresponding to choices
    :return: menu loops until "exit menu" is called
    """
    while True:
        response = input(prompt)
        response = response.lower().strip()
        while response != "1" and response != "2" and response != "3" and response != "4" and response != "q":
            print("That's not a valid input.")
            response = input(prompt)
        if dispatch_dict[response]() == "exit menu":
            break


main_prompt = ("""
Menu of Options
1) Send a 'Thank You' to a single donor
2) Send 'Thank You' letters to all donors
3) Create a Report
4) Exit Program
>>> Enter a selection please: 
""")

menu_dict = {"1": one_thanks,
             "2": send_and_confirm,
             "3": report,
             "4": quit_prog,
             "q": quit_prog}

if __name__ == "__main__":
    menu_selection(main_prompt, menu_dict)

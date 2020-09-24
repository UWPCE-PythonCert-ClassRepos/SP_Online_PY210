#!/usr/bin/env python3
# Mailroom3.py - Lesson05 Assignment - Exceptions and Comprehensions

import sys
import pathlib

donar_db = {"Mike": [200, 150, 50],
            "Tony": [150, 50, 250],
            "Sara": [150, 150, 150],
            }

main_prompt = "\n".join(("", "Welcome to the donars list",
                         "Please choose from below options:",
                         "s - Send a thank you",
                         "c - Create a report",
                         "sa - Send a letter to all the donars",
                         "q - Quit",
                         "Type a number to select >>> "))

ty_prompt = "\n".join(("", "Please type the full name of the donar OR",
                       "type 'list' to see a list of donars",
                       "Type input here >>>"))

ty_message = "\n".join(("", "Dear {}",
                        "Thank you for your generous donation of {:.2f}",))

letter = "\n".join(("", "Dear {},", "",
                    "    Thank you for your very kind donations totaling ${:.2f}.", "",
                    "    It will be put to very good use.", "",
                    "               Sincerely,",
                    "                  - The team"))


def exit_program():
    print('\nShutting down the program\n')
    sys.exit()


def thank_you():
    thank_you_name = input(ty_prompt)
    if thank_you_name == 'list':
        report()
    '''Exception added to ensure donation amount is a number'''
    amt = input("Please enter the donation amount >>>")
    try:
        amt = float(amt)
    except ValueError:
        print('\n--->Not a valid amount, please try your submission again')
    else:
        if donar_db.get(thank_you_name) is None:
            donar_db[thank_you_name] = [amt]
        else:
            donar_db.get(thank_you_name).append(amt)
        input(ty_message.format(thank_you_name, amt))
        print('')


def report():
    print('')
    head = '{:20}| {:>15}|{:>15}| {:>15}'.format(
        'donar Name', 'Total Given', 'Num Gifts', 'Average Gift')
    print(head)
    print('-'*72)

    for key, value in sorted(donar_db.items(), key=lambda i: sum(i[1]), reverse=True):
        line = '{:20} ${:>15.2f}  {:>15}  ${:15.2f}'.format(
            key, sum(value), len(value), (sum(value)/len(value)))
        print(line)
    print('')
    main()


def send_letter():
    for key, value in sorted(donar_db.items(), key=lambda i: sum(i[1]), reverse=True):
        form_letter = letter.format(key, sum(value))
        file_name = key.replace(" ", "_") + ".txt"
        pth = pathlib.Path('./')
        dest = pth.absolute() / file_name
        with open(dest, 'w') as outfile:
            outfile.write(form_letter)


# Switch function dict
switch_func_dict = {
    "s": thank_you,
    "c": report,
    "sa": send_letter,
    "q": exit_program,
}


def main():
    while True:
        response = input(main_prompt)
        try:
            switch_func_dict.get(response.lower())()
        except (ValueError, TypeError):
            print('\n--- -> Invalid Selection: Please select a correct input option.')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# Mailroom3.py - Lesson05 Assignment - Exceptions and Comprehensions

import sys
import pathlib

donor_db = {"Scrooge McDuck": [8000.00, 70000.00],
            "Montgomery Burns": [49.53],
            "Richie Rich": [1000000.00, 500000.00],
            "Chet Worthington": [200.00, 44387.63, 10200.00],
            "Silas Skinflint": [0.25, 1.00, 0.43]}

main_prompt = "\n".join(("", "Welcome to the donors list",
          "Please choose from below options:",
          "1 - Send a thank you",
          "2 - Create a report",
          "3 - Send a letter to all the donors",
          "4 - Quit",
          "Type a number to select >>> "))

ty_prompt = "\n".join(("", "Please type the full name of the donor OR",
        "type 'list' to see a list of donors",
        "Type input here >>>"))

ty_message = "\n".join(("", "Dear {}",
        "Thank you for your generous donation of {:.2f}",))

letter = "\n".join(("", "Dear {},","",
        "    Thank you for your very kind donations totaling ${:.2f}.","",
        "    It will be put to very good use.","",
        "               Sincerely,",
        "                  - The team"))

def exit_program():
    print('\nShutting down the program\n')
    sys.exit()

def thank_you():
    tyname = input(ty_prompt)
    if tyname == 'list':
        report()
    '''Exception added to ensure donation amount is a number'''
    amt = input("Please enter the donation amount >>>")
    try:
        amt = float(amt)
    except ValueError:
        print('\n--->Not a valid amount, please try your submission again')
    else:
        if donor_db.get(tyname) is None:
            donor_db[tyname] = [amt]
        else:
            donor_db.get(tyname).append(amt)
        input(ty_message.format(tyname, amt))
        print('')


def report():
    print('')
    head = '{:20}| {:>15}|{:>15}| {:>15}'.format('Donor Name', 'Total Given','Num Gifts', 'Average Gift')
    print(head)
    print('-'*72)

    for key,value in sorted(donor_db.items(),key=lambda i:sum(i[1]),reverse=True):
        line = '{:20} ${:>15.2f}  {:>15}  ${:15.2f}'.format(key, sum(value),len(value), (sum(value)/len(value)))
        print(line)
    print('')
    main()

def send_letter():
    for key,value in sorted(donor_db.items(),key=lambda i:sum(i[1]),reverse=True):
        form_letter = letter.format(key, sum(value))
        file_name = key.replace(" ", "_") + ".txt"
        pth = pathlib.Path('./')
        dest = pth.absolute() / file_name
        with open(dest, 'w') as outfile:
            outfile.write(form_letter)

# Switch function dict
switch_func_dict = {
    1: thank_you,
    2: report,
    3: send_letter,
    4: exit_program,
}

################## PRIMARY CODE BLOCK ######################################################3

# DELETE NOTE: home dir /Python_Cert/classrepo/SP_Online_PY210/students/adam_strong/lesson05
def main():
    while True:
        response = input(main_prompt)
        #switch_func_dict.get(int(response))()
        ''' Exception added to catch a non 1-4 value'''
        try:
            switch_func_dict.get(int(response))()
        except (ValueError,TypeError):
            print('\n----> Invalid Selection: Please input a number 1-4')

if __name__ == '__main__':
    # Guards against running automatically if this script is imported
    main()
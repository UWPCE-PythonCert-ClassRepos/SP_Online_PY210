#!/usr/bin/env python3
#Mailroom part 1
import sys  # imports go at the top of the filew

#donors
donor_db = [
    ("Krystal Perez", [50.00, 250.00]),
    ("Eddie Lau", [32.50]),
    ("Jimmy Jack", [200.00, 350.00, 400.00]),
    ("Grace Cool", [120.00, 75.00]),
    ("Adriel Molina", [45.00, 450.00]),
    ]

# menu prompt
prompt = "\n".join(("Welcome to the Mail Room!",
          "Please choose from below options:",
          "1 - Send a Thank you",
          "2 - Create a report",
          "3 - Exit",
          ">>> "))

#segregate donors
def list_donors():
    for i in range(len(donor_db)):
        print("{}".format(donor_db[i][0]))

# Send a thank you
def send_thanks():
    print("To view current donors, type 'list' ")
    names = input("Please provide the Full Name of a donor:")
    if names.lower() == 'list':
        list_donors()
        send_thanks()
    else:
        amount = get_amount()
        for donor in donor_db:
            if donor_db[0] == names:
                donor.append((names, amount))
                break
        else:
            donor_db.append((names,[amount]))
            email(names, amount)

#Creating a thank you email
def email(names, amount):
    print ("\n\nDear {}:\n Thank you for your generosity in the amount of ${}, we truly appreciate your support to our charity. \n Sincerely, \n MailRoom Team\n".format(names, amount))
    main()

#get the donation amounts
def get_amount():
        amount = float(input("please enter donation amounts : "))
        return amount

#create a report that calculate Donor Name, Total Given, Number of donatons, and the avarage amount of thier donations
def report():
    Title = "\n{:<12}{:<6}{:<15}{}{:<10}{}{:<10}".format(*('Donor Name','|','Total Given','|','Num Gifts','|','Average Gift'))
    print(Title)
    print ('-'*len(Title))
    donor_db_sort = sorted(donor_db, key = sorting, reverse = True)
    for everything in donor_db_sort:
        total = sum(everything[1])
        num = len(everything[1])
        average = total/num
        print('{:<18} ${:>12,.2f}{:>13}  ${:>12,.2f}'.format(everything[0],total,num,average))
    print('')


def sorting(everything):
    return sum(everything[1])

def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script


def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            send_thanks()
        elif response == "2":
            report()
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")


if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()

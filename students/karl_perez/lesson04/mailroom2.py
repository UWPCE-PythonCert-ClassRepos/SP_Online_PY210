#!/usr/bin/env python3
#Mailroom part 2
import sys  

#donors
donor_d = {
    "Krystal Perez": [50.00, 250.00],
    "Eddie Lau": [32.50],
    "Jimmy Jack": [200.00, 350.00, 400.00],
    "Grace Cool": [120.00, 75.00],
    "Adriel Molina": [45.00, 450.00],
    }

# menu prompt
prompt = "\n".join(("Welcome to the Mail Room!",
          "Please choose from below options:",
          "1 - Send a Thank You to a single donor.",
          "2 - Create a report",
          "3 - Send letters to all donors",
          "4 - Quit"
          ">>> "))

#menus
def menu(prompt, dispatch):
    while True:
        user_response = input(prompt)
        if user_response in dispatch:
            dispatch[user_response]()
        else:
            print("Please select a valid option")

#segregate donors
def list_donors():
	for key in donor_d.keys():
	   print(key)
	   print("")

# Send a thank you
def send_thanks():
    print("To view current donors, type 'list' ")
    names = input("Please provide the Full Name of a donor:")
    if names.lower() == 'list':
        list_donors()
    else:
         amount = input("Please enter a donation amount:\n")
         if names in donor_d:
            donor_d[names].append(float(amount))
         else:
            donor_d.update({names: [float(amount)]})
        #Try to use a dict and the .format() method to produce the letter as one big template, rather than building up a big string that produces the letter in parts.
         letterdict = {"donor_name": names, "donation_amount": float(amount)}
         print("Dear {donor_name}, we appreciate your generosity in the donation amount of ${donation_amount:.2f}.\n".format(**letterdict))


#create a report that calculate Donor Name, Total Given, Number of donatons, and the avarage amount of thier donations
def write_a_report():
    Title = "\n{:<12}{:<6}{:<15}{}{:<10}{}{:<10}".format(*('Donor Name','|','Total Given','|','Num Gifts','|','Average Gift'))
    print(Title)
    print ('-'*len(Title))
    donor_db_sort = sorted(donor_d, key = sorting, reverse = True)
    for everything in donor_db_sort:
        total = sum(donor_d.get(everything))
        num = len(donor_d.get(everything))
        average = total/num
        print('{:<18} ${:>12,.2f}{:>13}  ${:>12,.2f}'.format(everything,total,num,average))
    print('')


def sorting(everything):
    return sum(donor_d.get(everything))

def send_letters_all():
    for a, b in donor_d.items():
        text = f"Dear {a},\nOn behalf of our team, we want extend our gratitude for your donation in the amount of ${b[-1]:.2f}. Your total donations are ${sum(b):.2f}.\nAll proceeds will go to help the Save the Puppies Charity.\nThanks, the Team."
        with open(f"{a}.txt", "w") as f:
            f.write(text)

def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script

dispatch = {"1": send_thanks, "2": write_a_report, "3": send_letters_all, "4": exit_program}

if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
     menu(prompt, dispatch)

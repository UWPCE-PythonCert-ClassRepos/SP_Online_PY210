#! python
#------------------------------------------------
# Lesson 5 - Assignment 4: Mailroom, Part 3
#------------------------------------------------

import sys
from operator import itemgetter
from datetime import date

#This dictionary database contains the donor names and a history of their donation amounts.
donor_db = {"Jennifer Lee" : [1350.0, 120.17],
            "Linda Anderson" : [877.33],
            "Melissa Carey" : [663.23, 43.87, 1.32],
            "Dmitriy Mikutin" : [1663.23, 4300.87, 10432.0],
            "John Palmer" : [3312.00, 5500.00],
            "Henry Ma" : [250.75, 120.00, 55.50, 100.50]
            }

def menu_selection(prompt, dispatch):
    #This function will ask the user to choose an option from the menu,
    #and call the associated function in the dispatch dictionary.
    while True:
        response = input(prompt)
        if response in dispatch:
            dispatch[response]()
        else:
            print("That is not a valid option!")

def show_donor_list():
    #This function will show all donors.
    for name in donor_db:
        print(name)

def add_donation(name, amount):
    #This function will add a donation amount of a donor. If the donor does
    #not exist, it will add to donor_db{} first.
    donor_db.setdefault(name, []).append(amount)


def letter_to_donor(donor_name, amount, template_number):
    #This function will compose a letter to a donor. The template number indicates
    #which letter template to use.
    #   return letter in a string
    letter_layout = {"donor_first_name" : donor_name.split()[0],
                     "donation_amount" : amount,
                     "sender_name" : "Tiffany Kurnett",
                     "sender_title" : "President & CEO",
                     "sender_alignment" : ' '*25,
                     "new_paragraph_indent" : '\n   ',
                     "date" : date.today()
                    }
    sender_template = "\n".join(("\n\n\n\n{sender_alignment}Sincerely,",
                      "{sender_alignment}{sender_name}",
                      "{sender_alignment}{sender_title}",
                      "\n\n\n"))
    new_donation_template = "\n".join(("Dear {donor_first_name},",
                            "{new_paragraph_indent}Thank you for your generous gift of ${donation_amount:.2f} to support the work of ChangeALife. Your",
                            "donation will remain in your local community and be used by ChangeALife to provide programs",
                            "and services to those in need.",
                            "{new_paragraph_indent}On behalf of those whose lives will be impacted, please accept our sincere gratitude. May ",
                            "you know the deep satisfaction of having made a difference in the lives of others.",
                            "\n\n",
                            "Below is a summary of your gift.",
                            "",
                            "Amount: ${donation_amount:.2f}",
                            "Date: {date:%m-%d-%Y}",
                            sender_template)).format(**letter_layout)
    donation_history_template = "\n".join(("Dear {donor_first_name},",
                                "{new_paragraph_indent}Whether you are a new donor or have suppported ChangeALife for many years, your compassionate",
                                "generosity gives us the vital resource to provide programs and services to those in need. I hope",
                                "you will continue to support our work at ChangeALife. Your support means the world to the families",
                                "and people we serve.",
                                "{new_paragraph_indent}On behalf of those whose lives will be impacted and from all of us at ChangeALife, THANK YOU!",
                                "\n\n"
                                "Below is a summary of your gift.",
                                "",
                                "Amount: ${donation_amount:.2f}",
                                sender_template)).format(**letter_layout)

    templates = {1 : new_donation_template,      #to donor who had just made a donation
                 2 : donation_history_template   #for historical donations
                }
    return templates.get(template_number)

def send_a_thank_you():
    #This function will first prompt user for a donor's name, or type list to see
    #all donors. After a name is entered, it will prompt for a donation amount to
    #be added. At the end, a 'Thank You' letter will go out to the donor. The user
    #may choose to quit at anytime by typing 'q' at the prompt, and it will take
    #the user back to the main menu. For now, the letter will print to the terminal.
    prompt1 = "\n".join(("Please enter a full name or type 'list' to see all donors or q to quit:",
              ">>> "))
    prompt2 = "\n".join(("Please enter a donation amount or q to quit:",
              ">>> "))
    prompt3 = "\n".join(("Please enter a valid amount greater than zero or q to quit:",
              ">>> "))

    while True:
        name = input(prompt1)
        if name == 'list':
            show_donor_list()
        elif name == "q":
            return
        elif name:
            break
        else:
            continue

    while True:
        amount = input(prompt2)
        if amount == "q":
            return
        try:
            amount = float(amount)
        except ValueError:
            prompt2 = prompt3
            continue
        else:
            if amount > 0:
                break
            else:
                prompt2 = prompt3
                continue

    add_donation(name, amount)
    print(letter_to_donor(name, amount, 1))

def create_a_report():
    #This function will create a summary report to list all donors, their total donation
    #amount, number of donations and average amount. It will show in the order of total
    #donation amount from highest to lowest.
    summary = [(name, sum(amount), len(amount)) for (name, amount) in donor_db.items()]
    summary = sorted(summary, key=itemgetter(1), reverse=True)          #Sort by total donated from highest to lowest

    header = "{:<25s} | {:11s} | {:9s} | {:12s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(header)
    print(f"{'-'*len(header):s}")

    row = "{name:<25s}  ${total_donated:11.2f}  {gift_count:10d}  ${avg_amount:12.2f}".format
    for col in summary:
        print(row(name=col[0], total_donated=col[1], gift_count=col[2], avg_amount=col[1]/col[2]))
    print()

def send_letters_to_all_donors():
    #This function will write a letter to each donor into a file, and the file will be
    #created in the directory that the program is running on.
    for name, amounts in donor_db.items():
         filename = name.replace(" ", "_") + ".txt"
         with open(filename, 'w') as out_file:
             out_file.write(letter_to_donor(name, sum(amounts), 2))

def exit_program():
    print("Exiting the Mailroom program...")
    sys.exit()  # exit the interactive script

def main():
    #This function will call the menu_selection to prompt user to choose
    #a task from the menu.
    prompt = "\n".join(("Welcome to the ChangeALife Mailroom!",
             "Please choose from below options:",
             "1 - Send a Thank You to a donor",
             "2 - Create a Report",
             "3 - Send letters to all donors",
             "4 - Exit",
             ">>> "))
    dispatch = {"1" : send_a_thank_you,
                "2" : create_a_report,
                "3" : send_letters_to_all_donors,
                "4" : exit_program
               }
    menu_selection(prompt, dispatch)



if __name__ == "__main__":
    main()

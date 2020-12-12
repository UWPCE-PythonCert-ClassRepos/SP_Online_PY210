### Lesson_5 - Mailroom Part 3

from textwrap import dedent
import tempfile
import sys

donor_db = {'Jimmy Hendrix' : [23.23, 24.48],
            'Jack White' : [32.84, 48],
            'Keith Richards' : [68],
            'Jimmy Page' : [34, 89],
            'Albert Hamond' : [34, 64, 49],
            }

prompt = "\n".join(("Please select from the following options",
         "1 - Send a Thank You",
         "2 - Create a Report",
         "3 - Thank All",
         "4 - Quit",
         ">>> "))

def main():
    prompt_action = {"1" : thank_you,
                     "2" : report,
                     "3" : thank_all,
                     "4" : exit_program }

    while True:
        response = input(prompt)  
        try:
            prompt_action[response]()
        except KeyError:
            print ("try again")

def exit_program():
    print("Peace!")
    sys.exit()
    

def thank_you():

    while True:
        name = input("Please input donors full name or type 'list' to display existing registry: ")
        if name.lower() == 'list':
            print_donors()
            continue
        else:
            amount = float(input("Please donation amount: "))
            existing_donor = False
            if name.strip() in donor_db.keys():
                donor_db[name].append(amount)
            else:
                donor_db[name] = [amount]
            try:
                    if amount == 0:
                        print("Please enter none zero value!")
                    else:
                       print(thank_you_letter(name)) 
            except TypeError:
                print("Please input respones")
                print("\n")
                return 1
            break


def thank_all():
    """
    Generate thank-you emails to all donors in database
    :param donors: dictionary of donors
    :return: write email text to file for each donor
    """

    for donor in donor_db.keys():
        total_donated = round(sum(donor_db[donor]), 2)
        most_recent_donation = donor_db[donor][0]
        email_message = f"Dear {donor},\nThank you for your recent donation of ${most_recent_donation}! In total, " \
            f"you've donated {total_donated}!\n\n"
         
        with tempfile.TemporaryFile(mode='w+') as email_file:
            email_file.writelines(email_message)
            email_file.seek(0)
            print(email_file.read())


def thank_you_letter(name):
    return dedent('''
                Dear {},
                    Thank for your generous donation!!  Your
                    contribution is greatly appreciated.

                    Truly yours,

                    Guitar Greats.
                '''.format(name))

def print_donors():
    print("Donor list:\n")
    for donor in donor_db:
        print(donor)



def report():
    """Output a list of donors sorted by total donation amount."""
    # print header
    print("{:^25} | {:^15} | {:^9} | {:^15}".format(
        "Name", "Total Given", "Num Gifts", "Average Gift"))
    print("{:->73}".format(""))

    
    donors_sorted = sorted(donor_db.items(),
                           key=lambda i: sum(i[1]), reverse=True)

    
    for name, donate in donors_sorted:
        total = sum(donate)
        num = len(donate)
        avg = sum(donate) / len(donate)
        print("{:<25} | {:>15.2f} | {:>9} | {:>15.2f}".format(
            name, total, num, avg))
        



if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()

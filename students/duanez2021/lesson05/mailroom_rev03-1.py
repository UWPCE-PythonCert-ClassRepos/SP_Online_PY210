#######################################################################################################
# date          init    desc
# 20200625      djm     mail room part 1
# 20200707      djm     mail room part 2 (Dictionary implementations)
# 20200803      djm     mail room part 3, Lesson 5, exceptions and comprehensions
# 20200824      djm     mail room part 3 (comments from  natasha-aleksandrova 13 days ago)
#                       updating part 3 with changes from part 2 (see mailroom_rev02-1.py)
#               your data structure in lesson04 should be using a dictionary for donors data structure
# Changes:
#   donor_db to a dictionary object (see mailroom_rev02-1.py)
# Replaced:
#   replaced these functions from from mailroom_rev02-1.py to use dictionary objects
#   create_required_report
#   added get_sum_donations
#   get_number_of_donations
#   get_avg_donation_amt
#   check_donor_name
#   list_donors
#   add_new_donor
#   resolve_donor_name
#   add_donor_amt
#   prep_individual_email
#   send_email_to_all
#
#   additional changes (for lesson 5)
#   add_donor_amt (added try-block to catch entry of inappropriate amount values)
#   prep_individual_email (added try-block to catch error raised by add_donor_amt)
#   send_email_to_all list (added list comprehension)
#   main (added try-block to catch error raised by inappropriate menu value entries)
#
#   Duane McCollum Python self-paced winter 2020
#
#######################################################################################################
# original donor db, was a list

import sys, os  # imports go at the top of the file
#print(os.getcwd())
donor_db = {"William Gates, III": [653772.32, 12.17],
            "Jeff Bezos": [877.33],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
            "Catherine Zeta-Jones": [100.00, 100.00, 1000.00]
            }

new_prompt = "\n".join(("Choose an action:\n",
                    "1 - Send a Thank You to a single donor.",
                    "2 - Create a Report.",
                    "3 - Send letters to all donors.",
                    "4 - Quit\n",
                    ">>> "))


thankyou_2_prompt = "Send thank you to (full name)\n(Enter \'list\' for list of donors;\n\'exit\' to return to main menu): "
thankyou_for_amt_prompt = ("Donation amount: ")

def create_required_report():
    print('{0: <20}{1} {2: >12} {3} {4: ^10} {5} {6: >13}'.format('Donor Name','|', 'Total Given','|', 'Num Gifts','|','Average Gift'))
    print('{:''^66}'.format(' '))
    for idx, donor_name in enumerate(donor_db):
        t = (donor_name, get_sum_donations(donor_name), get_number_of_donations(donor_name), get_avg_donation_amt(donor_name))
        strFormat = '{0: <20.20}${1: >13,.2f}  {2:^11}  ${3:> 13,.2f}'
        print(strFormat.format(t[0], t[1], t[2], t[3]))
    print('\n')
    return True


def get_sum_donations(donor_name):
    sum_amt = sum(donor_db[donor_name])
    return sum_amt

def get_number_of_donations(donor_name):
    n = len(donor_db[donor_name])
    return n

def get_avg_donation_amt(donor_name):
    sm = get_sum_donations(donor_name)
    n = get_number_of_donations(donor_name)
    return round(sm/n, 2)

#check_donor_name('Jeff Bezos')
def check_donor_name(donor_name):
    """this function returns True if the
        donor name is found in the donor_db.
    """
    b = False
    for idx, dname in enumerate(donor_db):
        if donor_name.lower() == dname.lower():
            b = True
    return b

def list_donors():
    """ this function prints a list of donor names
        from the donor_db.
    """
    for idx, donor_name in enumerate(donor_db):
        print('{:<25}'.format(donor_name))

def add_new_donor(donor_name, amt):
    """ if the donor name is not in the donor_db
        add the name and the amount they donated.
    """
    if not check_donor_name(donor_name):
        donor_db[donor_name] = [float(amt)]
    return True

def resolve_donor_name(donor_name):
    """ this function returns the exact name
        found in the donor_db given a
        donor name. used for the email
        created for the donor with the proper
        capitalization/punctuation
        20200824 updated to use dictionary object
    """
    for idx, dname in enumerate(donor_db):
        if donor_name.lower() == dname.lower():
            return dname


def add_donor_amt(donor_name, amt):
    """ added try block for non-numeric amount entries
        and for amount entries LT zero
        20200804 lesson 05
        20200824 Changed to use dictionary objects"""
    for idx, dname in enumerate(donor_db):
        if donor_name.lower() == dname.lower():
            try:
                amt = float(amt)
            except ValueError:
                raise ValueError('enter a numeric amount')
            else:
                if amt <= 0:
                    raise ValueError('enter an amount > 0')
                else:
                    donor_db[dname].append(float(amt))
    return True


def prep_individual_email():
    """ added raise error on invalid  amt
        20200804 lesson 05
        20200824 updated to use dictionary object"""
    while True:
        thankyou_to_name = input(thankyou_2_prompt)
        while thankyou_to_name.lower() == "list":
            list_donors()
            thankyou_to_name = input(thankyou_2_prompt)
        if thankyou_to_name.lower() == "exit":
            break
        if not check_donor_name(thankyou_to_name):
            print("This is a new donor")
            amt = input(thankyou_for_amt_prompt)
            try:
                add_new_donor(thankyou_to_name, amt)
            except ValueError as e:
                print('\n{0} {1}\n'.format('Amount Error: ', str(e)))
            else:
                print('\n{0}\n'.format('Preparing email to: ', send_email(thankyou_to_name, True)))
        else:
            # existing donor
            amt = input(thankyou_for_amt_prompt)
            try:
                add_donor_amt(thankyou_to_name, amt)
            except ValueError as e:
                print('\n{0} {1}\n'.format('Amount Error: ', str(e)))
            else:
                print('\n{0}\n'.format('Preparing email to: ', send_email(thankyou_to_name, True)))
    return False
# donor_db
# prep_individual_email()


def send_email(donor_name, verbose_mode):
    """ 20200824 updated to use dictionary object"""
    donor_name = resolve_donor_name(donor_name)
    print('Creating emails to {}.'.format(donor_name))
    # for a single name, create an email file for each of their donations
    n = get_number_of_donations(donor_name)
    for idx, amt in enumerate(donor_db[donor_name]):
        template = 'Dear {:}, \n\n' '\t\tThank you for your very kind donation of ${:,.2f}.'
        template += '\n\n\t\tIt will be put to very good use.\n\n'
        template += '\t\t\tSincerly,\n\n'
        template += '\t\t\t\t-The Team.\n'
        email = template.format(donor_name, float(amt))
        # print(template.format(s, float(donor_db[idx][1][x])))
        if verbose_mode:
            print(email)
        # write email to file
        fname = donor_name + '_' + str(idx + 1) + 'of' + str(n) + '.txt'
        with open(fname, 'w') as f:
            f.write(email)
    return donor_name


def send_email_to_all():
    """ updated send_email_to_all
        to use dictionary object
        20200804 lesson 05"""
        # for a single name, create an email file for each of their donations
    x = [send_email(str(s), False) for s in donor_db]

def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script

# main prompt switching dictionary
main_prompt_dict = {1: prep_individual_email, 2: create_required_report, 3: send_email_to_all, 4: exit_program}


def main():
    while True:
        try:
            response = input(new_prompt)
            func = main_prompt_dict.get(int(response), lambda: print("Invalid Menu Choice. Menu choices are 1 thru 4."))
            func()
        except ValueError as err:
            print('Menu choices are 1 thru 4.')
        finally:
            False

if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()
# commit
#

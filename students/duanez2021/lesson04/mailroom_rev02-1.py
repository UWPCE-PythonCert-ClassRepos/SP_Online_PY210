#######################################################################################################
# 20200625      djm mail room part 1
# 20200707      djm mail room part 2 (Dictionary implementations)
# 20200821      djm mail room part 2 (comments from  natasha-aleksandrova 13 days ago)
#               your data structure in lesson04 should be using a dictionary for donors data structure
# Duane McCollum Python self-paced winter 2020
#
# Update your mailroom program to:
#
#         Use dicts where appropriate.
#         See if you can use a dict to switch between the user’s selections.
#         See if you can use a dict to switch between the users selections.
#         see Using a Dictionary to switch for what this means.
#         Convert your main donor data structure to be a dict.
#         Try to use a dict and the .format() method to produce the letter as one big template,
#         rather than building up a big string that produces the letter in parts.
#
#######################################################################################################
# original donor db, was a list
import sys, os  # imports go at the top of the file
donor_db = {"William Gates, III": [653772.32, 12.17],
            "Jeff Bezos": [877.33],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Mark Zuckerberg":[1663.23, 4300.87, 10432.0]
            }
# get the len of the list of donor amts


new_prompt = "\n".join(("Choose an action:\n",
                    "1 - Send a Thank You to a single donor.",
                    "2 - Create a Report.",
                    "3 - Send letters to all donors.",
                    "4 - Quit\n",
                    ">>> "))


thankyou_2_prompt = "Send thank you to (full name)\n(list for list, exit to return to main menu): "
thankyou_for_amt_prompt = ("Donation amount: ")

def create_required_report():
    print('{0: <20}{1} {2: >12} {3} {4: ^10} {5} {6: >13}'.format('Donor Name','|', 'Total Given','|', 'Num Gifts','|','Average Gift'))
    print ('{:''^66}'.format(' '))
    t = ()
    for idx, donor_name in enumerate(donor_db):
        t = (donor_name, get_sum_donations(donor_name), get_number_of_donations(donor_name),get_avg_donation_amt(donor_name))
        strFormat = '{0: <20.20}${1: >13,.2f}  {2:^11}  ${3:> 13,.2f}'
        print(strFormat.format(t[0], t[1], t[2], t[3]))
    print('\n')
    return True

def get_sum_donations(donor_name):
    sum_amt= sum(donor_db[donor_name])
    return sum_amt

def get_number_of_donations(donor_name):
    n = len(donor_db[donor_name])
    return n

def get_avg_donation_amt(donor_name):
    avrg = 0
    sm = get_sum_donations(donor_name)
    n = get_number_of_donations(donor_name)
    return round(sm/n, 2)


def check_donor_name(donor_name):
    b = False
    for i, j in enumerate(donor_db):
        if donor_name.lower() == j.lower():
            b = True
    return b

def list_donors():
    for idx, donor_name in enumerate(donor_db):
        print('{:<25}'.format(donor_name))

def add_new_donor(donor_name, amt):
    if not check_donor_name(donor_name):
        donor_db[donor_name]=[float(amt)]
    return True

def resolve_donor_name(donor_name):
    if check_donor_name(donor_name):
        for idx, dname in enumerate(donor_db):
            if donor_name.lower() == dname.lower():
                return dname
    else:
        return False #and raise an error

def add_donor_amt(donor_name, amt):
    donor_db[donor_name].append(float(amt))
    return True

def prep_individual_email():
    while True:
        thankyou_to_name = input(thankyou_2_prompt)
        while thankyou_to_name.lower() == "list":
            list_donors()
            thankyou_to_name = input(thankyou_2_prompt)
        if thankyou_to_name.lower() == "exit":
            break
        if not check_donor_name(thankyou_to_name):
            print("This is a new donor:")
            amt = input(thankyou_for_amt_prompt)
            add_new_donor(thankyou_to_name, amt)
        else:
            amt = input(thankyou_for_amt_prompt)
            add_donor_amt(thankyou_to_name, amt)
        # update data with new amount
        send_email(thankyou_to_name)
        # print("Send email to " + thankyou_to_name + ' for ' + str(amt))
    return False

#os.chdir("\\\\Nw\\data\\MMA_3D_PDF\\A005_2020")
#print(os.getcwd())
def send_email(donor_name):
    donor_name = resolve_donor_name(donor_name)
    print('Creating emails to {}.'.format(donor_name))
    # for a single name, create an email file for each of their donations
    n = get_number_of_donations(donor_name)
    for idx, amt in enumerate(donor_db[donor_name]):
        template = 'Dear {:}, \n\n' '\t\tThank you for your very kind donation of ${:,.2f}.'
        template += '\n\n\t\tIt will be put to very good use.\n\n'
        template += '\t\t\tSincerly,\n\n'
        template += '\t\t\t\t-The Team.\n'
        #= idx
        email = template.format(donor_name,float(amt))
        # print(template.format(s, float(donor_db[idx][1][x])))
        print(email)
        fname = donor_name + '_' + str(idx + 1) + 'of' + str(n) + '.txt'
        with open(fname, 'w') as f:
            f.write(email)
            f.close()
    return True


def send_email_to_all():
    # for a single name, create an email file for each of their donations
    for idx, donor_name in enumerate(donor_db):
        send_email(donor_name)
    return True


def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script

# main prompt switching dictionary
main_prompt_dict = {1: prep_individual_email, 2: create_required_report, 3: send_email_to_all, 4: exit_program}

def main():
    while True:
        response = input(new_prompt)
        func = main_prompt_dict.get(int(response), lambda: print("Invalid Entry"))
        func()

if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()
# commit
#


import sys  # imports go at the top of the file

##############################################################
# 20200625      djm mail room part 1
# Duane McCollum Python self-paced winter 2020
#
#     If the user (you) selects “Send a Thank You” option, prompt for a Full Name.
#
# Send a Thank You
#
#      If the user (you) selects “Send a Thank You” option, prompt for a Full Name.
#          If the user types list show them a list of the donor names and re-prompt.
#          If the user types a name not in the list, add that name to the data structure and use it.
#          If the user types a name in the list, use it.
#      Once a name has been selected, prompt for a donation amount.
#          Convert the amount into a number; it is OK at this point for the program to crash if someone types a bogus amount.
#          Add that amount to the donation history of the selected user.
#      Finally, use string formatting to compose an email thanking the donor for their
#      generous donation. Print the email to the terminal and return to the original prompt.
# #
#############################################################

donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0])
            ]

prompt = "\n".join(("Mailroom program:",
          "Please choose from these options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Quit\n",
          ">>> "))


thankyou_2_prompt = "Send thank you to (full name)\n(list for list, exit to return to main menu): "
thankyou_for_amt_prompt = ("Donation amount: ")


def create_simple_report(db):
    for i, j in enumerate(donor_db):
        name = donor_db[i][0]
        for k, m in enumerate (donor_db[i][1][:]):
            amt = donor_db[i][1][k]
            print('{:<25}' '${:>15,.2f}'. format(name, amt))
    #print ('\n')


def create_required_report(db):
    print('{0: <20}{1} {2: >12} {3} {4: ^10} {5} {6: >13}'.format('Donor Name','|', 'Total Given','|', 'Num Gifts','|','Average Gift'))
    print ('{:''^66}'.format(' '))
    t = ()
    for i, j in enumerate(db):
        name = donor_db[i][0]
        t = (name, get_sum_donations(db, name), get_number_of_donations(db, name),get_avg_donation_amt(db, name))
        strFormat = '{0: <20.20}${1: >13,.2f}  {2:^11}  ${3:> 13,.2f}'
        print(strFormat.format(t[0], t[1], t[2], t[3]))
    print('\n')
# create_required_report(donor_db)


def _create_required_report(db):
    #print ('Donor Name          | Total Given | Num Gifts | Average Gift')
    print('{0:_<20}{1}{2:_>12}{3}{4:_^10}{5}{6:_>13}'.format('Donor Name','|', 'Total Given','|', 'Num Gifts','|','Average Gift'))
    print ('{:''^66}'.format(' '))
    t = ()
    for i, j in enumerate(db):
        name = donor_db[i][0]
        t = (name, get_sum_donations(db, name), get_number_of_donations(db, name),get_avg_donation_amt(db, name))
        sp=25-len(name)
        #print (name, len(name), sp)
        #strFormat = '{:25}${:13,.2f}'    ' {:^3}     ${:>13,.2f}'
        #strFormat = '{0:<}{1:<' + str(sp) + '}'
        strFormat = '{0:_<20}${1:_>13,.2f}{2:_^10}${3:_>13,.2f}'
        #print (strFormat)
        #'{:25}{:5}${:13,.2f}'    ' {:^3}     ${:>13,.2f}'
        #print(strFormat.format(t[0], t[1], t[2], t[3]))
        print(strFormat.format(t[0], t[1], t[2], t[3]))
    print('\n')
 #_create_required_report(donor_db)


# create_required_report(donor_db)
# print('{:<25}'  ' {:<10}${:>15,.2f}'.format(t[i - 2], t[i - 1], t[i]))
# get_sum_donations(donor_db, 'Paul Allen')
# get_number_of_donations(donor_db, 'Paul Allen')
# get_avg_donation_amt(donor_db, 'Paul Allen')
# print ('\n')

def get_sum_donations(db, donor_name):
    sum_amt= 0.0
    for i, j in enumerate(db):
        if donor_name == db[i][0]:
            for k, m in enumerate (db[i][1][:]):
                sum_amt += db[i][1][k]
    return sum_amt


def get_number_of_donations(db, donor_name):
    n = 0
    for i, j in enumerate(db):
        if donor_name == db[i][0]:
            for k, m in enumerate (db[i][1][:]):
                n += 1
    return n


def get_avg_donation_amt(db, donor_name):
    avrg = 0
    sm = get_sum_donations(db, donor_name)
    n = get_number_of_donations(db, donor_name)
    return round(sm/n, 2)

# get_sum_donations(donor_db, 'Paul Allen')
# get_number_of_donations(donor_db,  'Paul Allen')
# get_avg_donation_amt(donor_db,  'Paul Allen')
#  create_simple_report(donor_db)


def list_donors(db):
    for i, j in enumerate(donor_db):
        print('{:<25}'.format( donor_db[i][0]))

# list_donors(donor_db)


def check_donor_name(db, s):
    b = False
    for i, j in enumerate(db):
        if s.lower() in db[i][0].lower():
            b = True
    return b


def add_donor_name(db, new_donor):
        new_tuple = (new_donor, [0.0])
        db.append(new_tuple)
        #print('added: {:<25}'.format(donor_db[-1][0]))


def add_new_donor(db, new_donor, a):
        amt = [float(a)]
        new_tuple = (new_donor, amt)
        db.append(new_tuple)

# add_new_donor(donor_db, "jinky jake", 11.33)


def add_donor_amt(db, donor_name, amt):
    for i, j in enumerate(db):
        if donor_name.lower() in db[i][0].lower():
            db[i][1].append(float(amt))


def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script


def thank_you(thank_you_name):
    print("Bye!")
    sys.exit()  # exit the interactive script


def send_email(db, donor_name, amt):
    donor = resolve_donor_name(db, donor_name)
    print('{:}. Thank you for your donation of ${:,.2f}.'.format(donor, float(amt)))


def resolve_donor_name(db, s):
    ret_name = s
    for i, j in enumerate(db):
        if s.lower() in db[i][0].lower():
            ret_name = db[i][0]
    return ret_name

#resolve_donor_name(donor_db, "PAUL ALLEN")


def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            while True:
                thankyou_to_name = input(thankyou_2_prompt)
                while thankyou_to_name.lower() == "list":
                    list_donors(donor_db)
                    thankyou_to_name = input(thankyou_2_prompt)
                if thankyou_to_name.lower() == "exit":
                    break

                if not check_donor_name(donor_db, thankyou_to_name):
                    print ("This is a new donor:")
                    amt = input(thankyou_for_amt_prompt)
                    add_new_donor(donor_db, thankyou_to_name, amt)
                else:
                    amt = input(thankyou_for_amt_prompt)
                    add_donor_amt(donor_db, thankyou_to_name, amt)
                # update data with new amount
                send_email(donor_db, thankyou_to_name, amt)
                #print("Send email to " + thankyou_to_name + ' for ' + str(amt))
        elif response == "2":
            create_required_report(donor_db)
            #response = input(prompt)
            pass
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")


if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()
# commit
#

#######################################################################################################
# date          init    desc
# 20200625      djm     mail room part 1
# 20200707      djm     mail room part 2 (Dictionary implementations)
# 20200803      djm     mail room part 3, Lesson 5, exceptions and comprehensions
#
# Changes to:
# _get_number_of_donations (added list comprehension)
# add_donor_amt (added try block to catch entry of inappropriate amount values)
# prep_individual_email (added try block to catch error raised by add_donor_amt)
# send_email_to_all list (added list comprehension)
# main (added try block to catch error raised by inappropriate menu value entries)
#
# Duane McCollum Python self-paced winter 2020
#
#
#
#######################################################################################################
# original donor db, a list

import sys, os  # imports go at the top of the file
print(os.getcwd())
donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0])
            ]

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
    print ('{:''^66}'.format(' '))
    t = ()
    for i, j in enumerate(donor_db):
        name = donor_db[i][0]
        t = (name, get_sum_donations(donor_db, name), _get_number_of_donations(name),get_avg_donation_amt(donor_db, name))
        strFormat = '{0: <20.20}${1: >13,.2f}  {2:^11}  ${3:> 13,.2f}'
        print(strFormat.format(t[0], t[1], t[2], t[3]))
    print('\n')
    return True


def get_sum_donations(db, donor_name):
    sum_amt= 0.0
    for i, j in enumerate(db):
        if donor_name == db[i][0]:
            for k, m in enumerate (db[i][1][:]):
                sum_amt += db[i][1][k]
    return sum_amt



def get_number_of_donations(donor_name):
    """older non-list comprehension version"""
    n = 0
    for i, j in enumerate(donor_db):
        if donor_name == donor_db[i][0]:
            for k, m in enumerate (donor_db[i][1][:]):
                n += 1
    return n

def _get_number_of_donations(donor_name):
    """newer non-list comprehension version
        added 20200804 for lesson 05"""
    n = [len(donor_db[i][1][:]) for i, j in enumerate(donor_db) if donor_db[i][0] ==str(donor_name)]
    return int(n[0])


def get_avg_donation_amt(db, donor_name):
    sm = get_sum_donations(db, donor_name)
    n = _get_number_of_donations(donor_name)
    return round(sm/int(n), 2)


def check_donor_name(db, s):
    b = False
    for i, j in enumerate(db):
        if s.lower() in db[i][0].lower():
            b = True
    return b

def list_donors(db):
    for i, j in enumerate(donor_db):
        print('{:<25}'.format( donor_db[i][0]))
    print('\n'.format(donor_db[i][0]))

def add_new_donor(new_donor, a):
    amt = [float(a)]
    new_tuple = (new_donor, amt)
    donor_db.append(new_tuple)

def resolve_donor_name(db, s):
    ret_name = s
    for i, j in enumerate(db):
        if s.lower() in db[i][0].lower():
            ret_name = db[i][0]
    return ret_name

def add_donor_amt(donor_name, amt):
    """ added try block for non-numeric amount entries
        and for amount entries LT zero
        20200804 lesson 05 """
    for i, j in enumerate(donor_db):
        if donor_name.lower() in donor_db[i][0].lower():
            try:
                amt = float(amt)
            except ValueError:
                raise ValueError('enter a numeric amount')
            else:
                if amt < 0:
                    raise ValueError('enter an amount > 0')
                else:
                    donor_db[i][1].append(float(amt))


def prep_individual_email():
    """ added raise error on invalid  amt
        20200804 lesson 05 """
    while True:
        thankyou_to_name = input(thankyou_2_prompt)
        while thankyou_to_name.lower() == "list":
            list_donors(donor_db)
            thankyou_to_name = input(thankyou_2_prompt)
        if thankyou_to_name.lower() == "exit":
            break
        if not check_donor_name(donor_db, thankyou_to_name):
            print("This is a new donor")
            amt = input(thankyou_for_amt_prompt)
            try:
                add_donor_amt(thankyou_to_name, amt)
            except ValueError as e:
                print('\n{0} {1}\n'.format('Amount Error: ', str(e)))
            else:
                send_email(thankyou_to_name)
        else:
            amt = input(thankyou_for_amt_prompt)
            try:
                add_donor_amt(thankyou_to_name, amt)
            except ValueError as e:
                print('\n{0} {1}\n'.format('Amount Error: ', str(e)))
            else:
                send_email(thankyou_to_name)
        # update data with new amount
        # send_email(thankyou_to_name)
        # print("Send email to " + thankyou_to_name + ' for ' + str(amt))
    return False
# prep_individual_email()

def send_email(donor_name):
    donor = resolve_donor_name(donor_db, donor_name)
    # for a single name, create an email file for each of their donations
    for i, j in enumerate(donor_db):
        if donor in j:
            idx = i
            n = get_number_of_donations(donor)
            for x in range(n):
                template = 'Dear {:}, \n\n' '\t\tThank you for your very kind donation of ${:,.2f}.'
                template += '\n\n\t\tIt will be put to very good use.\n\n'
                template += '\t\t\tSincerly,\n\n'
                template += '\t\t\t\t-The Team.\n'
                email = template.format(donor, float(donor_db[idx][1][x]))
                # print(template.format(s, float(donor_db[idx][1][x])))
                #print(email)
                fname = donor + '_' + str(x + 1) + 'of' + str(n) + '.txt'
                with open(fname, 'w') as f:
                    f.write(email)
                    f.close()
    print('Sent email to {}.\n'.format(donor))
    return True


def send_email_to_all():
    """ updated send_email_to_all
        to use a list comprehension
        20200804 lesson 05"""
    # for a single name, create an email file for each of their donations
    x = [send_email(str(s)) for s in donor_db]
    return True

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


import sys  # imports go at the top of the file

##############################################################
# 20200625      djm mail room part 1
# Duane McCollum Python self-paced winter 2020
#
#     If the user (you) selects “Send a Thank You” option, prompt for a Full Name.
#
#     If the user types list show them a list of the donor names and re-prompt.
#     If the user types a name not in the list, add that name to the data structure and use it.
#     If the user types a name in the list, use it.
#
#
#############################################################

donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ("Manuel Noriega", [100.00, 50.20, 1500000.0])
            ]

prompt = "\n".join(("Mailroom program:",
          "Please choose from these options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Quit\n",
          ">>> "))


thankyou_prompt = "\n".join(("Send thank you menu:",
          "Please choose from these options:",
          "1 - List Donor Names",
          "2 - Send thank you to (name)",
          "3 - Return to Main Menu\n",
          ">>> "))


def create_report(db):
    for i, j in enumerate(donor_db):
        name = donor_db[i][0]
        for k, m in enumerate (donor_db[i][1][:]):
            amt = donor_db[i][1][k]
            print('{:<25}' '${:>15,.2f}'. format(name, amt))
    print ('\n')



def list_donors(db):
    for i, j in enumerate(donor_db):
        print('{:<25}'.format( donor_db[i][0]))

# list_donors(donor_db)

def check_donor_name(db, s):
    b = False
    for i, j in enumerate(db):
        if s in db[i][0]: b = True
    return b

# print(check_donor_name(donor_db, 'Jeff Bozos'))
# print(check_donor_name(donor_db, 'Jeff Bezos'))
def add_donor_name(db, new_donor):
        new_tuple = (new_donor, [0.0])
        db.append(new_tuple)
        print('added: {:<25}'.format(donor_db[-1][0]))

new_donor = ('Joe bozos the 3rd', [0.0])
donor_db.append(new_donor)
add_donor_name(donor_db, "Joesph Bozo")

print('{:<25}'.format(donor_db[-1][0]))

add_donor_name(donor_db, 'Joseph Bozos')
create_report(donor_db)
def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script

def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            while True:
                thankyou_menu = input(thankyou_prompt)
                if thankyou_menu == "1":
                    list_donors(donor_db)
                elif thankyou_menu =="2" :
                    name_for_thankyou = input("Name of donor to send thank you: ")
                    print(name_for_thankyou)
                    check_donor_name(name_for_thankyou)

                elif thankyou_menu == "3":
                    break
                else:
                    print("Not a valid Send Thank you option!")
        elif response == "2":
            create_report(donor_db)
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")


if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()





type(donor_db)
'{:<25}' '${:>15,.2f}'.format(donor_db[0], donor_db[0][1][0])
'{:<25}' '${:>15,.2f}'.format(donor_db[0][0], donor_db[0][1][0])
'${:>15,.2f}'.format(donor_db[0][1][1])
import sys

donar_list = [
    ("Mike", [200, 150, 50]),
    ("Tony", [150, 50, 250]),
    ("Sarah", [150, 150, 150]),
]

# Calculates average $$ per donar


def average(donar_ave):
    return (sum(donar_ave) / len(donar_ave))


# Calculates average donation amount per donar
def total_donated(don_amts):
    return sum(don_amts[1])

# Prompts info from user, and sends thank you.


def thank_you():
    donar_name = input(
        "Enter donors full name (type 'list' to display all names)? > ").title()
    if donar_name == '':
        return
    if donar_name.lower() == 'list':
        for i in range(len(donar_list)):
            print(donar_list[i][0])
        return

    donation_amt = input("\n""How much did " + donar_name + " donate? > ")
    amt = round(float(donation_amt), 2)

    for i in range(len(donar_list)):
        if donar_name == donar_list[i][0]:
            donar_list[i][1].append(amt)
            break
    else:
        donar_list.append((donar_name, [amt]))

    # display a default thank you note addressed to the donor
    print('\n'.join(('\n''Dear ' + donar_name.title() + ',' + '\n',
                     'Thank you for your generous donation of $' + donation_amt + '.',
                     'Your commitment goes a long way in helping us',
                     'solve things that need to be solved.' + '\n',
                     'Warm regards,' + '\n',
                     'Me (:')))

# Creates and displays report from all donars


def create_report():
    print('{:20}{:15}{:15}{:15}'.format('Donar Name',
                                        '| Total Given', '| Num Gifts', '| Average Gift'))
    print('-' * 65)
    s_list = sorted(donar_list, key=total_donated, reverse=True)
    for i in range(len(s_list)):
        print(
            f'{s_list[i][0]:<20} $ {sum(s_list[i][1]):<13.2f} {len(s_list[i][1]):<13} $ {average(s_list[i][1]):<15.2f}')


def quit_program():
    # exit the function
    print("Bye!")
    sys.exit()  # exit the interactive script


if __name__ == "__main__":
    while True:
        prompt = input(
            "What would you like to do?:\n"
            "s - Send a Thank you\n"
            "c - Create a report\n"
            "q - Quit\n"
            "Please select:  \n")
        if prompt.lower() == "s":
            thank_you()
        elif prompt.lower() == "c":
            create_report()
        elif prompt.lower() == "q":
            quit_program()
        else:
            print("\nPlease enter s, c, or q\n")

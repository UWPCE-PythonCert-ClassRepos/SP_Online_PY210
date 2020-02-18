import sys
import operator
import os

#dictionary of current donors and donation amounts
donor_dict = {"Mouth Devereaux" : [4562.58, 3817.39],
            "Mikey Walsh" : [618.45, 49.20, 542.87],
            "Andy Carmichael" : [75.28, 99.25],
            "Chester Copperpot" : [750254.00, 802154.11, 1.75]
            }

def new_donor_dict_func():
    #creates new dict with donation amnt summed, counted, and averaged; sorted by total
    new_donor_dict = dict()
    for x, y in donor_dict.items():
        new_donor_dict.update({x:(sum(y),len(y),average(y))})
    new_sorted = dict(sorted(new_donor_dict.items(), key=operator.itemgetter(1),reverse=True))
    return new_sorted

def average(donor_ave):
    #calculates donation averages per donor
    return (sum(donor_ave) / len(donor_ave))

def ty_letter(a, b):
    #thank you letter
    return ('\n'.join(('\n''Dear {},\n',
    'Thank you for your generous donation of ${:.2f}.',
    'Your commitment goes a long way in helping us',
    'solve things that need to be solved.' + '\n',
    'Warm regards,' + '\n',
    'Mama Fratelli')).format(a,b))

def thank_you():
    #input option for the user to enter a new name, add amount to previous donor, or see list of previous donors
    donor_name = input("Enter donors full name (type 'list' to display all names)? > ").title()

    #if user does not enter a name or 'list' they will be brought back to the main menu
    if donor_name == '':
        return main()

    #displays previous donor list
    if donor_name == 'List':
        print(list(donor_dict.keys()))
        return main()

    #collect donation amount
    donation_amt = input("\n""How much did " + donor_name + " donate? > ")
    amt = round(float(donation_amt),2)

    #iterate through donor list, add new name and amount, or amount if the name was already on the list
    if donor_name in donor_dict.keys():
        donor_dict[donor_name].append(amt)
    else:
        donor_dict[donor_name] = [amt]

    print(ty_letter(donor_name,amt))
    return main()

def create_report():
    #display report of all donor with summed and sorted donation amounts
    print('{:20}{:15}{:15}{:15}'.format('Donor Name', '| Total Given', '| Num Gifts', '| Average Gift'))
    print('-' * 65)

    for name, dollars in new_donor_dict_func().items():
        print(f'{name:<20} $ {dollars[0]:<13.2f} {dollars[1]:<13} $ {dollars[2]:<15.2f}')
    return main()


def letters_to_all():
    #writes individual thank you letters to all donors
    for name, dollars in new_donor_dict_func().items():
        with open('./' + name + '.txt', 'w') as f:
            f.write(ty_letter(name,dollars[0]))
    print('\n''Thank you letters saved in the following directory:' + '\n'
        + os.getcwd())
    return main()


def quit_program():
    #exit the function
    print("Bye!")
    sys.exit()  # exit the interactive script


def main():
    prompt = "\n".join(("\n""Mailroom options",
          " Please choose from below options:",
          " 1 - Send a Thank You to a single donor",
          " 2 - Create a Report",
          " 3 - Send letters to all donors",
          " 4 - Quit",
          ">>> "))

    main_menu = {1: thank_you, 2: create_report, 3: letters_to_all, 4: quit_program,}
    response = int(input(prompt))
    main_menu.get(response)()

#confirm file is executed on it's own in the main program, or being imported
if __name__ == "__main__":
    main()

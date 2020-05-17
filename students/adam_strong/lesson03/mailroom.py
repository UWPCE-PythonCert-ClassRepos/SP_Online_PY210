#!/usr/bin/env python3
import sys

donor_db = [("Scrooge McDuck", [8000.00, 70000.00]),
            ("Montgomery Burns", [49.53]),
            ("Richie Rich", [1000000.00, 500000.00]),
            ("Chet Worthington", [200.00, 44387.63, 10200.00]),
            ("Silas Skinflint", [0.25, 1.00, 0.43]),
            ]

main_prompt = "\n".join(("", "Welcome to the donors list",
          "Please choose from below options:",
          "1 - Send a thank you",
          "2 - Create a report",
          "3 - Quit",
          "Type a number to select >>> "))

ty_prompt = "\n".join(("", "Please type the full name of the donor OR",
        "type 'list' to see a list of donors",
        "Type input here >>>"))

ty_message = "\n".join(("", "Dear {}",
        "Thank you for your generous donation of {:.2f}",))

def exit_program():
    print('Shutting down the program')
    sys.exit()

def thank_you():
    tyname = input(ty_prompt)
    if tyname == 'list':
        report()
    else:
        ind = 0
        for donors in donor_db:
            if tyname not in donors:
                ind += 1
            else:
                break

        amt = input("Please enter the donation amount >>>")
        if ind == len(donor_db):
            donor_db.append((tyname, [float(amt)]))
        else:
            donor_db[ind][1].append(float(amt))

        input(ty_message.format(tyname, float(amt)))

def sort_key(donor_db):
    return sum(donor_db[1])


def report():
    head = '{:20}| {:>15}|{:>15}| {:>15}'.format('Donor Name', 'Total Given','Num Gifts', 'Average Gift')
    print(head)
    print('-'*72)



    donorsort = sorted(donor_db, key = sort_key)
    donorsort.reverse()


    for donor in donorsort:
        line = '{:20} ${:>15.2f}  {:>15}  ${:15.2f}'.format(donor[0], sum(donor[1]),len(donor[1]), (sum(donor[1])/len(donor[1])))
        print(line)
    print('')


'''Primary code block'''

def main():
    while True:
        response = input(main_prompt)
        if response == '1':
            thank_you()
        elif response == '2':
            report()
        elif response == '3':
            exit_program()
        else:
            print('Not a valid response please try again')

if __name__ == '__main__':
    # Guards against running automatically if this script is imported
    main()
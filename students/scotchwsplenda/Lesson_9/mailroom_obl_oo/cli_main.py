
import mailroom_oo_dict
import sys


def mainy():
    while True:
        try:
            choice = int(input('''
Welcome to the main MAILROOM option menu:
1 - Initiate Grovel Sequence
2 - Data Metrics 3000
3 - Quit
4 - Send thank you notes to all donors
Indicate your choice:'''))
            swit_dic = {1: input_name, 3: exit_program,
                        2: analytics, 4: mass_mail}
            swit_dic[choice]()
        except KeyError:
            print("\n"+'You have entered a non-choice'
                  ', please get your life together')
        except ValueError:
            print("\n"+'You have entered a non-number'
                  ', please get your life together')


def input_name():
    while True:
        name = input("Enter donor name or enter 'list' for extant donors: ")
        if name == 'list':
            print(dc.donor_names())
        else:
            verify_name(name)


def verify_name(name):
    if dc.donor_db.get(name):
        print(f'{name} is a known donor')
    else:
        print(f'{name} is a new donor')
        don = input('continue Y/N? ')
        # if I add "or 'YES'" then it takes 'n' as a 'y', WTF?
        if don.upper() == 'Y':
            while True:
                don_amount = float(input(f"how much is ol' {name} donating?:"))
                if don_amount <= 0:
                    print(f'Do better {name}')
                else:
                    dc.add_contribution(name, don_amount)
                    print(dr.thanks_mail(name, don_amount))
                    mainy()
        if don.upper() == 'N' or 'NO':
            input_name()


def analytics():
    dc.data_metrics()


def mass_mail():
    dc.mass_mail()


def exit_program():
    print("Bye!")
    sys.exit()


if __name__ == "__main__":
    dc = mailroom_oo_dict.DonorCollection()
    dr = mailroom_oo_dict.Donor()
    dc.loadup
    mainy()

import mailroom_oo as mail
import sys


def menu():
    dict_menu = {'\n1.': 'Send a Thank You', 
                 '2.' : 'Create a Report', 
                 '3.' : 'Send Thank You - All Donors', 
                 '4.' : 'Quit'}
    for x, y in dict_menu.items():
        print(x, y)

def main():
    option_table = {1: mail.Donors.donor_name_collection,
               2: mail.Donors.create_report,
               3: mail.Donors.thankyou_print,
               4: sys.exit}
    while True:
        try:
            menu()
            user_input = input("\nChoice Selected: \n")
            option_table.get(int(user_input))()
        except TypeError:
            print()
            print("Please select a proper menu choice")
        except ValueError:
            print()
            print("Please select a proper menu choice")

if __name__ == "__main__":
    mail.Donors.dict_init()
    main()
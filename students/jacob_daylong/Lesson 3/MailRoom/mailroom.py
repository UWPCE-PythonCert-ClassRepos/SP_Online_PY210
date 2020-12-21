
#Write a small command-line script called mailroom.py. This script should be executable. The script should accomplish the following goals:

#It should have a data structure that holds a list of your donors and a history of the amounts they have donated.
#This structure should be populated at first with at least five donors, with between 1 and 3 donations each. You can store that data structure in the global namespace.
#The script should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”.
from operator import itemgetter, attrgetter

total_given = 0.00
full_name = ''
num_gifts = 0
table_header = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
donor_table = [['Jane Doe', 10000, 4000, 2000],
              ['John Doe', 10000, 2000, 5000, 3000],
              ['Bobby Newport', 2000, 100], ['Johnny Mnemonic', 900, 800, 1000], ['Phillip Dick', 2220]]

def menu():
    print()
    print("Please choose an option:")
    print("1. Send a Thank You")
    print("2. Create a Report")
    print("3. Quit")
    print()

def send_thankyou(full_name):
    print()
    while full_name == '':
        full_name = input("Please enter Donor's Full Name: ")
        if full_name == "list":
            print()
            print('|{:<{width}s}|'.format(*table_header, width=20))
            for row in donor_table:
                print('|{:<{width}s}|'.format(*row, width=20))
        elif full_name == 'quit':
            break
        else:
            for row in donor_table:
                if full_name.lower() == row[0].lower():
                    amt_given = input("Please enter Donor's gift amount: ")
                    row.append(int(amt_given))
                    mail_text = "Dear {}, \nThank you for your donation of ${}. \nSincerely, Jake".format(row[0], amt_given)
                    print(mail_text)
                    break
            
            if full_name != row[0] and full_name.lower() != "list":
                donor_table.append([full_name])
                amt_given = input("Please enter Donor's gift amount: ")
                donor_table[-1].append(int(amt_given))
                mail_text = "Dear {}, \nThank you for your donation of ${}. \nSincerely, Jake".format(donor_table[-1][0], amt_given)
                print(mail_text)

def donor_sort_key(entry):
    return sum(donor_table.get(entry))

def create_report(table_header, donor_table):
    print()
    print('|{:<{width}s}|{:<{width}s}|{:<{width}s}|{:<{width}s}|'.format(*table_header, width = 20))
    print('-------------------------------------------------------------------------------------')
    SortedDonors = sorted(donor_table, key=donor_sort_key, reverse=True)
    for row in SortedDonors:
        donor_total = sum(row[1:])
        donation_avg = donor_total/(len(row)-1)
        donation_qty = len(row)-1
 
        print('|{:<{width}s}|${:<19.2f}|{:<{width}d}|${:<19.2f}|'.format(row[0], donor_total, donation_qty, donation_avg, width = 20))



def main():
    while True:
        menu()
        user_input = input("Choice Selected: ")
        if user_input == '1':
            send_thankyou(full_name)
        elif user_input == '2':
            create_report(table_header, donor_table)
        elif user_input == '3':
            break

if __name__ == "__main__":
    main()
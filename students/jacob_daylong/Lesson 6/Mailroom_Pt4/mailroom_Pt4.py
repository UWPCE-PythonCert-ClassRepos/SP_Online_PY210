import tempfile
import sys

full_name = ''
table_header = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
donor_table = {}


def menu():
    dict_menu = {'\n1.': 'Send a Thank You', '2.' : 'Create a Report', '3.' : 'Send Thank You - All Donors', '4.' : 'Quit'}
    for x, y in dict_menu.items():
        print(x, y)

def thankyou_note(entry):
    note =('Dear Jake, Thank you for your donation of $500. Sincerely, Jake')
    return note

def donor_name_collection(full_name = 'List'):
     full_name = input("\nPlease enter donor's Full Name: ")
     while full_name == 'List':
        for entry in donor_table:
            print(entry)
        full_name = input("\nPlease enter donor's Full Name: ")
     try:
        user_input = input("Please enter donation amount:")
        if user_input.isnumeric:
            donor_amt = float(user_input)
        else:
            raise ValueError
     except (ValueError, UnboundLocalError):
        print("Please Enter a valid number")
        donor_amt = float(input("Please enter donation amount:"))

     send_thankyou(full_name, donor_amt)

def send_thankyou(full_name, donor_amt):
        if full_name not in donor_table:
                donor_table[full_name] = [donor_amt]
        else:
                donor_table[full_name] += [donor_amt]
    

        print(thankyou_note(full_name))

def thankyou_print():
    for entry in donor_table:
        dir = tempfile.gettempdir() + "/"
        filename = entry + '.txt'
        f = open(dir + filename, 'w')
        f.write(thankyou_note(entry))
        f.close
    print(dir)

def create_report():
    print('\n|{:<{width}s}|{:<{width}s}|{:<{width}s}|{:<{width}s}|'.format(*table_header, width = 20))
    print('-------------------------------------------------------------------------------------')
    sorted_donors = sorted(donor_table, key=donor_sort_key, reverse=True)
    for entry in sorted_donors:
        donation_total = sum(donor_table.get(entry))
        donation_qty = len(donor_table.get(entry))
        donation_avg = donation_total/donation_qty
        print('|{:<{width}s}|${:<19.2f}|{:<{width}d}|${:<19.2f}|\n'.format(entry, donation_total, donation_qty, donation_avg, width = 20))

def dict_init():
    donor_table['Jane Doe'] = [10000, 4000, 2000]
    donor_table['John Doe'] = [10000, 2000, 5000, 3000]
    donor_table['Bobby Newport'] = [2000, 100]
    donor_table['Johnny Mnemonic'] = [900, 800, 1000]
    donor_table['Phillip Dick'] = [2220]   

def donor_sort_key(entry):
    return sum(donor_table.get(entry))

def main():
    option_table = {1: donor_name_collection,
               2: create_report,
               3: thankyou_print,
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
    dict_init()
    main()

import tempfile

full_name = ''
table_header = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
donor_table = {}

def menu():
    dict_menu = {'\n1.': 'Send a Thank You', '2.' : 'Create a Report', '3.' : 'Send Thank You - All Donors', '4.' : 'Quit'}
    for x, y in dict_menu.items():
        print(x, y)

def thankyou_note(entry):
    note =(f'\nDear {entry}, \nThank you for your donation of ' 
          f'${sum(donor_table.get(entry)):.2f}. \nSincerely, Jake\n')
    return note

def send_thankyou(full_name):
    full_name = input("\nPlease enter donor's Full Name: ")
    while full_name == 'List':
        for entry in donor_table:
            print(entry)
        full_name = input("\nPlease enter donor's Full Name: ")

    donor_amt = float(input("Please enter the amount given: "))

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

def create_report(table_header, donor_table):
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
    while True:
        menu()
        user_input = input("\nChoice Selected: \n")
        if user_input == '1':
            send_thankyou(full_name)
        elif user_input == '2':
            create_report(table_header, donor_table)
        elif user_input == '3':
            thankyou_print()
        elif user_input == '4':
            break

if __name__ == "__main__":
    dict_init()
    main()

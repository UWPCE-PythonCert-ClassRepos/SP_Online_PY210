import tempfile

#full_name = ''
#table_header = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
#donor_table = {}
#sorted_donors = {}
#dir = ()
#donor_sort_key = {}

class Donors(object):
    full_name = ''
    table_header = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    donor_table = {}
    donor_sort_key = {}
    sorted_donors = {}

    def dict_init():
        Donors.add_donation('Jane Doe', [10000, 4000, 2000])
        Donors.add_donation('John Doe', [10000, 2000, 5000, 3000])
        Donors.add_donation('Bobby Newport', [2000, 100])
        Donors.add_donation('Johnny Mnemonic', [900, 800, 1000])
        Donors.add_donation('Phillip Dick', [2220])
    
    def add_donation(name, amount):
        if Donors.donor_table.get(name):
            if isinstance(Donors.donor_table[name], list):
                if isinstance(amount, list):
                    Donors.donor_table[name].extend(amount)
                else:
                    Donors.donor_table[name].extend([amount])
        else:
            if isinstance(amount, list):
                Donors.donor_table[name] = amount
            else:
                Donors.donor_table[name] = [amount]
        return Donors.donor_table
    
    def thankyou_print():
        for entry in Donors.donor_table:
            dir = tempfile.gettempdir() + "/"
            filename = entry + '.txt'
            with open(dir + filename, 'w') as outputfile:
                outputfile.writelines(Donor.thankyou_notes(entry))
        print("\nNote entries printed to the following directory:\n"+dir)
        return dir

    def create_report():
        print('\n|{:<{width}s}|{:<{width}s}|{:<{width}s}|{:<{width}s}|'.format(*Donors.table_header, width = 20))
        print('-------------------------------------------------------------------------------------')
        Donors.sorted_donors = sorted(Donors.donor_table, key=Donors.donor_sort_key, reverse=True)
        for entry in Donors.sorted_donors:
            donation_total = sum(Donors.donor_table.get(entry))
            donation_qty = len(Donors.donor_table.get(entry))
            donation_avg = donation_total/donation_qty
            print('|{:<{width}s}|${:<19.2f}|{:<{width}d}|${:<19.2f}|\n'.format(entry, donation_total, donation_qty, donation_avg, width = 20))
        return Donors.sorted_donors
        print(Donors.sorted_donors)
    
    def send_thankyou(full_name, donor_amt):
            Donors.add_donation(full_name, donor_amt)
            print(Donor.thankyou_note(full_name, donor_amt))

    def donor_name_collection():
        full_name = input("\nPlease enter donor's Full Name: ")
        while full_name == 'List':
            for entry in Donors.donor_table:
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
        Donors.send_thankyou(full_name, donor_amt)

    def donor_sort_key(entry):
        return sum(Donors.donor_table.get(entry))

class Donor():

        def thankyou_note(fullname, donor_amt):
            note = (f'\nDear {fullname}, \nThank you for your donation of ' 
                    f'${donor_amt:.2f}. \nSincerely, Jake\n')
            return note

        def thankyou_notes(entry):
            notes = (f'\nDear {entry}, \nThank you for your donation of ' 
                     f'${sum(Donors.donor_table.get(entry)):.2f}. \nSincerely, Jake\n')
            return notes
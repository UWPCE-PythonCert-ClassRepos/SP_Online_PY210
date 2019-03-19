
from operator import itemgetter

donors = {'Sandy Pie' : [75],
          'Judy Smith': [75, 100, 1000],
          'Mike Jones': [75, 1000],
          'Joe Smith' : [75, 100, 2000],
          'Kelly Blue': [75, 150, 275]}


def menu():
    while True:
        print()
        print('''Menu:
                    1. Send a Thank You.
                
                    2. Send all Thank You's
                   
                    3. Create a Report.
            
                    4. Quit.''')
        print()
        response = input("Please enter a number to make your selection. ")
        
        switch_func_dict = {1: ask_donor_name, 2: mulit_thanks 3: totals, 4: break}
        if response == '1':
        #     ask_donor_name()
            switch_func_dict.get(0)()    
        if response == '2':
        #     totals()
            switch_func_dict.get(1)()
        if response == '3':
        #     break
            switch_func_dict.get(2)()
        if response == '4':
            switch_func_dict.get(3)()


def list_donors():
    for item in donors:
        print(f'{item[0]}')
        
    
def ask_donor_name():

    # While collecting user input.
    while True:
        donor_name = input("Enter the full name of the donor. (or q to quit) ")
        
        if donor_name == 'q':
            return
        # If user types list print donors
        elif donor_name.upper() == "LIST":
            list_donors()
            continue
        else:  # user didn't type list
            donors[donor_name] = donors.get(donor_name, 0)
            for item in donors.items():
                if item == donor_name:
                    break
                else:
                    #donors.append((donor_name, list()))
                    donors[donor_name] = []
        donation(donor_name)
        break


def donation(donor_name):
    input_value = (input("Enter the donation amount (or q to quit) "))
    if input_value == 'q':
        return
    else:
        donation_amount = int(input_value)
        donors[donor_name].append(donation_amount)
        print(donors)
        #donorIndex = [item[0] for item in donors].index(donorName)
        # name, donations = donors[donorIndex]
        # donations.append(donation_amount)
        send_thank_you(donor_name, donation_amount)
        return


def send_thank_you(donor_name, donation_amount):
    print(f'Thank you {donor_name} for your donation of ${donation_amount} dollars.')
    print('We appeciate your generous suport of our club.')
    print()
    

# Create Report


def totals():
    output_list = []
    for name, donations in donors.items():
        total_Given = sum(donations)
        number_Gifts = len(donations)
        average_Gift = sum(donations)/len(donations)
        output_list.append((name, total_Given, number_Gifts, average_Gift))
    
    sorted_output = sorted(output_list, key=itemgetter(1), reverse=True)
    create_report(sorted_output)


def create_report(sorted_output):
    print()
    print('Donor Name                | Total Given | Num Gifts | Average Gift')
    print('-'*66)
    for name, total_Given, number_Gifts, average_Gift in sorted_output:
        print(f'{name:<27}${total_Given:>11.2f}{number_Gifts:>12}  ${average_Gift:>11.2f}')
    return


if __name__ == "__main__":
    menu()

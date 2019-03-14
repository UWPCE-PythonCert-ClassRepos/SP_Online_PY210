
from operator import itemgetter

Donors = [('Sandy Pie', [75]),
          ('Judy Smith', [75, 100, 1000]),
          ('Mike Jones', [75, 1000]),
          ('Joe Smith', [75, 100, 2000]),
          ('Kelly Blue', [75, 150, 275])]

def menu():
    quit = False
    while not quit:
        print()
        print('''Menu:   
                    1. Send a Thank You.
                
                    2. Create a Report.
            
                    3. Quit.''')
        print()
        response = input("Please enter a number to make your selection. ")
        if response == '1':
            donor_name()
            
        if response == '2':
            totals()    

        if response == '3':
            quit = True

def list_donors():
    print(Donors)
    donor_name()

def donor_name():
    done = False
    
    # While collecting user input.
    while not done:
        donorName = input("Enter the full name of the donor. (or q to quit) ")
        
        # If user types list print Donors.
        if donorName == 'q':
            return
        elif donorName.upper() == "LIST":
            list_donors()
            continue
        else:  # user didn't type list    
            #if donorName not in list(sorted(Donors, key=itemgetter(0))):
            if donorName not in [item[0] for item in Donors]:
                Donors.append((donorName,list()))
        donation(donorName)
        done = True
    
def list_donors():
    print(Donors)
    donor_name()
    return

def donation(donorName):    
    donationAmount = float(input("Enter the donation amount (or q to quit)"))
    if donationAmount == 'q':
        return
    else:
        # donorIndex = list(map(itemgetter(0), Donors)).index(donorName)
        donorIndex = [item[0] for item in Donors].index(donorName)
        name, donations = Donors[donorIndex]
        donations.append(donationAmount)
        #print(Donors)
        send_thank_you(name, donationAmount)
        return

def send_thank_you(name, donationAmount):
    print(f'Thank you {name} for your donation of ${donationAmount} dollars.')
    print('We appeciate your generous suport of our club.')
    print()
    return

# Create Report
def totals():
    output_list = []
    for name, donations in Donors:
        total_Given = sum(donations)
        print(sum(donations))
        number_Gifts = len(donations)
        print(len(donations))
        average_Gift = sum(donations)/len(donations)
        print(sum(donations)/len(donations))
        output_list.append((name, total_Given, number_Gifts, average_Gift))
        print(output_list)
    print(output_list)
    sorted_output = sorted(output_list, key=itemgetter(1), reverse=True)
    print(sorted_output)

    print() 
    print('Donor Name                | Total Given | Num Gifts | Average Gift')
    print('-'*66)
    for name, total_Given, number_Gifts, average_Gift in sorted_output:
        print(f'{name:<27}${total_Given:>11.2f}{number_Gifts:>12}  ${average_Gift:>11.2f}')

    return

if __name__ == "__main__":
    menu()

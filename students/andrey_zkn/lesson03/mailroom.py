# Part 1
import sys

donors = [('Alexander Pushkin', [200, 100, 340]),
          ('Mikhail Lermontov', [300, 100]),
          ('Leo Tolstoy', [150, 250, 100]),
          ('Fyodor Dostoevsky', [125]),
          ('Anton Chekhov', [100, 250]),
          ('Nikolai Gogol', [325, 150]),
          ]

prompt = "\n".join (("Please select from the following options:",
          "1 - Send a Thank You Letter",
          "2 - Create a Report",
          "3 - Quit ",
          " >>> "))


def find_donor_name(name_input):
    for donor in donors:
        if name_input.lower() == donor[0].lower():
            return donor
    return None


def thank_you_message(donor, amount):
    print(f'\nDear {donor.title()},')
    print(f'\nThank you for your generous donation of ${amount:,.2f}.' +
          '\nWe value your contribution and support.' +
          '\n\nSincerely,\n\nNew Horizon Charity Director\n')   


def send_thank_you():
    mail_to = input ("Enter the full name of a donor or 'list' for current donors ")
    while mail_to.lower() == "list":
        for name in donors:
            print(name[0])
        mail_to = input ("Please enter a  full name of a donor ")        
    donor = find_donor_name(mail_to)
    if donor is None:
        donor = (mail_to, [])
        donors.append(donor)
    amount = float(input ("Enter the donation amount"))
    donor[1].append(float(amount))
    thank_you_message(mail_to, amount)

    
def summation(arg):
    return sum(arg[1])

def create_report():
    header ='\n{:<20}|{:^15}|{:^15}|{:>15}'.format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(header)
    print('-'*len(header))
    donors_sorted = sorted(donors, key = summation, reverse = True)
    for donor in donors_sorted:
        total = sum(donor[1])
        num = len(donor[1])
        avg = total/num
        print('{:<20} ${:>14,.2f}{:>14}  ${:>16,.2f}'.format(donor[0],total,num,avg))
    print('')    
    

def quit_now():
    print("Good bye and see you next time!")
    sys.exit()

  
def main():
    while True:
        option = input(prompt)
        if option == '1':
            send_thank_you()
        elif option == '2':
            create_report()
        elif option == '3':
            quit_now()
        else: 
           print("Not a valid option. Please select one of the available options!")

if __name__ == "__main__":
    main()  


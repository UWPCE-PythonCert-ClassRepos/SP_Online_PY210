#!/usr/bin/env python3

#Mailroom script part one. Using list data structures
import sys

donors = [("Bill Gates",[539000,235642]),
          ("Jeff Bezos",[108356,204295,897345]),
          ("Satya Nadella",[236000,305352]),
          ("Mark Zuckerberg",[153956.35]),
          ("Mark Cuban",[459035,369.50,570.89])]

prompt = "\n".join(("Please Select from Items Below:",
                    "1 - Send A Thank You",
                    "2 - Create A Report",
                    "3 - Quit",
                    " "))

def send_thanks():
    print('\n',"For A Complete Donor List Type 'List'\n ")
    donor_list = []

    #create a unique list of donor names
    for donor in donors:
        name = donor[0]
        donor_list.append(name)

    while True:
        donor_name = input("What donor(s) are you looking for?\n ").title()
        if donor_name == 'List':
            print('\n',"Here is A Complete List of Donor Names\n ")
            print(donor_list)
        else:
            break

    #prompt for donation amount
    amount = float(input("How Much Did This Person Donate?\n "))

    #Donor name found in list
    if donor_name in donor_list:
        for name in donors:
            if name[0] == donor_name:
                name[1].append(amount)
                print(donors)

            else:
                continue

    #Donor name not found in list
    else:
        tup = (donor_name,amount)
        donors.append(tup)

    #Write Thank You Note
    print('Dear {},'.format(donor_name),
    '\n\nThank you for your show of support and generosity.',
     ' Your Donation of ${:,.1f} '.format(amount),'will contribute to saving Olympic Marmots',
     ' in Washington State.',' These Marmota are special and a unique gift to the Olympic ',
      'National Park ecosystem.\n',
     '\nAs a way of saying thank you. ',
      'You will be receiving your very own Olympic Marmot t-shirt in the mail!\n\n',
      'Sincerely,\n\n',
     'The Olympic Marmot Wildlife Foundation\n',sep = '')

def create_report():
    print('{:<25}{}{:^15}{}{:^15}{}{:^15}'.format('Donor Name','|','Total Given','|','Num Gifts','|','Average Gift'))
    str_len = len('{:<25}{}{:^15}{}{:^15}{}{:^15}'.format('Donor Name','|','Total Given','|','Num Gifts','|','Average Gift'))
    print('-' * str_len)

    def sum_value(donations):
        item = donations[1]
        return sum(item)

    sorted_donations = sorted(donors,key = sum_value, reverse=True)

    for item in sorted_donations:
        name = item[0]
        Total_Given = sum(item[1])
        Num_Gift = len(item[1])
        Avg_Gift = Total_Given/Num_Gift

        Total_Given = '{:,.0f}'.format(Total_Given)
        Avg_Gift = '{:,.0f}'.format(Avg_Gift)

        print('{:<25}${:^15}{:^15}${:^15}'.format(name,Total_Given,Num_Gift,Avg_Gift))

def exit_from():
    print('Work Completed. Good Bye!')
    sys.exit()

def main():
    while True:
        response = input(prompt)

        if response == "1":
            send_thanks()

        elif response == "2":
            create_report()

        elif response == "3":
            exit_from()

main()


donor = [
    ["William Gates", 653772.32, 2],
    ["Jeff Bezos", 16396.10, 3],
    ["Paul Allen", 877.33, 1],
    ["Mark Zuckerberg",708.42, 3],
]

def donor_name_list(donor):
    donor_name=[]
    for name in donor:
        donor_name.append(name[0])
    return donor_name

def print_donor_report(donor):
    row='| {name:20} | {sign_1:1}  {amount:>15} | {num_gifts:^10} | {sign_2:1} {avg_gift:<15,.2f} |'.format

    print('| {:20} | {:1}  {:^15} | {:^10} | {:1} {:<15} |'.format('Donor Name', ' ' ,'Total Given','Num Gifts','','Average Gift'))
    print('-'*78)
    for p in donor:
        print(row(name=p[0],sign_1='$',amount=p[1], num_gifts=p[2],sign_2='$',avg_gift=int(p[1])/int(p[2])))

def add_new_donor(name,amount,times,donor):
    new_donor=[name,amount,times]
    donor.append(new_donor)
    return donor

def thank_you_letter(donor):

    while True:
        print('The current name on the list are :', donor_name_list(donor))
        user_input=str(input('What is the name of donor? ')).title()
        if user_input.lower() == 'back':
            return False
        thx_amount = input('How much did ' + user_input + ' donate? $ ')
        if str(thx_amount.lower()) == 'back':
            return False
        if user_input not in donor_name_list(donor):
            new_donor=input('Do you want to add {} as a new donor? (YES or NO) '.format(user_input.title()))
            if new_donor.lower()== 'back':
                return False
            elif new_donor.upper()== 'NO':
                continue
            else:
                thx_name=user_input
                times=1
                add_new_donor(thx_name, thx_amount, times, donor)
                break
        else:
            thx_name=user_input
            count_times(thx_name, donor)
            total_given(thx_name, thx_amount, donor)
            break
    print('\nEMAIL CONTENT: ')
    print('{}, Thank you for your generous donation of ${:,.2f} to us.\n'.format(thx_name,float(thx_amount)))

def count_times(thx_name,donor):
    for i in range(0,len(donor)):
        if thx_name == donor[i][0]:
            donor[i][2]=int(donor[i][2])+1
            number=donor[i][2]
    return number

def total_given(thx_name, thx_amount, donor):
    for i in range(0,len(donor)):
        if thx_name == donor[i][0]:
            donor[i][1]=float(donor[i][1]) + float(thx_amount)
            thx_amount=donor[i][1]
    return thx_amount


def print_menu_task():
    print('''
    Menu of Options
    1) Send a Thank You letter
    2) View Donor Report
    3) Exit Program
    Note: You can type 'back' to return to Main Menu
    ''')
    print()

def input_menu_choice():
    choice= int(input('Which choice would you to perform? [1 to 3]: '))
    print()
    return choice
def exit_program():
    print('Exit the Program')


while __name__ == '__main__':
    print_menu_task()
    number=input_menu_choice()
    if number==1:
        thank_you_letter(donor)
    elif number ==2:
        print_donor_report(donor)
    elif number ==3:
        exit_program()
        break


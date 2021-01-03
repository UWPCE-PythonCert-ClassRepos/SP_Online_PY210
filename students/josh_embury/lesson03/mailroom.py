lst_donor_table = [
['Henry Michalson', 10, 500, 25],
['Phil Hutch', 76],
['Galileo Humpkins', 22000, 100, 490],
['Methusela Honeysuckle', 18, 69, 76000],
['Lavender Goombs', 55000, 25],
['test', 1]
]
def show_menu():
    # shows user list of options
    # return is void
    """  Display a menu of choices to the user
    :return: nothing
    """
    print('''
    Menu of Options
    1) Send a Thank You
    2) Create a Report
    3) quit
    ''')
    print()  # Add an extra line for looks
def get_user_choice():
    # asks user for choice
    # returns integer value of user's choice
    """ Gets the menu choice from a user
    :return: string
    """
    choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
    print()  # Add an extra line for looks
    return choice

def send_thank_you():
    lst_donors = []
    for current_donor in lst_donor_table:
        lst_donors.append(current_donor[0])
    donor = ''
    while(len(donor) < 1):
        donor = input('Please enter full name of donor >>> ')
        if donor == 'list':
            print(lst_donors)
            donor = ''
    new_donation = int(input('Please enter the donation amount >>> '))
    if donor in lst_donors:
        for i in range(0, len(lst_donors)):
            if lst_donors[i] == donor:
                lst_donor_table[i].append(new_donation)
    else:
        lst_donor_table.append([donor, new_donation])
    str_thankyou = f'Thank you, {donor} for the generous gift of {new_donation}. You are incredibly nice.'
    print(str_thankyou)

def get_donor_data(donor_name):
    for current_donor in lst_donor_table:
        if current_donor[0] == donor_name:
            lst_gifts = current_donor[1:]
    return [sum(lst_gifts), len(lst_gifts), sum(lst_gifts)/len(lst_gifts)]

def sort_donor_table(input_list):
    lst_donation_totals = []
    for item in input_list:
        lst_donation_totals.append(get_donor_data(item[0])[0])
    lst_donation_totals.sort()
    copy_donor_table =list(input_list)
    sorted_list = []
    n = 0
    while(n < len(input_list)):
        for item in copy_donor_table:
            if get_donor_data(item[0])[0] == lst_donation_totals[-1]:
                sorted_list.append(item)
                lst_donation_totals.pop(-1)
                copy_donor_table.pop(copy_donor_table.index(item))
        n += 1
    return sorted_list

def format_row(info_list):
    return '{:<26} {:<2} {:10.2f} {:>11} {:^2} {:10.2f}'.format(info_list[0],info_list[1],info_list[2],info_list[3], info_list[4], info_list[5])
def create_report():
    header = '{:<25} {:^10} {:^10} {:^10}'.format('Donor Name', '| Total Given', '| Num Gifts', '| Average Gift')
    print(header)
    print('------------------------------------------------------------------')

    # sort the donor table
    lst_sorted_donor_table = sort_donor_table(lst_donor_table)
    for current_donor in lst_sorted_donor_table:
        donor_data = get_donor_data(current_donor[0])
        new_row = [current_donor[0], '$', donor_data[0], donor_data[1], "$", donor_data[2]]
        print(format_row(new_row))


if __name__ == '__main__':
    while(True):
        show_menu()  # Shows menu
        strChoice = get_user_choice()  # Get menu option
        if (strChoice.strip() == '1'):
            send_thank_you()
        elif(strChoice.strip() == '2'):
            create_report()
        elif(strChoice == '3'):
            break   # and exit

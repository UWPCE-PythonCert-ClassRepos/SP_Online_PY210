'''This script stores a list of donors and their donations and creates a report upon command'''
donors = {'Alan Smith': (234.32, 23433.93, 46480.43), 'Ben': (565.34, 233905.49), 'Charlie': (213820.43,), 'Dan': (238924.23, 970597.44, 291.49), 'Eddy': (1830.32, 2084.49)}
align_name = '{:20}'
align_sum = '{:11.2f}'
align_num = '{:9.0f}'
align_avg = '{:12.2f}'
dollar_string = ' $'

'''User inputs prompts'''
action_input = 'Choose an action: \n\n1 - Send a Thank You to a single donor. \n2 - Create a Report. \n3 - Send letters to all donors. \n4 - Quit \n> '
name_input = 'What is the full name > '
donation_input = 'What is the donation amount > '
'''Letter output'''
paragraph = 'Dear {},\n\n Thank you for your generous donation of ${:.2f}! \n It will be put to very good use. \n\nSincerely, \nThe Team\n'

def sorting(value):
    return value[1]

'''Takes the sum of all donor's donations'''
def donor_sum(donor_tuple):
    donators = 0
    a = 0
    while a < len(donor_tuple):
        donators = donators + donor_tuple[a]
        a = a + 1
    return donators

'''Takes the average of all donors donations'''
def donor_average(donor_tuple):
    donor_avg = donor_sum(donor_tuple) / (len(donor_tuple))	
    return donor_avg

'''Outputs a report of all donors names, donation sums, averages, and number of donations'''
def createareport():
    middle_string = ''
    '''Title string of the report'''
    top_string = '\n' + align_name.format('Donor Name') + '  ' + 'Total Given' + '  ' + 'Num Gifts' + '  ' + 'Average Gift' + '\n' + '\n'
    donors_revised = []
    for x, y in donors.items():
        donors_revised.append((x, donor_sum(y), len(y), donor_average(y)))
    donors_revised.sort(key = sorting, reverse = True)
    for i in range(len(donors_revised)):
        middle_string = middle_string + align_name.format(donors_revised[i][0]) + dollar_string + align_sum.format(donors_revised[i][1]) + '  ' + align_num.format(donors_revised[i][2]) + dollar_string + align_avg.format(donors_revised[i][3]) + '\n'
    print(top_string + middle_string)

'''Function to send thank you to single donor'''
def sub_res():
    sub_response(name_input, donation_input, donors)

'''Function to send thank you to single donor'''
def sub_response(action, action_two, dictionary):
    name = input(action)
    while name == 'list':
        for key in donors:
            print(key)
        name = input(action)
    amount = input(action_two)
    amount = float(amount)
    if name not in dictionary:
        dictionary[name] = (amount,)
    else:
        dictionary[name] = dictionary[name] + (amount,)
    print(paragraph.format(name, amount))

'''Writes all the donor letters to a file in {name}.txt format'''
def all_donors():
    for key, value in donors.items():
        with open(key + '.txt', 'w+') as f:
            f.write(paragraph.format(key,value[-1]))
        f.close()

'''Quits the program'''
def quit():
    print('quitting this menu')
    return 'exit menu'

'''Invokes the script'''
def main_response(action, dictionary):
    while True:
        response = input(action)
        if dictionary[response]() == 'exit menu':
            break

'''User choices'''
response_dict = {'1': sub_res, '2': createareport, '3': all_donors, '4': quit}

'''Main interation'''
if __name__ == '__main__':
    main_response(action_input, response_dict)





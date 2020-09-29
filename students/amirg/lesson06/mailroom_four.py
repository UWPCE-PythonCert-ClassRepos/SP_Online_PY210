'''This script stores a list of donors and their donations and creates a report upon command'''
donors = {'Alan Smith': (234.32, 23433.93, 46480.43), 
              'Ben': (565.34, 233905.49), 
              'Charlie': (213820.43,), 
              'Dan': (238924.23, 970597.44, 291.49), 
              'Eddy': (1830.32, 2084.49)}
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
    '''Returns second value of sequence for sorting purposes'''
    return value[1]

def donor_sum(donor_tuple):
    '''Takes the sum of all donor's donations for a tuple input'''
    donators = 0
    a = 0
    while a < len(donor_tuple):
        donators = donators + donor_tuple[a]
        a = a + 1
    return donators

def donor_average(donor_tuple):
    '''Takes the average of all donors donations for a tuple input'''
    donor_avg = donor_sum(donor_tuple) / (len(donor_tuple)) 
    return donor_avg

def get_list():
    '''Action for when list is prompted'''
    keys = ''
    for key in donors.keys():
        keys = keys + key
        print(key)
    return keys

def get_name():
    '''Getting name of input'''
    name = input(name_input)
    while name == 'list':
        get_list()
        name = input(name_input)
    return name

def get_amount():
    '''Getting input amount'''
    amount = input(donation_input)
    try:
        amount = float(amount)
    except ValueError:
        print('Must type a numerical amount, try again')
        return get_amount()
    return amount

def add_name_amount(input_one, input_two):
    '''adds name and/or amount to list'''
    name = input_one
    amount = input_two
    if name not in donors:
        donors[name] = (amount,)
    else:
        donors[name] = donors[name] + (amount,)
    return donors

def sub_res():
    '''Function to send thank you to single donor'''
    returned_donor = get_name()
    returned_amount = get_amount()
    add_name_amount(returned_donor, returned_amount)
    sub_response(returned_donor, returned_amount)

def sub_response(input_one, input_two):
    '''Function to send thank you to single donor'''
    name = input_one
    amount = input_two
    final_string = paragraph.format(name, amount)
    print (final_string)
    return final_string

def createareport():
    '''Outputs a report of all donors names, donation sums, averages, and number of donations'''
    middle_string = ''
    #Title string of the report
    top_string = '\n' + align_name.format('Donor Name') + '  ' + 'Total Given' + '  ' + 'Num Gifts' + '  ' + 'Average Gift' + '\n' + '\n'
    #List comprehension 
    donors_revised = [(x, donor_sum(y), len(y), donor_average(y)) for x, y in donors.items()]
    donors_revised.sort(key = sorting, reverse = True)
    #List comprehension for donor information output
    middle_string = [align_name.format(donors_revised[i][0]) + dollar_string + align_sum.format(donors_revised[i][1]) + '  ' + align_num.format(donors_revised[i][2]) + dollar_string + align_avg.format(donors_revised[i][3]) + '\n' for i in range(len(donors_revised))]
    final_string = top_string + ''.join(middle_string)
    print (final_string)
    return final_string

def write_donor_test(i, j):
    '''Text for letters'''
    return paragraph.format(i, j[-1])

def write_donors(x, y):
    '''Write letter to a single donor'''
    with open(x + '.txt', 'w+') as f:
        f.write(write_donor_test(x, y))
    f.close()

def all_donors():
    '''Writes all the donor letters to a file in {name}.txt format'''
    letter = [write_donors(key, value) for key, value in donors.items()]

def quit():
    '''Quits the program'''
    print('quitting this menu')
    return 'exit menu'

def main_response(action, dictionary):
    '''Invokes the script'''
    while True:
        #Error handle will loop until input is valid
        try:
            response = input(action)
            if dictionary[response]() == 'exit menu':
                break
        except KeyError:
            print('\nInvalid input, try again\n')

'''User choices'''
response_dict = {'1': sub_res, '2': createareport, '3': all_donors, '4': quit}

'''Main interation'''
if __name__ == '__main__':
    main_response(action_input, response_dict)





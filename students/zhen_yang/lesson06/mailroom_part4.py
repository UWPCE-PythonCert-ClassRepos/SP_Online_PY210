import os
import sys

""" Data Sturcture for Mail Room Four """
donors_db = {
    'Adan William': [100.75, 1200, 3200.45],
    'Peter Chiykowski': [25.25, 4340.25],
    'Sara Gogo': [650],
    'Jason Zhang': [150.00, 35.50, 80.75],
    'Zooe Bezos': [10, 20]
}
output_directory = 'res_dr'
parent_directory = os.getcwd()
my_path = os.path.join(parent_directory, output_directory)

thankyou_template = "Dear {},\n" + \
    "     Thank you for your generous donation of ${:,.2f} \n" + \
    "     Total Amount:${:,.2f} Number of Gifts:{} Avg Amount:${:,.2f}.\n" + \
    "     It will be put to very good use.\n\n" + \
    "                       Sincerely,\n" + \
    "                           Zhen "

# prompt the three options for user
ori_prompt = '\n'.join(("-- Choose an action: -- ",
                        "1 - Send a Thank You Letter to a single donor.",
                        "2 - Create_Report.",
                        "3 - Send Thank You Letters to all donors.",
                        "4 - Quit \n"))
# prompt the user to input full name of the donor and donation amount
donor_name_prompt = "Please input donor's full name or input 'list' or \
input 'quit' or 'q' to quit : "
donoation_amount_prompt = "Please input the donation amount  or \
input 'quit' or 'q' to quit : "

""" -- Define All The Functions for Option 1: send_thankyou_text -- """
def valid_input(input_str, input_flag):
    if input_str == 'q' or input_str == 'quit':
        quit_program()
    if input_flag == 1:# for valid options
        try:
            if int(input_str) in switch_option_dict:
                return input_str
            else:
                print(" Please input a valid option. ")
                return -1
        except ValueError:
            print(" Please input a valid option. ")
            return -1
    elif input_flag == 2:# for valid donor name
        if input_str == 'list':
            list_donor_names()
            return -1
        else:
            return input_str
    elif input_flag == 3:# for valid donation amount
        try: # Convert the amount into a number
            input_str = float(input_str)
        except ValueError:
            print("Please input a number for donation amount.\
Thank you!: ")
            return -1
        else:
            if float(input_str) >= 0:
                input_amount = float(input_str)
                return input_amount
            else:
                print("Please input a positive number for donation \
amount. Thank you!: ")
                return -1

def out_put(key, amount):
    val = donors_db.get(key)
    tot = sum(donors_db[key])
    avg = tot / len(val)
    return thankyou_template.format(key, amount, tot, len(val), avg)

def generate_thankyou_text(key, amount):
    print(out_put(key, amount))
    return key, amount

# list all the donor's name
def list_donor_names():
    print("The donor name list: ")
    test_list = []
    for key in donors_db.keys():
        print(f"{key}   ", end="")
        test_list.append(key)
    print("\n")
    return test_list

# add new donor or update donation amount of existing donor
def add_update_donor_db(d_name, amount):
    if d_name in donors_db:# for exitsting donor
        donors_db[d_name].append(amount)
    elif d_name != 'list': # for new donor
        donors_db[d_name] = [amount]

def send_thankyou_text():
    while True:
        d_name = input(donor_name_prompt).strip()
        valid_name = valid_input(d_name, 2)
        if valid_name != -1:# valid donor name
            amount = input(donoation_amount_prompt).strip()
            valid_amount = valid_input(amount, 3)
            while valid_amount == -1:# valid donation amount
                amount = input(donoation_amount_prompt).strip()
                valid_amount = valid_input(amount, 3)
            add_update_donor_db(d_name, valid_amount)
            generate_thankyou_text(d_name, valid_amount)
            break

""" -- Define All Functions for Option 2: create_report() -- """
# generate the formater for the report
def generate_report_formater():
    title = '{:^20s}|{:^15s}|{:^15s}|{:^20s}'
    # scientific notation output
    #formater_content = '{:<20s} ${:>14,.2e}{:>15d}  ${:>17,.2e}'
    content = '{:<20s} ${:>14,.2f}{:>15d}  ${:>17,.2f}'
    return title, content

# sort key function
def sort_key(donor):
    # sort the record based on the total amount of the money donated
    return sum(donor[1])
    # sort the record based on the first name
    #return donor[0].split(" ")[0]

# generate_report()
def generate_report(formater_title, formater_content):
    column_list = ['Donor Name', 'Total Amount', 'Num Gifts', 'Average Amount']
    # print the Title of the report
    print(formater_title.format(*column_list))
    print('-' * 71)
    """ sort the record based on the first name
    note: dict.items() return an unsorted list of key value pair
    the return from sorted() is a sorted list of key and value """
    # using lambda function to get the sort key
    #for mykey, val in sorted(donors_db.items(), key=lambda i: sum(i[1])):
    for mykey, val in sorted(donors_db.items(), key=sort_key):
        print(formater_content.format(str(mykey), sum(val),
              len(val), sum(val) / len(val)))
    print("\n")
    return column_list

def create_report():
    formater = ""
    formater = generate_report_formater()
    generate_report(formater[0], formater[1])

""" -- Define All Functions for Option 3: send_letters() -- """
def generate_output_file_name(key, val):
    name_list = key.split()
    new_name = "_".join(name_list)
    file_name = '{}\\{}.txt'.format(my_path, new_name)
    return file_name

def generate_output_content(key, val, file_name):
    last_donation = val[-1]
    try:
        with open(file_name, 'w') as out_file:
            out_file.write(out_put(key, last_donation))
            return 1
    except IOError:
        print("Can't open the file for output!")
        return -1

def generate_output_file():
    print(" All the thank you letters are generated under directory:")
    print(f"{my_path}")
    # create the 'res_dr' directory only if it doesn't exist.
    if not os.path.exists(output_directory):
        os.mkdir(my_path)
    output_records = 0
    for key, val in donors_db.items():
        file_name = generate_output_file_name(key, val)
        generate_output_content(key, val, file_name)
        output_records = output_records + 1 # total number of records
    return output_records

def send_letters():
    generate_output_file()

""" -- Define Option 4: quit_program -- """
def quit_program():
    print("Bye!")
    sys.exit()

# use a dict to switch between options
switch_option_dict = {
    1: send_thankyou_text,
    2: create_report,
    3: send_letters,
    4: quit_program
}

""" -- Define main() function -- """
def main():
    #Forever while loop to let user choose one of four options.
    while True:
        input_str = input(ori_prompt).strip()
        if valid_input(input_str, 1) != -1:
            switch_option_dict.get(int(input_str))()

# put main interaction into the __main__ block
if __name__ == '__main__':
    main() # calling the main() function

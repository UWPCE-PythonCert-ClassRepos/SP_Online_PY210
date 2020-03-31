######################
# Mail Room Part Two #
######################
import os


###############################################################################
# Data Sturcture for Mail Room Two
###############################################################################
donors_db = {
    'Adan William': [100.75, 1200, 3200.45],
    'Peter Chiykowski': [25.25, 4340.25],
    'Sara Gogo': [650],
    'Jason Zhang': [150.00, 35.50, 80.75],
    'Zooe Bezos': [10, 20]
}


thankyou_template = "Dear {},\n" + \
    "     Thank you for your generous donation of ${:,.2f} \n" + \
    "     Total Amount:${:,.2f} Number of Gifts:{} Avg Amount:${:,.2f}.\n" + \
    "     It will be put to very good use.\n\n" + \
    "                       Sincerely,\n" + \
    "                           Zhen "

##################
# prompt the three options for user
##################
def ori_prompt():
    print("-- Choose an action: -- ")
    print("1 - Send a Thank You Letter to a single donor.")
    print("2 - Create_Report.")
    print("3 - Send Thank You Letters to all donors.")
    print("4 - Quit ")
    input_str = input()
    input_str.strip()
    return input_str


##################
# prompt the user to input full name of the donor
##################
def fullname_prompt():
    input_str = input("Please input donor's full name or input 'list' or \
input 'quit' or 'q' to quit : ")
    input_str.strip() # remove any whitespace
    if input_str.isdigit():
        print("Input is a number not a name.")
        return -1
    elif input_str == 'quit' or input_str == 'q':
        quit_program()
    return input_str


##################
# prompt the user to input a donation amount
##################
def amount_prompt():
    input_str = input("Please input the donation amount  or \
input 'quit' or 'q' to quit : ")
    input_str.strip()  # remove any whitespace
    if input_str == 'quit' or input_str == 'q':
        quit_program()
    # Convert the amount into a number
    try:
        input_str = float(input_str)
    except ValueError:
        print("Please input a number for donation amount. Thank you!")
        return -1
    if float(input_str) >= 0:
        input_amount = float(input_str)
        return input_amount
    else:
        print("Plese input a positive number for donation amount. Thank you! ")
        return -1

def out_put(key, amount):
    val = donors_db.get(key)
    tot = sum(donors_db[key])
    avg = tot / len(val)
    return thankyou_template.format(key, amount, tot, len(val), avg)


##################
# print the thank you letter to a single donoar on screen
# or print to different files to all donors
##################
def thankyou_letter(*argv):
    if len(argv) == 2:# to single donor on the screen
        print(out_put(argv[0], argv[1]))

    elif len(argv) == 3:# to all donors to a file
        last_donation = argv[1][len(argv[1]) - 1]
        argv[2].write(out_put(argv[0], last_donation))


###################################
# define send_thankyou() Option 1 #
###################################
def send_thankyou():
    d_name = fullname_prompt()
    if d_name != -1:
        while d_name == 'list':# list all the donor's name
            print("The donor name list: ")
            for key in donors_db.keys():
                print(f"{key}   ", end="")
            print("\n")

            d_name = fullname_prompt()
        if d_name == -1: # quit the task
            return
        if d_name in donors_db:# for exitsting donor
            amount = amount_prompt()
            if amount != -1: # if user doesn't want to quit the task
                donors_db[d_name].append(amount)
                #print(f"1.donor[{d_name}]:{donors_db[d_name]}")
                thankyou_letter(d_name, amount)
        else: # for new donor,
            amount = amount_prompt()
            if amount != -1: # if user does't want to quit the task
                donors_db[d_name] = [amount]
                #print(f"2.donor[{d_name}]:{donors_db[d_name]}")
                thankyou_letter(d_name, amount)

# sort key function
def sort_key(donor):
    # sort the record based on the first name
    return donor[0].split(" ")[0]


###################################
# define create_report() Option 2 #
###################################
def create_report():
    col_1 = 'Donor Name'
    col_2 = 'Total Amount'
    col_3 = 'Num Gifts'
    col_4 = 'Average Amount'
    formater_title = '{:^20s}|{:^15s}|{:^15s}|{:^20s}'
    # scientific notation output
    #formater_content = '{:<20s} ${:>14,.2e}{:>15d}  ${:>17,.2e}'

    formater_content = '{:<20s} ${:>14,.2f}{:>15d}  ${:>17,.2f}'

    # print the Title of the report
    print(formater_title.format(col_1, col_2, col_3, col_4))
    print('-' * 71)

    # sort the record based on the first name
    # note: dict.items() return a list of key value pair
    # the return from sorted() is a sorted list of key and value
    for mykey, val in sorted(donors_db.items(), key=sort_key):
        tot_amount = 0
        avg_amount = 0
        name = str(mykey)
        count = len(val)
        for j in val:
            tot_amount = tot_amount + j
        avg_amount = tot_amount / count
        print(formater_content.format(name, tot_amount, count, avg_amount))

    print("\n")


#######################################
# define send_all_thankyou() Option 3 #
#i######################################
def send_all_thankyou():
    directory = 'res_dr'
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, directory)
    print(" The Thank you letters are generated under directory:")
    print(f"{path}")
    if not os.path.exists(directory):
        os.mkdir(path)
    for key, val in donors_db.items():
        name_list = key.split()
        new_name = "_".join(name_list)
        file_name = '{}\\{}.txt'.format(path, new_name)
        with open(file_name, 'w') as out_file:
            thankyou_letter(key, val, out_file)


###################################
# define Quit_Program()  Option 4 #
###################################
def quit_program():
    print("Bye!")
    exit()

# use a dict to switch between options
switch_option_dict = {
    1: send_thankyou,
    2: create_report,
    3: send_all_thankyou,
    4: quit_program
}


#################################
# define main() function        #
#################################
def main():
    #Forever loop for letting user choose one of three options.
    while True:
        input_str = ori_prompt()
        if input_str.isdigit() and int(input_str) in switch_option_dict:
            switch_option_dict.get(int(input_str))()
        else:
            print(" Please input a valid option. ")

# put main interaction into the __main__ block
if __name__ == '__main__':
    # calling the main() fuction
    main()

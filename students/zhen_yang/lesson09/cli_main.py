# cli_main.py
# Command Line Interface Module
#This module has a set user-interaction menu functions to handle each of the
#option of the mailroom program.
import os
import io
import sys
import webbrowser
from donor_models import Donor, DonorCollection
from html_render import *


output_directory = 'allthankyou_letters_dr'
parent_directory = os.getcwd()
my_path = os.path.join(parent_directory, output_directory)

donors_db = DonorCollection()

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


def create_initial_donor_database():
    donor_1 = Donor('Adan', 'William', 100.75)
    donor_1.add_donation_amount(1200)
    donor_1.add_donation_amount(3200.45)

    donor_2 = Donor('Peter', 'Chiykowski', 25.25)
    donor_2.add_donation_amount(4340.25)

    donor_3 = Donor('Sara', 'Gogo', 650)

    donor_4 = Donor('Jason', 'Zhang', 150.00)
    donor_4.add_donation_amount(35.50)
    donor_4.add_donation_amount(80.75)

    donor_5 = Donor('Zooe', 'Bezos', 10)
    donor_5.add_donation_amount(20)

    #donors_db = DonorCollection()
    donors_db.update_donors_db(donor_1)
    donors_db.update_donors_db(donor_2)
    donors_db.update_donors_db(donor_3)
    donors_db.update_donors_db(donor_4)
    donors_db.update_donors_db(donor_5)

###########################################
# -- Define Option 1: send_thankyou_text --
###########################################
def valid_name(oldname):
    name = oldname.split()
    # if name doesn't contain last name, then last name is empty
    if len(name) == 1:
        name.append('')
    else:
        name = name[:2]
    new_donor = Donor(name[0], name[1], 0)
    the_donor = donors_db.find_donor(new_donor)
    if the_donor is None: # donor name is not on the donor database
        print(f"The donor name '{oldname}' is not on the donor data base.")
        input_str = input('Do you still want to create the donor? y or n ')
        if input_str == 'y':
            return name # 'name' is just a string
        elif input_str == 'n':
            return -1
        else:
            print("Unknown input. ")
            return -1
    else:
        return name


def valid_input(input_str, input_flag):
    if input_str == 'q' or input_str == 'quit':
        quit_program()
    if input_flag == 1:# validate the program options
        try:
            if int(input_str) in switch_option_dict:
                return input_str
            else:
                print(" Please input a valid option. ")
                return -1
        except ValueError:
            print(" Please input a valid option. ")
            return -1
    elif input_flag == 2:# validate the donor name
        if input_str == 'list':
            list_donor_names()
            return -1
        else:
            name = valid_name(input_str)
            if name == -1:
                return -1
            else:
                return name
    elif input_flag == 3:# validate the donation amount
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

def list_donor_names():
    print("The donor name list: ")
    for donor in donors_db._donorList:
        print(f"{donor._first_name} {donor._last_name}, ", end="")
    print("\n")


def send_thankyou_text():
    while True:
        d_name = input(donor_name_prompt).strip()
        valid_name = valid_input(d_name, 2)# validate the donor name
        if valid_name != -1:# valid donor name
            amount = input(donoation_amount_prompt).strip()
            valid_amount = valid_input(amount, 3)# validate the donation
            while valid_amount == -1:# invalid donation amount
                amount = input(donoation_amount_prompt).strip()
                valid_amount = valid_input(amount, 3)
            # get a new donor object
            donor = Donor(valid_name[0], valid_name[1], valid_amount)
            # update the donor database
            donor = donors_db.update_donors_db(donor)
            # print the thank you letter for current donor
            print(donor.generate_thankyou_letter())
            break

######################################
# -- Define Option 2: create_report --
######################################
def create_report():
    print(donors_db.create_report_title())
    print(donors_db.create_report_content())
    create_html_report()
    # open the 'donor_report.html in webbrowser'
    filename = '{}\\{}'.format(parent_directory, 'donors_report.html')
    #webbrowser.open_new_tab(filename)
    webbrowser.open_new_tab('donors_report.html')


def render_page(page, filename):
    f = io.StringIO()
    page.render(f)
    html_content = f.getvalue()
    #print(html_content)
    with open(filename, 'w') as outfile:
        outfile.write(html_content)
        return html_content

def create_html_report():
    page = Html()
    ############
    # set the html table customer setting
    ############
    head = Head()
    style = Style()
    style.append(Customer('#customers {border-collapse: \
collapse; width: 50%;}'))
    #style.append(Customer('#customers tr:nth-child(even)'))
    #style.append(Customer('   {background-color: #f2f2f2;}'))
    style.append(Customer('#customers th {'))
    style.append(Customer('   border: 3px solid #9c9c9c;'))
    style.append(Customer('   padding: 8px; padding-top: 12px; \
padding-bottom:12px;'))
    style.append(Customer('   text-align: center;'))
    style.append(Customer('   color: c0c0c0;}'))
    style.append(Customer('#customers td:nth-child(even)'))
    style.append(Customer('   {text-align: right}'))
    style.append(Customer('#customers td:nth-child(odd)'))
    style.append(Customer('   {text-align: center}'))
    style.append(Customer('#customers td {'))
    style.append(Customer('   border: 3px solid #9c9c9c;'))
    style.append(Customer('   padding: 8px;}'))
    style.append(Customer('body {background-image: url(table_background.jpg)}'))
    head.append(style)
    page.append(head)
    ############
    # output the donor table contents
    ############
    body = Body()
    body.append(H(1, 'Donation Report',
                  style="font-style: oblique; color: 9c9c9c"))
    table = Table(id='customers')
    column_list = Tr()
    column_list.append(Th('Donor Name'))
    column_list.append(Th('Total Amount'))
    column_list.append(Th('Num Gifts'))
    column_list.append(Th('Average Amount'))
    table.append(column_list)
    for donor in donors_db.sort_donors_db():
        donor_tr = Tr()
        name = '{} {}'.format(donor._first_name, donor._last_name)
        donor_tr.append(Td(name))
        if donor.total_amount > 1000000:
            donor_tr.append(Td('${:,.3e}'.format(donor.total_amount)))
        else:
            donor_tr.append(Td('${:,.2f}'.format(donor.total_amount)))
        donor_tr.append(Td('{}'.format(donor.total_gifts)))
        if (donor.total_amount / donor.total_gifts) > 1000000:
            donor_tr.append(Td('${:,.3e}'.format
                            (donor.total_amount / donor.total_gifts)))
        else:
            donor_tr.append(Td('${:,.2f}'.format
                            (donor.total_amount / donor.total_gifts)))

        table.append(donor_tr)
    body.append(table)
    page.append(body)
    return render_page(page, 'donors_report.html')


#####################################
# -- Define Option 4: send_letters --
#####################################
def generate_output_filename(donor):
    return '{}\\{}_{}.txt'.format(my_path, donor._first_name,
                                  donor._last_name)

def generate_output_content(donor, file_name):
    try:
        with open(file_name, 'w+') as out_file:
            out_file.write(donor.send_letters())
    except IOError:
        print(f"Can't open the file {file_name }for output!")


def send_letters():
    print(" All the thank you letters are generated under directory:")
    print(f"{my_path}")
    # create the 'allthankyou_letters_dr' directory only if it doesn't exist.
    if not os.path.exists(output_directory):
        os.mkdir(my_path)

    sorted_list = donors_db.sort_donors_db()
    for donor in sorted_list:
        file_name = generate_output_filename(donor)
        generate_output_content(donor, file_name)

#####################################
# -- Define Option 4: quit_program --
#####################################
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

##############################
# -- Define main() function --
##############################
def main():
    #generate the initial donor database
    create_initial_donor_database()

    #Forever while loop to let user choose one of four options.
    while True:
        input_str = input(ori_prompt).strip()
        if valid_input(input_str, 1) != -1:
            switch_option_dict.get(int(input_str))()

# put main interaction into the __main__ block
if __name__ == '__main__':
    main() # calling the main() function

#!/usr/bin/env python3


from donor_models import Donor
from donor_models import DonorCollection
from mailroom_control import MailroomControl

###################################

global canned_sorted_report
global canned_thankyou_email
global canned_all_donors_listed
global canned_all_thankyou_letters

charity_name = "ABC Charity"

all_donors = DonorCollection()
mailroom_control = MailroomControl(charity_name)

###################################

# default donors db
db_donors2 = {
            "Jane Smith": [25, 50],
            "Tom Adams": [100],
            "Helen Smalls": [10, 20, 30],
            "Ming Chan": [50],
            "Mary Jones": [5, 10, 15]}

###################################

# general support methods

def init():
    global canned_sorted_report
    global canned_thankyou_email
    global canned_all_donors_listed
    global canned_all_thankyou_letters
    canned_sorted_report = "canned_sorted_report.txt"
    canned_thankyou_email = "canned_thankyou_email.txt"
    canned_all_donors_listed = "canned_all_donors_listed.txt"
    canned_all_thankyou_letters = "canned_all_thankyou_letters.txt"


def init_donors_collection():
    for key, value in db_donors2.items():
        donor_name = key
        donations_ary = value
        dx = Donor(donor_name, donations_ary)
        all_donors.add_donor(dx)
    #diag_show()


def diag_show():
    for key, value in all_donors.dict_donors.items():
        donor_name = key
        donations_ary = value
        msg = ""
        msg += f"donor {donor_name} donations are {donations_ary}"
        print(msg)


def read_file(in_filespec):
    with open(in_filespec, "r") as f:
        data = f.read()
    return data


def write_file(in_filespec, in_msg):
    with open(in_filespec, "w") as f:
        f.write(in_msg)


###################################

# op support methods

def get_all_donors():
    return all_donors


def get_mailroom_control():
    return mailroom_control


###################################

# main Operations

def op_receive_donation():
    thankyou_email = mailroom_control.receive_donation(all_donors)
    # write_file(canned_thankyou_email, msg)
    return thankyou_email


def op_display_list_of_donors():
    listed_donors = mailroom_control.display_donors(all_donors.dict_donors)
    # write_file(canned_all_donors_listed, listed_donors)
    return listed_donors


def op_create_report():
    report = mailroom_control.create_report(all_donors.dict_donors)
    # write_file(canned_sorted_report, report)
    return report


def op_write_letters_to_all():
    all_thankyou_letters = mailroom_control.write_letters_to_all_donors(all_donors.dict_donors)
    # write_file(canned_all_thankyou_letters, all_thankyou_letters)
    quit()


def op_done():
    print("mailroom end")
    quit()


###################################

def mailroom_main():
    print("mailroom begin")

    op_action_dict = {
                    'D': op_receive_donation,
                    'L': op_display_list_of_donors,
                    'R': op_create_report,
                    'W': op_write_letters_to_all,
                    'Q': op_done
                     }

    while True:
        operation = mailroom_control.ui_menu_main()
        op_action_dict.get(operation)()

###################################

# main, test funcs

init()
init_donors_collection()

if __name__ == "__main__":
    mailroom_main()




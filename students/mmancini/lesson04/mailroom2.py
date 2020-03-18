#!/usr/bin/env python3

charity_name = "ABC Charity"

db_donors2 = {
            "Jane Smith": [25, 50],
            "Tom Adams": [100],
            "Helen Smalls": [10, 20, 30],
            "Ming Chan": [50],
            "Mary Jones": [5, 10, 15]}

####################################


def show_donors2():
    print(f"List of Donors:")
    for donor in db_donors2.keys():
        print(f" ", donor)


def process_new_donor2(name):
    amount_ary = []

    amount = menu_donation_amount2()
    amount_ary.append(amount)

    db_donors2.update({name: amount_ary})
    print(f"new donor {name} donated {amount}")

    return amount


def process_existing_donor2(name):

    amount = menu_donation_amount2()
    amounts_ary = db_donors2[name]
    amounts_ary.append(amount)
    db_donors2[name] = amounts_ary
    print(f"existing donor {name} donated {amount}")

    return amount


def send_thankyou2():
    msg = ""
    msg += "Please enter donor name or 'list' for list of donors:\n"
    msg += ".....>>"

    entry = ""
    need_entry = True
    while need_entry:
        entry = input(msg)
        if entry.lower() == 'list':
            show_donors2()
        else:
            # have a donor name
            need_entry = False

    donor_name,  donation_amount = process_donor2(entry)
    process_send_thankyou_email2(donor_name, donation_amount)


def main_menu2():
    msg = ""
    msg += "Please enter option from below:\n"
    msg += " S: Send thank you note\n"
    msg += " R: Create report\n"
    msg += " W: Send letters to all\n"
    msg += " Q: Quit\n"
    msg += ".....>>"

    entry = input(msg)

    return entry

###################################


def done2():
    quit()


def mailroom2():
    print("mailroom begin")

    op_action_dict = {
                    'S': send_thankyou2,
                    'R': create_report_sorted2,
                    'W': write_letters_to_all2,
                    'Q': done2
                     }

    while True:
        operation = main_menu2()
        op_action_dict.get(operation)()

    # print("mailroom end")


###################################


# main, test funcs

if __name__ == "__main__":

    # mailroom()
    mailroom2()


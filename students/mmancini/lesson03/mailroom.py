#!/usr/bin/env python3

charity_name = "ABC Charity"

db_donors = [("Jane Smith", [25, 50]),
             ("Tom Adams", [100]),
             ("Helen Smalls", [10, 20, 30]),
             ("Ming Chan", [50]),
             ("Mary Jones", [5, 10, 15])]


####################################

def get_donor_stats(in_donor):
    stats_ary = []

    donations_ary = in_donor[1]

    num_donations = 0
    tot_of_donations = 0
    for donation_amount in donations_ary:
        num_donations += 1
        tot_of_donations += donation_amount
    avg_of_donations = tot_of_donations / num_donations

    stats_ary.append(tot_of_donations)
    stats_ary.append(num_donations)
    stats_ary.append(avg_of_donations)

    return stats_ary


def create_report():
    print(f"Donor Report:")

    hdr1 = ["Donor Name ", "Donation Total", "Number of Donations", "Donation Average"]
    hdr2 = ["-----------", "--------------", "-------------------", "----------------"]

    print("   {: <20} {: >20} {: >20} {: >20}".format(*hdr1))
    print("   {: <20} {: >20} {: >20} {: >20}".format(*hdr2))
    for donor in db_donors:
        donor_stats = get_donor_stats(donor)
        print("   {: <20} {: >20} {: >20} {: >20}".format(donor[0].ljust(10, ' '), *donor_stats))


def menu_donation_amount():
    msg = ""
    msg += "Please enter a donation amount::\n"
    msg += ".....>>"

    donation_amount_entry = int(input(msg))

    return donation_amount_entry


def show_donors():
    print(f"List of Donors:")
    for donor in db_donors:
        print(f" ", donor[0])


def process_new_donor(name):
    amount_ary = []

    amount = menu_donation_amount()
    amount_ary.append(amount)

    db_donors.append((name, amount_ary))

    print(f"new donor {name} donated {amount}")

    return amount


def process_existing_donor(name):
    donor_names_lst = [x[0] for x in db_donors]
    x = donor_names_lst.index(name)

    amount = menu_donation_amount()
    db_donors[x][1].append(amount)
    print(f"existing donor {name} donated {amount}")

    return amount


def process_send_thankyou_email(in_name, in_amount):
    print(f"Thank You Email:")
    msg = ""
    msg += f"To: {in_name}@abc.def:\n"

    msg += f"From: {charity_name}.org:\n"
    msg += f"Subject:  Thank You:\n"
    msg += f"Body: Dear {in_name} Thank You for your generous donation of ${in_amount}:\n"
    msg += ""

    print(msg)


def process_donor(in_name):

    donor_names_lst = [x[0] for x in db_donors]

    if in_name in donor_names_lst:
        amount_donated = process_existing_donor(in_name)
    else:
        amount_donated = process_new_donor(in_name)

    return in_name, amount_donated


def send_thankyou():
    msg = ""
    msg += "Please enter donor name or 'list' for list of donors:\n"
    msg += ".....>>"

    entry = ""
    need_entry = True
    while need_entry:
        entry = input(msg)
        if entry.lower() == 'list':
            show_donors()
        else:
            # have a donor name
            need_entry = False

    donor_name,  donation_amount = process_donor(entry)
    process_send_thankyou_email(donor_name, donation_amount)


def main_menu():
    msg = ""
    msg += "Please enter option from below:\n"
    msg += " S: Send thank you note\n"
    msg += " R: Create report\n"
    msg += " Q: Quit\n"
    msg += ".....>>"

    entry = input(msg)

    return entry

###################################


def mailroom():
    print("mailroom begin")

    is_done = False
    while True:
        operation = main_menu()

        if operation == 'S':
            send_thankyou()
        elif operation == 'R':
            create_report()
        elif operation == 'Q':
            is_done = True
        else:
            print(f"Invalid Entry, please retry: ==> ", operation)

        if is_done:
            break

    print("mailroom end")


###################################


# main, test funcs

if __name__ == "__main__":
    mailroom()


#!/usr/bin/env python3

charity_name = "ABC Charity"

db_donors2 = {
            "Jane Smith": [25, 50],
            "Tom Adams": [100],
            "Helen Smalls": [10, 20, 30],
            "Ming Chan": [50],
            "Mary Jones": [5, 10, 15]}

####################################


def get_donor_stats2(in_donor):
    stats_ary = []

    donations_ary = db_donors2[in_donor]

    num_donations = 0
    tot_of_donations = 0
    for donation_amount in donations_ary:
        num_donations += 1
        tot_of_donations += donation_amount
    avg_of_donations = tot_of_donations / num_donations

    stats_ary.append(tot_of_donations)
    stats_ary.append(num_donations)
    stats_ary.append(avg_of_donations)

    # print("fstats={}",stats_ary)
    return stats_ary


def create_report2():
    print(f"Donor Report:")

    hdr1 = ["Donor Name ", "Donation Total", "Number of Donations", "Donation Average"]
    hdr2 = ["-----------", "--------------", "-------------------", "----------------"]

    print("   {: <20} {: >20} {: >20} {: >20}".format(*hdr1))
    print("   {: <20} {: >20} {: >20} {: >20}".format(*hdr2))
    for donor in db_donors2:
        donor_stats = get_donor_stats2(donor)
        print("   {: <20} {: >20} {: >20} {: >20}".format(donor.ljust(10, ' '), *donor_stats))


def create_report_sorted2():
    print(f"Donor Report:")

    # sort donors report by total donation
    db2 = []
    for donor in db_donors2:
        donor_stats = get_donor_stats2(donor)
        tup = (donor,)
        tup += (donor_stats[1],)
        tup += (donor_stats[2],)
        db2.append((donor_stats[0], tup))
    db2.sort(reverse=True)

    hdr1 = ["Donor Name ", "Donation Total", "Number of Donations", "Donation Average"]
    hdr2 = ["-----------", "--------------", "-------------------", "----------------"]

    print("   {: <20} {: >20} {: >20} {: >20}".format(*hdr1))
    print("   {: <20} {: >20} {: >20} {: >20}".format(*hdr2))

    # for key, value in db_donors2.items():
    for donor_info in db2:

        tup_info = donor_info[1]
        rpt_donation_line = {"donor_name": tup_info[0], "donation_total": donor_info[0], "number_of_donations": tup_info[1],
                             "donation_average": tup_info[2]}
        print("   {donor_name: <20} {donation_total: >20} {number_of_donations: >20} "
                  "{donation_average: >20}".format(**rpt_donation_line))


def menu_donation_amount2():
    msg = ""
    msg += "Please enter a donation amount::\n"
    msg += ".....>>"

    donation_amount_entry = int(input(msg))

    return donation_amount_entry


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


def process_send_thankyou_email2(in_name, in_amount):
    print(f"Thank You Email:")

    dict_data_line = {"donor_name": in_name, "donation_amount": float(in_amount)}

    msg = ""
    msg += f"To: {in_name}@abc.def:\n"

    msg += f"From: {charity_name}.org:\n"
    msg += f"Subject:  Thank You:\n"
    msg += f"Body: Dear {in_name} Thank You for your generous donation of ${in_amount}:\n".format(**dict_data_line)
    msg += ""

    print(msg)

    return msg


def process_donor2(in_name):

    donor_names_lst = db_donors2.keys()
    if in_name in donor_names_lst:
        amount_donated = process_existing_donor2(in_name)
    else:
        amount_donated = process_new_donor2(in_name)

    return in_name, amount_donated


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


def write_letters_to_all2():

    for key, value in db_donors2.items():

        donor_name = key
        donations_ary = value
        donations_total = sum(donations_ary)

        filename = donor_name + ".txt"
        with open(filename, "w") as f:
            dict_data_line = {"donor_name": donor_name, "donation_amount": float(donations_total)}
            thank_you_letter = ""
            thank_you_letter += f"Dear {donor_name} Thank You for your generous donations " \
                                f"totaling ${donations_total}:\n".format(**dict_data_line)
            f.write(thank_you_letter)


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


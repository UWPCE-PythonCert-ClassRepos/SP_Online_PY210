#!/usr/bin/env python3

charity_name = "ABC Charity"

db_donors = {
            "Jane Smith": [25, 50],
            "Tom Adams": [100],
            "Helen Smalls": [10, 20, 30],
            "Ming Chan": [50],
            "Mary Jones": [5, 10, 15]}

####################################


def get_donor_stats(in_donor):
    stats_ary = []

    donations_ary = db_donors[in_donor]

    num_donations = len(donations_ary)
    tot_of_donations = sum(donations_ary)
    avg_of_donations = tot_of_donations / num_donations

    stats_ary.append(tot_of_donations)
    stats_ary.append(num_donations)
    stats_ary.append(avg_of_donations)

    # print("fstats={}",stats_ary)
    return stats_ary


def get_highest_donor_average_comprehensions(in_highest_avg_donation_to_beat):
    print(f"Donors with a donation average higher than $" + str(in_highest_avg_donation_to_beat))

    # use list Comprehensions

    # first get the stats of all donors
    dict_donors_avg = {}
    for donor in db_donors:
        donor_stats = get_donor_stats(donor)
        dict_donors_avg[donor] = donor_stats[2]

    # using list comprehensions determine donors with highest average donations
    lst_high_donors = [i for i in dict_donors_avg if dict_donors_avg[i] > in_highest_avg_donation_to_beat]
    # print(*lst_high_donors, sep="\n")

    print(" {: <20} =  {: <20}".format("Donor", "Average"))
    for donor in lst_high_donors:
        print(" {: <20} =  {: <20}" .format(donor, dict_donors_avg[donor]))
    print("")


def create_report():
    print(f"Donor Report:")

    hdr1 = ["Donor Name ", "Donation Total", "Number of Donations", "Donation Average"]
    hdr2 = ["-----------", "--------------", "-------------------", "----------------"]

    print("   {: <20} {: >20} {: >20} {: >20}".format(*hdr1))
    print("   {: <20} {: >20} {: >20} {: >20}".format(*hdr2))
    for donor in db_donors:
        donor_stats = get_donor_stats(donor)
        print("   {: <20} {: >20} {: >20} {: >20}".format(donor.ljust(10, ' '), *donor_stats))


def create_report_sorted():
    print(f"Donor Report:")

    # sort donors report by total donation
    db2 = []
    for donor in db_donors:
        donor_stats = get_donor_stats(donor)
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
        rpt_donation_line = {"donor_name": tup_info[0], "donation_total": donor_info[0],
                             "number_of_donations": tup_info[1],
                             "donation_average": tup_info[2]}
        print("   {donor_name: <20} {donation_total: >20} {number_of_donations: >20} "
              "{donation_average: >20}".format(**rpt_donation_line))


def menu_donation_amount():
    msg = ""
    msg += "Please enter a donation amount::\n"
    msg += ".....>>"

    donation_amount_entry = -1
    while donation_amount_entry < 0:
        try:
            donation_amount_entry = int(input(msg))
        except ValueError:
            print('\nInvalid entry, Please enter a positive single dollar amount!')

    return donation_amount_entry


def show_donors():
    print(f"List of Donors:")
    print(f" ", *db_donors.keys())


def process_new_donor(name):
    amount_ary = []

    amount = menu_donation_amount()
    amount_ary.append(amount)

    db_donors.update({name: amount_ary})
    print(f"new donor {name} donated {amount}")

    return amount


def process_existing_donor(name):

    amount = menu_donation_amount()
    db_donors[name].append(amount)
    print(f"existing donor {name} donated {amount}")

    return amount


def process_send_thankyou_email(in_name, in_amount):
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


def process_donor(in_name):

    donor_names_lst = db_donors.keys()
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


def write_letters_to_all():

    for key, value in db_donors.items():

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


def main_menu():
    msg = ""
    msg += "Please enter option from below:\n"
    msg += " S: Send thank you note\n"
    msg += " s: Show highest donors comprehensions\n"
    msg += " R: Create report\n"
    msg += " W: Send letters to all\n"
    msg += " Q: Quit\n"
    msg += ".....>>"

    entry = input(msg)

    return entry


###################################


def show_highest_donors_comprehensions():
    highest_avg_donation_to_beat = 35       # arbitrary
    get_highest_donor_average_comprehensions(highest_avg_donation_to_beat)


def done():
    quit()


def mailroom():
    print("mailroom begin")

    op_action_dict = {
                    'S': send_thankyou,
                    's': show_highest_donors_comprehensions,        # list comprehensions
                    'R': create_report_sorted,
                    'W': write_letters_to_all,
                    'Q': done
                     }

    while True:
        operation = main_menu()

        try:
            op_action_dict.get(operation)()
        except TypeError:
            print('\n\nInvalid operation code.  Please retry!')

    # print("mailroom end")


###################################


# main, test funcs

if __name__ == "__main__":

    mailroom()


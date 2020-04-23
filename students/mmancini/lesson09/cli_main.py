#!/usr/bin/env python3


from donor_models import Donor
from donor_models import Donor_Collection

###################################

charity_name = "ABC Charity"

all_donors = Donor_Collection()

###################################

# db_donors2 = {
#             "Jane Smith": [25, 50],
#             "Tom Adams": [100],
#             "Helen Smalls": [10, 20, 30],
#             "Ming Chan": [50],
#             "Mary Jones": [5, 10, 15]}

###################################

def get_all_donors():
    return all_donors


def get_donor_stats(in_donor,in_dict_all_donors):
    stats_ary = []

    donations_ary = in_dict_all_donors[in_donor]

    num_donations = 0
    tot_of_donations = 0

    num_donations = len(donations_ary)
    tot_of_donations = sum(donations_ary)
    avg_of_donations = tot_of_donations / num_donations

    stats_ary.append(tot_of_donations)
    stats_ary.append(num_donations)
    stats_ary.append(avg_of_donations)

    # print("fstats={}",stats_ary)
    return stats_ary


def create_report(in_dict_donors_db):

    print(f"Donor Report:")

    # sort donors report by total donation
    db2 = []
    for donor in in_dict_donors_db:
        donor_stats = get_donor_stats(donor,in_dict_donors_db)
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


def write_letters_to_all(in_dict_donors_db):

    for key, value in in_dict_donors_db.items():

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


###################################


def ui_main_menu():
    msg = ""
    msg += "Please enter option from below:\n"
    msg += " S: Send thank you note\n"
    msg += " R: Create report\n"
    msg += " W: Send letters to all\n"
    msg += " Q: Quit\n"
    msg += ".....>>"

    #***MMM entry = input(msg)
    #entry = 'R'
    entry = 'W'

    return entry

###################################

def done2():
    quit()


def mailroom_main():
    print("mailroom begin")

    op_action_dict = {
                    #'S': send_thankyou2,
                    'R': create_report,
                    'W': write_letters_to_all,
                    'Q': done2
                     }

    while True:
        operation = ui_main_menu()
        op_action_dict.get(operation)()

        #***MMM
        break

    # print("mailroom end")





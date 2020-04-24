#!/usr/bin/env python3


###################################


class MailroomControl():

    def __init__(self, in_charity_name):
        self.charity_name = in_charity_name
        pass

    ######################################

    # Support lib methods

    def get_donor_stats(self, in_donor, in_dict_all_donors):
        stats_ary = []

        donations_ary = in_dict_all_donors[in_donor]

        num_donations = len(donations_ary)
        tot_of_donations = sum(donations_ary)
        avg_of_donations = tot_of_donations / num_donations

        stats_ary.append(tot_of_donations)
        stats_ary.append(num_donations)
        stats_ary.append(avg_of_donations)

        # print("fstats={}",stats_ary)
        return stats_ary


    def process_donor_donation(self, in_all_donors, name, amount):
        in_all_donors.add_donation(name, amount)
        print(f"donor {name} donated {amount}")
        email = self.send_thankyou_email(name, amount)
        return email


    ###################################

    # Mailroom control methods

    def display_donors(self, in_dict_all_donors):
        hdr_listed_donors = f"List of Donors:"
        listed_donors = hdr_listed_donors + "\n" + str((f" ", *in_dict_all_donors.keys()))
        print(listed_donors)
        return listed_donors


    def send_thankyou_email(self, in_name, in_amount):
        print(f"Thank You Email:")

        dict_data_line = {"donor_name": in_name, "donation_amount": float(in_amount)}

        msg = ""
        msg += f"To: {in_name}@abc.def:\n"

        msg += f"From: {self.charity_name}.org:\n"
        msg += f"Subject:  Thank You:\n"
        msg += f"Body: Dear {in_name} Thank You for your generous donation of ${in_amount}:\n".format(**dict_data_line)
        msg += ""

        print(msg)
        return msg


    def create_report(self, in_dict_donors_db):
        print(f"Donor Report:")

        # sort donors report by total donation
        db2 = []
        for donor in in_dict_donors_db:
            donor_stats = self.get_donor_stats(donor, in_dict_donors_db)
            tup = (donor,)
            tup += (donor_stats[1],)
            tup += (donor_stats[2],)
            db2.append((donor_stats[0], tup))
        db2.sort(reverse=True)

        hdr1 = ["Donor Name ", "Donation Total", "Number of Donations", "Donation Average"]
        hdr2 = ["-----------", "--------------", "-------------------", "----------------"]

        hdrline1 = ("   {: <20} {: >20} {: >20} {: >20}".format(*hdr1)) + "\n"
        hdrline2 = ("   {: <20} {: >20} {: >20} {: >20}".format(*hdr2)) + "\n"

        rptlines = ""
        # for key, value in db_donors2.items():
        for donor_info in db2:

            tup_info = donor_info[1]
            rpt_donation_line = {"donor_name": tup_info[0], "donation_total": donor_info[0],
                                 "number_of_donations": tup_info[1],
                                 "donation_average": tup_info[2]}
            rptlines += ("   {donor_name: <20} {donation_total: >20} {number_of_donations: >20} "
                         "{donation_average: >20}".format(**rpt_donation_line)) + "\n"

        report = hdrline1 + hdrline2 + rptlines
        print(report)
        return report


    def receive_donation(self, in_dict_donors_db):
        donor_name = self.ui_menu_specify_donor_name()
        donation_amount = self.ui_menu_specify_donation_amount()
        thankyou_email = self.process_donor_donation(in_dict_donors_db, donor_name, donation_amount)
        return thankyou_email


    def write_letters_to_all_donors(self, in_dict_donors_db):
        all_thankyou_letters = ""
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
                all_thankyou_letters += thank_you_letter
                f.write(thank_you_letter)
        return all_thankyou_letters

    ###################################

    # ui Menus

    def ui_menu_main(self):
        msg = ""
        msg += "Please enter option from below:\n"
        msg += " D: Receive donation\n"
        msg += " L: Display list of donors\n"
        msg += " R: Create report\n"
        msg += " W: Write letters to all\n"
        msg += " Q: Quit\n"
        msg += ".....>>"

        entry = input(msg)

        return entry


    def ui_menu_specify_donor_name(self):
        msg = ""
        msg += "Please enter donor name :\n"
        msg += ".....>>"

        entry = input(msg)

        return entry


    def ui_menu_specify_donation_amount(self):
        msg = ""
        msg += "Please enter a donation amount::\n"
        msg += ".....>>"

        donation_amount_entry = int(input(msg))

        return donation_amount_entry




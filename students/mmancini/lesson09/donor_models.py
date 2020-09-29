#!/usr/bin/env python3


###################################


class Donor():

    def __init__(self, full_name, in_donations):
        self.name = full_name
        self.lst_donations = in_donations


    def add_to_donations(self, in_donation_amount):
        self.lst_donations.append(in_donation_amount)


    @property
    def get_tot_donations(self):
        donations_total = sum(self.lst_donations)
        return donations_total


    @property
    def get_num_donations(self):
        num_donations = len(self.lst_donations)
        return num_donations


    @property
    def get_avg_donations(self):
        dt = self.get_tot_donations
        nd = self.get_num_donations
        avg_donations = dt / nd
        return avg_donations


    def get_donor_stats(self):
        stats_ary = []
        stats_ary.append(self.get_tot_donations)
        stats_ary.append(self.get_num_donations)
        stats_ary.append(self.get_avg_donations)
        return stats_ary


    def send_thankyou_email(self, in_charity_name, in_donated_amount):
        print(f"Thank You Email:")

        dict_data_line = {"donor_name": self.name, "donation_amount": float(in_donated_amount)}

        msg = ""
        msg += f"To: {self.name}@abc.def:\n"

        msg += f"From: {in_charity_name}.org:\n"
        msg += f"Subject:  Thank You:\n"
        msg += f"Body: Dear {self.name} Thank You for your generous donation of ${in_donated_amount}:\n".format(**dict_data_line)
        msg += ""

        print(msg)
        return msg


    def __str__(self):
        return str(f"name:{self.name}, donations:{self.lst_donations}")


class DonorCollection():
    def __init__(self, donors=None):
        if donors is None:
            donors = {}
        self.dict_donors = donors


    def add_donor(self, in_donor):
        self.dict_donors[in_donor.name] = in_donor


    @property
    def get_donors(self):
        return self.dict_donors


    def add_donation(self, in_donor_name, in_donation_amount):
        donor_names_lst = self.dict_donors.keys()
        if in_donor_name in donor_names_lst:
            # existing donor donation
            donor = self.dict_donors[in_donor_name]
            donor.add_to_donations(in_donation_amount)
        else:
            # new donor donation
            donor = Donor(in_donor_name, [in_donation_amount])
            self.add_donor(donor)
        return donor

    def write_letters(self):
        all_thankyou_letters = ""
        for key, donor in self.get_donors.items():
            donations_total = donor.get_tot_donations
            filename = donor.name + ".txt"
            with open(filename, "w") as f:
                dict_data_line = {"donor_name": donor.name, "donation_amount": float(donations_total)}
                thank_you_letter = ""
                thank_you_letter += f"Dear {donor.name} Thank You for your generous donations " \
                                    f"totaling ${donations_total}:\n".format(**dict_data_line)
                all_thankyou_letters += thank_you_letter
                f.write(thank_you_letter)
        return all_thankyou_letters


    def display_donors(self):
        dict_all_donors = self.get_donors
        hdr_listed_donors = f"List of Donors:"
        listed_donors = hdr_listed_donors + "\n" + str((f" ", *dict_all_donors.keys()))
        print(listed_donors)
        return listed_donors


    def create_report(self):
        print(f"Donor Report:")

        # sort donors report by total donation
        db2 = []
        for name, donor in self.get_donors.items():
            donor_stats = donor.get_donor_stats()
            tup = (donor.name,)
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


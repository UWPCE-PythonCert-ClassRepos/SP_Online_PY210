

thank_you_tmp = ("\n Subject: Thank You !!!\n"
                 "\n Dear {0:},\n"
                 "\n Thank you for your latest donation of ${1:,.2f}.\n"
                 " We are so glad you have made {2:} donation(s)"
                 " totaling ${3:,.2f}.\n"
                 " Your continued support will help our"
                 " foundation achive our goals.\n\n"
                 " Regards,\n       Foundation Leadership Team\n"
                 )

report_tmp = " {0:<25} ${1:>11.2f}  {2:>10d}  ${3:>12.2f}"

class Donor():

    def __init__(self, name, donation=None):
        if isinstance(name, str):
            self.name = name.upper()
        else:
            raise TypeError("Donor class initialization requires a 'str' "
                            "object as first input argument")
        if donation and float(donation) >= 0:
            self.donations = (float(donation), ) if donation else ()

    def add_donation(self, donation):
        if donation and float(donation) >= 0:
        self.donations = self.donations + (float(donation),)

    @property
    def avg_donation(self):
        return sum(self.donations)/len(self.donations)

    @property
    def total_donation(self):
        return sum(self.donations)


class DonorCollection():

    def __init__(self, donor=None):
        if not donor or isinstance(donor, Donor):
            self.donors = [donor] if donor else []
        else:
            raise TypeError("DonorCollection class requires "
                            "'Donor' object as input")

    def add_donor(self, donor):
        if self.check_name(donor) == -1:
            self.donors.append(donor)

    @property
    def report(self):
        """Generate report summary of donations by donor."""
        total_donation = []
        for donor in self.donors:
            total_donation.append([donor.total_donation, donor])
        total_donation.sort(reverse=True)
        report_out = []
        for _, donor in total_donation:
            report_out.append(report_tmp.format(donor.name,
                                                donor.total_donation,
                                                len(donor.donations),
                                                donor.avg_donation))
        return report_out

    @property
    def donor_list(self):
        """Create a sorted list of donor names by last name."""
        list_of_donors = []
        sorted_list = []
        for donor in self.donors:
            sorted_list.append([donor.name[-1], donor.name])
        for _, donor in sorted_list:
            list_of_donors.append(donor)
        return list_of_donors

    def check_name(self, name):
        result = -1
        for i, donor in enumerate(self.donors):
            if name.upper() == donor.name:
                result = i
                break
        return result

    def thank_you(self, name, tmp=thank_you_tmp):
        """Return Thank You message text."""
        for donor in self.donors:
            if name.upper() == donor.name:
                return tmp.format(donor.name,
                                  donor.donations[-1],
                                  len(donor.donations),
                                  donor.total_donation)

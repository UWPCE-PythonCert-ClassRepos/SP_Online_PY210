#!/usr/bin/env python3

class Donor():

    def __init__(self, name, donations):
        self.name = name
        self.donations = donations

    def new_donation(self, donation):
        self.donations.append(donation)

    def number_of_donations(self):
        return len(self.donations)

    def avg_donation(self):
        return sum(self.donations)/len(self.donations)

    def sum_donations(self):
        return sum(self.donations)


def second_sort(elem):
    return elem[1]


class DonorCollection():

    def __init__(self, *args):
        self.donors = {d.name: d for d in args}

    def new_donation(self, name, donation):
        if self.donors.get(name):
            self.donors[name].new_donation(donation)
        else:
            self.donors[name] = Donor(name, donation)
        print("\nDear {},\nThank you for your generous donation of ${:.2f}!\n".format(name, donation))

    def get_report(self):
        report = []
        for donor_obj in self.donors.values():
            new_entry = (donor_obj.name, donor_obj.sum_donations(), donor_obj.number_of_donations(), donor_obj.avg_donation())
            report.append(new_entry)
        report.sort(key=second_sort, reverse=True)
        return report

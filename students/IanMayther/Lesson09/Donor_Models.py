#!/usr/bin/env python3

"""
Donor Class and Donation Class
"""

class Donor(object):
    """
    Control all data related to a specific donor
    """
    #donations = []

    def __init__(self, name=None):
        if name is None:
            raise AttributeError("Must supply Donor Name")
        elif isinstance(name, str):
            self.name = name
            self.donations = []
        else:
            raise TypeError("Input must be str")

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return "{}".format(self.name)

    def append(self,new_content):
        if isinstance(new_content, (float, int)):
            self.donations.append(float(new_content))
        elif isinstance(new_content, list):
            for i in range(len(new_content)):
                self.donations.append(new_content[i])
        return self.donations

    def email(self):
        body = f"""Greetings {self.name}\n
    \n
    Thank you so much for your generous contribution to our charity.\n
    It is donors like you who make our work of building schools for ants' possible.\n
    With your gift of ${sum(self.donations)}, means (10) or (20) more schools can be built to help the ants learn to read.\n
    \n
    Sincerely,\n
    Derek Zoolander\n
    Founder and C.E.O. of Derek Zoolander Charity for Ants Who Can't Read Good (DZCAWCRG)\n"""
        return body

    def thank_you(self):
        body = "Thanks {} for your ${:.2f} in donations.".format(self.name, sum(self.donations))
        return body

    #Propreties of donors for calculations




class Donor_Collect(object):
    """
    Processes all the donors information doesn't work with donor functions
    """

    #donors = []

    def __init__(self):
        '''
        TO BE REMOVED LATER
        MS = Donor("Morgan Stanley")
        CV = Donor("Cornelius Vanderbilt")
        JDR = Donor("John D. Rockefeller")
        SG = Donor("Stephen Girard")
        AC = Donor("Andrew Carnegie")
        '''
        self.donors = []

    def __str__(self):
        return "Collection of Donors: {}".format(str(self.donors))

    def __repr__(self):
        return "{}".format(repr(self.donors))

    def append(self,new_content):
        if isinstance(new_content, Donor):
            self.donors.append(new_content)
        else:
            raise AttributeError("Only Class Donors can be append to .Donors list")
        return self.donors

    def calc_report(self):
        new_dict = {}
        for donor in self.donors:
            new_dict[repr(donor)] = []
            new_dict[repr(donor)].append(sum(donor.donations))
            new_dict[repr(donor)].append(len(donor.donations))
            new_dict[repr(donor)].append(sum(donor.donations)/len(donor.donations))


        temp_dict = {k: [sum(v), len(v), sum(v)/len(v)] for k, v in sorted(new_dict.items())}
        calc_dict = sorted(temp_dict.items(), key=lambda t: t[1], reverse=True)
        return calc_dict

    def print_report(self):
        #Header
        print("\n")
        print("{0:<25s}|{1:^15s}|{2:^15s}|{3:>12s}".format("Donor Name", "Total Given", "# of Gifts","Avg. Gift"))
        print("-" * 72)

        for i in self.calc_report():
            print("{0:<25s}${1:>14.2f}{2:>17d}  ${3:>11.2f}".format(i[0], i[1][0], i[1][1], i[1][2], end =''))
        print("\n")

        return
    
    def print_don_list(self):
        i = 1
        for item in self.donors:
            print(f"[{i}] - {item}")
            i += 1
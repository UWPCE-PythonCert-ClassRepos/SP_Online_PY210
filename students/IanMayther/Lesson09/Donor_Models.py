#!/usr/bin/env python3

"""
Donor Class and Donation Class
"""

import pathlib
import os
import math
import re

class Donor(object):
    """
    Control all data related to a specific donor
    """

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

#create property for donor initials

    def append(self,new_content):
        '''Appends Donor donations'''
        if isinstance(new_content, (float, int)):
            self.donations.append(float(new_content))
        elif isinstance(new_content, list):
            for i in range(len(new_content)):
                self.donations.append(new_content[i])
        return self.donations

    def email(self):
        '''Creates text for thank you email'''
        body = f"""Greetings {self.name}\n
        \n
        Thank you so much for your generous contribution to our charity.\n
        It is donors like you who make our work of building schools for ants' possible.\n
        With your gift of ${math.fsum(self.donations)}, means (10) or (20) more schools can be built to help the ants learn to read.\n
        \n
        Sincerely,\n
        Derek Zoolander\n
        Founder and C.E.O. of Derek Zoolander Charity for Ants Who Can't Read Good (DZCAWCRG)\n"""
        return body

    def thank_you(self):
        '''Creates Thank you for individual donors'''
        body = "Thanks {} for your ${:.2f} in donations.".format(self.name, sum(self.donations))
        return body


class Donor_Collect(object):
    """
    Processes all the donors information doesn't work with donor functions
    """

    def __init__(self):
        self.donors = []

    def __str__(self):
        return "Collection of Donors: {}".format(str(self.donors))

    def __repr__(self):
        return "{}".format(repr(self.donors))

    def append(self,new_content):
        '''Append Donors to collection'''
        if isinstance(new_content, Donor):
            self.donors.append(new_content)
        else:
            raise AttributeError("Only Class Donors can be append to .Donors list")
        return self.donors

    def calc_report(self):
        ''''Creates table values for processing'''
        new_dict = {}
        for donor in self.donors:
            new_dict[repr(donor)] = []
            new_dict[repr(donor)].append(sum(donor.donations))
            new_dict[repr(donor)].append(len(donor.donations))
            new_dict[repr(donor)].append(sum(donor.donations)/len(donor.donations))

        return new_dict

    def print_report(self):
        '''Prints Donor data for reports'''
        #Header
        print("\n")
        print("{0:<25s}|{1:^15s}|{2:^15s}|{3:>12s}".format("Donor Name", "Total Given", "# of Gifts","Avg. Gift"))
        print("-" * 72)

        temp_dict = sorted(self.calc_report().items(), key=lambda t: t[1], reverse=True)
        for i in temp_dict:
            print("{0:<25s}${1:>14.2f}{2:>17d}  ${3:>11.2f}".format(i[0], i[1][0], i[1][1], i[1][2], end =''))
        print("\n")

        return temp_dict
    
    def print_don_list(self):
        '''Creates list for selection from existing donors'''
        i = 1
        for item in self.donors:
            print(f"[{i}] - {item}")
            i += 1

    def send_letter(self):
        '''Outputs Email for all donors'''
        path = pathlib.Path.cwd() / 'Lesson09'
        for i in self.donors:
            file_name = repr(i) + '_Thank you Letter.txt'
            with open(os.path.join(path, file_name), 'w') as l:
                l.write(i.email())
        print(f"Sending Letters to disk: {path}\n")
        pass

    def donor_validation(self, test_name):
        '''
        Validate if donor exists
        Return True if donor initials matches existing
        '''
        don_name = ''
        valid = False
        temp_list = re.findall('[A-Z][^A-Z]*', str(test_name))
        for word in temp_list:
            don_name += word[0]

        for donor in self.donors:
            if don_name == str(donor.name):
                valid = True
                break
            else:
                valid = False

        return valid
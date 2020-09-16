#/usr/bin/env python3
import sys
from donor_models import Donor, DonorCollection

# Your user interaction code will interact wtih DonorCollection class instance like below:
donations = DonorCollection(Donor("natasha", 100, '02-04-2015'))
donations.add_donation("bob", 40, '05-08-1994')
donations.add_donation("bob", 50, '06-08-2010')


# name = input("enter name>")
# value = input("enter value>")
# date = input("enter date>")

# donations.add_donation(name, value, date)
#donations.get_report()

#donations.send_thank_you("bob")
donations.send_letters()

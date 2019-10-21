#!/usr/bin/env python3
from donor_models import  Donor, DonorCollection

def donor_init_test():
    d = Donor("frank", 100)
    assert d.name == 'frank'
    assert d.donations == [100]

def add_donation_test():
    d = Donor("frank", 100)
    d.add_donation(1000)
    assert d.donations == [100, 1000]
    d.add_donation(10000)
    assert d.donations == [100, 1000, 10000]
    
def donation_calc_test():
    d = Donor("frank", 100)
    d.add_donation(1000)
    d.add_donation(10000)
    assert d.avg_donations() == 3700
    assert d.count_donation() == 3
    assert d.total_donations() == 11100
    assert d.recent_donation() == 10000
    
def donation_email_test():
    d = Donor("frank", 100)
    d.add_donation(1000)
    d.add_donation(10000)
    assert d.send_thank_you() =='Dear frank,\n\nThanks you for your generous donation of 10000.00.\n\nSincerly,\nThe Weyland-Yutani Corporation'

def list_donors_test():
    d = DonorCollection()
    assert d.list_donors() == 'William Gates, III\nJeff Bezos\nPaul Allen\nMark Zuckerberg\n'
    
def report_test():
    d = DonorCollection()
    test =  d.donor_report()
    assert test == '\nDonor Name                  | Total Given | Num Gifts | Average Gift  \n--------------------------------------------------------------------\nWilliam Gates, III           $  653784.49           2  $   326892.24\nMark Zuckerberg              $   16396.10           3  $     5465.37\nJeff Bezos                   $     877.33           1  $      877.33\nPaul Allen                   $     708.42           3  $      236.14\n'




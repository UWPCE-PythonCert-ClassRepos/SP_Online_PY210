#!/usr/bin/env python

"""
Jack Anderson
03/10/2020
UW PY210
Lesson 09
Unit tests for Donor and DonorClass classes
"""

import pytest
from datetime import date
from cli_main import *
import os

##############################
# Unit Tests for  Donor Class
##############################

def test_donor_init():
    # Test donor_init
    c = Donor("david")
    print(c.name, c.donations)
    assert c.name == "David"
    assert c.donations == []

    c2 = Donor("jACk aNderSOn", [5])
    print(c2.name, c2.donations)
    assert c2.name == "Jack Anderson"
    assert c2.donations == [5]


    c3 = Donor("David", [1,2,3])
    print(c3.donations)
    assert c3.donations == [1,2,3]
    # assert False
    # assert False


def test_add_donation():
    # Test adding donation returns all donations for donor
    c = Donor("bob")
    c.add_donation(5)
    print(c.donations)
    assert c.donations == [5]

    c1 = Donor("David", (1, 2, 3))
    c1.add_donation(10)
    print(c1.donations)
    assert 10 in c1.donations
    assert c1.donations == [1, 2, 3, 10]

    # assert False
    # assert False

def test_sum_donations():
    # Test sum donations is returned
    c = Donor('Jim', (2, 7, 11))
    print(c.sum_donations)
    assert c.sum_donations == 20
    assert c.sum_donations == sum(c.donations)

    c1 = Donor("bob", (3.33, 2.25, 2.75))
    print(c1.sum_donations)
    assert c1.sum_donations == sum(c1.donations)

    # assert False
    # assert False

def test_num_donations():
    # Test number of donations is returned
    c = Donor("pete", [2])
    print(c.num_donations)
    assert c.num_donations == len(c.donations)

    c.add_donation(10)
    print(c.num_donations)
    assert c.num_donations == len(c.donations)

    c1 = Donor('Jim', (2, 7, 11))
    print(c1.num_donations)
    assert c1.num_donations == len(c1.donations)

    c2 = Donor('sarah')
    print(c2.num_donations)
    assert c2.num_donations == len(c2.donations)

    # assert False
    # assert False

def test_avg_donation():
    # Test ave donation is returned
    c = Donor('Jim', (4, 5, 6))
    print(c.avg_donation)
    assert c.avg_donation == 5
    assert c.avg_donation == c.sum_donations / c.num_donations

    c1 = Donor("jack", [2.50, 3.50, 4.25, 1.25])
    print(c1.avg_donation)
    assert c1.avg_donation == c1.sum_donations / c1.num_donations

    # assert False
    # assert False

def test_report_template():
    #Test report template is returned
    c = Donor('Jim', (4, 5, 6))
    print(c.report_template())
    template = '{name:<21}\t$ {total:>{width}.2f}\t{count:^{width}}\t$ {avg:>{width}.2f}'.format(
        name='Jim', total=15, count=3, avg=5.00, width=10)
    assert c.report_template() == template

    # assert False
    # assert False


def test_thanks_template():
    #Test thanks template is returned when donor and donation is provided
    c = Donor('mary', [100])
    print(c.donations)
    print(c.thanks_template())

    assert 'Mary' in c.thanks_template()
    assert '$100.00' in c.thanks_template()

    # assert False
    # assert False

######################################
# Unit Tests for  DonorCollection Class
#######################################

def test_donor_collection_init():
    # Test the DonorCollection init
    dc = DonorCollection()
    print(dc.donors_dict['Jack'])
    assert 'Jack' in dc.donors_dict

    print(dc.donors_dict['Ricky Boys'])
    assert [1345.50, 1123.00] == dc.donors_dict['Ricky Boys']

    assert 'Lacey Coffin Greene' in dc.donors_dict
    assert 1500 in dc.donors_dict['Lacey Coffin Greene']

    # assert False
    # assert False

def test_add_donor():
    #Test new donor is included in return of donors dict. Test adding donation to donor is returned in donors dict
    dc = DonorCollection()
    print(dc.donors_dict)
    dc.add_donor('mark', [100.25])
    print(dc.donors_dict)
    assert 'mark' in dc.donors_dict
    assert dc.donors_dict['mark'] == [100.25]

    dc.add_donor("Jack", [100])
    print(dc.donors_dict['Jack'])
    assert dc.donors_dict['Jack'] == [1044, 2232, 123.49, 100]

    # assert False
    # assert False

def test_list_donors():
    # Test a list of donors are returned
    dc = DonorCollection()
    print(dc.list_donors())
    assert 'Bubbles Trailer' and 'Jack' in dc.list_donors()

    # assert False
    # assert False

def test_report_header():
    # Test the format of the report header is correct
    dc = DonorCollection()
    print(dc.report_header())

    template = header = '{name:<21}\t| {total:^{width}}\t| {count:^{width}}\t| {avg:>{width}}'\
        .format(name='Donor Name', total='Total Given', count='Num Gifts', avg='Average Gift', width=10)
    line = "=" * 70
    assert dc.report_header() == '\n' + template + '\n' + line

    # assert False
    # assert False

def test_sort_donors():
    # Test donors are returned, sorted by most > least donated
    dc = DonorCollection()
    print(dc.sorted_dict)

    assert dc.sorted_dict[0] > dc.sorted_dict[1]

    # assert False
    # assert False


def test_create_report():
    # Test user can create report
    dc = DonorCollection()
    print(dc.report_header())
    for i in dc.create_report():
        print(i)
    x = dc.create_report()

    assert x[0] > x[1]

    # assert False
    # assert False


def test_send_email_all():
    # Create email for all donors and tests the email exists
    dir = 'outgoing_emails_{date}'.format(date=date.today()).replace("-", "_")
    dc = DonorCollection()
    print(dc.send_email_all())

    jack = "Jack_{date}.txt".format(date=date.today()).replace("-", "_")
    ricky = "Ricky_Boys_{date}.txt".format(date=date.today()).replace("-", "_")

    email_list = list(os.listdir(f"{dir}"))
    print(email_list)

    assert jack in email_list
    assert ricky in email_list


def create_directory_for_test(self):
    # Tests the create directory function
    dir = 'mail_testing'
    c = DonorCollection()
    print(c.create_directory(dir))
    dir_list = list(os.listdir())

    assert dir in dir_list


def test_create_email():
    # Test for Donor() class. Test user can create a single email
    c = Donor('harry', [100])
    dir = 'outgoing_emails_{date}'.format(date=date.today()).replace("-", "_")
    print(c.create_email(dir))
    file = "{dir}/Harry_{date}.txt".format(dir=dir, date=date.today()).replace("-", "_")
    with open(file, 'r') as f:
        data = f.read()
    assert 'Harry' in data
    assert '100.00' in data

    # assert False
    # assert False


def test_remove_donor():
    # test function in donorcollection class to remove a donor from the donor dict
    dc = DonorCollection()
    dc.remove_donor('mark')

    assert "mark" not in dc.donors_dict

    dc.remove_donor('Jack')
    assert 'Jack' not in dc.donors_dict

    dc.add_donor("Jack",[1044, 2232, 123.49] )
    assert 'Jack' in dc.donors_dict

    # assert False
    # assert False



####################################################################################
#             Clean up test data and reset the donors dict                         #
####################################################################################

def test_clean_up_test_data():
    # Function to clean up test data and reset to the default donors dict
    dir = 'outgoing_emails_{date}'.format(date=date.today()).replace("-", "_")
    email_list = list(os.listdir(f"{dir}"))

    print(email_list)

    try:
        for i in email_list:
            print(i)
            os.remove("{d}/{f}".format(d=dir, f=i))
    except FileNotFoundError:
        print("Unable to locate file")
        raise FileNotFoundError

    os.rmdir(dir)
    assert dir not in os.listdir()

    default = [['Bubbles Trailer', [1500.24, 2523.33, 3012.12]],
               ['Julien Park', [2520.99, 1623, 123.23]],
               ['Ricky Boys', [1345.50, 1123.00]],
               ['Jack', [1044, 2232, 123.49]],
               ['Lacey Coffin Greene', [1500, 1625, 1305, 3400.87]]]
    saved_data = {donor[0]: donor[1] for donor in default}

    with open('donors.pckl', 'wb') as f:
        pickle.dump(saved_data, f)
        f.close()

    # assert False
    # assert False

#!/usr/bin/env python

"""
UW
Python210
Jack Anderson
02/24/20

Test Suite for the mailroom program
"""
import unittest
from datetime import date
from mailroom_pt4 import *
import os

now = date.today()

#SEND THANKS TEST CASES

def test_list_names():
    assert list_names() == ['Bubbles Trailer', 'Julien Park', 'Ricky Boys', 'Jack Anderson', 'Lacey Coffin Greene']

def test_add_new_donor_and_donation():
    add_items('Jerry Ross', 750.99)
    assert donors_dict['Jerry Ross'] == [750.99]

def test_add_returning_donor_donations():
    add_items('Jack Anderson', 500)
    assert donors_dict['Jack Anderson'] == [500, 1044, 2232, 4123.56]

def test_create_email_template():
    assert thanks_template('Bob', 100.00) == 'Hello Bob,\n\nThank you for your recent gift of $100.00! \nWe will use your gift to help with costs for our upcoming play! \nThank you for giving!\n\nBest Regards, \nThe Blanchford Community Center!'


# CREATE REPORT TEST CASES
def test_donor_details():
    assert donor_details('Sam Smith', ([5, 10, 50, 20])) == ('Sam Smith', 85, 4, 21.25)

def test_report_header():
    expected = '{name:<21}\t| {total:^{width}}\t| {count:^{width}}\t| {avg:>{width}}' \
        .format(name='Donor Name', total='Total Given', count='Num Gifts', avg='Average Gift', width=10)
    assert report_header() == print(expected)

def test_report_template():
    name, total, count, avg = ('Sam Smith', 85, 4, 21.25)
    assert report_template(name, total, count, avg) == print(f'{name:<21}\t$ {total:>{10}.2f}\t{count:^{10}}\t$ {avg:>{10}.2f}')

#Create Email File
def test_create_dir_if_not_found():
    assert create_directory(test=1) == 'test_directory' in list(os.listdir())


def test_create_file_name_printout():
    name = 'testUser'
    template = f'testing_email_filename'
    expected = f"Email file '{date.today()}_{name}.txt' has been created for {name} in the outgoing_mail directory"
    assert create_file(name, template) == print(expected)

def test_create_file_text():
    template = 'testing_email_filename'
    filename = f'testUser_{date.today()}.txt'
    f = open(f'outgoing_emails/{filename}')
    actual_text = f.read()
    assert actual_text == template


def test_clean_up_test_data():
    x = date.today()
    os.remove(f'outgoing_emails/testUser_{x}.txt')
    os.rmdir("test_directory")
    email_list = list(os.listdir("outgoing_emails"))
    assert f"testUser_{date.today()}.txt" not in email_list and "test_directory" not in os.listdir()




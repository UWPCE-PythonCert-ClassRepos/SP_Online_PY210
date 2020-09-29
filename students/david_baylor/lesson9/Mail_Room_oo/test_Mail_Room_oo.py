#!/usr/bin/env python3

"""
test_Mail_Room.py
By David Baylor on 12/29/19
uses python 3

designed for Mail Room part 4 and latter.

unit tests Mail_room_oo.

"""

import pytest
import os

from Mail_Room_oo import Donor,DonorCollection

class TestMailRoom:
    # def setup_method(self):

    def test_donor(self):
        Fred = Donor("Fred", 100)
        assert Fred.total_donated == 100
        assert Fred.donations == 1
        assert Fred.name == "Fred"

    def test_add_donor(self):
        donors = DonorCollection()
        donors.add_donation("Jack", 100)
        assert "Jack" in donors.donor_dict

    def test_get_donor(self):
        donors = DonorCollection()
        donors.add_donation("Jack", 100)
        donor = donors.get_donor("Jack")
        assert donor.name == "Jack"
        assert donor.total_donated == 100
        assert donor.donations == 1

    def test_sort_lst(self):
        donors = DonorCollection()
        donors.add_donation("Jeff Bezos", 200, 2)
        donors.add_donation("Elon Musk", 600, 3)
        donors.add_donation("Bill Gates", 50, 1)
        donors.add_donation("Mark Zuckerberg", 75, 5)
        sorted_lst = donors.sort_lst()
        print(list(donors.donor_dict.values()))
        print(sorted_lst)
        assert sorted_lst[0].name == "Elon Musk"

    def test_lt(self):
        d1 = Donor("Elon Musk", 600, 3)
        d2 = Donor("Jeff Bezos", 200, 2)
        assert (d2 < d1) == True

    def test_average_donation(self):
        d1 = Donor("Elon Musk", 600, 3)
        assert d1.average_donation == 200

    def test_donor_alredy_in_donor_dict(self):
        donors = DonorCollection()
        donors.add_donation("Jeff Bezos", 200, 2)
        donors.add_donation("Jeff Bezos", 200)
        assert donors.donor_dict["Jeff Bezos"].total_donated == 400
        assert donors.donor_dict["Jeff Bezos"].donations == 3

    def test_check_donor_in_db(self):
        donors = DonorCollection()
        donors.add_donation("Jeff Bezos", 200, 2)
        assert donors.check_donor_in_db("Jeff Bezos") == True

    def test_check_donor_not_in_db(self):
        donors = DonorCollection()
        donors.add_donation("Jeff Bezos", 200, 2)
        assert donors.check_donor_in_db("Elon Musk") == False
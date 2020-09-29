#!/usr/bin/env python3

"""
test_Mail_Room.py
By David Baylor on 12/29/19
uses python 3

designed for Mail Room part 4 and latter.

unit tests Mail_room

"""

import pytest
import os

import Mail_Room_part4


class TestMailRoom:
    def setup_method(self):
        self.data = {"Bill" : [100, 2], 
            "John" : [75, 3], 
            "Joe"  : [150, 3], 
            "Fred" : [3.5, 1]}

    def test_list(self):
        assert Mail_Room_part4.make_list(self.data) == "Bill\nJohn\nJoe\nFred\n"

    def test_update_data_name_in_data(self):
        Mail_Room_part4.update_data("Bill", 100, self.data)
        assert self.data == {"Bill" : [200, 3], "John" : [75, 3], "Joe"  : [150, 3], "Fred" : [3.5, 1]}

    def test_update_data_name_not_in_data(self):
        Mail_Room_part4.update_data("Jack", 100, self.data)
        assert self.data == {"Bill" : [100, 2], "John" : [75, 3], "Joe"  : [150, 3], "Fred" : [3.5, 1], "Jack" : [100, 1]}
   
    def test_write_email(self):
        assert Mail_Room_part4.wirite_email("jack", 100) == """Dear Jack,\n\nThank you for your generous donnation of $100.\n\n                    -The Team"""

    def test_make_table(self):
        assert Mail_Room_part4.make_table(self.data) == """
Donor Name                | Total Given | Num Gifts | Average Gift
--------------------------|-------------|-----------|-------------
Joe                       |$         150|          3|$        50.0
Bill                      |$         100|          2|$        50.0
John                      |$          75|          3|$        25.0
Fred                      |$         3.5|          1|$         3.5"""

    def test_creat_file(self):
        simp_data = {"Bill" : [100, 2], "John" : [75, 3]}
        Mail_Room_part4.send_all(simp_data)
        assert os.path.isfile("letter_to_Bill.txt") and os.path.isfile("letter_to_John.txt")
        os.remove("letter_to_Bill.txt")
        os.remove("letter_to_John.txt")

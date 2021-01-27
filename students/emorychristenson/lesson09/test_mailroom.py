#!/usr/bin/env python3

import os
import unittest
import pytest
from mailroom import *

# DonorClass tests

class TestDonorClass(unittest.TestCase):

    def setUp(self):
        self.D1 = Donor("John Jingleheimer", [10])
        self.D2 = Donor("Princess Consuela", [20])
        self.D3 = Donor("Calvin Hobbes", [50])

    def test_donor(self):
        assert self.D1.name == "John Jingleheimer"
        # with self.assertRaises(TypeError):
        #         self.D1.name = 5
        # with self.assertRaises(ValueError):
        #         self.D1.name = ""

    def test_donation(self):
        assert self.D1.donations == [10]

    def test_add_donation(self):
        self.D1.add_donation(10)
        assert self.D1.donations == [10, 10]
        with self.assertRaises(ValueError):
            self.D1.add_donation(-5)
        with self.assertRaises(TypeError):
            self.D1.add_donation("Nope")
        with self.assertRaises(AttributeError):
            self.D1.donations = 10

    def test_sum_donations(self):
        self.D1.add_donation(20)
        assert self.D1.sum_donations() == 30

    def test_count_donations(self):
        assert self.D2.donation_count() == 1
        self.D2.add_donation(20)
        assert self.D2.donation_count() == 2

    def test_average_donation(self):
        self.D3.add_donation(10)
        self.D3.add_donation(26)
        self.D3.add_donation(20)
        assert self.D3.average_donation() == 26.5
    

# DonorCollection tests

class TestDonorCollection(unittest.TestCase):

    def setUp(self):
        self.C1 = DonorCollection()
        self.D1 = Donor("John Jingleheimer", [10])
        self.D2 = Donor("Princess Consuela", [20])
        self.D3 = Donor("Calvin Hobbes", [50])

    def test_collection(self):
        assert self.C1.donors == []

    def test_add_donor(self):
        self.C1.add_donor(self.D1)
        assert self.C1.donors[0].name == "John Jingleheimer"
        assert len(self.C1.donors) == 1

    def test_list_donors(self):
        self.C1.add_donor(self.D1)
        self.C1.add_donor(self.D2)
        assert self.C1.list_donors() == ["John Jingleheimer", "Princess Consuela"]

    def test_get_donors(self):
        self.C1.add_donor(self.D1)
        self.C1.add_donor(self.D2)
        assert self.C1.get_donors() == self.C1.donors

    def test_generate_report(self):
        self.C1.add_donor(self.D1)
        self.C1.add_donor(self.D2)
        self.C1.add_donor(self.D3)
        assert self.C1.generate_report() == [["Calvin Hobbes", 50, 1, 50.0],
                                            ["Princess Consuela", 20, 1, 20.0],
                                            ["John Jingleheimer", 10, 1, 10.0]]
    


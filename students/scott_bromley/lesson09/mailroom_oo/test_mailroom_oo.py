#!/usr/bin/env python3

from pytest import mark, raises
from unittest.mock import Mock
from datetime import datetime
from donor_models import Donor, DonorCollection


@mark.Donor
class DonorTests:

    @mark.donor
    @mark.parametrize("test_input, expected", [
        (("Bill Ackerman", [1818.18, 72.00, 54, 363636.36]), ["Bill Ackerman", [1818.18, 72.00, 54.00, 363636.36],
                                                              "Bill", "Ackerman", 4, 365580.54, 91395.13]),
        (("Seth Klarman", (6666666.66, 5454.54)), ["Seth Klarman", [6666666.66, 5454.54], "Seth", "Klarman", 2,
                                                   6672121.20, 3336060.60]),
        (("Wiley Coyote", [0.01]), ["Wiley Coyote", [0.01], "Wiley", "Coyote", 1, 0.01, 0.01]),
        (("Yosemite Sam", 7200.72), ["Yosemite Sam", [7200.72], "Yosemite", "Sam", 1, 7200.72, 7200.72])
    ])
    def test_donor_creation(self, test_input, expected):
        donor = Donor(test_input[0], test_input[1])
        assert donor.donor_name == expected[0]
        assert donor.donations == expected[1]
        assert donor.first_name == expected[2]
        assert donor.last_name == expected[3]
        assert donor.num_donations == expected[4]
        assert donor.total_donations == expected[5]
        assert donor.avg_donation == expected[6]

    @mark.donor
    @mark.parametrize("test_input, expected", [
        (("    ", [18.18]), ValueError),
        (("l", [18.18]), AttributeError),
        (("'", [18.18]), AttributeError),
        ((666, [18.18]), TypeError),
        (("Carl ", [18.18]), AttributeError),
        ((" Brutananadilewski", [18.18]), AttributeError)
    ])
    def test_donor_creation_error(self, test_input, expected):
        with raises(expected):
            Donor(test_input[0], test_input[1])

    @mark.donor
    @mark.parametrize("test_input, expected", [
        (("Gabe Kotter", {"donation_1": [1818.18]}), TypeError),
        (("Gabe Kotter", "666.66"), TypeError)
    ])
    def test_donor_donations_error(self, test_input, expected):
        with raises(expected):
            Donor(test_input[0], test_input[1])

    @mark.donor
    @mark.parametrize("test_input, expected", [
        ("Carl Brutananadilewski", ["Carl Brutananadilewski", []])
    ])
    def test_from_donor_name(self, test_input, expected):
        donor = Donor.from_donor_name(test_input)
        assert donor.donor_name == expected[0]
        assert donor.donations == expected[1]

    @mark.donor
    @mark.parametrize("test_input, expected", [
        (("Carl Brutananadilewski", [72.72], 18.18), [[72.72, 18.18], 2, 90.90, 45.45]),
        (("Carl Brutananadilewski", [], 1818.18), [[1818.18], 1, 1818.18, 1818.18])
    ])
    def test_donor_add_donation(self, test_input, expected):
        donor = Donor(test_input[0], test_input[1])
        donor.add_donation(test_input[2])
        assert donor.donations == expected[0]
        assert donor.num_donations == expected[1]
        assert donor.total_donations == expected[2]
        assert donor.avg_donation == expected[3]

    @mark.donor
    @mark.parametrize("test_input, expected", [
        (("Carl Brutananadilewski", [18.18], []), TypeError),
        (("Carl Brutananadilewski", [18.18], -18.18), ValueError),
        (("Carl Brutananadilewski", [18.18], "Eighteen dollars eighteen cents"), TypeError),
        (("Carl Brutananadilewski", [18.18], 0), ValueError),
        (("Carl Brutananadilewski", [18.18], 0.00), ValueError)
    ])
    def test_donor_add_donation_error(self, test_input, expected):
        donor = Donor(test_input[0], test_input[1])
        with raises(expected):
            donor.add_donation(test_input[2])

    @mark.donor
    @mark.parametrize("test_input, expected", [
        (("Carl Brutananadilewski", []), ValueError),
        (("Carl Brutananadilewski", None), ValueError),
    ])
    def test_avg_donation_err(self, test_input, expected):
        donor = Donor(test_input[0], test_input[1])
        with raises(expected):
            donor.avg_donation

    @mark.letter
    @mark.parametrize("test_input, expected", [
        (("Carl Brutananadilewski", [18.18, 1818.18, 72.72, 54.54]), ["Carl Brutananadilewski",
                                                                      f"{datetime.today().strftime('%Y-%d-%m')}", "54.54",
                                                                      "1963.62"])
    ])
    def test_thank_you(self, test_input, expected):
        donor = Donor(test_input[0], test_input[1])
        assert expected[0] in donor.thank_you()
        assert expected[1] in donor.thank_you()
        assert expected[2] in donor.thank_you()
        assert expected[3] in donor.thank_you()

    @mark.letter
    @mark.parametrize("test_input, expected", [
        (("Carl Brutananadilewski", []), ValueError),
        (("Carl Brutananadilewski", None), ValueError)
    ])
    def test_thank_you_error(self, test_input, expected):
        donor = Donor(test_input[0], test_input[1])
        with raises(expected):
            donor.thank_you()

    @mark.report
    @mark.parametrize("test_input, expected", [
        (("Carl Brutananadilewski", [18.18, 1818.18, 72.72, 54.54, 1000.00]), ["Carl Brutananadilewski", "2,963.62", "5",
                                                                               "592.72"]),
        (("Carl Brutananadilewski", [727272.72]), ["Carl Brutananadilewski", "727,272.72", "1", "727,272.72"])
    ])
    def test_report_row(self, test_input, expected):
        donor = Donor(test_input[0], test_input[1])
        assert expected[0] in donor.report_row()
        assert expected[1] in donor.report_row()
        assert expected[2] in donor.report_row()
        assert expected[3] in donor.report_row()

    @mark.report
    @mark.parametrize("test_input, expected", [
        (("Carl Brutananadilewski", []), ValueError),
        (("Carl Brutananadilewski", None), ValueError)
    ])
    def test_report_row_error(self, test_input, expected):
        donor = Donor(test_input[0], test_input[1])
        with raises(expected):
            donor.thank_you()

    @mark.donor
    @mark.parametrize("test_input", [
        ("Carl Brutananadilewski", [18.18, 1818.18, 72.72, 54.54]),
        ("Carl Brutananadilewski", [])
    ])
    def test_donor_str(self, test_input):
        donor = Donor(test_input[0], test_input[1])
        assert donor.__str__() == f"Donor: {test_input[0]}, Donations: {test_input[1]}"

    @mark.donor
    @mark.parametrize("test_input", [
        ("Carl Brutananadilewski", [18.18, 1818.18, 72.72, 54.54]),
        ("Carl Brutananadilewski", [])
    ])
    def test_donor_repr(self, test_input):
        donor = Donor(test_input[0], test_input[1])
        assert donor.__repr__() == f"Donor('{test_input[0]}', {test_input[1]})"


@mark.DonorCollection
class DonorCollectionTests:
    """
    DonorCollection unit tests
    """
    @mark.collection
    def test_donor_collection_creation(self, donors):
        donor_names = ["Bill Ackerman", "Mark Cuban", "Mark Zuckerberg", "Michael Bloomberg", "Seth Klarman",
                       "David Einhorn"]
        donor_collection = DonorCollection(donors)
        for donor in donor_names:
            assert donor in donor_collection.donors

    @mark.collection
    def test_donor_collection_creation_list(self, donors):
        donor_names = ["Bill Ackerman", "Mark Cuban", "Mark Zuckerberg", "Michael Bloomberg", "Seth Klarman",
                       "David Einhorn"]
        donor_collection = DonorCollection(list(donors))
        for donor in donor_names:
            assert donor in donor_collection.donors

    @mark.collection
    @mark.parametrize("test_input, expected", [
        ({Donor("Carl Brutananadilewski", [72000.00]), Mock("Larry Miller", [1818.18])}, TypeError),
        (Donor("Carl Brutananadilewski", [18.18]), TypeError),
        ((Donor("Carl Brutananadilewski", [18.18])), TypeError),
        ({}, ValueError),
        ([], ValueError),
        (None, ValueError),
        ("", ValueError)
    ])
    def test_donor_collection_error(self, test_input, expected):
        with raises(expected):
            DonorCollection(test_input)

    @mark.collection
    @mark.parametrize("test_input, expected", [
        (Donor("Carl Brutananadilewski", [1818.18]), "Carl Brutananadilewski"),
        (Donor("Jerry Seinfeld"), "Jerry Seinfeld"),
        ({Donor("Larry David", [7272.72])}, "Larry David")
    ])
    def test_donor_collection_append(self, test_input, expected, donors):
        donor_collection = DonorCollection(donors)
        donor_collection.append(test_input)
        assert expected in donor_collection.donors

    @mark.collection
    @mark.parametrize("test_input, expected", [
        ([Donor("Sammie Davis Jr"), Donor("Larry Miller"), Donor("Mel Brooks", [1000.00])], ["Sammie Davis Jr",
                                                                                             "Larry Miller",
                                                                                             "Mel Brooks"]),
        ({Donor("Larry David", [7272.72]), Donor("Elaine Benes", [1818.18]), Donor("Cosmo Kramer"),
          Donor("George Costanza", [162.16])}, ["George Costanza", "Larry David", "Elaine Benes", "Cosmo Kramer"])
    ])
    def test_donor_collection_append_multiple(self, test_input, expected, donors):
        donor_collection = DonorCollection(donors)
        donor_collection.append(test_input)
        for donor in expected:
            assert donor in donor_collection.donors

    @mark.collection
    @mark.parametrize("test_input, expected", [
        ("Mel Brooks, 18.18", TypeError),
        ([Donor("Jerry Seinfeld", [90.00]), Mock("Larry David")], TypeError)
    ])
    def test_donor_collection_append_error(self, test_input, expected, donors):
        donor_collection = DonorCollection(donors)
        with raises(expected):
            donor_collection.append(test_input)

    @mark.collection
    def test_donor_collection_report(self, donors):
        donor_collection = DonorCollection(donors)
        print(donor_collection.report())
        assert False

    @mark.collection
    @mark.parametrize("test_input, expected", [
    ])
    def test_donor_collection_report_error(self, test_input, expected):
        pass


    @mark.collection
    @mark.parametrize("test_input, expected", [
        ([Donor("Carl Brutananadilewski", [18.18])], "DonorCollection: {'Carl Brutananadilewski': "
                                                     "Donor('Carl Brutananadilewski', [18.18])}"),
        ([Donor("Carl Brutananadilewski", [])], "DonorCollection: {'Carl Brutananadilewski': "
                                                "Donor('Carl Brutananadilewski', [])}")
    ])
    def test_donor_collection_str(self, test_input, expected):
        donor_collection = DonorCollection(test_input)
        assert donor_collection.__str__() == expected

    @mark.collection
    @mark.parametrize("test_input, expected", [
        ([Donor("Carl Brutananadilewski", [18.18])], "DonorCollection({'Carl Brutananadilewski': "
                                                     "Donor('Carl Brutananadilewski', [18.18])})"),
        ([Donor("Carl Brutananadilewski", [])], "DonorCollection({'Carl Brutananadilewski': "
                                                "Donor('Carl Brutananadilewski', [])})")
    ])
    def test_donor_collection_repr(self, test_input, expected):
        donor_collection = DonorCollection(test_input)
        assert donor_collection.__repr__() == expected

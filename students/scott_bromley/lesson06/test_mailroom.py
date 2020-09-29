#!/usr/bin/env python3

import datetime
import mailroom4 as mailroom
from pathlib import Path as path
from pytest import mark, raises


@mark.unit
class MailroomTests:

    @mark.donor
    def test_list_donors(self, donors):
        donor_names = ['Michael Bloomberg', 'Bill Ackerman', 'David Einhorn', 'Seth Klarman', 'Mark Zuckerberg']
        assert bool(mailroom.list_donors(**donors)) is True
        assert type(mailroom.list_donors(**donors)) is list
        assert all(names in donor_names for names in mailroom.list_donors(**donors))

    @mark.donor
    @mark.parametrize("test_input, expected", [
        (dict(), TypeError),
        ({'':[], '':[]}, TypeError),
        ])
    def test_list_donors_exception(self, test_input, expected):
        with raises(expected) as info:
            mailroom.list_donors(test_input)

    @mark.donor
    @mark.parametrize("test_input, expected", [
        (("Mel Brooks", [666.66]), 6),
        (("Rodney Dangerfield", None), 7),
        (("Gene Wilder", [54.54, 7272.72, 1800.18]), 8),
        (("Gilda Radner", []), 9),
        (("Jerry Lewis", [0.00]), 10)
    ])
    def test_update_donor(self, test_input, expected, donors):
        mailroom.donors = donors
        mailroom.update_donor(test_input)
        assert len(donors.keys()) == expected

    @mark.donor
    @mark.parametrize("test_input, expected", [
        (("", [1818.18]), TypeError),
        (tuple(), IndexError)
        ])
    def test_update_donor_exception(self, test_input, expected):
        with raises(expected):
            mailroom.update_donor(test_input)

    @mark.report
    def test_get_report(self, report):
        assert bool(mailroom.get_report(report)) is True
        assert type(mailroom.get_report(report)) is list
        assert len(mailroom.get_report(report)) == 7
        assert mailroom.get_report(report)[0][1] == 5000000.00
        assert mailroom.get_report(report)[-1] == ['Jerry Lewis', 0.0, 1, 0.0]
        assert mailroom.get_report(report)[4][1] > mailroom.get_report(report)[5][1]

    @mark.report
    @mark.parametrize("test_input, expected", [
        ({}, ValueError),
        ([], ValueError),
        (tuple(), ValueError)
    ])
    def test_get_report_exception(self, test_input, expected):
        with raises(expected):
            mailroom.get_report(test_input)

    @mark.letter
    @mark.parametrize("test_input, expected", [
        (("Golda Meir", 1818.18), "Golda Meir"),
        (("Zev Jabotinsky", 3636.36), "$3636.36"),
        (("Yitzhak Rabin", 54.54), str(datetime.datetime.now().date()))
    ])
    def test_format_thank_you(self, test_input, expected):
        assert expected in mailroom.format_thank_you(test_input)
        assert expected in mailroom.format_thank_you(test_input)
        assert expected in mailroom.format_thank_you(test_input)

    @mark.letter
    @mark.parametrize("test_input, expected", [
        (("", 1818.18), ValueError),
        (("Jerry Lewis", 0.00), ValueError)
    ])
    def test_format_thank_you_exception(self, test_input, expected):
        with raises(expected):
            mailroom.format_thank_you(test_input)

    @mark.letter
    def test_send_thank_you_all_donors(self, thank_yous):
        mailroom.donors = thank_yous
        mailroom.send_thank_you_all_donors()
        today = str(datetime.datetime.now().date()).replace('-', '_')
        assert path.exists(path(f"Albert_Einstein_{today}.txt"))
        assert path.exists(path(f"Max_Born_{today}.txt"))
        assert path.exists(path(f"Fritz_Haber_{today}.txt"))
        assert path.is_file(path(f"Albert_Einstein_{today}.txt"))
        assert path.is_file(path(f"Max_Born_{today}.txt"))
        assert path.is_file(path(f"Fritz_Haber_{today}.txt"))

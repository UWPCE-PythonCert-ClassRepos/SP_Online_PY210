#!/usr/bin/env python3
# =============================================================================
# Python210 | Fall 2020
# -----------------------------------------------------------------------------
# Lesson06
# Mailroom Part 4 (test_mailroom4.py)
# Steve Long 2020-11-06 | v4
#
# Requirements:
# =============
#
#   [1] Modularize mailroom v3 application to optimize the separation between
#       business logic and the user interface (UI).
#   [2] Write unit tests for functions other than those which can only be
#       evaluated thru interaction with the terminal (e.g., other than UI
#       components).
#   [3] Run tests using pytest app.
#
# Assumptions:
# ============
#
#   - Each unit test should cover a specific functionality. Content, object
#     existence, and feedback should be decomposed into separate operations
#     or at least clearly identifiable blocks within a test function. In
#     other words, follow the same process as we used in JUnit.
#
# Implementation:
# ===============
#
#   [1] Written to be run with pytest.
#
#   [2] There are a total of 68 functional tests for mailroom4. Many have
#       multiple test parameters designed to cover multiple use-cases.
#
#   [3] There are 13 functions of the 68 that can only be interactively tested
#       with the terminal; can only be visually/subjectively evaluated. Tests
#       exist for these functions but set to always pass.
#
#   [4] Several helper functions were created. The more complicated,
#       standalone functions were separated into module longsa_utils.
#
#   [5] The primary data structure within mailroom4 was "monkey-patched"
#       to improve testing efficiency and reduce dependency on the module's
#       other functions which are also being tested.
#
#   [6] The mailroom code was already modularized in previous versions.
#       The concept of getters, setters, and separation of UI from business
#       logic had already been introduced.
#
#   [7] Mailroom4 has a few minor code changes from mailroom3.
#
# Dependencies:
# =============
#
#   mailroom4
#   longsa_utils
#
# Script Usage:
# =============
#
#   pytest test_mailroom4.py -vv
#
# Issues:
# =======
#
#   Given sufficient time, I would refactor even more of the existing
#   functions.
#
# History:
# ========
#
# 000/2020-10-06/sal/
#   Created (test_mailroom4.py).
#
# =============================================================================

import mailroom4 as mailroom
import re
import pathlib
import longsa_utils as utils

# == Helper data and functions ===============================================

# Initial donor data shall consist of 3 or more donors. Each donor shall
# -- at a minimum -- contain the donor's name and a sequence of donations
# they have made.
_First_Donors_Tuple = \
    (("Rene Descartes", (21.00, 199.95, 2063.45, 77.00, 1638.00)),
     ("Immanuel Kant", (153784.00, 153784.00)),
     ("Soren Kierkegaard", (334.00, 43821.00, 3978.00)),
     ("Vandana Shiva", (661.12,)),
     ("Jean-Paul Sartre", ()),
     ("Albert Camus", (5000.00, 5000.00, 5000.00, 5000.00)),
     ("Ralph Ellison",
      (3950.00, 4051.00, 4152.00, 4253.00, 4354.00, 4455.00)),
     ("Michel Foucault",
      (72452.00, 72454.00, 72936.00, 73024.00, 73918.00, 87270.00)),
     ("David Hume", ()),
     ("Thomas Aquinas", (75.00, 0.57)),
     ("Friedrich Nietzsche",
      (602.05, 605.97, 618.26, 618.27, 620.06, 668.08, 668.08, 703.52, 709.15,
       712.01, 720.15)))

# Aggregate donor data shall be contained in a dict, each donor keyed on the
# donor's name.
_First_Donors_Dict = {name.lower(): donor
                      for name, donor
                      in [(donor[0], donor)
                      for donor
                      in _First_Donors_Tuple]}


def make_nonupdated_test_donor():
    """
    Make a donor without a computed total and average donation field.
    """
    return ("Al Swearingen", (17.00, 18.00, 19.00), 0.00, 0.00)


def my_name_is(state):
    """
    Retrieve the donor name from the state container.
    """
    return "My name is {}".format(state["name"])


def make_test_donor():
    """
    Create a test donor tuple.
    """
    return ("Al Swearingen", (17.00, 18.00, 19.00), 0.00, 0.00)


_TEST_DONOR_1 = ("Zephram Cochrane", (99.00, 20.63, 2161.50), 2281.13, 760.38)
_TEST_DONOR_2 = ("John Lizardo", (), 0.00, 0.00)
_TEST_DONOR_3 = make_nonupdated_test_donor()


def make_test_donors():
    """
    Build a dict (map) of donors for the application from _TEST_DONOR_1,
    _TEST_DONOR_2, and _TEST_DONOR_3.
    """
    donors = {name.lower(): donor
              for name, donor
              in [(donor[0], donor)
              for donor
              in [_TEST_DONOR_1, _TEST_DONOR_2, _TEST_DONOR_3]]}
    return donors


def initialize_mailroom():
    """
    Initialize an easy-to-test 3-donor mailroom (populated entirely by
    starship captains!)
    """
    donor_1 = ("Jonathan Archer", (99.00, 20.63, 2161.50), 2281.13, 760.38)
    donor_2 = ("Chris Pike", (), 0.00, 0.00)
    donor_3 = ("James Kirk", (17.00, 18.00, 19.00), 54.00, 18.00)
    donors = {name.lower(): donor
              for name, donor
              in [(donor[0], donor)
              for donor
              in (donor_1, donor_2, donor_3)]}
    mailroom._Donors = donors
    success = (len(mailroom._Donors) == 3)
    if (not success):
        raise Exception("initialize_mailroom failure")
    return donors


# == Mailroom string utils


# str safe_input(str <prompt>)
# ----------------------------------------------------------------------------
# NOT COVERED (requires user input)
def test_safe_input():
    assert(True)


# str clean_name(str <name>)
# ----------------------------------------------------------------------------
# Input from the user shall have extra spaces removed.
def test_clean_name():
    test_data \
        = [["Fred", "Fred"],
           ["Dever-Connor  ", "Dever-Connor"],
           ["  Shaat Rabah", "Shaat Rabah"],
           [" ibn Rashid  ", "ibn Rashid"],
           [" not  the name  of a flavor   ", "not the name of a flavor"],
           ["Ragnar   Lothbruk", "Ragnar Lothbruk"]]
    for arg, expected in test_data:
        actual = mailroom.clean_name(arg)
        assert(actual == expected)


# str check_name_case(str <name>, bool <override_correction>=True)
# ----------------------------------------------------------------------------
# Donor names shall be "Capitalized": The first character shall be
# uppercase; subsequent characters shall be lowercase.
#
# If the name is modified by the application, it shall be presented to the to
# the user for exceptance or rejection. QA: This feature is not tested.
def test_check_name_case():
    test_data \
        = [["Fred", "Fred"],
           ["FRED", "Fred"],
           ["fred", "Fred"],
           ["MacIntosh", "Macintosh"],
           ["O'Rourke", "O'rourke"],
           ["John Dever-Connor", "John Dever-connor"],
           ["2Pac", "2pac"]]
    for arg, expected in test_data:
        actual = mailroom.check_name_case(arg, False)
        assert(actual == expected)


# str get_time_stamp()
# ----------------------------------------------------------------------------
# A timestamp shall be used for differentiating files. The timestamp shall
# be a string of date and time numbers conforming to the following format:
#
# YYYY-MM-dd-hh-mm-ss
#
# where YYYY is year, MM is month, dd is day of the month, hh is hour of the
# day, mm is minutes of the hour, and ss are seconds of the minute.
def test_get_time_stamp():
    time_stamp_1 = mailroom.get_time_stamp()
    pattern = r"\d\d\d\d-\d\d-\d\d-\d\d-\d\d-\d\d"
    match = re.search(pattern, time_stamp_1)
    assert(match is not None)
    expected_span = (0, 19)
    assert(match.span() == expected_span)
    time_stamp_2 = mailroom.get_time_stamp()
    assert(time_stamp_2 >= time_stamp_1)


# == Mailroom input data processing tests


# bool is_floatable(int|float|bool|str|None <v>)
# ----------------------------------------------------------------------------
# String input values which represent floating point values shall be evaluated
# for their ability to be coerced into numeric values.
def test_is_floatable():
    test_data = [[0, True],
                 ["0", True],
                 [3.14, True],
                 ["3.14", True],
                 [-7, True],
                 ["-7", True],
                 [-20.63, True],
                 ["-20.63", True],
                 [+4, True],
                 ["+4", True],
                 ["fred", False],
                 ["", False],
                 [True, True],
                 [False, True]]
    for arg, expected in test_data:
        actual = mailroom.is_floatable(arg)
        assert(actual == expected)


# bool is_intable(int|float|bool|str|None <v>)
# ----------------------------------------------------------------------------
# String input values which represent integer values shall be evaluated
# for their ability to be coerced into numeric values.
def test_is_intable():
    test_data = [[0, True],
                 ["0", True],
                 [3.14, True],
                 ["3.14", False],
                 [-7, True],
                 ["-7", True],
                 [-20.63, True],
                 ["-20.63", False],
                 [+4, True],
                 ["+4", True],
                 ["fred", False],
                 ["", False],
                 [True, True],
                 [False, True]]
    for arg, expected in test_data:
        actual = mailroom.is_intable(arg)
        print("mailroom.is_intable({}) = {}".format(arg, actual))
        assert(actual == expected)


# == Mailroom donor cached attributes


# str donor_name(tuple <donor>)
# ----------------------------------------------------------------------------
# The name accessor shall accept a donor as the argument and return the
# donor's name as a string.
def test_donor_name():
    global _TEST_DONOR_1
    expected = _TEST_DONOR_1[0]
    actual = mailroom.donor_name(_TEST_DONOR_1)
    assert(actual == expected)


# == Mailroom donor computed cached attributes


# float donor_total_gift(tuple <donor>)
# ----------------------------------------------------------------------------
# The total_gift accessor shall accept a donor as the argument and return the
# donor's net gift amount as a floating point value.
def test_donor_total_gift():
    global _TEST_DONOR_1
    expected = _TEST_DONOR_1[2]
    actual = mailroom.donor_total_gift(_TEST_DONOR_1)
    assert(actual == expected)


# float donor_average_gift(tuple <donor>)
# ----------------------------------------------------------------------------
# The average_gift accessor shall accept a donor as the argument and return
# the donor's average of all gift amounts as a floating point value.
def test_donor_average_gift():
    global _TEST_DONOR_1
    expected = _TEST_DONOR_1[3]
    actual = mailroom.donor_average_gift(_TEST_DONOR_1)
    assert(actual == expected)


# == Mailroom donor modifiable cached attributes


# tuple donor_gifts(tuple <donor>)
# ----------------------------------------------------------------------------
# The gifts accessor shall accept a donor as the argument and return
# the donor's sequence of gift amounts. This sequence can be empty.
def test_donor_gifts():
    global _TEST_DONOR_1
    expected = _TEST_DONOR_1[1]
    actual = mailroom.donor_gifts(_TEST_DONOR_1)
    assert(actual == expected)


# == Mailroom donor computed uncached attributes


# int donor_gift_count(tuple <donor>)
# ----------------------------------------------------------------------------
# The gift count accessor shall accept a donor as the argument and return
# the donor's number of gifts as an integer >= 0.
def test_donor_gift_count():
    global _TEST_DONOR_1, _TEST_DONOR_2
    for donor in (_TEST_DONOR_1, _TEST_DONOR_2):
        expected = len(donor[1])
        actual = mailroom.donor_gift_count(donor)
        assert(actual == expected)


# float donor_last_gift(donor)
# ----------------------------------------------------------------------------
# The last gift accessor shall accept a donor as the argument and return
# the last element of the donor's sequence of gift amounts. If the sequence
# is empty, the returned value is None.
def test_donor_last_gift():
    global _TEST_DONOR_1, _TEST_DONOR_2
    test_data = [[_TEST_DONOR_1, 2161.50],
                 [_TEST_DONOR_2, None]]
    for donor, expected in test_data:
        actual = mailroom.donor_last_gift(donor)
        assert(actual == expected)


# == Mailroom donor utils


# donor apply_donor_rules(tuple <donor>)
# ----------------------------------------------------------------------------
# Application of donor attribute rules shall cause the donor's computed cached
# attributes to be recomputed.
def test_apply_donor_rules():
    test_donor = make_nonupdated_test_donor()
    expected = ("Al Swearingen", (17.00, 18.00, 19.00), 54.00, 18.00)
    mailroom._Donors = make_test_donors()
    actual = mailroom.apply_donor_rules(test_donor)
    assert(actual == expected)


# == Mailroom donor data load


# tuple initial_donors()
# ----------------------------------------------------------------------------
# Initial donor data shall consist of 3 or more donors. Each donor shall
# -- at a minimum -- contain the donor's name and a sequence of donations
# they have made.
def test_initial_donors():
    global _First_Donors_Tuple
    expected = _First_Donors_Tuple
    actual = mailroom.initial_donors()
    assert(actual == expected)


# int load_donors()
# ----------------------------------------------------------------------------
# Aggregate donor data shall be contained in a dict, each donor keyed on the
# donor's name.
def test_load_donors():
    global _First_Donors_Dict
    mailroom._Donors = {}
    expected = len(_First_Donors_Dict)
    actual = mailroom.load_donors()
    # -- Same number of items verification.
    assert(actual == expected)
    exp_donors = _First_Donors_Dict
    act_donors = mailroom._Donors
    # -- Verify that every item in the expected dict exists in the actual dict
    for exp_name, exp_donor in exp_donors.items():
        exp_gifts = exp_donor[1]
        act_donor = act_donors[exp_name]
        assert(act_donor is not None)
        act_gifts = act_donor[1]
        assert(act_gifts == exp_gifts)
    # -- Verify that no additional items exist in the actual dict that don't
    #    exist in the expected dict
    for act_name, act_donor in act_donors.items():
        act_gifts = act_donor[1]
        exp_donor = exp_donors[act_name]
        assert(exp_donor is not None)
        exp_gifts = exp_donor[1]
        assert(exp_gifts == act_gifts)


# == Mailroom donor add/delete/edit


# donor get_donor(str <name>)
# ----------------------------------------------------------------------------
# A donor shall be retrievable by the donor's name. An invalid name shall
# return None.
def test_get_donor():
    expected = ("Thomas Aquinas", (75.00, 0.57), 75.57, 37.78)
    name = expected[0]
    mailroom.load_donors()
    actual = mailroom.get_donor(name)
    assert(actual == expected)
    expected = None
    actual = mailroom.get_donor("Marco Ramius")
    assert(actual == expected)


# bool add_donor(str <name>)
# ----------------------------------------------------------------------------
# A donor shall be added to the donor aggregate if the donor's name is unique
# and shall be confirmed by the add operation.
def test_add_donor():
    mailroom.load_donors()
    #
    # Verify that the method confirms the add operation for a new donor.
    #
    expected_donor_name = "Kahless"
    expected_donor = (expected_donor_name, (), 0.0, 0.0)
    expected_return_value = True
    actual_return_value = mailroom.add_donor(expected_donor_name)
    assert(actual_return_value == expected_return_value)
    #
    # Verify that method actually added the donor.
    #
    actual_donors = mailroom._Donors
    actual_donor = actual_donors[expected_donor[0].lower()]
    assert(actual_donor == expected_donor)
    #
    # Verify that the method confirms failure when attempting to add a donor
    # with the same name.
    #
    expected_return_value = False
    actual_return_value = mailroom.add_donor(expected_donor_name)
    assert(actual_donor == expected_donor)


# bool add_donor_gift(tuple <donor_in>, float <gift>)
# ----------------------------------------------------------------------------
# The donor add gift operation shall append a append a numeric value greater
# than zero to the donor's gift sequence and confirm that the operation
# succeeded. A value not greater than zero shall fail. A non-numeric value
# shall fail.
# NOTE: This function only handles the non-numeric rule; the > 0 rule is
# handled upstream.
def test_add_donor_gift():
    mailroom.load_donors()
    name = "David Hume"
    before_donor = mailroom._Donors[name.lower()]
    before_gift = before_donor[1]
    before_gift_count = len(before_gift)
    gift = 39.78
    expected_return_value = True
    actual_return_value = mailroom.add_donor_gift(before_donor, gift)
    # Adding a gift shall return True if successful
    assert(actual_return_value == expected_return_value)
    after_donor = mailroom._Donors[name.lower()]
    after_gift = after_donor[1]
    after_gift_count = len(after_gift)
    # Adding a gift shall increase the gift count by 1
    assert(after_gift_count == (before_gift_count + 1))
    # Added gift shall be the last item in donor gift sequence
    after_last_gift = None if after_gift_count == 0 else after_gift[-1]
    assert(after_last_gift == gift)
    # Adding a non-numeric gift shall fail.
    before_donor = after_donor
    before_gift = before_donor[1][-1]
    gift = "money"
    expected_return_value = False
    actual_return_value = mailroom.add_donor_gift(before_donor, gift)
    assert(actual_return_value == expected_return_value)
    after_donor = mailroom._Donors[name.lower()]
    after_gift = after_donor[1][-1]
    assert(before_gift == after_gift)


# == Mailroom report generation


# int donor_data_width(int|float|str <v>)
# ----------------------------------------------------------------------------
# Data width...
#   ...for a string value shall be the number of chars in the string;
#   ...for an int value shall be the number of digits in the value;
#   ...for a float value shall be the width of the printed value of the
#   number rounded to 2 decimal places
#   in the value plus one for the decimal.
def test_donor_data_width():
    test_data = (("", 0), ("fred", 4), (270, 3), (3.14159, 4), (557.1, 5))
    for v, expected in test_data:
        actual = mailroom.donor_data_width(v)
        assert(actual == expected)


# tuple report_col_names()
# ----------------------------------------------------------------------------
# The overall donor report columns shall include the donor name, total amount
# of gifts, number of gifts, and average gift.
def test_report_col_names():
    expected = ("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    actual = mailroom.report_col_names()
    assert(actual == expected)


# tuple report_column_widths(<tuple> reported_donors)
# ----------------------------------------------------------------------------
# Report column widths shall be determined for each column based on the
# maximum of the column name width and the column values.
def test_report_column_widths():
    mailroom.load_donors()
    donors_tuple = tuple(mailroom._Donors.values())
    expected = (19, 11, 9, 12)  # via tedious eye-balling!
    actual = mailroom.report_column_widths(donors_tuple)
    assert(actual == expected)


# str justify(col_value, col_width, justification, prefix)
# ----------------------------------------------------------------------------
# Reported column value shall allow for right- or left-justification over a
# fixed width and with an optional leading units prefix.
def test_justify():
    test_data = ((("Shaat Rabah", 17, "L", ""), "Shaat Rabah      ", 17),
                 (("Shaat Rabah", 17, "R", ""), "      Shaat Rabah", 17),
                 (("1783.14", 12, "L", "$"), "$1783.14    ", 12),
                 (("1783.14", 12, "R", "$"), "$    1783.14", 12),
                 (("3", 7, "L", ""), "3      ", 7),
                 (("3", 7, "R", ""), "      3", 7),
                 (("fracture", 5, "L", ""), "fract", 5),
                 (("fracture", 5, "R", ""), "fract", 5))
    for args, expected_str, expected_width in test_data:
        actual_str = mailroom.justify(*args)
        assert(actual_str == expected_str)
        actual_width = len(actual_str)
        assert(actual_width == expected_width)


# str format_money(value, width)
# ----------------------------------------------------------------------------
# Reported floating point money value shall be right-justified over a fixed
# width to two decimal places and have a leading "$" char.
def test_format_money():
    test_data = (((0, 7), "$  0.00"),
                 ((1783.00, 10), "$  1783.00"),
                 ((98765.43, 12), "$   98765.43"))
    for args, expected in test_data:
        actual = mailroom.format_money(*args)
        assert(actual == expected)


# str format_int(value, width)
# ----------------------------------------------------------------------------
# Reported int value shall be right-justified over a fixed width.
def test_format_int():
    test_data = (((3, 7), "      3"),
                 ((1783, 10), "      1783"),
                 ((98765, 12), "       98765"))
    for args, expected in test_data:
        actual = mailroom.format_int(*args)
        assert(actual == expected)


# str format_str(value, width)
# ----------------------------------------------------------------------------
# Reported str value shall be left-justified over a fixed width.
def test_format_str():
    test_data = ((("Flux Capacitor", 16), "Flux Capacitor  "),
                 (("John Bigboote", 16), "John Bigboote   "),
                 (("Noodles Romanoff", 7), "Noodles"))
    for args, expected in test_data:
        actual = mailroom.format_str(*args)
        assert(actual == expected)


# str report_row_separator(sep_char, col_widths)
# ----------------------------------------------------------------------------
# Report row separator line shall be created from a single character based on
# the column widths with a 2-char separation between columns.
def test_report_row_separator():
    test_data = \
        ((("-", (12, 7, 5)),
         "------------------------------"),
         (("=", (2, 32, 14)),
          "======================================================"),
         (("?", (1, 4)),
          "????????"),
         (("+", (1,)),
          "+"),
         (("+", ()),
          ""))
    for args, expected in test_data:
        actual = mailroom.report_row_separator(*args)
        assert(actual == expected)


# str report_header(col_names, col_widths)
# ----------------------------------------------------------------------------
# Report row header shall include as the first row a left-justified
# "Donor Report" title; second row, a separator based on "=", column names,
# and widths; and third row, a separator based on "-", column names, and
# widths.
def test_report_header():
    col_names = ("Name", "Gift", "#", "Other")
    col_widths = (14, 6, 3, 17)
    expected = \
        ("\nDonor Report\n=================================================\n"
         "Name           | Gift   | #   | Other            \n"
         "-------------------------------------------------")
    print(expected)
    actual = mailroom.report_header(col_names, col_widths)
    print(actual)
    assert(actual == expected)


# str report_row(tuple <donor>,
#                tuple <accessors>,
#                tuple <col_widths>,
#                tuple <col_fmts>)
# ----------------------------------------------------------------------------
# A report row shall represent a donor and show name (str), total gift
# amount ($), gift count (int), and average gift ($).
def test_report_row():
    attr_accessors = (mailroom.donor_name,
                      mailroom.donor_total_gift,
                      mailroom.donor_gift_count,
                      mailroom.donor_average_gift)
    col_widths = (19, 11, 9, 12)
    col_fmts = tuple([mailroom.format_str,
                      mailroom.format_money,
                      mailroom.format_int,
                      mailroom.format_money])
    mailroom.load_donors()
    donors = mailroom._Donors
    name = "Ralph Ellison"
    donor = donors[name.lower()]
    expected = "Ralph Ellison         $  25215.00           6   $    4202.50"
    actual = mailroom.report_row(donor, attr_accessors, col_widths, col_fmts)
    assert(actual == expected)
    name = "David Hume"
    donor = donors[name.lower()]
    expected = 'David Hume            $      0.00           0   $       0.00'
    actual = mailroom.report_row(donor, attr_accessors, col_widths, col_fmts)
    assert(actual == expected)


# str make_donors_net_values_report(dict <donors>)
# ----------------------------------------------------------------------------
# The aggregate summary for the donor report shall include the following
# displayed in the order shown:
#
# Donor count  = <int:net-number-of-donors>
# Gift count   = <int:net-number-of-gifts-from-all-donors>
# Net gifts    = <$:net-gift-amount-from-all-donors>
# Average gift = <$:average-gift-amount-from-all-donors>
#
# Quantities shall be right-justified.
def test_make_donors_net_values_report():
    mailroom.load_donors()
    donors = mailroom._Donors
    #
    # NOTE: The expected value was eye-balled. It needs to be changes if the
    #       initial load set of required calculations change.
    #
    expected = ("Donor count  =           11\n"
                "Gift count   =           40\n"
                "Net gifts    = $  864951.69\n"
                "Average gift = $   21623.79")
    actual = mailroom.make_donors_net_values_report(donors)
    assert(actual == expected)


# str make_donors_report()
# ----------------------------------------------------------------------------
# Mailroom shall generate a donors report string that for each donor provides
# donor name, total gift quantity, number of gifts, and average gift. It shall
# also provide a net values summary that includes donor count, net gift count,
# net gifts, and average net gift. The string shall display as a table.
def test_make_donors_report():
    initialize_mailroom()
    #
    # NOTE: The expected value was eye-balled. That is why a smaller donor
    #       set was used.
    #
    expected = \
        ('\n'
         'Donor Report\n'
         '========================================================\n'
         'Donor Name      | Total Given | Num Gifts | Average Gift\n'
         '--------------------------------------------------------\n'
         'Jonathan Archer   $   2281.13           3   $     760.38\n'
         'James Kirk        $     54.00           3   $      18.00\n'
         'Chris Pike        $      0.00           0   $       0.00\n'
         '--------------------------------------------------------\n'
         'Donor count  =            3\n'
         'Gift count   =            6\n'
         'Net gifts    = $    2335.13\n'
         'Average gift = $     389.19\n'
         '--------------------------------------------------------')
    actual = mailroom.make_donors_report()
    assert(actual == expected)


# == Mailroom message file management


# bool create_folder(Path <folder_path>)
# ----------------------------------------------------------------------------
# When required, mailroom shall create a file system folder with the provided
# name in the working folder of the running application.
def test_create_folder():
    folder_name = "pholder"
    folder_path = pathlib.Path.cwd().joinpath(folder_name)
    if (folder_path.exists()):
        folder_path.rmdir()
    # Folder does not exist; create new
    assert(mailroom.create_folder(folder_path))
    assert(folder_path.exists())
    # Folder does exist; overwrite
    assert(mailroom.create_folder(folder_path))
    assert(folder_path.exists())
    # Cleanup
    folder_path.rmdir()


# str make_donor_basename(str <name>)
# ----------------------------------------------------------------------------
# The message folder for an individual donor shall be based on a base name
# that is based on the donor's name in all lowercase and following the pattern
#
# <last_name>[-<first_name>[-<middle_name>]]
#
# Int and float values and the strings "", ".", and ".." shall be invalid.
def test_make_donor_basename():
    test_data = (("Ewan MacTeagle", "macteagle-ewan"),
                 ("Miles Edward O'Brien", "obrien-miles-edward"),
                 ("Douglas Dever-Conner", "deverconner-douglas"),
                 ("Klaatu", "klaatu"),
                 (4, None),
                 ("", None),
                 (".", None),
                 ("..", None))
    for arg, expected in test_data:
        actual = None
        try:
            actual = mailroom.make_donor_basename(arg)
        except (SyntaxError, TypeError, ValueError, AttributeError) as ex:
            print(str(ex))  # Doesn't actually print
            assert(actual == expected)
        else:
            assert(actual == expected)


# str root_folder_path()
# ----------------------------------------------------------------------------
# The mailroom root donor message folder shall be in the application working
# folder and shall be named "donor-messages".
def test_root_folder_path():
    expected = str(pathlib
                   .PurePath(mailroom.__file__)
                   .parent
                   .joinpath("donor-messages"))
    actual = str(mailroom.root_folder_path())
    assert(actual == expected)


# Path donor_folder_path(Path <root_folder_path>, str <donor_name>)
# ----------------------------------------------------------------------------
# The donor message folder path shall be a subfolder under root donor message
# folder and named with the base-name format constructed from the donor name.
def test_donor_folder_path():
    donor_name = "Ewan MacTeagle"
    donor_base_name = "macteagle-ewan"
    donor_root_folder_path = (pathlib
                              .Path(mailroom.__file__)
                              .parent
                              .joinpath("donor-messages"))
    expected = str(donor_root_folder_path.joinpath(donor_base_name))
    actual = str(mailroom.donor_folder_path(donor_root_folder_path,
                                            donor_name))
    assert(actual == expected)


# Path donor_document_path(folder_path, donor_name, t_stamp)
# ----------------------------------------------------------------------------
# The donor message document path shall be based on the donor folder path and
# and the document name based on the pattern
#
# <base-name>-<time-stamp>-<index>.txt
#
# where <base-name>     ::= <last_name>[-<first_name>[-<middle_name>]];
# and   <time-stamp>    ::= YYYY-MM-dd-hh-mm-ss, where YYYY is year, MM is
#                           month, dd is day of the month, hh is hour of the
#                           day, mm is minutes of the hour, and ss are seconds
#                           of the minute;
# and   <index>         ::= a value inclusively between "000" and "999".
def test_donor_document_path():
    donor_name = "Ewan MacTeagle"
    root_folder_name = "donor-messages"
    donor_folder_name = "macteagle-ewan"
    t_stamp = "2063-04-05-03-29"
    donor_folder_name = "macteagle-ewan"
    donor_doc_name\
        = "-".join((donor_folder_name, "{}-000.txt".format(t_stamp)))
    donor_folder_path = (pathlib
                         .Path(mailroom.__file__)
                         .parent
                         .joinpath(root_folder_name,
                                   donor_folder_name))
    expected = str(donor_folder_path.joinpath(donor_doc_name))
    actual = str(mailroom.donor_document_path(donor_folder_path,
                                              donor_name,
                                              t_stamp))
    assert(actual == expected)


# == Mailroom UI utilities

# dict make_state(str <name=None>,
#                 int <id=None>,
#                 float <gift=None>,
#                 str <message=None>)
# ----------------------------------------------------------------------------
# Command functions shall use a dict instance known as a state representing
# the important state values of a donor or the donor aggregate. The state
# shall include one or more of the following key-value pairs:
#
# "name":       (str) Donor's name;
# "id":         (int) Donor's one-bsed row position in an ordered tuple
#                     representation of a donor collection;
# "gift":       ($)   Latest gift value;
# "message":    (str) Thank-you message for donor's latest gift;
# "time_stamp": (str) Time of command call.
def test_make_state():
    t_stamp = "2063-04-05-03-29"
    expected = {
        "name": "Jonathan Archer",
        "id": 1,
        "gift": 25.00,
        "message": "The larch",
        "time_stamp": t_stamp
    }
    expected = ["Jonathan Archer", 1, 25.00, "The Larch"]
    state = mailroom.make_state("Jonathan Archer", 1, 25.00, "The Larch")
    actual = [state["name"], state["id"], state["gift"], state["message"]]
    assert(actual == expected)


# None|str|int|float|bool|... do_cmd(fmap, cmd, state)
# ----------------------------------------------------------------------------
# UI screens shall dispatch operations mapped to command keystrokes.
def test_do_cmd():
    fmap = {":F": my_name_is}
    cmd = ":F"
    state = {"name": "Kizer Souze"}
    expected = my_name_is(state)
    actual = mailroom.do_cmd(fmap, cmd, state)
    assert(actual == expected)


# str make_menu_prompt(str <menu_directions>)
# ----------------------------------------------------------------------------
# The application shall provide direction for input of a command, text value,
# or numeric value in order to accomplish a task.
def test_make_menu_prompt():
    expected = "INPUT: Type [:H]elp for assistance > "
    actual = mailroom.make_menu_prompt("Type [:H]elp for assistance")
    assert(actual == expected)


# list sorted_donor_names()
# ----------------------------------------------------------------------------
# For donor listing purposes, donors shall be sorted in descending order by
# the name provided by the user.
def test_sorted_donor_names():
    initialize_mailroom()
    expected = ['Chris Pike', 'James Kirk', 'Jonathan Archer']
    actual = mailroom.sorted_donor_names()
    assert(actual == expected)


# str generate_message(donor)
# ----------------------------------------------------------------------------
# The mailroom application shall be capable of generating one of two
# messages for a donor based on the donor's gifts:
#
# (1) If the donor has made at least one gift, a thank-you message for the
#     donor's last gift; or
# (2) If the donor has made no gifts, a message requesting that they do.
def test_generate_message():
    initialize_mailroom()
    donors = mailroom._Donors
    #
    # Donor who made one or more gifts.
    #
    key = "jonathan archer"
    donors = mailroom._Donors
    donor = donors[key]
    expected = ("Dear Jonathan Archer\n\nThanks for your recent gift of "
                "$2161.50.\n\nRegards,\n\nACME Charities")
    actual = mailroom.generate_message(donor)
    assert(actual == expected)
    #
    # Donor who made no gifts.
    #
    key = "chris pike"
    donor = donors[key]
    expected = ("Dear Chris Pike\n\nPlease consider making a gift to our "
                "organization. It's tax deductible.\n\n"
                "Regards,\n\nACME Charities")
    actual = mailroom.generate_message(donor)
    assert(actual == expected)


# == Mailroom user-input translation


# str interpret_response(str <response_in>, str <override_correction>)
# ----------------------------------------------------------------------------
def test_interpret_response():
    #
    # Keyboard input shall be interpreted as (1) a command, (2) text value, or
    # (3) numeric value. The validity of the specific value is handled
    # separately.
    #
    # Commands shall be recognized as any value starting with a colon and shall
    # be output as the colon and the second character of the value in uppercase
    # format. Example: :report is :R.
    #
    # Text and numeric values shall be trimmed of whitespace and output without
    # further modification.
    #
    test_data = ((":quit", ":Q"), (":xit", ":X"), (":report", ":R"),
                 (":list", ":L"), (":message", ":M"), (":new", ":N"),
                 (":send", ":S"), (":zoo", ":Z"), ("1", "1"), ("2", "2"),
                 ("3", "3"),
                 ("0.00", "0.00"), ("9.95", "9.95"), ("2783.15", "2783.15"),
                 ("3.14159", "3.14159"), ("", ""), ("fred", "Fred"),
                 ("benjamin sisko", "Benjamin Sisko"))
    for arg, expected in test_data:
        vargs = []
        if (type(arg) == str):
            vargs = (arg.upper(), arg.capitalize(), arg)
        else:
            vargs = (arg,)
        for varg in vargs:
            actual = mailroom.interpret_response(arg, False)
            assert(expected == actual)


# bool send_message(<dict> state, <bool> acknowledge)
# ----------------------------------------------------------------------------
# Mailroom shall be capable of simulating the sending of a thank-you note to a
# donor for their last gift or a request for gift by writing text to a
# uniquely-named document. If successful, the operation shall optionally print
# an acknowledgement. If successful, the operation shall return True.
#
# The document shall created within a folder named specifically for the
# donor. There shall be a root folder for collecting all such donor
# folders.
#
# NOTE: Test does not confirm feedback printing.
def test_send_message():
    donor = ("Jonathan Archer", (99.00, 20.63, 2161.50), 2281.13, 760.38)
    name = donor[0]
    gift = donor[1][-1]
    t_stamp = "2063-04-05-03-29"
    message =\
        ("Dear {},\n\nThanks for your donation of ${}.\n\nFCA"
         .format(name, gift))
    state = {
             "name": name,
             "gift": gift,
             "message": message,
             "time_stamp": t_stamp
             }
    success = mailroom.send_message(state, False)
    assert(success)
    root_folder_name = "donor-messages"
    donor_folder_name = "archer-jonathan"
    donor_doc_name\
        = "-".join((donor_folder_name, "{}-000.txt".format(t_stamp)))
    donor_doc_path = (pathlib
                      .Path(mailroom.__file__)
                      .parent
                      .joinpath(root_folder_name,
                                donor_folder_name,
                                donor_doc_name))
    assert(donor_doc_path.exists())
    donor_doc_path.unlink()


# bool send_message_to_donor(dict <state>)
# ----------------------------------------------------------------------------
# NOTE: Giving this method a pass due to UI feedback being the only
# difference from function send_message.
def test_send_message_to_donor():
    assert(True)


# bool send_messages_to_donors(dict <state>)
# ----------------------------------------------------------------------------
# Mailroom shall be capable of simulating the sending of a thank-you note to
# all donors. Collectively, this includes message delivery requirements for
# each donor.
def test_send_messages_to_donors():
    #
    # Flush donor-messages/.
    #
    root_folder_name = "donor-messages"
    root_folder_path = (pathlib
                        .Path(mailroom.__file__)
                        .parent
                        .joinpath(root_folder_name))
    utils.purge_folder_content(root_folder_path)
    #
    # Mailroom shall simulate sending a thank-you note to all donors,
    # fulfilling the requirement for each donor individually but without
    # printing an acknowledgement. If successful, the operation shall
    # return True.
    #
    donors = initialize_mailroom()
    t_stamp = "2063-04-05-03-29"
    state = {"time_stamp": t_stamp}
    success = mailroom.send_messages_to_donors(state)
    #
    # Verify that method returns indication of success.
    #
    assert(success)
    success = True
    for key, donor in list(donors.items()):
        key_comp = key.split(" ")
        key_comp.reverse()
        donor_base_name = "-".join(key_comp)
        donor_folder_name = donor_base_name
        donor_doc_name = "-".join((donor_folder_name,
                                   "{}-000.txt".format(t_stamp)))
        donor_doc_path = (pathlib
                          .Path(mailroom.__file__)
                          .parent
                          .joinpath(root_folder_name,
                                    donor_folder_name,
                                    donor_doc_name))
        success = success and donor_doc_path.exists()
    #
    # Verify that all documents generated.
    #
    assert(success)


# == Mailroom data verification rules


# bool verify_existing_donor_name(str <name>)
# ----------------------------------------------------------------------------
# The donor's name shall be discoverable within the donor aggregate of the
# application.
def test_verify_existing_donor_name():
    initialize_mailroom()
    test_data = (("Chris Pike", True),
                 ("Jim Kirk", False),
                 ("Jonathan Archer", True),
                 ("", False))
    for name, expected in test_data:
        actual = mailroom.verify_existing_donor_name(name)
        assert(actual == expected)


# bool verify_existing_donor_id(int <id>)
# ----------------------------------------------------------------------------
# The donor's row ID shall be discoverable within the donor aggregate of the
# application.
def test_verify_existing_donor_id():
    test_data = ((1, True), (3, True), (0, False), (4, False))
    for id, expected in test_data:
        actual = mailroom.verify_existing_donor_id(id)
        assert(actual == expected)


# bool verify_new_donor(are <name>)
# ----------------------------------------------------------------------------
# A donor is new if the key based on the donor's name is not mapped to an
# element in the donor aggregate.
def test_verify_new_donor():
    initialize_mailroom()
    test_data = (("Chris Pike", False),              # Duplicate
                 ("Jim Kirk", True),                 # 1+ Alphanum new
                 ("Jonathan Archer", False),         # Duplicate
                 ("", False),                        # Too short
                 ("Milhouse Slater-Kinney", True),   # 1+ Alpha + "-" new
                 ("2Pac Shakur", True),              # 1+ Alphanum + "-" new
                 ("#'(lambda(a)(nth 3 a))", False),  # Invalid symbol(s)
                 ("1138", False),                    # No alpha
                 ("R2D2", True),                     # 1+ Alphanum new new
                 ("Michael O'Hanlon", True),         # 1+ Alpha + "'" new
                 ("A", False),                       # Too short
                 ("--", False),                      # No alpha
                 ("-8", False),                      # No alpha
                 ("'8", False),                      # No alpha
                 ("'L", True),                       # 1 Alpha + "'" new
                 ("-R", True))                       # 1 Alpha + "-" new
    for name, expected in test_data:
        actual = mailroom.verify_new_donor(name)
        assert(actual == expected)


# bool verify_gift(gift)
# ----------------------------------------------------------------------------
# A donor gift is acceptable if it is a numeric value of type float, int, or
# string that is convertable to a float, which is greater than zero.
def test_verify_gift():
    test_data = ((0, False), (-1, False), (0.01, True), (111, True),
                 ("9.95", True), ("0", False), ("Fred", False))
    for gift, expected in test_data:
        actual = mailroom.verify_gift(gift)
        assert(actual == expected)


# == Mailroom user interface


# dict fmap_messenger_ui()
# ----------------------------------------------------------------------------
# For the displayed donor the following command-to-function mapping shall
# exist:
#
# :S   Function that accepts a state instance that sends a message to the
#      donor.
def test_fmap_messenger_ui():
    test_data = ((":S", mailroom.send_message_to_donor),)
    fmap = mailroom.fmap_messenger_ui()
    assert(type(fmap) == dict)
    exp_cmd_key = None
    exp_cmd_fnc = None
    act_cmd_key = None
    act_cmd_fnc = None
    for exp_cmd_key, exp_cmd_fnc in test_data:
        try:
            act_cmd_fnc = fmap.get(exp_cmd_key)
        except Exception:
            act_cmd_fnc = None
        finally:
            assert(exp_cmd_fnc == act_cmd_fnc)
    for act_cmd_key, act_cmd_fnc in fmap.items():
        try:
            exp_cmd_fnc = fmap.get(act_cmd_key)
        except Exception:
            exp_cmd_fnc = None
        finally:
            assert(act_cmd_fnc == exp_cmd_fnc)


# donor get_donor_by_id(id)
# ----------------------------------------------------------------------------
# A donor shall be retrievable by ID, which is its relative position (starting
# at 1) in a sorted donor sequence; an ID less than 1 or more than the number
# of donors shall retrieve None.
def test_get_donor_by_id():
    initialize_mailroom()
    expected_name = "Jonathan Archer"
    id = 3
    donor = mailroom.get_donor_by_id(id)
    actual_name = donor[0]
    assert(actual_name == expected_name)
    id = 0
    donor = mailroom.get_donor_by_id(id)
    assert(donor is None)
    id = 4
    donor = mailroom.get_donor_by_id(id)
    assert(donor is None)


# donor get_donor_by_name(name)
# ----------------------------------------------------------------------------
# A donor shall be retrievable by name; a nonexistent name shall retrieve
# None.
def test_get_donor_by_name():
    initialize_mailroom()
    expected_name = "Jonathan Archer"
    name = "Jonathan Archer"
    donor = mailroom.get_donor_by_name(name)
    actual_name = donor[0]
    assert(actual_name == expected_name)
    expected_name = "Shaat Rabah"
    name = "Shaat Rabah"
    donor = mailroom.get_donor_by_name(name)
    assert(donor is None)


# void add_gift(state)
# ----------------------------------------------------------------------------
# Mailroom shall be capable of adding a numeric gift value greater than zero
# to a valid donor.
def test_add_gift():
    initialize_mailroom()
    #
    # Add a valid gift to a valid donor.
    #
    name = "Chris Pike"
    key = "chris pike"
    gift = 601.17
    state = {"name": name, "gift": gift}
    mailroom.add_gift(state)
    donor = mailroom._Donors[key]
    gifts = donor[1]
    last_gift = gifts[-1]
    assert(last_gift == gift)
    #
    # Add an invalid numeric gift to a valid donor.
    #
    gift = 0.00
    state = {"name": name, "gift": gift}
    mailroom.add_gift(state)
    donor = mailroom._Donors[key]
    gifts = donor[1]
    last_gift = gifts[-1]
    assert(last_gift != gift)
    #
    # Add an invalid gift to a valid donor.
    #
    gift = "gold-pressed latinum"
    state = {"name": name, "gift": gift}
    mailroom.add_gift(state)
    donor = mailroom._Donors[key]
    gifts = donor[1]
    last_gift = gifts[-1]
    assert(last_gift != gift)
    #
    # Add a valid gift to an invalid donor.
    #
    name = "Jeffrey Lebowski"
    key = "jeffrey lebowski"
    gift = 1.00
    state = {"name": name, "gift": gift}
    mailroom.add_gift(state)
    try:
        donor = mailroom._Donors[key]
        gifts = donor[1]
        last_gift = gifts[-1]
    except KeyError:
        gifts = None
        last_gift = None
    finally:
        assert(last_gift != gift)


# dict fmap_donor_ui()
# ----------------------------------------------------------------------------
# For the displayed donor the following command-to-function mapping shall
# exist:
#
# :M   Function that shows the message UI;
# :G   Function that shows prompt for adding another gift.
def test_fmap_donor_ui():
    test_data = ((":M", mailroom.show_messenger_ui),
                 (":G", mailroom.add_gift))
    fmap = mailroom.fmap_donor_ui()
    assert(type(fmap) == dict)
    exp_cmd_key = None
    exp_cmd_fnc = None
    act_cmd_key = None
    act_cmd_fnc = None
    for exp_cmd_key, exp_cmd_fnc in test_data:
        try:
            act_cmd_fnc = fmap.get(exp_cmd_key)
        except Exception:
            act_cmd_fnc = None
        finally:
            assert(exp_cmd_fnc == act_cmd_fnc)
    for act_cmd_key, act_cmd_fnc in fmap.items():
        try:
            exp_cmd_fnc = fmap.get(act_cmd_key)
        except Exception:
            exp_cmd_fnc = None
        finally:
            assert(act_cmd_fnc == exp_cmd_fnc)


# add_new_donor(state)
# ----------------------------------------------------------------------------
# A donor with a name that does not exist in the donor aggregate shall be
# appendable to the donor aggregate.
def test_add_new_donor():
    initialize_mailroom()
    name = "Jon Snow"
    key = "jon snow"
    assert(not (key in mailroom._Donors.keys()))
    state = {"name": name}
    mailroom.add_new_donor(state)
    assert((key in mailroom._Donors.keys()))


# dict fmap_new_donor_ui()
# ----------------------------------------------------------------------------
# For the application main UI the following command-to-function mapping shall
# exist:
#
# :N   Function that adds a new donor with the name provided by the user (in-
#      directly accessible to the user);
def test_fmap_new_donor_ui():
    test_data = ((":N", mailroom.add_new_donor),)
    fmap = mailroom.fmap_new_donor_ui()
    assert(type(fmap) == dict)
    exp_cmd_key = None
    exp_cmd_fnc = None
    act_cmd_key = None
    act_cmd_fnc = None
    for exp_cmd_key, exp_cmd_fnc in test_data:
        try:
            act_cmd_fnc = fmap.get(exp_cmd_key)
        except Exception:
            act_cmd_fnc = None
        finally:
            assert(exp_cmd_fnc == act_cmd_fnc)
    for act_cmd_key, act_cmd_fnc in fmap.items():
        try:
            exp_cmd_fnc = fmap.get(act_cmd_key)
        except Exception:
            exp_cmd_fnc = None
        finally:
            assert(act_cmd_fnc == exp_cmd_fnc)


# dict fmap_mailroom_ui()
# ----------------------------------------------------------------------------
# For the application main UI the following command-to-function mapping shall
# exist:
#
# :L   Function that displays a sorted, enumerated list of donors;
# :M   Function that sends thank-you/request messages to all donors;
# :N   Function that shows the add-new-donor UI;
# :O   Function that shows the detail donor UI for the selected donor (in-
#      directly accessible to the user);
# :R   Function that displays a donor report.
def test_fmap_mailroom_ui():
    test_data = ((":L", mailroom.print_donor_names),
                 (":M", mailroom.send_messages_to_donors),
                 (":N", mailroom.show_new_donor_ui),
                 (":O", mailroom.show_donor_ui),
                 (":R", mailroom.print_donors_report))
    fmap = mailroom.fmap_mailroom_ui()
    assert(type(fmap) == dict)
    exp_cmd_key = None
    exp_cmd_fnc = None
    act_cmd_key = None
    act_cmd_fnc = None
    for exp_cmd_key, exp_cmd_fnc in test_data:
        try:
            act_cmd_fnc = fmap.get(exp_cmd_key)
        except Exception:
            act_cmd_fnc = None
        finally:
            assert(exp_cmd_fnc == act_cmd_fnc)
    for act_cmd_key, act_cmd_fnc in fmap.items():
        try:
            exp_cmd_fnc = fmap.get(act_cmd_key)
        except Exception:
            exp_cmd_fnc = None
        finally:
            assert(act_cmd_fnc == exp_cmd_fnc)


# == Mailroom user interface


# print_app_title()
# ----------------------------------------------------------------------------
# NOT COVERED (displays value to screen only)
def test_print_app_title():
    assert(True)


# print_ui_header(ui_title)
# ----------------------------------------------------------------------------
# NOT COVERED (displays value to screen only)
def test_print_ui_header():
    assert(True)


# print_ui_menu_break_line()
# ----------------------------------------------------------------------------
# NOT COVERED (displays value to screen only)
def test_print_ui_menu_break_line():
    assert(True)


# print_vmsg(ver_name, data, msg)
# ----------------------------------------------------------------------------
# NOT COVERED (displays value to screen only)
def test_print_vmsg():
    assert(True)


# print_donors_report(_state)
# ----------------------------------------------------------------------------
# NOT COVERED (displays value to screen only)
def test_donors_report():
    assert(True)


# print_donor_names(_state)
# ----------------------------------------------------------------------------
# NOT COVERED (displays value to screen only)
def test_print_donor_names():
    assert(True)


# print_donor(donor)
# ----------------------------------------------------------------------------
# NOT COVERED (displays value to screen only)
def test_print_donor():
    assert(True)


# show_messenger_ui(state)
# ----------------------------------------------------------------------------
# NOT COVERED (displays value to screen only)
def test_show_messenger_ui():
    assert(True)


# show_donor_ui(state)
# ----------------------------------------------------------------------------
# NOT COVERED (displays value to screen only)
def test_show_donor_ui():
    assert(True)


# show_new_donor_ui(state)
# ----------------------------------------------------------------------------
# NOT COVERED (displays value to screen only)
def test_show_new_donor_ui():
    assert(True)


# show_mailroom_ui()
# ----------------------------------------------------------------------------
# NOT COVERED (displays value to screen only)
def test_show_mailroom_ui():
    assert(True)


# run_mailroom()
# ----------------------------------------------------------------------------
# NOT COVERED (displays value to screen only)
def test_run_mailroom():
    assert(True)

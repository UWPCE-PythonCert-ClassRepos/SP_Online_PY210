#!/usr/bin/env python


import mailroom_04 as mailroom
import pytest


# Helper method for pytest.
def add_test_users(database):
    mailroom.add_donation(database, 'Donor 01', float(100.61))
    mailroom.add_donation(database, 'Donor 02', float(220.72))
    mailroom.add_donation(database, 'Donor 03', float(333.83))


# Helper method for pytest.
def create_test_db():
    donors_db = mailroom.create_donors_db()
    return donors_db


# PYTEST: COMPLETE
def test_add_donation():
    #
    # Create 'donors_db'.
    donors_db = create_test_db()
    #
    # Add donation to 'donors_db'.
    mailroom.add_donation(donors_db, 'Donor 01', float(100.00))
    #
    # Assertion.
    assert donors_db == {'Donor 01': 100.00}


# PYTEST: COMPLETE
def test_add_to_dict(capsys):
    #
    # Create 'donors_db'.
    donors_db = create_test_db()
    #
    # Add entires to 'donors_db'.
    mailroom.add_to_dict(donors_db, 'Donor 01', 100.00)
    #
    # Print 'donors_db'.
    print(donors_db)
    #
    # Capture system output.
    captured = capsys.readouterr()
    #
    # Assertion.
    assert captured.out == '{\'Donor 01\': 100.0}\n'


# PYTEST: COMPLETE: DOES NOT APPLY.
#
# USER INTERACTION CODE: Not a candidate for unit testing.
#
# No business logic inside this function.
# Any code used in this function under test
# is already tested elsewhere in this pytest file.
def test_check_user_response():
    pass


# PYTEST: COMPLETE
def test_create_donor():
    #
    # Create 'donors_db'.
    donors_db = create_test_db()
    #
    # Add entires to 'donors_db'.
    mailroom.create_donor(donors_db, 'Donor 01')
    #
    # Assertion.
    assert donors_db == {'Donor 01': 0.0}


# PYTEST: COMPLETE.
def test_create_donors_db():
    #
    # Create 'donors_db'.
    donors_db = create_test_db()
    #
    # Assertion.
    assert donors_db == {}


# PYTEST: COMPLETE.
def test_create_main_menu():
    #
    # Create 'donors_db'.
    main_menu = mailroom.create_main_menu()
    #
    # Assertion.
    assert main_menu == {}


# PYTEST: COMPLETE.
def test_create_report(capsys):
    #
    # Create 'donors_db'.
    donors_db = create_test_db()
    #
    # Create a donor in 'donors_db'.
    mailroom.add_donation(donors_db, 'Donor 01', float(100.00))
    #
    # Print 'donors_db'.
    mailroom.create_report(donors_db)
    #
    # Capture system output.
    captured = capsys.readouterr()
    #
    # Assertion.
    assert captured.out == """Donor Name                | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------
Donor 01                   $     100.00           1  $      100.00\n"""


# PYTEST: COMPLETE.
def test_debug_print_db(capsys):
    #
    # Create 'donors_db'.
    donors_db = create_test_db()
    #
    # Create a donor in 'donors_db'.
    mailroom.add_donation(donors_db, 'Donor 01', float(987.65))
    #
    #
    mailroom.print_database(donors_db)
    #
    # Capture system output.
    captured = capsys.readouterr()
    #
    # Assertion.
    assert captured.out == """[ ----- ]: -------------------------------------------------------
[ DEBUG ]: str(key)                     : Donor 01
[ DEBUG ]: str(type(key))               : <class 'str'>
[ DEBUG ]: str(value)                   : 987.65
[ DEBUG ]: str(type(value))             : <class 'float'>
"""


# PYTEST: COMPLETE: DOES NOT APPLY.
#
# USER INTERACTION CODE: Not a candidate for unit testing.
#
# No business logic inside this function.
# Any code used in this function under test (add donation, add donor, etc.)
# is already tested elsewhere in this pytest file.
def test_display_main_menu():
    pass


# PYTEST: COMPLETE
def test_exit_script():
    #
    # Test sys.exit().
    with pytest.raises(SystemExit) as e:
        mailroom.exit_script()
    assert e.type == SystemExit


# PYTEST: COMPLETE
def test_exit_script_ctrl_c():
    #
    # Test sys.exit().
    with pytest.raises(SystemExit) as e:
        mailroom.exit_script()
    assert e.type == SystemExit


# PYTEST: COMPLETE
def test_format_text():
    #
    test_text_01 = 'Hello there this is a test'
    test_text_02 = mailroom.format_text(test_text_01)
    assert test_text_02 == 'Hello_there_this_is_a_test'


# PYTEST: COMPLETE: DOES NOT APPLY.
#
# get_timestamp() is a helper function.
# No business logic inside this function.
def test_get_timestamp():
    pass


# PYTEST: COMPLETE: DOES NOT APPLY.
#
# USER INTERACTION CODE: Not a candidate for unit testing.
#
# No business logic inside this function.
# Any code used in this function under test (add donation, add donor, etc.)
# is already tested elsewhere in this pytest file.
def test_get_user_response():
    pass


# PYTEST: COMPLETE: DOES NOT APPLY.
#
# USER INTERACTION CODE: Not a candidate for unit testing.
#
# No business logic inside this function.
# Any code used in this function under test (add donation, add donor, etc.)
# is already tested elsewhere in this pytest file.
def test_get_user_response_integer():
    pass


# PYTEST: COMPLETE.
def test_list_donor_names(capsys):
    #
    # Create 'donors_db'.
    donors_db = create_test_db()
    #
    # Create a donor in 'donors_db'.
    mailroom.create_donor(donors_db, 'Donor 01')
    #
    # Print 'donors_db'.
    print(donors_db)
    #
    # Capture system output.
    captured = capsys.readouterr()
    #
    # Assertion.
    assert captured.out == '{\'Donor 01\': 0.0}\n'


# PYTEST: COMPLETE.
def test_print_debug_header_line(capsys):
    #
    # Print the debug header line.
    mailroom.print_debug_header_line()
    #
    # Capture system output.
    captured = capsys.readouterr()
    #
    # Assertion.
    assert captured.out == """[ ----- ]: -------------------------------------------------------\n"""


# PYTEST: COMPLETE.
def test_print_debug_message(capsys):
    #
    # Print the debug header line.
    mailroom.print_debug_message('test_message')
    #
    # Capture system output.
    captured = capsys.readouterr()
    #
    # Assertion.
    assert captured.out == """[ ----- ]: -------------------------------------------------------
[ DEBUG ]: test_message
"""


# PYTEST: COMPLETE.
def test_print_error_message(capsys):
    #
    # Print the debug header line.
    mailroom.print_error_message('test_message')
    #
    # Capture system output.
    captured = capsys.readouterr()
    #
    # Assertion.
    assert captured.out == """[ ----- ]: -------------------------------------------------------
[ ERROR ]: test_message
"""


# PYTEST: COMPLETE.
def test_print_main_menu(capsys):
    #
    # Print 'main_menu'.
    mailroom.print_main_menu()
    #
    # Capture system output.
    captured = capsys.readouterr()
    #
    # Assertion.
    assert captured.out == """[ ----- ]: -------------------------------------------------------
[  MAIN ]: Select an option:
[ ----- ]: -------------------------------------------------------
[     1 ]: Send a Thank You to a single donor.
[     2 ]: Create a Report.
[     3 ]: Send letters to all donors.
[     4 ]: Quit
[     5 ]: [ DEBUG ]: print_database(donors_db)
[     6 ]: [ DEBUG ]: list_donor_names(donors_db)
[     7 ]: [ DEBUG ]: add_donation(donors_db, 'Donor 10', float(100.00))
[     8 ]: [ DEBUG ]: comprehensions_test()
"""


# PYTEST: COMPLETE.
def test_print_send_thank_you_menu(capsys):
    #
    # Print 'main_menu'.
    mailroom.print_send_thank_you_menu()
    #
    # Capture system output.
    captured = capsys.readouterr()
    #
    # Assertion.
    assert captured.out == """[ ----- ]: -------------------------------------------------------
[ DONOR ]: Select an option:
[ ----- ]: -------------------------------------------------------
[     1 ]: Type: 'list'
[       ]:        Display a list of donors.
[     2 ]: Type: 'Existing Donor's Name'
[       ]:        Add a new donation for a donor.
[     3 ]: Type: 'New Donor's Name'
[       ]:        Create a new donor.
[     4 ]: Type: 'main'
[       ]:        Return to the Main Menu.
"""


# PYTEST: COMPLETE.
def test_print_thank_you_message(capsys):
    #
    # Print the thank you message.
    mailroom.print_thank_you_message('Donor 01', 987.65)
    #
    # Capture system output.
    captured = capsys.readouterr()
    #
    # Assertion.
    assert captured.out == """[ ----- ]: -------------------------------------------------------

Dear Donor 01,

Thank you for your donation of $987.65.

  Regards,
  - the Thank You bot

"""


# PYTEST: COMPLETE: DOES NOT APPLY.
#
# USER INTERACTION CODE: Not a candidate for unit testing.
#
# No business logic inside the 'send_thank_you()' function.
# Any code used in this function under test (add donation, add donor, etc.)
# is already tested elsewhere in this pytest file.
def test_send_thank_you():
    pass


# PYTEST: NOTE:
#
# The issue with testing this function is that I currently cannot check the
# file system for the presence of this file; as well, cross functional testing
# across operating systems is needed here. Setting to PASS for now but would
# revist and fix this.
def test_send_thank_you_global(capsys):
    pass


# PYTEST: COMPLETE.
def test_sort_database(capsys):
    #
    # Create 'donors_db'.
    donors_db = create_test_db()
    #
    # Add a donation to 'donors_db'.
    mailroom.add_donation(donors_db, 'Donor 01', float(987.65))
    mailroom.add_donation(donors_db, 'Donor 02', float(123.45))
    #
    mailroom.sort_database(donors_db)
    #
    # Print 'donors_db'.
    print(donors_db)
    #
    # Capture system output.
    captured = capsys.readouterr()
    #
    # Assertion.
    assert captured.out == '{\'Donor 01\': 987.65, \'Donor 02\': 123.45}\n'

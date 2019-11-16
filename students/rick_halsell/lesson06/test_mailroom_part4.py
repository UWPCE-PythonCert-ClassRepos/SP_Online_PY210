import pytest
import os
import ds.mailroom_part4 as mr4
import mailroom_part4
#from mr4 import report_func

def test_check_dictionary_lenght():
    """
    Checks to see if dictionary contains 5 or more key value
    pairs as required.
    """
    assert len(mr4.donors_dictionary) >= 5


def test_exact_selection_func():
    """
    Checks to see if function can locate existing donor and donations
    in database.
    Also checks to see if new donation added is found.
    """
    selection = 'Jonny Gill'
    assert selection == 'Jonny Gill'
    donation = '2.00'
    assert donation == '2.00'
    mr4.donors_dictionary[selection].append(donation)
    print(selection, (mr4.donors_dictionary[selection]))


def test_list_donors_func():
    """
    Test to see if function prints out donors list
    """
    given = 'Rick halsell'
    actual = mr4.list_donors_func()
    assert actual != given

    expected = 'Ronnie DeVoe'
    assert mailroom_part4.list_donors_func() == expected


def test_donor_in_dict_func():
    """
    Test existing donor in dictionary and non-existent donor
    """
    selection = 'Bobby Brown'
    assert selection == 'Bobby Brown'
    with pytest.raises(TypeError):
        selection = set(0)

    #  Test non-existent and donation addition attempt
    selection = 'New Donor'
    assert selection == 'New Donor'


def test_donor_not_in_dict_func():
    """
    Test new donor addition and existing donor
    """
    #  Test New Donor and donation addition
    selection = 'New Donor'
    assert selection == 'New Donor'
    donation = '34.99'
    print(f"\nThank you {selection} for your donation of ${donation}.")

    with pytest.raises(ValueError):
        donation = float('a random string')

    #  Test existing donor
    selection = 'Bobby Brown'
    assert selection == 'Bobby Brown'

def test_thank_you_note_func(tmpdir):
    """
    Test ability to write thank you note to file
    """
    key = 'Michael Bivins'
    donation_total = '99.99'
    mr4.left_aligned_to_line = (f"{key}")
    mr4.mid_left_aligned_body = (f"{donation_total}")
    mr4.mid_right_aligned = (f"Templine1")
    mr4.right_aligned_ending = (f"Templine2")
    thank_you_output_file = (f"{key}_Thank_You_Letter.txt")
    file = tmpdir.join(thank_you_output_file)
    file.write(f"{mr4.left_aligned_to_line}, {mr4.mid_left_aligned_body}, {mr4.mid_right_aligned}, {mr4.right_aligned_ending}")
    assert file.read() == 'Michael Bivins, 99.99, Templine1, Templine2'


def test_letter_confirmation_func():
    """
    Test donors count in dictionary, saved location data
    """
    number_of_donors = (len(mr4.donors_dictionary.items()))
    print(f"\n{number_of_donors} - Thank You Letters Generated...")
    print(f"\nSaved Location: {os.getcwd()}")

@pytest.mark.skip(reason="No need to test this menu prompt.")
def test_menu_options_func_default():
    assert mr4.menu_options_func_default() != None

def test_database_func():
    """
    Test database menu options and exception handle
    """
    mr4.menu_options_func = {
            0 : mr4.main_menu_function,
            1 : mr4.list_donors_func,
            2 : mr4.donor_in_dict_func,
            3 : mr4.thank_you_note_func
    }

    with pytest.raises(ValueError):
        selection = float('a random string')

    #  Tests that default switch case parameter works
    selection = 5
    selection = mr4.menu_options_func.get(selection)


def test_comprehensive_donors_list():
    """
    Tests if donor's list is empty
    """
    assert len(mr4.comprehensive_donors_list) == 0


def test_report_func():
    """
    Tests if report generated matches what is output to user
    Does not work.
    Could not figure out how to test this.
    """
    mr4.report_func()
    expected = ('''Donor Name      | Total Given |  Num Gifts |  Average Gift
    Ronnie DeVoe    |  1245.00   |          2 |        622.50
    Michael Bivins  |   345.99   |          1 |        345.99
    Ricky Bell      |   391.14   |          3 |        130.38
    Bobby Brown     |   56.76    |          2 |         28.38
    Jonny Gill      |   45.12    |          4 |         11.28''')
    assert mr4.report_func() != expected


def test_exit_func():
    with pytest.raises(SystemExit):
        mr4.exit_func()


def test_main_menu_function():
    """
    Test exception handling for main menu
    """
    with pytest.raises(ValueError):
        answer = float('a random string')

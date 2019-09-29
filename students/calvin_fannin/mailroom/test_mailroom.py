import pytest
import mailroom as mr
import os


def test_search_fullname():
    """ Search for fullname in dataset """
    donorname = "Jeff Kingbird"
    assert mr.search_fullname(donorname) == True


def test_get_next_key():
    expected = 7
    assert mr.get_next_key() == expected


def test_search_fullname_not_found():
    """ Search for fullname NOT in dataset """
    donorname = "JeffY Kingbird"
    assert mr.search_fullname(donorname) == False


def test_get_name_index():
    """ Test getting the index of given name """
    donorname = "Jeff Kingbird"
    expected = 2
    assert mr.get_name_index(donorname) == expected


def test_create_summary():
    """ Test the create summary output """
    expected = [['John Kestrel', 653788.49, 3, 217929.49666666667],
    ['Jeff Kingbird', 877.33, 1, 877.33],
    ['Paul Jacobin', 708.4200000000001, 3, 236.14000000000001],
    ['Mark Tanager', 16396.1, 3, 5465.366666666666],
    ['Anna Hummingbird', 7650.0, 3, 2550.0],
    ['Calvin Fannin', 645.0, 1, 645.0]]
    assert mr.create_summary() == expected


def test_add_donation_new_donor():
    """ Test adding a donation to new donor """
    newdonor = "Vera Fannin"
    amount = 745.0
    expected = {'name':'Vera Fannin', 'amount':[745.0]}
    newIndexdonor = 7
    mr.add_donation_new_donor(newdonor,amount)
    assert mr.donations[newIndexdonor] == expected


def test_add_donation_existing():
    """ Test adding a donation to existing donor """
    amount = 745.0
    expected = {'name':'Calvin Fannin', 'amount':[645.0, 745.0]}
    indexdonor = 6
    mr.add_donation(indexdonor,amount)
    assert mr.donations[indexdonor] == expected


def test_files_exist():
    """ Test that file was created """
    for afile in mr.write_letters_all_donors():
        assert os.path.isfile(afile)


def test_if_file_isempty():
    """ Test file has some contents """
    for afile in mr.write_letters_all_donors():
        assert os.stat(afile).st_size > 0


def test_create_email():
    """ Test output of Create email"""
    expected = "\n".join (("Hi Calvin Fannin",
         "",
         "Thank you for your generous donations of 145.55.",
         "",
         "Respectfully,",
         "Hydro Flask"))
    assert mr.create_email('Calvin Fannin', 145.55) == expected

def test_exit():
    """ Test that it exits the system """
    with pytest.raises(SystemExit):
        mr.quit_program()


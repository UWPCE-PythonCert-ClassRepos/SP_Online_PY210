#!/usr/bin/env python3
import pytest
import donor_models as dm
import os
import cli_main as cli

# utility function for testing
def create_data():
    #Sample data
    names = [("Calvin","Fleming"), ("Mary", "Andrews")]
    donorslist = [dm.Donor(*name,1200.00) for name in names]
    dc = dm.DonorCollection(donorslist)
    return dc


def test_create_donor():
    """ Test the creation of a donor """
    value  = 745.0
    mydonor = dm.Donor("Calvin", "Fannin",value)
    assert mydonor.fullname == "Calvin Fannin"
    assert mydonor.fname == "Calvin"
    assert mydonor.lname == "Fannin"
    assert sum(mydonor.donations) == 745.0


def test_modify_donor():
    """ Test modifing of a donor """
    value  = 745.0
    mydonor = dm.Donor("Vicky", "Kego",value)
    mydonor.fname = "Vicki"
    mydonor.lname = "Fannin"
    assert mydonor.fullname == "Vicki Fannin"


def test_add_donation():
    """ Test adding a donation to a donor """
    value  = 500.0
    mydonor = dm.Donor("Vicky", "Kego",value)
    mydonor.add_donation(500.0)
    assert sum(mydonor.donations) == 1000
    assert len(mydonor.donations) == 2


def test_create_empty_donorcollection():
    """ Test the creation of a empty donor collection """
    dc = dm.DonorCollection()
    assert dc.list_donors() == []


def test_add_donors():
    """ Test the adding of a donor to the donor collection """
    dc = create_data()
    value  = 745.0
    mydonor = dm.Donor("Bera", "Youkul",value)
    dc.add_donor(mydonor)
    assert len(dc.donors) == 3


def test_create_summary():
    """ Test the create summary output for reports"""
    dc = create_data()
    expected = [['Calvin Fleming', 1200.0, 1, 1200.0], ['Mary Andrews', 1200.0, 1, 1200.0]]
    assert dc.create_summary() == expected



def test_add_donation_by_name():
    """ Test the creation of a donor """
    dc = create_data()
    dc.add_donation('Mary Andrews',1200.00)
    assert dc.donors[1].fullname == 'Mary Andrews'
    assert sum(dc.donors[1].donations) == 2400.00


def test_negative_donation():
    """ Test the input of a negative donation """
    with pytest.raises(ValueError):
        value  = -745.0
        mydonor = dm.Donor("Bera", "Youkul",value)


def test_non_numeric_donation():
    """ Test the input of non numeric donation"""
    with pytest.raises(TypeError):
        value  = 'ten dollars'
        mydonor = dm.Donor("Bera", "Youkul",value)


def test_search_full_name():
    """ Test the search of a donor by name """
    dc = create_data()
    mydonor = dm.Donor("    Spacey", "MCFly   ",500.00)
    dc.add_donor(mydonor)
    lookupname = 'Mary Andrews'
    badname = 'Pinky Blandy'
    name2= '     Spacey MCFly              '
    result = dc.search_fullname(lookupname)
    falseresult = dc.search_fullname(badname)
    spaces = dc.search_fullname(name2)
    assert result == True
    assert falseresult == False
    assert spaces == True


def test_files_exist():
    """ Test that file was created """
    for afile in cli.write_letters_all_donors():
        assert os.path.isfile(afile)


def test_if_file_isempty():
    """ Test file has some contents """
    for afile in cli.write_letters_all_donors():
        assert os.stat(afile).st_size > 0


def test_create_email():
    """ Test output of Create email"""
    expected = "\n".join (("Hi Calvin Fannin",
         "",
         "Thank you for your generous donations of 145.55.",
         "",
         "Respectfully,",
         "Hydro Flask"))
    assert cli.create_email('Calvin Fannin', 145.55) == expected

def test_exit():
    """ Test that it exits the system """
    with pytest.raises(SystemExit):
        cli.quit_program()
















#!/usr/bin/env python3

from mailroom4 import * 

# data 

donor = ('Nathan Explosion', [39595, 35081, 93295])

# donor dict data

donor_dict = {
    "Nathan Explosion": [39595, 35081, 93295]
}

# testing appending and adding the donor dictionary

def test_donor_dict_update_append():
    donor_dict_update(donor="Nathan Explosion", donation_amount="1234", donor_dict=donor_dict)
    expected = {"Nathan Explosion": [39595, 35081, 93295, 1234]}
    assert donor_dict == expected

def test_donor_dict_update_add():
    donor_dict_update(donor="Pickles", donation_amount="1234", new_donor=True, donor_dict=donor_dict)
    expected = {"Nathan Explosion": [39595, 35081, 93295, 1234], "Pickles": [1234]}
    assert donor_dict == expected

def test_thank_you_letter():
    expected = "Dear Pickles,\n\nThank you for your generous donation of $40! As you certianly know, kittens\nand metal are awesome and your donation will insure that others will be able\nto enjoy kittens and metal.\n\nThank you,\n\nKitten and Metal Charity\n\n"
    assert thank_you_letter(["Pickles", 40]) == expected

def test_table_header():
    expected = 'Donor Name               |Total Given |Num Gifts |Average Gift\n--------------------------------------------------------------'
    assert table_header() == expected

def test_row_formatter():
    row = ["Pickles", 45434, 3, 45434/3]
    expected = 'Pickles                  |$   45434.00|         3|$   15144.67'
    assert row_formatter(row) == expected

def test_donor_info_report(): 
    expected = ['Nathan Explosion', 167971, 3, 167971/3]
    assert donor_info(donor) == expected

def test_donor_info_letters():
    expected = ['Nathan Explosion', 3, 167971]
    assert donor_info(donor, letters=True) == expected

def test_thank_you_letter_all_donors():
    expected = "Dear Nathan Explosion,\n\n\tYou have made 3 donations to the kittens and metal charity totaling $167971.\n\nThank you,\n\n\tKitten and Metal Charity"
    assert thank_you_letter(['Nathan Explosion', 3, 167971], all_donors=True) == expected

def test_write_to_file():
    wd = os.getcwd()
    os.mkdir(wd + "/" + "test_dir")
    donor_letter = "This is test text!"
    write_to_file(donor_letter, "test_dir", "donor")
    f = open(wd + "/" + "test_dir" + "/" + "donor.txt", "r")
    new_file = f.read()
    assert new_file == donor_letter

def remove_directy():
    wd = os.getcwd()
    os.remove(wd + "/" + "test_dir")

if __name__ == '__main__':
    test_donor_dict_update_append()
    test_donor_dict_update_add()
    test_thank_you_letter()
    test_table_header()
    test_row_formatter()
    test_donor_info_report()
    test_thank_you_letter_all_donors()
    test_write_to_file()
    remove_directy()
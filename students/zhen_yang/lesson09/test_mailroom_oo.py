# test_mailroom_oo.py
# This module contains all the test functions for testing all the logic code
# written in the module donor_models.py

from donor_models import Donor, DonorCollection
from cli_main import *

####################
# test class 'Donor'
####################
def test_Donor_init():
    donor = Donor('Zhen', 'Yang', 230)
    assert donor.first_name == 'Zhen'
    assert donor.last_name == 'Yang'
    assert donor.donation[0] == 230

def test_add_donation_amount():
    donor = Donor('Zhen', 'Yang', 230)
    donor.add_donation_amount(100)
    assert donor._first_name == 'Zhen'
    assert donor._last_name == 'Yang'
    assert donor.donation[1] == 100
    assert donor.total_amount == 330
    assert donor.total_gifts == 2

# generate_thankyou_letter() return an output string
def test_generate_thankyou_letter():
    donor = Donor('Zhen', 'Yang', 230)
    donor.add_donation_amount(100)
    my_str = donor.generate_thankyou_letter().strip()
    assert my_str.startswith('Dear')
    assert my_str.endswith('Zhen')
    assert 'Yang' in my_str # test last name
    assert '100' in my_str # test total donation

# create example donor database.
donor_1 = Donor('Adan', 'William', 100.75)
donor_1.add_donation_amount(1200)
donor_1.add_donation_amount(3200.45)
donor_2 = Donor('Peter', 'Chiykowski', 25.25)
donor_2.add_donation_amount(4340.25)
donor_3 = Donor('Sara', 'Gogo', 650)
donor_4 = Donor('Jason', 'Zhang', 150.00)
donor_4.add_donation_amount(35.50)
donor_4.add_donation_amount(80.75)
donor_5 = Donor('Zooe', 'Bezos', 10)
donor_5.add_donation_amount(20)

donors_db = DonorCollection() # the donor data base
donors_db.update_donors_db(donor_1)
donors_db.update_donors_db(donor_2)
donors_db.update_donors_db(donor_3)
donors_db.update_donors_db(donor_4)
donors_db.update_donors_db(donor_5)

# test send thank you letter to each donor.
def test_send_letters():
    donor_list = []
    sorted_list = donors_db.sort_donors_db()
    for donor in sorted_list:
        my_str = donor.send_letters().strip()
        donor_list.append(my_str)
    my_str = ''.join(donor_list)
    assert my_str.startswith('Dear')
    assert my_str.endswith('Zhen')
    assert 'Adan William' in my_str
    assert 'Peter Chiykowski' in my_str
    assert 'Sara Gogo' in my_str
    assert 'Jason Zhang' in my_str
    assert 'Zooe Bezos' in my_str

###############################
# test class 'DonorCollection'
###############################
def test_update_donors_db():
    donor_1 = Donor('Adan', 'William', 100.75)
    donor_1.add_donation_amount(1200)
    donor_1.add_donation_amount(3200.45)
    donor_2 = Donor('Peter', 'Chiykowski', 25.25)
    donor_2.add_donation_amount(4340.25)
    donor_3 = Donor('Sara', 'Gogo', 650)
    my_donor_list = DonorCollection() # the donor data base
    # test adding new donors to the data base
    my_donor_list.update_donors_db(donor_1)
    my_donor_list.update_donors_db(donor_2)
    my_donor_list.update_donors_db(donor_3)
    assert len(my_donor_list.donorList) == 3 # test total number of donors
    assert my_donor_list.donorList[0].first_name == 'Adan'
    assert my_donor_list.donorList[0].last_name == 'William'
    assert my_donor_list.donorList[0].donation[1] == 1200
    assert my_donor_list.donorList[1].first_name == 'Peter'
    assert my_donor_list.donorList[1].last_name == 'Chiykowski'
    assert my_donor_list.donorList[1].donation[1] == 4340.25
    assert my_donor_list.donorList[2].first_name == 'Sara'
    assert my_donor_list.donorList[2].last_name == 'Gogo'
    assert my_donor_list.donorList[2].donation[0] == 650
    # test adding donation to existing donor
    donor_new = Donor('Sara', 'Gogo', 100)
    my_donor_list.update_donors_db(donor_new)
    assert len(my_donor_list.donorList) == 3 # still three donors
    assert my_donor_list.donorList[2].first_name == 'Sara'
    assert my_donor_list.donorList[2].last_name == 'Gogo'
    assert my_donor_list.donorList[2].total_gifts == 2 # total gifts changed
    assert my_donor_list.donorList[2].total_amount == 750 # tot amount changed


# sort the donors based on their total donation, then first name, then last name
def test_sort_donors_db():# using above 'donors_db' data base
    sorted_list = donors_db.sort_donors_db()
    assert sorted_list[0].last_name == 'Bezos'
    assert sorted_list[1].last_name == 'Zhang'
    assert sorted_list[2].last_name == 'Gogo'
    assert sorted_list[3].last_name == 'Chiykowski'
    assert sorted_list[4].last_name == 'William'


# create_report() returns a long string
def test_create_report_tile_content():# using above 'donors_db' data base
    # test the title of report
    title = donors_db.create_report_title()
    assert 'Donor Name' in title
    assert 'Total Amount' in title
    assert 'Num Gifts' in title
    assert 'Average Amount' in title
    # test the content of report
    content = donors_db.create_report_content()
    assert content.startswith('Zooe Bezos')
    # make sure the sorted order based on total donation is corrected
    assert content.index("Zooe Bezos") < content.index("Jason Zhang")
    assert content.index("Jason Zhang") < content.index("Sara Gogo")
    assert content.index("Sara Gogo") < content.index("Peter Chiykowski")
    assert content.index("Peter Chiykowski") < content.index("Adan William")


###############################
# test functions in cli_main.py
###############################
def test_valid_input():
    # test validating the program option
    assert valid_input(8, 1) == -1# invalid program option '8'
    # test validating the donotion amount
    assert valid_input(-12.00, 3) == -1 # invalid donation amount

def test_generate_output_filename():
    sorted_list = donors_db.sort_donors_db()
    for donor in donors_db._donorList:
        file_name = generate_output_filename(donor)
        assert os.path.isfile(file_name)

def test_creat_html_report():
    content = create_html_report().strip()
    assert content.startswith('<!DOCTYPE html>')
    assert content.endswith('</html>')
    assert content.index("<head") < content.index("<body")

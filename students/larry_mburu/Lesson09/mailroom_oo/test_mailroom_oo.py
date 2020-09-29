from donor import Donor
from donor_collection import DonorDb
import os

"""
This module is used to unit-test the mailroom program specifically, the donor.py module
and the donor_collection.py module. 
"""

####
#section 1 - Test Donor Class and functions
####
def test_donor_init():
    """
    Test the initialization of the Donor Class
    """

    donor = Donor()
    assert isinstance(donor, Donor)
    donor.fname = 'Erick'
    assert donor.fname == 'Erick'
    donor.lname = 'Smith'
    assert donor.lname == 'Smith'

def test_add_donation(): 
    """
    Test addition of a donation amount to the 
    donor object, using the add_donation() method
    in the Donor class
    """

    donor = Donor() 
    donor.add_donation(100)
    assert 100 in donor.donation_history

def test_letter(): 
    """
    Test the a single formatted letter to an
    individual donor, in the Donor class, 
    letter() method.
    """

    donor = Donor()
    donor.fname = 'Erick'
    donor.lname = 'Smith'
    donor.add_donation(100)

    expected_template = f"""Dear {donor.fname + ' ' + donor.lname},
        Thank you for your kind donation of ${donor.donation_history[-1]}.

        It will be put to very good use.

        Sincerely,

        - The Cloud Squad"""

    assert expected_template == donor.letter()

def test_thank_you(): 
    """
    Test thank_you function, in Donor class
    that sends thank you email to donor for donation 
    """

    donor = Donor()
    donor.fname = 'Erick'
    donor.lname = 'Smith'
    amount = 100
    donor.add_donation(amount)
    email = donor.thank_you_email()
    assert email == f"Thank you {donor.fname} {donor.lname} for your generous donation of ${amount:.2f} dollars"

####### 
# Section 2 - Test Donor Collection 
#######

def test_db_init():
    """
    Test the initialization of the Donor Database
    __init__() method in the DonorDb class
    """

    db = DonorDb()
    assert isinstance(db, DonorDb)
    assert isinstance(db.database, dict)

def test_add_db_sample(): 
    """
    Test the initialization of sample data to the database
    in the DonorDb class, add_db_sample() method
    """

    db = DonorDb() 
    db.add_db_sample()
    donors = list(db.database)
    assert donors == ['William Gates', 'Mark Zuckerberg', 'Jeff Bezos', 'Paul Allen', 'Bill Gates'] 

def test_add_donor(): 
    """
    Test the adding of a donor object to the DonorDb, 
    via the add_donor() method in the DonorDb class
    """

    donor = Donor()
    donor.fname = 'Erick'
    donor.lname = 'Smith'
    donor.add_donation(100)

    db = DonorDb() 
    db.add_donor(donor)
    key = donor.fname + ' ' + donor.lname
    assert key in db.database

def test_search(): 
    """
    Test the searching of a donor in the DonorDb
    class, search() method
    """

    db = DonorDb()
    donor = Donor()
    donor.fname = 'Bill'
    donor.lname = 'Gates'
    isFound = db.search(donor)
    assert isFound is not None
    assert isinstance(isFound, Donor)
    
def test_list_donors(): 
    """
    Test the list of donors in the DonorDb class, 
    list_donors() method
    """

    db = DonorDb() 
    donor_list = db.list_donors()
    assert donor_list == ['William Gates', 'Mark Zuckerberg', 'Jeff Bezos', 'Paul Allen', 'Bill Gates'] 

def test_send_letters(): 
    """
    Test the sending of letters to all donors in the
    DonorDb class, send_letters() method
    """

    db = DonorDb()
    db.send_letters()
    test_file = 'William_Gates.txt'
    assert os.path.isfile(test_file)

def test_statistics(): 
    """
    Test statistics() method in the DonorDb class
    """

    db = DonorDb() 
    summary = db.statistics()
    assert isinstance(summary, list)
    assert isinstance(summary[0], tuple)
    assert isinstance(summary[0][0], str)
    assert isinstance(summary[0][1], float)
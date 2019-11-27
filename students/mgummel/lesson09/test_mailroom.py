#! /usr/bin/env python3
from donor_models import *
import pytest, os


def test_donor_init():
    d1 = Donor("Paul Allen", 2343.99)
    d2 = Donor("Jeff Bezos", 423.10)
    d3 = Donor("Kanye West", 0.01)

    # Test that _full_name gets set properly
    assert d1._full_name == "Paul Allen"
    assert d2._full_name == "Jeff Bezos"
    assert d3._full_name == "Kanye West"

    # Test that the _donation list gets set properly
    assert 2343.99 in d1._donations
    assert 423.10 in d2._donations
    assert 0.01 in d3._donations


def test_average():
    donor1 = Donor("William Gates, III", 653772.32)
    donor2 = Donor("Paul Allen", 663.23)
    assert donor1.avg_donation == 653772.32
    assert donor2.avg_donation == 663.23

    donor1.add_donation(10.00)
    assert donor1.avg_donation == 653782.32 / 2
    assert donor2.avg_donation == 663.23

    donor1.add_donation(532.79)
    donor2.add_donation(368.45)
    assert donor1.avg_donation == 654315.11 / 3
    assert donor2.avg_donation == 1031.68 / 2

def test_total_donation():
    d1 = Donor("Mark Zuckerberg", 1663.23)
    d2 = Donor("Marc Benioff", 45023.15)
    
    assert d1.total_donation == 1663.23
    assert d2.total_donation == 45023.15

    d1.add_donation(100.00)
    d2.add_donation(55.00)
    assert d1.total_donation == 1763.23
    assert d2.total_donation == 45078.15

    d2.add_donation(100.00)
    assert d1.total_donation == 1763.23
    assert d2.total_donation == 45178.15

def test_num_of_donations():
    d1 = Donor("50 Cent", 2343.99)
    d2 = Donor("Meek Mills", 423.10)
    d3 = Donor("Kanye West", 0.01)

    assert d1.num_of_donations == 1
    assert d2.num_of_donations == 1
    assert d3.num_of_donations == 1

    d1.add_donation(43.99)
    d3.add_donation(432.10)
    assert d1.num_of_donations == 2
    assert d2.num_of_donations == 1
    assert d3.num_of_donations == 2

    d3.add_donation(42.99)
    assert d1.num_of_donations == 2
    assert d2.num_of_donations == 1
    assert d3.num_of_donations == 3

def test_last_donation():
    d1 = Donor("50 Cent", 2343.99)
    d2 = Donor("Meek Mills", 423.10)
    d3 = Donor("Kanye West", 0.01)

    assert d1.last_donation == 2343.99
    assert d2.last_donation == 423.10
    assert d3.last_donation == 0.01

    d1.add_donation(43.99)
    d3.add_donation(432.10)
    assert d1.last_donation == 43.99
    assert d2.last_donation == 423.10
    assert d3.last_donation == 432.10

    d3.add_donation(42.99)
    assert d1.last_donation == 43.99
    assert d2.last_donation == 423.10
    assert d3.last_donation == 42.99

def test_str():
    d1 = Donor("Kris Smith", 23.43)
    assert ("Kris Smith") in d1.__str__()
    assert ("23.43") in d1.__str__()
    assert ("It will be put to very good use.") in d1.__str__()

    d1.add_donation(417.56)
    assert ("Kris Smith") in d1.__str__()
    assert ("417.56") in d1.__str__()
    assert ("It will be put to very good use.") in d1.__str__()

def test_add_donation():
    d1 = Donor("Kris Smith", 23.43)
    d2 = Donor("Kris Smith Jr.", 42.23)

    assert 23.43 in d1._donations
    assert 42.23 in d2._donations

    d1.add_donation(123456.78)
    assert (123456.78) in d1._donations

    d1.add_donation(987654.23)
    d2.add_donation(7894.76)
    assert (7894.76) in d2._donations
    assert (987654.23) in d1._donations

def test_filename():
   d1 = Donor("Kris Smith II", 23.43)
   d2 = Donor("Matt Gummel, IV", 100000.00)

   assert d1.filename == "Kris_Smith_II.txt"
   assert d2.filename == "Matt_Gummel_IV.txt"

def test_data():
    d1 = Donor("50 Cent", 2343.99)
    d2 = Donor("Meek Mills", 423.10)
    d3 = Donor("Kanye West", 0.01)
    
    # Test initial data to return for report
    assert d1.data == ("50 Cent", 2343.99, 1, 2343.99)
    assert d2.data == ("Meek Mills", 423.10, 1, 423.10)
    assert d3.data == ("Kanye West", 0.01, 1, 0.01)

    # Add some donations and verify data has changed correctly
    d1.add_donation(0.01)
    d2.add_donation(0.90)
    d1.add_donation(2.00)
    assert d1.data == ("50 Cent", 2346.00, 3, 782.00)
    assert d2.data == ("Meek Mills", 424.00, 2, 212.00)
    assert d3.data == ("Kanye West", 0.01, 1, 0.01)


def test_dc_init():
    Paul_Allen = Donor("Paul Allen", 2343.99)
    Jeff_Bezos = Donor("Jeff Bezos", 423.10)
    dc1 = DonorCollection(Paul_Allen, Jeff_Bezos)
    
    assert Paul_Allen in dc1.donor_list
    assert Jeff_Bezos in dc1.donor_list


def test_add_donor():
    Carmelo_Anthony = Donor("Carmelo Anthony", 10.07)
    Michael_Jordan = Donor("Michael Jordan", 598.71)
    Kevin_Durrant = Donor("Kevin Durrant", 953.48)
    Paul_Pierce = Donor("Paul Pierce", 12.45)

    #Initialize Donor Collection
    dc1 = DonorCollection(Carmelo_Anthony, Michael_Jordan)
    dc1.add_donor(Kevin_Durrant)
    dc1.add_donor(Paul_Pierce)

    # Test that original member exists as well as the donors that were
    # added to the collection
    assert Carmelo_Anthony in dc1.donor_list
    assert Kevin_Durrant in dc1.donor_list
    assert Paul_Pierce in dc1.donor_list



def test_generate_names():
    Michael_Jordan = Donor("Michael Jordan", 598.71)
    Kevin_Durrant = Donor("Kevin Durrant", 953.48)
    Carmelo_Anthony = Donor("Carmelo Anthony", 10.07)
    dc1 = DonorCollection(Michael_Jordan, Kevin_Durrant)
    full_name_list = ["Michael Jordan", "Kevin Durrant"]
    names1 = ('\n').join(full_name_list)

    full_name_list2 = ["Michael Jordan", "Kevin Durrant", "Carmelo Anthony"]
    names2 = ('\n').join(full_name_list2)
    assert names1 == dc1.generate_list_of_names()

    dc1.add_donor(Carmelo_Anthony)
    assert names2 == dc1.generate_list_of_names()




def test_find_donor():
    Michael_Jordan = Donor("Michael Jordan", 598.71)
    Kevin_Durrant = Donor("Kevin Durrant", 953.48)
    Carmelo_Anthony = Donor("Carmelo Anthony", 10.07)
    dc1 = DonorCollection(Michael_Jordan, Kevin_Durrant, Carmelo_Anthony)

    assert dc1.find_donor("Michael Jordan") == Michael_Jordan
    assert dc1.find_donor("Paul Pierce") == None
    assert dc1.find_donor("Matt Gummel") == None
    assert dc1.find_donor("Carmelo Anthony") == Carmelo_Anthony
    assert dc1.find_donor("Bill Gates") == None 


def test_report_data():
    Michael_Jordan = Donor("Michael Jordan", 598.71)
    Kevin_Durrant = Donor("Kevin Durrant", 953.48)
    Carmelo_Anthony = Donor("Carmelo Anthony", 10.07)
    dc1 = DonorCollection(Michael_Jordan, Kevin_Durrant, Carmelo_Anthony)

    report_list = dc1.report_data()
    
    assert type(report_list[0]) == tuple
    assert len(report_list) == 3
    assert Michael_Jordan._full_name in report_list[0]
    assert Michael_Jordan.avg_donation in report_list[0]
    assert Michael_Jordan.total_donation in report_list[0]
    assert Michael_Jordan.num_of_donations in report_list[0]
    assert Kevin_Durrant.total_donation in report_list[1]
    assert Kevin_Durrant._full_name in report_list[1]
    assert Carmelo_Anthony._full_name in report_list[2]



def test_send_letters():
    Michael_Jordan = Donor("Michael Jordan", 598.71)
    Kevin_Durrant = Donor("Kevin Durrant", 953.48)
    Carmelo_Anthony = Donor("Carmelo Anthony", 10.07)
    dc1 = DonorCollection(Michael_Jordan, Kevin_Durrant, Carmelo_Anthony)
    
    dc1.letters_to_send('.')
    # Verify all leters are present 
    assert os.path.exists('./Michael_Jordan.txt')
    assert os.path.exists('./Kevin_Durrant.txt')
    assert os.path.exists('./Carmelo_Anthony.txt')

    dc1.add_donor(Donor("Matt Gummel", 123233.99))
    dc1.letters_to_send('.')

    # Verfiy that  new file exists
    assert os.path.exists('./Matt_Gummel.txt')

    # Test file content
    with open('./Michael_Jordan.txt', 'r', encoding='utf-8') as donor_email_file:
        email_file = donor_email_file.read()
    assert ("Michael Jordan") in email_file
    assert ("598.71") in email_file
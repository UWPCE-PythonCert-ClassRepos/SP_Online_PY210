from mailroom4 import *
import os, fnmatch

def create_test_dict():
    return {"Ben Wyatt": [1663.23, 4300.87, 10432.0],
              "Ron Swanson": [100000],
              "April Ludgate": [10, 1.52, 0.25],
              "Ann Perkins": [100, 100],
              "Leslie Knope": [1663.23, 4300.87, 1432.0]}

#---------TESTING FUNCTION 1: SEND THANK YOU---------#
def tester_add_donor():
    plus_donor = {"full_name": 'Thomas Montgomery Haverford', "first_name": 'Thomas',
                 "amount": 10}
    test_dict = create_test_dict()
    new_donor = add_donation(plus_donor, test_dict)
    assert new_donor["Thomas Montgomery Haverford"] == [10]

def test_add_donation():
    plus_donation = {"full_name": 'Ron Swanson', "first_name": 'Ron', "amount": 10}
    test_dict = create_test_dict()
    new_donation = add_donation(plus_donation, test_dict)
    assert new_donation["Ron Swanson"] == [100000, 10]

# ---------TESTING FUNCTION 2: GENERATE REPORT---------#
def test_sum_donors():
    test_dict = create_test_dict()
    donor_rep_test = sum_donors(test_dict)
    assert donor_rep_test[0] == ["Ron Swanson", 100000, 1, 100000]
    assert donor_rep_test[1] == ["Ben Wyatt", 16396.1, 3, 16396.1/3]
    assert donor_rep_test[2] == ["Leslie Knope", 7396.1, 3, 7396.1/3]
    assert donor_rep_test[3] == ["Ann Perkins", 200, 2, 100]
    assert donor_rep_test[4] == ["April Ludgate", 11.77, 3, 11.77/3]

# ---------TESTING FUNCTION 3: THANK YOU DUMP---------#
def test_file_save():
    test_dict = create_test_dict()
    td = os.getcwdb()
    for person, donations in test_dict.items():
        save_file(person, donations, td)

    listOfFiles = os.listdir('.')
    filenames = {"Leslie_Knope.txt", "April_Ludgate.txt", "Ben_Wyatt.txt", "Ron_Swanson.txt", "Ann_Perkins.txt"}
    for name in filenames:
        os.remove(name)
    assert filenames.issubset(listOfFiles) is True
    assert os.getcwdb() == td

# ---------TESTING FUNCTION 4: EXIT---------#
def test_exit():
    test_dict = create_test_dict()
    assert save_exit(test_dict) is False

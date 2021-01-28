from mailroom5 import *
import os, fnmatch

def create_test_dict():
    ds = DonorCollection({})
    ds.add_donor(Donor("Ben Wyatt", [1663.23, 4300.87, 10432.0]))
    ds.add_donor(Donor("Ron Swanson", [100000]))
    ds.add_donor(Donor("April Ludgate", [10, 1.52, 0.25]))
    ds.add_donor(Donor("Ann Perkins", [100, 100]))
    ds.add_donor(Donor("Leslie Knope", [1663.23, 4300.87, 1432.0]))
    return ds

#---------TESTING FUNCTION 1: SEND THANK YOU---------#
def tester_add_donor():
    Tom = Donor('Thomas montgomery haverford', [10])
    print(Tom.name)
    test_ds = create_test_dict()
    test_ds.add_donor(Tom)
    print(test_ds.donors.keys())
    assert test_ds.donors["Thomas Montgomery Haverford"].donations == [10]


def test_add_donation():
    test_ds = create_test_dict()
    test_ds.donors['Ron Swanson'].add_donation(10)
    print(test_ds.donors.keys())
    print(test_ds.donors["Ron Swanson"].donations)
    assert test_ds.donors["Ron Swanson"].donations == [100000, 10]


def test_thank_you():
    test_ds = create_test_dict()
    thank_you_print = test_ds.donors['Ron Swanson'].generate_thank_you()
    print(thank_you_print)
    assert thank_you_print == f"Dear Ron,\n\tThank you for your generous donation of $100000.00! " \
                          "Each dollar you donate ends up providing endless value for our town. \n\t" \
                          "We appreciate your gift and hope our partnership extends well into the future. \n" \
                          "Regards, \n\tThe Pawnee Restoration Fund"

def test_check_donor():
    test_ds = create_test_dict()
    assert test_ds.check_donor("Ron Swanson") is True
    assert test_ds.check_donor("Tammy Two") is False

# ---------TESTING FUNCTION 2: GENERATE REPORT---------#
def test_gen_report():
    test_ds = create_test_dict()
    assert test_ds.donors["Ron Swanson"].donor_report == ["Ron Swanson", 100000, 1, 100000]


def test_sum_donors():
    test_ds = create_test_dict()
    print(test_ds.printed_report[1])
    print(test_ds.printed_report[2])
    print(test_ds.printed_report[3])
    print(test_ds.printed_report[4])
    print(test_ds.printed_report[5])

    assert test_ds.printed_report[1] == f"{'Ron Swanson': <20}${float(100000):^20,.2f}{'1' : ^20}${'100000.00' : >20}"
    assert test_ds.printed_report[2] == f"{'Ben Wyatt': <20}${float(16396.1):^20,.2f}{'3' : ^20}${'5465.37' : >20}"
    assert test_ds.printed_report[3] == f"{'Leslie Knope': <20}${float(7396.1):^20,.2f}{'3' : ^20}${'2465.37' : >20}"
    assert test_ds.printed_report[4] == f"{'Ann Perkins': <20}${float(200):^20,.2f}{'2' : ^20}${'100.00' : >20}"
    assert test_ds.printed_report[5] == f"{'April Ludgate': <20}${float(11.77):^20,.2f}{'3' : ^20}${'3.92' : >20}"

# ---------TESTING FUNCTION 3: THANK YOU DUMP---------#
def test_file_save():
    test_ds = create_test_dict()
    td = os.getcwdb()
    for name, donor in test_ds.donors.items():
        donor.save_file(td)

    listOfFiles = os.listdir('.')
    print(listOfFiles)
    filenames = {"Leslie_Knope.txt", "April_Ludgate.txt", "Ben_Wyatt.txt", "Ron_Swanson.txt", "Ann_Perkins.txt"}
    print(filenames)
    for name in filenames:
        os.remove(name)
    assert filenames.issubset(listOfFiles) is True
    assert os.getcwdb() == td

import pytest
from donor_models import DonorCollection
from donor_models import Donor

"""
Becky Larson 
Created 10/5/2020
Updated 10/11/2020
"""

#belarson: add tests for failures and complete passed tests

donors_data = {Donor("Cher", [1000.00, 245.00]),
               Donor("Drew Barrymore", [25000.00]),
               Donor("Charlie Brown", [25.00, 50.01, 100.00]),
               Donor("Jack Black", [256.00, 752.50, 10101.00]),
               Donor("Sam Smith", [5500.00, 24.00]),
               }


donor_list = ["Cher, 1000.00, 245.00",
               "Drew Barrymore, 25000.00",
               "Charlie Brown, 25.00, 50.01, 100.00",
               "Jack Black, 256.00, 752.50, 10101.00",
               "Sam Smith, 5500.00, 24.00"
               ]


""" don't run unless special test
def func_get_donor_collection_from_string():
    print("test__ func_get_donor_collection_from_string")
    donor_collection = [Donor.from_string(d) for d in donor_list]
    print(f'fgdcfs.... len(donor_collection) {len(donor_collection)}')
    return donor_collection


def func_get_donor_collection():
    print("test__ func_get_donor_collection")
    donor_collection = DonorCollection(donors_data)
    print(f'fgdc.... len(donor_collection) {len(donor_collection)}')
    return donor_collection


def test_func_get_donor_collection():
    test_collection = func_get_donor_collection()
    print(f'tgdc.... len(test_collection) {len(test_collection)}')
    assert len(test_collection) == 5
    for donor in check_donor_names:
       assert donor in donor_collection.donors


def test_func_get_donor_collection_from_string():
    test_collection = func_get_donor_collection_from_string()
    print(f'tgdcfs.... len(test_collection) {len(test_collection)}')
    assert len(test_collection) == 5
"""

""" Donor tests """
test_name_sam = "Sam Smith"
test_name_cher = "Cher"


def test_donor_init():
    test_name = test_name_sam
    test_donations = [1000.00, 245.00]
    donor = Donor(test_name, test_donations)

    assert donor.donor_name == test_name
    assert donor.donations == test_donations
    assert donor.first_name == "Sam"
    assert donor.last_name == "Smith"
    assert donor.num_donations == 2
    assert donor.total_donations == 1245.0
    assert donor.avg_donation == 622.5


def test_donor_no_last_name():
    test_name = test_name_cher
    test_donations = [1000.00, 245.00]
    donor = Donor(test_name, test_donations)

    assert donor.donor_name == test_name
    assert donor.donations == [1000.00, 245.00]
    assert donor.first_name == "Cher"
    assert donor.last_name == ""
    assert donor.num_donations == 2
    assert donor.total_donations == 1245.0
    assert donor.avg_donation == 622.5


def test_from_donor_name():
    test_name = test_name_sam
    donor = Donor.from_donor_name(test_name)
    assert donor.donor_name == test_name
    assert donor.donations == []


def test_add_donation():
    test_name = test_name_sam
    test_donations = [5500.00, 24.00, 24.00, 24.00, 24.00]
    donor = Donor(test_name, test_donations)
    donor.add_donation(150.50)
    print(f'.... donor.donations[-1] {donor.donations[-1]}')
    assert donor.donations[-1] == 150.50


def test_donations():
    pass 


def test_donor_name():
    pass 


def test_num_donations():
    test_name = test_name_sam
    test_donations = [5500.00, 24.00, 24.00, 24.00, 24.00, 24.00, 24.00, 24.00, 24.00]
    donor = Donor(test_name, test_donations)
    print(f'.... donor.num_donations {donor.num_donations}')
    assert donor.donor_name == test_name
    assert donor.num_donations == 9


def test_total_donations():
    test_name = test_name_cher
    test_donations = [1000.00, 245.00]
    donor = Donor(test_name, test_donations)
    print(f'.... donor.total_donations {donor.total_donations}')
    assert donor.donor_name == 'Cher'
    assert donor.total_donations == 1245.00


def test_avg_donation():
    test_name = test_name_cher
    test_donations = [1000.00, 200.00]
    donor = Donor(test_name, test_donations)
    print(f'.... donor.avg_donation {donor.avg_donation}')
    assert donor.donor_name == test_name
    assert donor.avg_donation == 600


def test_avg_donation_no_donations():
    test_name = test_name_sam
    test_donations = []
    donor = Donor(test_name, test_donations)
    assert donor.avg_donation == 0


def test_donor__len__():
    donor = Donor("Sam Smith", [5500.00, 24.00, 24.00, 24.00, 24.00])
    print(f'.... len(donor) {len(donor)}')
    assert len(donor) == 5


def test_format_ty():
    test_name = test_name_sam
    test_donations = [5500.00, 24.00, 250.00]
    donor = Donor(test_name, test_donations)
    test_thankd_you = donor.format_ty()
    print(f'tft.... len(donor) {len(donor)}')
    print(f'tft.... test_donations[-1]{ test_donations[-1]}')
    print(f'tft.... test_thankd_you {test_thankd_you}')
    assert len(donor) == len(test_donations)
    assert test_name in test_thankd_you
    assert str(test_donations[-1]) in test_thankd_you


def test_report_write_row():
    test_name = test_name_sam
    test_donations = [5500.00, 24.00, 250.00]
    donor = Donor(test_name, test_donations)
    test_row = donor.report_row()
    print(f'trwr.... test_row {test_row}')

    assert test_name in test_row
    assert "5,774.00" in test_row
    assert "   3" in test_row
    assert "1,924.67" in test_row


def test_donor__str__():
    test_name = test_name_sam
    test_donations = [500.00, 25.00, 34.00, 44.00, 84.00]
    donor = Donor(test_name, test_donations)

    print(f'.... str(donor) {str(donor)}')
    assert str(donor) == "Sam Smith,500.00,25.00,34.00,44.00,84.00"


def test_donor__lt__():
    donor = Donor("Sam Smith", [150.00, 100.00])
    donor2 = Donor("Cher", [50.00, 1200.00])
    assert donor < donor2
    assert donor2 > donor


def test_from_string():
    donor = Donor.from_string("Sam Smith,500.00,25.00,34.00,44.00,84.00")
    print(f'.... donor {donor}')
    assert donor.donor_name == "Sam Smith"
    assert donor.donations == [500.0,25.0,34.0,44.0,84.0]


def test_donor_repr():
    test_name = test_name_sam
    test_donations = [500.00, 25.00, 34.00, 44.00, 84.00]
    donor = Donor(test_name, test_donations)
    assert donor.__repr__() == f"Donor('{test_name}', {test_donations})"


def test_sort_key():
    pass


def test_sort_by_donations():
    pass


# data collection tests
# belarson -- add test to add donation
#------------------------------------------------------------------------
check_donor_names = ["Cher", "Drew Barrymore", "Charlie Brown",
                       "Jack Black","Sam Smith"]


def test_donor_collection__init():
    donor_collection = DonorCollection(donors_data)
    print(f'tidc.... len(donor_collection) {len(donor_collection)}')
    assert len(donor_collection) == 5
    for donor in check_donor_names:
       assert donor in donor_collection.donors


def test_donor_collection_list():
    donor_collection = DonorCollection(list(donors_data))
    for donor in check_donor_names:
        assert donor in donor_collection.donors


def test_donor_collection_tuple():
    donor_collection = DonorCollection(tuple(donors_data))
    for donor in check_donor_names:
        assert donor in donor_collection.donors


def test_dc__len__():
    donor_collection = DonorCollection(donors_data)
    print(f't__len__.... len(donor_collection) {len(donor_collection)}')
    assert len(donor_collection) == 5


def test_donors():
    donor_collection = DonorCollection(donors_data)
    donor_donors = donor_collection.donors
    print(f'td.... donor_donors --  {donor_donors}')
    for donor in check_donor_names:
        assert donor in donor_donors


def test_donor_collection_creation_no_donors():
    donor_collection = DonorCollection()
    assert donor_collection.donors == ()
    assert len(donor_collection.donors) == 0


def test_donor_collection_append():
    donor = Donor("Peter Pan", [5.00, 10.00, 15.00, 20.00, 25.00])
    donor_collection = DonorCollection(donors_data)

    donor_collection.append(donor)
    assert "Peter Pan" in donor_collection.donors


"""!!! update test results if data changes  """
donors_data_report = {Donor("Cher", [1000.00, 245.00]),
				   Donor("Drew Barrymore", [25000.00]),
				   Donor("Charlie Brown", [25.00, 50.01, 100.00]),
				   Donor("Jack Black", [256.00, 752.50, 10101.00]),
				   Donor("Sam Smith", [5500.00, 24.00]),
				   }


def test_donor_collection_report():
    header = ['Donor Name', '|', 'Total Given', '|', 'Num Gifts', '|', 'Average Gift']

    num_donations = ["1", "3", "2", "2", "3"]
    total_donations = ["25,000.00", "11,109.50", "5,524.00", "1,245.00", "175.01"]
    avg_donations = ["25,000.00",  "3,703.17", "2,762.00", "622.50", "58.34"]

    donor_collection = DonorCollection(donors_data_report)

    print(donor_collection.report())
    for col in header:
        assert col in donor_collection.report()
    for donor in check_donor_names:
        assert donor in donor_collection.report()
    for number in num_donations:
        assert number in donor_collection.report()
    for total in total_donations:
        assert total in donor_collection.report()
    for avg in avg_donations:
        assert avg in donor_collection.report()


def test_donor_collection_str():
    donor_collection = DonorCollection(donors_data)
    donor_str = donor_collection.__str__()
    print(f"tdcs_ donor_str  : {donor_str}")
    print(f"tdcs_ type donor_str  : {type(donor_str)}")
    test_val = "DonorCollection: "
    assert test_val in str(donor_str)

    test_val = "'Charlie Brown': Donor('Charlie Brown', [25.0, 50.01, 100.0])"
    assert test_val in str(donor_str)

    test_val = "'Cher': Donor('Cher', [1000.0, 245.0])"
    assert test_val in str(donor_str)

    test_val = "'Jack Black': Donor('Jack Black', [256.0, 752.5, 10101.0])"
    assert test_val in str(donor_str)

    test_val = "'Sam Smith': Donor('Sam Smith', [5500.0, 24.0])"
    assert test_val in str(donor_str)

    test_val = "'Drew Barrymore': Donor('Drew Barrymore', [25000.0])"
    assert test_val in str(donor_str)


def test_donor_collection_repr():
    donor_collection = DonorCollection(donors_data)
    
#    assert donor_collection.__repr__() == expected
    donor_repr = donor_collection.__repr__()
    print(f"tdcr_ donor_repr  : {donor_repr}")

    test_val = "DonorCollection("
    assert test_val in str(donor_repr)

    test_val = "'Charlie Brown': Donor('Charlie Brown', [25.0, 50.01, 100.0])"
    assert test_val in str(donor_repr)

    test_val = "'Cher': Donor('Cher', [1000.0, 245.0])"
    assert test_val in str(donor_repr)

    test_val = "'Jack Black': Donor('Jack Black', [256.0, 752.5, 10101.0])"
    assert test_val in str(donor_repr)

    test_val = "'Sam Smith': Donor('Sam Smith', [5500.0, 24.0])"
    assert test_val in str(donor_repr)

    test_val = "'Drew Barrymore': Donor('Drew Barrymore', [25000.0])"
    assert test_val in str(donor_repr)

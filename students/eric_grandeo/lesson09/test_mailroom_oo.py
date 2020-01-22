#tests for mailroom_oo.py

import pytest
from mailroom_oo import *

#test 1: creates class, get name
def test_donor():
    donor = Donor("Bill Gates", 500)
    assert donor.name == "Bill Gates"
    assert donor.donations == 500
    

#test 2: test get instance
def test_get_instance():
    donor = Donor("Bill Gates", [50, 100, 150] )
    assert {"Bill Gates": [50, 100, 150]} == donor.donor

#test 3: test adding a donation
def test_add_donation():
    donor = Donor("Bill Gates")
    donor.add_donation(500)
    assert donor.donations == [500]

#test 4: summing donations
def test_sum_donations():
    donor = Donor("Bill Gates", [50, 100, 150])
    assert donor.sum_donations == 300

#test 5: number of donations
def test_num_donations():
    donor = Donor("Bill Gates", [50, 100, 150])
    assert donor.num_donations == 3

#test 6: average donations
def test_avg_donations():
    donor = Donor("Bill Gates", [50, 100, 150])
    assert donor.avg_donations == 100

#test 7:thank you email
def test_thank_you():
    donor = Donor("Bill Gates", [50, 100, 150])
    
    test_result = """
        Dear {name},
        Thank you very much for the generous donation of ${donation:,.2f}
        It is very much appreciated.
        Respectfully,

        Eric G.
        """.format(name="Bill Gates", donation=150)

    assert donor.thank_you == test_result

#test 8: getting donor objects into donorcollections
def test_donorcollections():
    d = DonorCollection()
    d.add_donor("Bill Gates", [50, 100, 150])
    d.add_donor("Paul Allen", [150, 200, 250])
    assert ['Bill Gates', 'Paul Allen'] == d.donor_names
    assert {"Bill Gates": [50, 100, 150], "Paul Allen": [150, 200, 250]} == d.donor_dict

    

#test 9: updating existing donor
def test_update_donor():
    d = DonorCollection()
    d.add_donor("Bill Gates", [50, 100, 150])
    d.add_donor("Paul Allen", [150, 200, 250])
    #assert {"Bill Gates": [50, 100, 150], "Paul Allen": [150, 200, 250]} == d.donor_dict
    d.add_donor("Bill Gates", 500)
    assert {"Bill Gates": [50, 100, 150, 500], "Paul Allen": [150, 200, 250]} == d.donor_dict
    

#test 10: test create report data 
def test_report_data():
    d = DonorCollection()
    d.add_donor("Bill Gates", [50, 100, 150])
    d.add_donor("Paul Allen", [150, 200, 250, 700])
    d.add_donor("Mark Zuckerberg", [100, 300, 1000])
    d.add_donor("Jeff Bezos", [250, 750, 100, 1500])
    
    assert OrderedDict([('Jeff Bezos', [2600, 4, 650.0]),
                        ('Mark Zuckerberg', [1400, 3, 466.6666666666667]),
                        ('Paul Allen', [1300, 4, 325.0]),
                        ('Bill Gates', [300, 3, 100.0])]) == d.report_data


#test 11: generate report
def test_generate_report():
    d = DonorCollection()
    d.add_donor("Bill Gates", [50, 100, 150])
    d.add_donor("Paul Allen", [150, 200, 250, 700])
    d.add_donor("Mark Zuckerberg", [100, 300, 1000])
    d.add_donor("Jeff Bezos", [250, 750, 100, 1500])
    print(d.generate_report(d.report_data))
    #assert False


#Lesson 9 Test Donor Models

from oo_mailroom_donor_models import*

donor_db = {"Abraham Lincoln": [145674.32, 2],
            "Barack Obama": [3456324.11, 2], 
            "Charlie Brown":[453.67,1],
            "Doctor Who": [5600, 1],
            "Eve WallE":[2.22, 1]
                }

def test_init():
    d1 = Donor ("Eve WallE", [2.22,1])
    assert d1.donor_name == "Eve WallE"
    assert d1.donation_amount == 2.22
    assert d1.donation_number == 1

def test_thanks_one():
    assert Donor.thanks_one('Eve WallE', 5) == "Generating a Thank You Note:\n" \
    "Dear {}, thank you for your donation of ${:^10.2f}!".format('Eve WallE', 5)

#def test_list_donors():
 #   assert DonorCollection.list_donors() == dict.keys(['Abraham Lincoln','Barack Obama', 'Charlie Brown','Doctor Who', 'Eve WallE'])

def test_create_report_header():
    header = ('Donor Name', 'Total Donation', 'Number of Donations', 'Average Donation')
    line = "-" * 66
    expected =  "{:<24} | {:^13} | {:^11} | {:^11}\n" \
        "{}".format(*header, line)
    assert DonorCollection.create_report_header() == expected

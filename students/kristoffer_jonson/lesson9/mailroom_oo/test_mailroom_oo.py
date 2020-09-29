import pytest
from donor_models import DonorCollections
from donor_models import Donor
from cli_main import *
import os

#Test creation of donor object and math operations
def test_donor():
    d = Donor('Kris',[100,200])
    assert d.donor == 'Kris'
    assert d.donations == [100,200]
    assert d.num_donations == 2
    assert d.sum_donations == 300
    d.enter_donation(300)
    assert d.donations == [100,200,300]

#Setup function to create donor collection object with test donor
def setup_donor_collection():
    donorcollection = DonorCollections()
    donorcollection.add_donor("William", [653772.32, 12.17])
    return donorcollection

#Test donor collection for addition of donor with donations
def test_donor_collection():
    donorcollection = DonorCollections()
    assert donorcollection.donor_list == []
    donorcollection.add_donor("William", [653772.32, 12.17])
    assert donorcollection.donor_list[0].donor == 'William'
    assert donorcollection.donor_list[0].donations == [653772.32, 12.17]

#Test add donation to existing donor
def test_donor_collection_add_donation():
    donorcollection = setup_donor_collection()
    donorcollection.add_donation('William',100)
    assert donorcollection.donor_list[0].donations == [653772.32, 12.17, 100]

#Test addition of donor to donor class
def test_donor_collection_add_donor():
    donorcollection = setup_donor_collection()
    donorcollection.add_donor('Kris',[100,200])
    assert donorcollection.donor_list[0].donor == 'William'
    assert donorcollection.donor_list[0].donations == [653772.32, 12.17]
    assert donorcollection.donor_list[1].donor == 'Kris'
    assert donorcollection.donor_list[1].donations == [100,200]

#Test creation of list of donor names
def test_donor_collection_list_donors():
    donorcollection = setup_donor_collection()
    donorcollection.add_donor('Kris',[100,200])
    list_donors = donorcollection.list_donors()
    assert list_donors == 'William' + '\n' + 'Kris' + '\n'

#Test creation of thank you card with  donor and donation
def test_donor_collection_create_card():
    donorcollection = setup_donor_collection()
    card_text = donorcollection.create_card('Kris',100)
    assert 'Kris' in card_text
    assert '100' in card_text

#Test creation of report detailing donor name, donations and average donation
def test_donor_collection_create_report():
    donorcollection = setup_donor_collection()
    card_text = donorcollection.create_report()
    sample_card = 'Donor Name                | Total Given | Num Gifts | Average Gift\n--------'
    sample_card += '----------------------------------------------------------\n'
    sample_card += 'William                    $   653784.49           2 $   326892.24\n'
    assert card_text == sample_card

#Test cli main call of report creation
def test_cli_main_create_report():
    donorcollection = setup_donor_collection()
    assert create_report(donorcollection) == donorcollection.create_report()

#Test creation of thank you cards to file
def test_all_thank_you():
    donorcollection = setup_donor_collection()
    all_thank_you(donorcollection)
    assert os.path.exists('./cards/William' + '.txt')
    card_text = ''
    filename = './cards/William' + '.txt'
    with open(filename, 'r') as f:
        card_text += f.read()
    f.closed
    assert card_text == donorcollection.create_card('William',12.17)
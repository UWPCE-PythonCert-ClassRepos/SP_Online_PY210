
import pytest
import os.path
from donor_models import *
from cli_main import *

def test_creating_new_instance_of_DonorCollection():
    db = DonorCollection()
    assert db.donor_dic == {}

def test_add_new_donor():
    db = DonorCollection()
    db.add_donation('pooria', 100)
    assert db.donor_dic['pooria'].donation_list == [100]
    assert db.donor_dic['pooria'].name == 'Pooria'


def test_add_donation_for_existing_donor():
    db.add_donation('john', 100)
    assert  db.list_of_donors == ['pooria', 'john']

def test_donation_value_is_valid():
    with pytest.raises(ValueError):
        db.add_donation('john', 0)

def test_find_donor():
    assert db.find_donor('pooria') == 'Donor:pooria, Donations:Donor Pooria with 100 donation'

def test_add_new_donartion():
    db.add_donation('pooria', 330)
    assert db.donor_dic['pooria'].donation_list == [100, 330]
    assert db.donor_dic['pooria'].max_donation == 430
    assert db.donor_dic['pooria'].avr_donation == 215.0
    assert db.donor_dic['pooria'].num_of_donation == 2

def test_write_letter_to_file():
    write_letter_to_file('peter')
    d = datetime.datetime.today()
    assert os.path.isfile('peter_{}_{}_{}.txt'.format(d.year, d.month, d.day))
    assert not os.path.isfile('per_{}_{}_{}.txt'.format(d.year, d.month, d.day))

def test_write_letter_for_everyone():
    write_letter_for_everyone()
    d = datetime.datetime.today()
    for name in db.donor_dic.keys():
        file_name = '{}_{}_{}_{}.txt'.format(name,d.year, d.month, d.day)
        assert os.path.isfile(file_name)
        assert not os.path.isfile('pooria_2019_6_5.txt')
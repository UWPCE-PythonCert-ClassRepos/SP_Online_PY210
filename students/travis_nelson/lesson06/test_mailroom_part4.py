#!

import mailroom_part4 as mr
from os import path
import pytest


def test_initial_donor_db():
    assert len(mr.donor_db) == 5


def test_validate_input_donor():
    response = mr.validate_input_donor('5')
    assert response is None
    response = mr.validate_input_donor('list')
    assert response is 'list'
    response = mr.validate_input_donor('Bob')
    assert response is 'Bob'
    response = mr.validate_input_donor(2)
    assert response is None


def test_process_donor():
    beginning_donor_db_length = len(mr.donor_db)
    mr.process_donor('Jeff Bezos')
    new_donor_db_length = len(mr.donor_db)
    assert beginning_donor_db_length == new_donor_db_length
    mr.process_donor('Freddie Gibbs')
    new_donor_db_length = len(mr.donor_db)
    assert new_donor_db_length > beginning_donor_db_length


def test_validate_donation():
    response = mr.validate_donation('5')
    assert response == '5'
    response = mr.validate_donation('invalid')
    assert response is None
    response = mr.validate_donation('323323ks')
    assert response is None


def test_store_new_donation():
    beginning_number_donations = len(mr.donor_db['Brax Dingle'])
    mr.store_new_donation("Brax Dingle", "3244")
    new_number_donations = len(mr.donor_db['Brax Dingle'])
    assert new_number_donations == beginning_number_donations + 1
    mr.store_new_donation("Freddie Gibbs", "64")
    assert len(mr.donor_db["Freddie Gibbs"]) == 1
    with pytest.raises(TypeError):
        mr.store_new_donation("Travis")


def test_sum_donations():
    donations = mr.donor_db['Brax Dingle']
    tested_sum = mr.sum_donations('Brax Dingle')
    assert sum(donations) == tested_sum


def test_get_report():
    expected_rows = len(mr.donor_db)
    written_rows = mr.get_report()
    assert expected_rows == written_rows


def test_generate_all_thanks():
    mr.generate_all_thanks()
    for i in mr.donor_db:
        assert path.isfile(f"{i}.txt")

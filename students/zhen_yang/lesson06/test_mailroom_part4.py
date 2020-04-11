"""
Test code for mailroom_part4.py


"""
import os
import mailroom_part4 as m4
import pytest


# Test the data structure donors_db
def test_original_donors_db():
    assert len(m4.donors_db) == 5
# Test the valid_options()
def test_valid_input():
    assert m4.valid_input('-8', 1) == -1 # invalid option
    assert m4.valid_input('abc', 1) == -1 # invalid option
    assert m4.valid_input('2', 1) == '2' # valid option
    assert m4.valid_input('list', 2) == -1 # invalid donor name
    assert m4.valid_input('number', 3) == -1 # invalid donoation amount
    assert m4.valid_input(-12, 3) == -1 # invalid donoatio amount
    assert m4.valid_input(12, 3) == 12 # valid donoatio amount

# Test Functions in Option 1: send thankyou text
def test_list_donor_name():
    donor_list = [key for key in m4.donors_db.keys()]
    assert donor_list == m4.list_donor_names()

def test_add_update_donor_db():
    d_name = 'Sara Gogo'# existing donor
    amount = 88.88
    m4.add_update_donor_db(d_name, amount)
    print(f" 1. vallist:{m4.donors_db[d_name]}")
    assert(amount in m4.donors_db[d_name])
    d_name = 'Z Yang' # new donor
    amount = 888.12345
    m4.add_update_donor_db(d_name, amount)
    print(f" 2. vallist:{m4.donors_db[d_name]}")
    assert(amount in m4.donors_db[d_name])

def test_generate_thankyou_text():
    d_name = 'Adan William'
    amount = 1000.00
    res_list = m4.generate_thankyou_text(d_name, amount)
    assert res_list[0] == 'Adan William' and res_list[1] == 1000.00


# Test Functions in Option 2: create report
def test_generate_report_formater():
    title = '{:^20s}|{:^15s}|{:^15s}|{:^20s}'
    # scientific notation output
    #formater_content = '{:<20s} ${:>14,.2e}{:>15d}  ${:>17,.2e}'
    content = '{:<20s} ${:>14,.2f}{:>15d}  ${:>17,.2f}'
    res_list = m4.generate_report_formater()
    assert res_list[0] == title and res_list[1] == content

def test_generate_report():
    col_list = ['Donor Name', 'Total Amount', 'Num Gifts', 'Average Amount']
    assert col_list == m4.generate_report('{}{}{}{}', '{}{}{}{}')


#  Test Functions in Option 3: send_letters
def test_generate_output_file():
    expected_tot_num_donors = len(m4.donors_db)
    generated_tot_num_donors = m4.generate_output_file()
    assert expected_tot_num_donors == generated_tot_num_donors

def test_generate_output_content():
    for key, val in m4.donors_db.items():
        file_name = m4.generate_output_file_name(key, val)
        output_flag = m4.generate_output_content(key, val, file_name)
        expected_output_flag = 1
        assert output_flag == expected_output_flag
        assert os.path.isfile(file_name)

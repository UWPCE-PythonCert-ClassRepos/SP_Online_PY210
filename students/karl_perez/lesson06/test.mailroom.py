from mailroom import *
import os
from os import listdir

def create_clean_dictionary():
    donor_information = [["Krystal Perez", 50.00, 250.00],
    ["Eddie Lau", 32.50],
    ["Jimmy Jack", 200.00, 350.00, 400.00],
    ["Grace Cool", 120.00, 75.00],
    ["Adriel Molina", 45.00, 450.00]]
    donor_info = {donor[0] : donor[1:] for donor in donor_information}
    return donor_info

def test_thank_you_short():
    name1 = 'Krystal Perez'
    amount1 = 40
    assert thank_you_short(name1, amount1) == 'Dear Krystal Perez, thanks for the $40.00'

def test_update_dict_new_name():
    clean_dict = create_clean_dictionary()
    name1 = 'Christian Williams'
    amount1 = 700

    new_dict = update_dict(clean_dict, name1, amount1)
    assert new_dict[name1][-1] == amount1

def test_update_dict_existing_name():
    clean_dict = create_clean_dictionary()
    name1 = 'Eddie Lau'
    amount1 = 99
    new_dict = update_dict(clean_dict, name1, amount1)
    assert new_dict[name1][-1] == amount1

#def list_donors():

def test_calculator():
    clean_dict = create_clean_dictionary()
    name1 = 'Adriel Molina'
    total, number, average, name = calculator(clean_dict, name1)
    assert total == 495.00
    assert number == 2
    assert average == 247.50
    assert name == 'Adriel Molina'

def test_generate_report():
    clean_dict = create_clean_dictionary()
    assert generate_report(clean_dict)[0][-1] == 'Krystal Perez'
    assert generate_report(clean_dict)[1][-1] == 'Eddie Lau'
    assert generate_report(clean_dict)[2][-1] == 'Jimmy Jack'
    assert generate_report(clean_dict)[3][-1] == 'Grace Cool'
    assert generate_report(clean_dict)[4][-1] == 'Adriel Molina'

def test_generate_thank_you_long():
    clean_dict = create_clean_dictionary()
    assert generate_thank_you_long(clean_dict, 'Eddie Lau') == 'Dear Eddie Lau,\n   We appreciate your generosity in the donation amount of $32.50.\n Sincerely, The Charity Team'

def test_send_letters_to_all_donors():
    clean_dict = create_clean_dictionary()
    send_letters_to_all_donors(clean_dict)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filenames = listdir(dir_path)
    assert 'Krystal Perez.txt' in filenames
    assert 'Eddie Lau.txt' in filenames
    assert 'Jimmy Jack.txt' in filenames
    assert 'Grace Cool.txt' in filenames
    assert 'Adriel Molina.txt' in filenames

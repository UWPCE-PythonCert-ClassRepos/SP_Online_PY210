from mailroom import *
import os
from os import listdir

def create_clean_dictionary():
    donor_information = [["Bill Gates", 345678, 454540], ["Mark Zuckerberg", 6487, 4978,5487,1678], ["Jeff Bezos", 842], ["Paul Allen", 425, 3523], ["Kanye West", 4, 1235234]]
    donor_info = {donor[0] : donor[1:] for donor in donor_information}
    return donor_info

def test_generate_thank_you_text_short():
    name1 = 'Bill Gates'
    amount1 = 10
    assert generate_thank_you_text_short(name1, amount1) == 'Dear Bill Gates, thanks for the $10.00'

def test_update_dictionary_new_name():
    clean_dict = create_clean_dictionary()
    name1 = 'Kid Cudi'
    amount1 = 420

    new_dict = update_dictionary(clean_dict, name1, amount1)
    assert new_dict[name1][-1] == amount1

def test_update_dictionary_existing_name():
    clean_dict = create_clean_dictionary()
    name1 = 'Kanye West'
    amount1 = 99
    new_dict = update_dictionary(clean_dict, name1, amount1)
    assert new_dict[name1][-1] == amount1

#def list_donors():

def test_calculate_report():
    clean_dict = create_clean_dictionary()
    name1 = 'Paul Allen'
    total, number, average, name = calculate_report(clean_dict, name1)
    assert total == 3948.00
    assert number == 2
    assert average == 1974.00
    assert name == 'Paul Allen'

def test_generate_report():
    clean_dict = create_clean_dictionary()
    assert generate_report(clean_dict)[0][-1] == 'Kanye West'
    assert generate_report(clean_dict)[1][-1] == 'Bill Gates'
    assert generate_report(clean_dict)[2][-1] == 'Mark Zuckerberg'
    assert generate_report(clean_dict)[3][-1] == 'Paul Allen'
    assert generate_report(clean_dict)[4][-1] == 'Jeff Bezos'

def test_generate_thank_you_text_long():
    clean_dict = create_clean_dictionary()
    assert generate_thank_you_text_long(clean_dict, 'Mark Zuckerberg') == 'Dear Mark Zuckerberg,\n   Thank you for your kind gifts of $6487, $4978, $5487, and $1678.\n                      Sincerely, this non-profit'

def test_send_letters_to_all_donors():
    clean_dict = create_clean_dictionary()
    send_letters_to_all_donors(clean_dict)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filenames = listdir(dir_path)
    assert 'Kanye West.txt' in filenames
    assert 'Bill Gates.txt' in filenames
    assert 'Mark Zuckerberg.txt' in filenames
    assert 'Paul Allen.txt' in filenames
    assert 'Jeff Bezos.txt' in filenames
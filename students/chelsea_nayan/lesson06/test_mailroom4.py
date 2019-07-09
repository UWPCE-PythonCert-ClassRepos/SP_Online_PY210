# Unit testing for mailroom4.py

from mailroom4 import *
import os

# Use with test_sort_report() and send()
donors_dict = {
'Man Mannington': [123234.12, 120000.00, 70000000],
'Soupe Ballinger': [1.00],
'Yufus Lordgagger': [100.00, 200.00, 300.00],
'Prince Variety': [1.50, 2.00],
'Malakai Maitai': [10000000, 300000, 354132]
}

donors_dict_v2 = {
'Man Mannington': [123234.12, 120000.00, 70000000],
'Soupe Ballinger': [1.00],
'Yufus Lordgagger': [100.00, 200.00, 300.00],
'Prince Variety': [1.50, 2.00],
'Malakai Maitai': [10000000, 300000, 354132],
'Laptop Broken': [10000000000]
}

def test_note_thankyou():
    assert note_thankyou(['Philip', 0]) == ("Thank you Philip for your generous donation of $0.00.")
    assert note_thankyou(['Layla' , 0.248273498]) == ("Thank you Layla for your generous donation of $0.25.")

# Takes in parameters: (donor_names, total_given, num_gifts, average_gift)
def test_setup_report():
    assert setup_report('Chelsea', '1000', '4', '2') == [1, 1, 12, 1]

def test_header_report():
    assert header_report([0, 0, 0, 0]) == ("Donor Name|  Total Given |  Num Gifts |  Average Gift" + "\n" + "-----------------------------------------------------")
    assert header_report([10, 20, 30, 4]) == ("Donor Name|  Total Given         |  Num Gifts                  |  Average Gift" + "\n" + "------------------------------------------------------------------------------")

def test_sort_report():
    assert sort_report(donors_dict) == [('Man Mannington', [123234.12, 120000.0, 70000000]), ('Malakai Maitai', [10000000, 300000, 354132]), ('Yufus Lordgagger', [100.0, 200.0, 300.0]), ('Prince Variety', [1.5, 2.0]), ('Soupe Ballinger', [1.0])]

    assert sort_report(donors_dict_v2) == [('Laptop Broken', [10000000000]), ('Man Mannington', [123234.12, 120000.0, 70000000]), ('Malakai Maitai', [10000000, 300000, 354132]), ('Yufus Lordgagger', [100.0, 200.0, 300.0]), ('Prince Variety', [1.5, 2.0]), ('Soupe Ballinger', [1.0])]

def test_text_send():
    assert text_send('Pope', 40) == ('''
    Dear Pope,

        Thank you for your super, duper total donation of $40.00.
        I will buy so many things for myself.

            You're the best,
                - Chelsea
    ''')

def test_send():
    send()
    assert os.path.exists("./Man_mannington.txt")

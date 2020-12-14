from mailroom_Pt4 import *

donor = ()

donor_table = {}

def test_donor_table_init():
    dict_init()
    expected = {'Bobby Newport': [2000, 100], 'Jane Doe': [10000, 4000, 2000], 'John Doe': [10000, 2000, 5000, 3000], 'Johnny Mnemonic': [900, 800, 1000], 'Phillip Dick': [2220]}
    assert donor_table == expected

def test_send_thankyou():
    expected = 'Dear Jake, Thank you for your donation of $500. Sincerely, Jake'
    assert send_thankyou('Jake', 500) == expected

if __name__ == '__main__':
    test_send_thankyou()
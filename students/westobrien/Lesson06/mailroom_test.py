from mailroom import *

donor_db = {'Bob': [5.00, 10.00, 20.00, 15000.00],
            'Kathy': [20, 00],
            'Sherry': [50.00, 100.00],
            'Sophia': [1000.00],
            'Chet': [10000.00, 10000.00]}



def test1():
    assert print_list() == donor_db.keys()

def test2():
    assert donation_amount('Bob', 50) == "\n Thank you Bob For your generous donation of 50 dollars! We appreciate your generous support"

def test3():
    assert add_donor('Isabel', 100) ==  "\n Thank you Isabel For your generous donation of 100 dollars! We appreciate your generous support"

def test4():
    assert create_report_2('Isabel', 100, 10, 10) == "\n {:25s} $ {:13.2f} {:13}  $ {:12.2f}".format('Isabel', 100, 10, 10)

def test6():
    file_create('Bob')
    assert 'Bob.txt'

def test5():
    expected = "Dear Bob,\nThank you for your very kind donation of $15085.00\n\nIt will be put to very good use\nSincerely, \n\t The Team"
    assert letter_write('Bob', open('Bob.txt')) == expected


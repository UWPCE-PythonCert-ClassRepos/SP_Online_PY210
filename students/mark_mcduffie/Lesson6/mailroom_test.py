import Mailroom_part4 as mailroom
import os.path
import pathlib


def test_donor_list():
    assert donors["Jim Johnson"] == [20000.0, 3500.0, 1600.0]
    assert donors["Steve James"] == [100000.0]

def test_donor_names():
    names = mailroom.donor_names(donors)
    assert names[0] == "Jim Johnson"
    assert names[4] == "Steve James"


def test_email():
    email = ('Dear Steve James,'
             '\n \tThank you for your donation of $100,000.00. '
             '\nYour generosity is greatly appreciated, we '
             '\nlook forward to hearing from you again. '
             "\nCheers, \nThe Mailroom")
    assert mailroom.print_email("Steve James", 100000) == email

def test_final_letters():
    dirpath = pathlib.Path('./').absolute()
    letter1 = os.path.join(dirpath, 'Bob Miller.txt')
    letter2 = os.path.join(dirpath, 'Jim Johnson.txt')
    assert os.path.exists(letter1)
    assert os.path.exists(letter2)

if __name__== "__main__":
    donors = mailroom.donors()
    test_donor_list()
    test_donor_names()
    test_email()
    test_final_letters()
    print("Pass")
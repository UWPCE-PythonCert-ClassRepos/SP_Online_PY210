#!/usr/bin/env python

"""
test code for the arguments lab
"""
import sys, os.path

# you can change this import to test different versions
from mailroom4 import add_donation, getdb, print_list, create_report, gen_letter, send_letters, getmydir

# add_donation test
def test_1():
    assert "Albert Einstein" in getdb()  # pre_condition sanity test
    new_name = "aleksandr lyapunov"
    new_amount = 731
    res = add_donation(new_name, new_amount)
    assert res == "=== Thank You, Aleksandr Lyapunov, for the $731.00 donation! ===" # resulting string is correctly generated
    assert "Aleksandr Lyapunov" in getdb()   # new entry name is in the database
    assert 731 in getdb()["Aleksandr Lyapunov"]  # new amount is in the database
    
# print_list test
def test_2():
    assert print_list() == "\tAlbert Einstein: [1535.2, 15]\n\tRichard Feinman: [150, 17]\n\tLev Landau: [53, 121, 35, 79]\n\tNiels Bohr: [135.2, 15]\n\tIlya Prigogine: [15.2, 10]\n\tAleksandr Lyapunov: [731]\n"

# create_report test
def test_3():
    teststr = """
 ----------------------------------------------------------------------
 Donor Name               |    Total Given| Num Gifts  |   Average Gift
 ----------------------------------------------------------------------
 Albert Einstein          |$       1550.20|     2      |$        775.10
 Richard Feinman          |$        167.00|     2      |$         83.50
 Lev Landau               |$        288.00|     4      |$         72.00
 Niels Bohr               |$        150.20|     2      |$         75.10
 Ilya Prigogine           |$         25.20|     2      |$         12.60
 Aleksandr Lyapunov       |$        731.00|     1      |$        731.00
 ----------------------------------------------------------------------
"""
    assert create_report() == teststr 

# test generate_letters function for existing entry
def test_4():
    expected = """Dear Lev Landau,

	Thank you for your very kind donation of $288.

	It will be put to very good use.

			Sincerely,
			   -The Team."""
    assert gen_letter("Lev Landau", 288) == expected

# test generate_letters function for new entry
def test_5():
    expected = """Dear Aleksandr Lyapunov,

	Thank you for your very kind donation of $731.

	It will be put to very good use.

			Sincerely,
			   -The Team."""
    assert gen_letter("Aleksandr Lyapunov", 731) == expected

# test files for letters have been generated
def test_6():
    tdb = getdb()
    send_letters(tdb)
    curdir = getmydir() # get current directory from the main program
    files = os.listdir(curdir)
    for name in tdb:
        assert "_".join(name.split())+".txt" in files
    
# test content of the newly generated file matches
def test_7():
    expected = """Dear Aleksandr Lyapunov,

	Thank you for your very kind donation of $731.

	It will be put to very good use.

			Sincerely,
			   -The Team."""
    
    os.chdir(getmydir()) # change to current directory
    tdb = getdb() # rerieve the database
    send_letters(tdb) # generate letters and write to current directory
    fname = "Aleksandr_Lyapunov.txt"
    
    try:                            # Catch File Open Exceptions
        file = open(fname,'r')
        read_text = file.read()
        file.close()
    except (OSError, IOError):
        print("File Open Error for: ",fname)
    
    assert read_text == expected


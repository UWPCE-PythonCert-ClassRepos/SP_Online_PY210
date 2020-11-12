#!/usr/bin/env python

"""
Test Suite for the Object Oriented Mailroom
"""
import os.path, sys

from donor_models import write_file, Donor, DonorCollection
# from cli_main import send_letters, getmydir


# ============================================================================
# Donor class tests
# ============================================================================

ndonor = Donor("Alfred n. whitehead", [153, 139])

def test_01(): # Donor Constructor Tests
    assert(ndonor.get() == {'Alfred N. Whitehead': [153, 139]})
    assert(ndonor.name == 'Alfred N. Whitehead')
    assert(ndonor.record == [153, 139])
    
def test_02(): # Donor set test    
    assert(ndonor.get() == {'Alfred N. Whitehead': [153, 139]})
    ndonor.set('jane doe', [1,2,3])
    assert(ndonor.get() == {'Jane Doe': [1, 2, 3]})  

# add donation
def test_03():
    ndonor.add_donation(700)
    assert(ndonor.get() == {'Jane Doe': [1, 2, 3, 700]})  

# Generate Letter
def test_04():
    expected = """Dear Jane Doe,

	Thank you for your very kind donation of $700.

	It will be put to very good use.

			Sincerely,
			   -The Team."""
    assert ndonor.letter == expected

# Totals
def test_05():
    ndonor.set("Alfred n. whitehead", [153, 139, 32])
    assert(ndonor.get_totals() == [324, 3, 108.0] )
    assert(ndonor.get_donations_count() == 3)
    assert(ndonor.get_donations_total() == 324)
    assert(ndonor.get_donations_average() == 108.0)
    assert(ndonor.donations_count == 3)
    assert(ndonor.donations_total == 324)
    assert(ndonor.donations_average == 108.0)

# save letter
def test_06():    
    assert(ndonor.save_letter()=='written: Alfred_N._Whitehead.txt')
    
# ============================================================================
# DonorCollection class tests
# ============================================================================

ndonors = DonorCollection()

# Constructor and add
def test_07():
    ndonors.add(ndonor)   # adds the ndonor, but doesn't change it
    assert(ndonors.donors[0].get() == {'Alfred N. Whitehead': [153, 139, 32]})
    ndonors.add(Donor("Ilya Prigogine", [10,15,20]))
    assert(ndonors.donors[1].get() == {'Ilya Prigogine': [10, 15, 20]})

# Element accessors
def test_08():
    ndonors.add(Donor("Aleksandr Kholmogorov", [7,11,13]))
    assert(ndonors.front == {'Alfred N. Whitehead': [153, 139, 32]})
    assert(ndonors.back == {'Aleksandr Kholmogorov': [7, 11, 13]})
    assert(ndonors[1].get() == {'Ilya Prigogine': [10, 15, 20]})
    assert(ndonors.elem(1) == {'Ilya Prigogine': [10, 15, 20]})

# Find by name
def test_09():
    assert(ndonors.find('Ilya Prigogine').get() == {'Ilya Prigogine': [10, 15, 20]})
    ndonors.find('Aleksandr Kholmogorov').add_donation(3)
    assert(ndonors.find('Aleksandr Kholmogorov').get_totals() == [34, 4, 8.5])
    assert(ndonors.find('New Guy') == None)

# Print List
def test_10():
    exp_list = """	Alfred N. Whitehead: [153, 139, 32]
	Ilya Prigogine: [10, 15, 20]
	Aleksandr Kholmogorov: [7, 11, 13, 3]
"""
    assert(ndonors.print_list() == exp_list)
    assert(ndonors.list == exp_list)

# Create Report
def test_11():
    exp_report = """
 ----------------------------------------------------------------------
 Donor Name               |    Total Given| Num Gifts  |   Average Gift
 ----------------------------------------------------------------------
 Alfred N. Whitehead      |$        324.00|     3      |$        108.00
 Ilya Prigogine           |$         45.00|     3      |$         15.00
 Aleksandr Kholmogorov    |$         34.00|     4      |$          8.50
 ----------------------------------------------------------------------
"""
    assert(ndonors.create_report() == exp_report)
    assert(ndonors.report == exp_report)

# Write Letters
def test_12():
    exp = """Sending letters to all donors...
===--------------------------------------
Dear Alfred N. Whitehead,

	Thank you for your very kind donation of $32.

	It will be put to very good use.

			Sincerely,
			   -The Team.
written: Alfred_N._Whitehead.txt
===--------------------------------------
Dear Ilya Prigogine,

	Thank you for your very kind donation of $20.

	It will be put to very good use.

			Sincerely,
			   -The Team.
written: Ilya_Prigogine.txt
===--------------------------------------
Dear Aleksandr Kholmogorov,

	Thank you for your very kind donation of $3.

	It will be put to very good use.

			Sincerely,
			   -The Team.
written: Aleksandr_Kholmogorov.txt
"""
    assert(ndonors.send_letters()==exp)

## ========== Legacy Test Cases after this ===============
# # add_donation test
# def test_1():
    # assert "Albert Einstein" in getdb()  # pre_condition sanity test
    # new_name = "aleksandr lyapunov"
    # new_amount = 731
    # res = add_donation(new_name, new_amount)
    # assert res == "=== Thank You, Aleksandr Lyapunov, for the $731.00 donation! ===" # resulting string is correctly generated
    # assert "Aleksandr Lyapunov" in getdb()   # new entry name is in the database
    # assert 731 in getdb()["Aleksandr Lyapunov"]  # new amount is in the database
    
# # print_list test
# def test_2():
    # assert print_list() == "\tAlbert Einstein: [1535.2, 15]\n\tRichard Feinman: [150, 17]\n\tLev Landau: [53, 121, 35, 79]\n\tNiels Bohr: [135.2, 15]\n\tIlya Prigogine: [15.2, 10]\n\tAleksandr Lyapunov: [731]\n"

# # create_report test
# def test_3():
    # teststr = """
 # ----------------------------------------------------------------------
 # Donor Name               |    Total Given| Num Gifts  |   Average Gift
 # ----------------------------------------------------------------------
 # Albert Einstein          |$       1550.20|     2      |$        775.10
 # Richard Feinman          |$        167.00|     2      |$         83.50
 # Lev Landau               |$        288.00|     4      |$         72.00
 # Niels Bohr               |$        150.20|     2      |$         75.10
 # Ilya Prigogine           |$         25.20|     2      |$         12.60
 # Aleksandr Lyapunov       |$        731.00|     1      |$        731.00
 # ----------------------------------------------------------------------
# """
    # assert create_report() == teststr 

# # test generate_letters function for existing entry
# def test_4():
    # expected = """Dear Lev Landau,

	# Thank you for your very kind donation of $288.

	# It will be put to very good use.

			# Sincerely,
			   # -The Team."""
    # assert gen_letter("Lev Landau", 288) == expected

# # test generate_letters function for new entry
# def test_5():
    # expected = """Dear Aleksandr Lyapunov,

	# Thank you for your very kind donation of $731.

	# It will be put to very good use.

			# Sincerely,
			   # -The Team."""
    # assert gen_letter("Aleksandr Lyapunov", 731) == expected

# # test files for letters have been generated
# def test_6():
    # tdb = getdb()
    # send_letters(tdb)
    # curdir = getmydir() # get current directory from the main program
    # files = os.listdir(curdir)
    # for name in tdb:
        # assert "_".join(name.split())+".txt" in files
    
# # test content of the newly generated file matches
# def test_7():
    # expected = """Dear Aleksandr Lyapunov,

	# Thank you for your very kind donation of $731.

	# It will be put to very good use.

			# Sincerely,
			   # -The Team."""
    
    # os.chdir(getmydir()) # change to current directory
    # tdb = getdb() # rerieve the database
    # send_letters(tdb) # generate letters and write to current directory
    # fname = "Aleksandr_Lyapunov.txt"
    
    # try:                            # Catch File Open Exceptions
        # file = open(fname,'r');
        # read_text = file.read();
        # file.close();
    # except (OSError, IOError):
        # print("File Open Error for: ",fname)
    
    # assert read_text == expected


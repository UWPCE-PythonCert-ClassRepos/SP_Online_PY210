from mailroom import *
from os import listdir

#-----TEST Sending Thank You-----
#Test 'list' -- skipped because involves printing

#Test 'exit'
def test_exit(test_dict):
    assert give_thanks(test_dict,'exit') == None

#Test existing name
def test_existing_name(test_dict):
    fullname = 'Colonel Sanders'
    donation = 10
    add_to_list(test_dict, fullname, donation)
    assert test_dict[fullname][-1] == 10

    #Test new name
def test_new_name(test_dict):
    fullname = 'Jimmy John'
    donation = 25
    add_to_list(test_dict,fullname,donation)
    assert test_dict[fullname][-1] == 25

#-----TEST Creating Report-----
#Test calculate_report
def test_calc_report(test_dict):
    name = 'Wendy Smith'
    total, number, avg = calculate_report(name, test_dict)
    assert total == 30
    assert number == 2
    assert avg == 15

#Test form_report
def test_form_report(test_dict):
    name_lst_sorted, donor_report = form_report(test_dict)
    assert name_lst_sorted == ['Burger King','Colonel Sanders','Wendy Smith','John Silver','Ronald McDonald']

def create_test_dict():
    return {'Ronald McDonald': [1, 2, 3], 'Wendy Smith': [10, 20], 'Burger King': [100, 200],
              'John Silver': [5, 10], 'Colonel Sanders': [20, 30]}

#-----TEST Writing All Thanks/Letters-----

#Working (files exist)
def test_created_files(test_dict):
    directory = 'C:\Python_Random_stuff\session06\practice_folder' #Will need to change this to a file on your computer
    many_thanks(test_dict,directory)
    filenames = listdir(directory)
    assert 'RonaldMcDonald.txt' in filenames
    assert 'WendySmith.txt' in filenames
    assert 'ColonelSanders.txt' in filenames
    assert 'BurgerKing.txt' in filenames
    assert 'JohnSilver.txt' in filenames

#Test thank_you_text
def test_thank_you():
    donor = 'Chucky Cheese'
    assert thank_you_text(donor) == f'Dear {donor}, \n Thank you for your generous donation. We appreciate the support from people like you. \n Thank you,\n Charity Name'

#-----RUN THE TESTS-----
#A new test_dict is created each time to ensure it was not modified by a previous test

#Testing exit
test_dict = create_test_dict()
test_exit(test_dict)

#Testing existing name addition
test_dict = create_test_dict()
test_existing_name(test_dict)

#Testing new_name addition
test_dict = create_test_dict()
test_new_name(test_dict)

#Testing calc_report
test_dict = create_test_dict()
test_calc_report(test_dict)

#Testing form report
test_dict = create_test_dict()
test_form_report(test_dict)

#Testing thank you files exist in directory
test_dict = create_test_dict()
test_created_files(test_dict)

#Testing thank_you text
test_thank_you()
#!/usr/bin/env python3
#Mario Alvarenga
#Lesson 06
#Mailroom Part 4


#REGRESSION TEST FOR mailroom.py
#Must utilize latest version of mailroom


#If using pytest to run, please suppress input error with -s.


#Imports needed
import sys
import os

#Check versioning
from mailroom import i_VERSION     #Import version and functions we need to test
iMINVERSION = 4
if i_VERSION < iMINVERSION:
    print('\n\nPlease use version: {vers} of mailroom.py!\nExiting...\n\n'.format(vers = str(iMINVERSION)))
    sys.exit()

#TEST 1
from mailroom import f_get_donor_name_case
def test_f_get_donor_name_case():
    TESTCASE1 = ['uwu','Senpai']
    assert f_get_donor_name_case('UWU',TESTCASE1) == 'uwu'
    assert f_get_donor_name_case('senpai',TESTCASE1) == 'Senpai'
    assert f_get_donor_name_case('does not exist',TESTCASE1) == ''
    return
#-----------------------Start of Functions requiring inputs--------------------------------#

#TEST 2 - test that data can append
from mailroom import f_add_donation_2_list
def test_f_add_donation_2_list():
    TESTCASE2 = {
        'Senpai1': [1,2],
        'Senpai2': [3,3]
    }
    REGRESSION1 = {
        'Senpai1': [1,2,3],
        'Senpai2': [3,3]
    }
    REGRESSION2 = {
        'Senpai1': [1,2,3],
        'Senpai2': [3,3],
        'uwumaster': [1]
    }
    assert f_add_donation_2_list('senpai1',3,TESTCASE2) == REGRESSION1
    assert f_add_donation_2_list('uwumaster',1,TESTCASE2) == REGRESSION2
    return


#TEST 3 - test returning email text
from mailroom import f_generate_email
def test_f_generate_email():
    TESTCASE3 = {
        'Senpai1': [1,2],
        'Senpai2': [3,3]
    }
    GOLDENEGG = 'Dear Senpai1, \n\tThank you for your generous donation of $3.00!\nYour contribution will help new arrivals recieve the highest quality care possible.\nPlease know that your donation makes a world of difference.\n\nSincerly,\n\t\tThe Good Place Team'
    assert f_generate_email('senpai1',3,TESTCASE3) == GOLDENEGG
    return
    #Don't need to test this function too much, pretty simple. It's mostly dependent on f_get_donor_name_case so that has to be strongly protected



#TEST 4 - test printing email and asking for more input
from mailroom import f_execute_thank_you
def test_f_execute_thank_you():
    #MAKE SURE USER INPUT IS 3 BOTH TIMES, otherwise the test fails. Not much t test this type of user input
    #SUPPRESS with -s when running pytest
    TESTCASE4 = {
        'Senpai1': [1,2],
        'Senpai2': [3,3]
    }
    GOLDENEGG = 'Dear Senpai1, \n\tThank you for your generous donation of $3.00!\nYour contribution will help new arrivals recieve the highest quality care possible.\nPlease know that your donation makes a world of difference.\n\nSincerly,\n\t\tThe Good Place Team'
    assert f_execute_thank_you('senpai1',TESTCASE4) == GOLDENEGG
    GOLDENEGG = 'Dear Senpai2, \n\tThank you for your generous donation of $3.00!\nYour contribution will help new arrivals recieve the highest quality care possible.\nPlease know that your donation makes a world of difference.\n\nSincerly,\n\t\tThe Good Place Team'
    assert f_execute_thank_you('senpAi2',TESTCASE4) == GOLDENEGG
    return


#TEST 5 - Test recieving input  - should be similar tests to test 4
from mailroom import f_thank_you_input
def test_f_thank_you_input():
    #MAKE SURE USER INPUT IS 3 BOTH TIMES, otherwise the test fails. Not much t test this type of user input
    #SUPPRESS with -s when running pytest
    #Test is dependent on mocking up what the actual module contains
    
    GOLDENEGG1 = {
        'Lionel Messi': [12450, 49563, 65897, 58690,3],
        'Cristiano Ronaldo':[65000, 98520],
        'Robert Lewandowski':[85005,48912,856940],
        'Neymar Dos Santos':[26598, 74158],
        'Karim Benzema':[865204, 58740, 15069]
        }
    GOLDENEGG2 = {
        'Lionel Messi': [12450, 49563, 65897, 58690,3],
        'Cristiano Ronaldo':[65000, 98520,4],
        'Robert Lewandowski':[85005,48912,856940],
        'Neymar Dos Santos':[26598, 74158],
        'Karim Benzema':[865204, 58740, 15069]
        }
    GOLDENEGG3 = {
        'Lionel Messi': [12450, 49563, 65897, 58690,3],
        'Cristiano Ronaldo':[65000, 98520,4],
        'Robert Lewandowski':[85005,48912,856940],
        'Neymar Dos Santos':[26598, 74158],
        'Karim Benzema':[865204, 58740, 15069],
        'uwuman': [1]
        }
    #input should be "Lionel messi" followed by a "3"
    assert f_thank_you_input() == GOLDENEGG1
    #input should be "cristiano ronaldo" followed by a "4"
    assert f_thank_you_input() == GOLDENEGG2
    #input should be "uwuman" followed by a "1"
    assert f_thank_you_input() == GOLDENEGG3
    return
#-----------------------End of Functions requiring inputs--------------------------------#

#TEST 6 - Test sending all letters
from mailroom import f_send_all_letters
def test_f_send_all_letters():
    TESTCASE6 = {
        'uwuboy': [1,5,320],
        'senpaiman543': [6,50,9],
        'CallMeCarson': [69]
    }
    #
    #Create list of paths to check against
    #
    desktop_path = ['{path}{subfolder}{file}.txt'.format(path = os.path.normpath(os.path.expanduser("~/Desktop")),subfolder = os.path.normpath('/'),file = name) for name in TESTCASE6]
    assert f_send_all_letters(TESTCASE6) == desktop_path
    return


#TEST 7 - Test generating report data drom dictionary  - should be similar tests to test 4
from mailroom import f_sort_criteria, f_generate_report_data
def test_f_generate_report_data():
    TESTCASE7 = {
        'senpaiman543': [6,50,9],
        'uwuboy': [1,5,320],
        'CallMeCarson': [69]
    }
    firstrow = [('uwuboy', 326, 3,326/3)]   
    secondrow = [('CallMeCarson',69,1,69)]
    thirdrow =  [('senpaiman543',65,3,65/3)] 
    assert f_generate_report_data(TESTCASE7) == firstrow+secondrow+thirdrow
    

#TEST 8 - Test printing report data from tuple list - can not evaluate by pytest (for now). Look at stdIO for pass/fail judgement
from mailroom import f_print_report
def test_f_print_report():
    firstrow = [('uwuboy', 326, 3,326/3)]   
    secondrow = [('CallMeCarson',69,1,69)]
    thirdrow =  [('senpaiman543',65,3,65/3)]
    goldenegg =  firstrow+secondrow+thirdrow
    f_print_report(goldenegg)
    return


#TEST 9 - Testing minor functions
from mailroom import f_create_report, f_exit_program, f_print_error
def test_minor_functions():
    TESTCASE9 = {
        'senpaiman543': [6,50,9],
        'uwuboy': [1,5,320],
        'CallMeCarson': [69]
    }
    #criteria development
    firstrow = [('uwuboy', 326, 3,326/3)]   
    secondrow = [('CallMeCarson',69,1,69)]
    thirdrow =  [('senpaiman543',65,3,65/3)]
    goldenegg =  f_print_report(firstrow+secondrow+thirdrow)
    assert f_create_report(TESTCASE9) == goldenegg
    message1 = 'Not a valid option. Please try again!'
    assert f_print_error() == message1
    #don't test exit program, because we don't want to exit THIS program right away

#TEST 10 - Test user input
#Use this function to also drive the testing of all unit tests without pytest
from mailroom import main
def test_main():
    TESTCASE10 = {
        'senpaiman543': [6,50,9],
        'uwuboy': [1,5,320],
        'CallMeCarson': [69]
    }
    #1
    #main(TESTCASE10) - interesting case study was that the dictionary did not have its value updated with a passed parameter 
    #but when using the global variable default case it did...... I think it is because in the test case the variable was localized already and the scope could not be reached.
    #
    main()
    return

test_main()


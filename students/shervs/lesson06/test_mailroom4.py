from mailroom4 import *

test_name1 = "Moli Smith"
test_name2 = "Kevin Johnson"
test_name3 = "Greg Jones"
test_donation = 12.45
test_dict_blank = {}
test_dict = {test_name2: [1.21 , 45],
             test_name3: [844.31]
            }
test_dict2 = {"Pam Rossi II": [1000.00 , 1345.12, 23.1],
             "Melvin Marvin": [20.1, 300.20],
             "Steve Amorosi": [43.34]
            }
test_file_name = "test.txt"
test_message1 = "this is a test"
test_message2= '''Dear Greg Jones,

     Thank you for your donation of $844 throughout these years.

     Cheers,

          -The team'''

def test_add_donor():
    expected = { test_name1: [] }
    assert add_donor(test_name1, test_dict_blank) == expected

def test_generate_thank_you_text():
    expected = f"Thank you {test_name1} for your generous donation of $12.45"
    assert generate_thank_you_text(test_name1,test_donation) == expected

def test_add_donation():
    expected = {test_name2: [1.21 , 45 , 12.45],
                test_name3: [844.31]
               }
    assert add_donation(test_name2, test_donation, test_dict) == expected
   
def test_generate_donor_list():
    expected = print("Kevin Johnson\nGreg Jones\n")
    assert generate_donor_list(test_dict) == expected

def test_get_report():  
    expected =[('Pam Rossi II', 2368.22, 3, 789.4066666666666), ('Melvin Marvin', 320.3, 2, 160.15), ('Steve Amorosi', 43.34, 1, 43.34)]
    assert get_report(test_dict2) == expected
   
def test_write_to_file():
    write_to_file(test_file_name, test_message1)
    assert os.path.exists(test_file_name)    
   
def test_letter_text():
    expected = test_message2
    assert letter_text(test_name3, test_dict[test_name3])[1] == expected
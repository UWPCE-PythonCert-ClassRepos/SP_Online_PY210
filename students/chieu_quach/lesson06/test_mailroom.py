#!/usr/bin/env python

import pytest
from mailroom_part4 import select_user, updating_list, send_thankyou, users_list

donation_list = [{'full name': 'William Gates III', "Amount": 653684.49,
                     "num_gift": "2", "avg_amt": 326892.24},
                 {'full name': 'Mark Zukerberg', 'Amount': 16396.10,
                     'num_gift': '3', 'avg_amt': 5465.37},
                 {'full name': 'Jeff Bezos', 'Amount': 873.33,
                     'num_gift': '1', 'avg_amt': 873.33},          
                 {'full name': 'Paul Allen', 'Amount': 708.42,
                     'num_gift': '3', 'avg_amt': 236.14 }]

def test_select_user():
   
    assert select_user("Mark Zukerberg") == ("Mark Zukerberg", 16396.10, 3, 5465.37)
             

def test_user_list():

    msgz = ['William Gates III        653684.49       2                   326892.24 ',
           'Mark Zukerberg            16396.10       3                     5465.37 ',
           'Jeff Bezos                  873.33       1                      873.33 ',
           'Paul Allen                  708.42       3                      236.14 ']

    assert users_list() == msgz
           
def test_sent_thankyou():
    
    msgj = (" Dear Mark Zukerberg,\n\tThank you for your generous donation of 144.15\n"
        " \tIt will be put to very good use.\n\n\t"
            "   Sincerely,\n\t"
            "    -The Team\n")

    
     # assert send_thankyou(("Mark Zukerberg", 3100) == msgj 
      #assert(send_thankyou(11, 14) == 25)
    assert send_thankyou("Mark Zukerberg", 144.15) == msgj
      
def test_updating():
   #Updatin user record
   
    #assert updating_list(name) == ("Mark Zukerberg", 17896.1, 4, 4474.02)
    assert updating_list("Mark Zukerberg", 1500) == ("Mark Zukerberg", 17896.1, 4, 4474.02)
    assert updating_list("Jeff Bezos", 3400) == ('Jeff Bezos', 4273.33, 2, 2136.66)
      
        


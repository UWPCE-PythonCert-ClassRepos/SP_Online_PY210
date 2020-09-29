#!/usr/bin/env python3
#lesson6
#https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/mailroom-part4.html
from mailroom import create_a_report, send_thank_you_one, send_thank_you_all
##import mock
from unittest import mock
import os.path
  
#Test report display
#inputs
def test_report_display():
    breakfast_db = {
                "pancakes": [34,42,2],
                "eggs": [7],
                "bacon": [2,3,4,5,6],
                "hashbrowns": [10,15,20]
                }
    
    report_format = {
                "Header": "{Col 1: <28}|{Col 2: ^13}|{Col 3: ^11}|{Col 4: ^13}",
                "Filler": "-" * 68,
                "Rows":"{0: <28} ${1: >11.2f}   {2: >9}  ${3: >12.2f}"
                }
    
    report_headers = {
                "Col 1": "Food",
                "Col 2": "Total Eaten",
                "Col 3": "Meals",
                "Col 4": "Avg Eaten"
                }
    
    #build what the report should output
    report_test_answer = [
                            "Food                        | Total Eaten |   Meals   |  Avg Eaten  ",
                            "--------------------------------------------------------------------",
                            "pancakes                     $      78.00           3  $       26.00",
                            "hashbrowns                   $      45.00           3  $       15.00",
                            "bacon                        $      20.00           5  $        4.00",
                            "eggs                         $       7.00           1  $        7.00"
                            ]
    
    #use function from mailroom to build report
    test_report = create_a_report(report_format, report_headers, breakfast_db)
    #test
    for i in range(0,len(test_report)):
        assert test_report[i] == report_test_answer[i]
    
#Test thank you one
def test_thank_you_one():
    ##This will fail if ran more than once in a row due to apending the database while the test is static
    thanks_test_answer = "\n".join(("Dear Frank Dudeguy,",
                                    "",
                                    "Thank you for your generous donation of 1000000.00.  Your total donations of 1000000.00 are greatly appriciated.",
                                    "",
                                    "Sincerly,",
                                    "The Weyland-Yutani Corporation"
                                    ))
        
    #select the input values to mock based on what is asked
    def mock_input(prompt):
        if "full name" in prompt.lower():
            return "Frank Dudeguy"
        if "amount" in prompt.lower():
            return 1000000
    
    #mock the inputs and assert the match to the answer
    with mock.patch("builtins.input", mock_input):
        assert send_thank_you_one() == thanks_test_answer
    

#Test thank you all
def test_thank_you_all():
    donor_db = {
                "William Gates, III": [653772.32, 12.17],
                "Jeff Bezos": [877.33],
                "Paul Allen": [663.23, 43.87, 1.32],
                "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
                }      
    
            
    thank_you_email = "\n".join(("Dear {donor},",
                "",
                "Thank you for your generous donation of {donation:.2f}.  Your total donations of {total:.2f} are greatly appriciated.",
                "",
                "Sincerly,",
                "The Weyland-Yutani Corporation"
              ))
    #Build a mock for the write out prompt
    def mock_input(prompt):
        if "directory name" in prompt.lower():
            return "no"

    #Execute thank you write out
    with mock.patch("builtins.input", mock_input):
        send_thank_you_all(donor_db)
        
    #Check if all the files are there
    for key, value in donor_db.items():
        file_name = key + '.txt'
        os.path.exists(file_name)
        
        #Check that the files have correct text
        with open(file_name, 'r') as thank_you:
            thanks_dict = {"donor": key, "donation": value[-1], "total": sum(value)}
            test = thank_you.read()
            assert test == thank_you_email.format(**thanks_dict)
            

    

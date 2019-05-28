from mailroom_part_4 import *
import os

a_dict = {
        "Jeff Bezos": {
            "donation_total": 877.33,
            "times_donated": 1,
            "average_donation": 877.33
        },
        "Paul Allen": {
            "donation_total": 708.42,
            "times_donated": 3,
            "average_donation": 236.14
        }
    }

'''
ensure that list of names returned is a string
'''
def test_list_names():
    names = list_names()
    assert type(names) is str

'''
Verify sorted donors is always returned as a list
'''
def test_sort_donors():
    output = sorted(a_dict.items(), key=sort_donors, reverse=True)
    assert type(output) is list

'''
Test to ensure any dictionary passed into report is formatted properly
and returns the correct values and type based on key 
'''
def test_generate_report():
    single_report = generate_report(a_dict)
    assert donors_list["Paul Allen"]["donation_total"] == 708.42
    assert type(donors_list["Paul Allen"]["donation_total"]) == float

'''
Test that emails are correctly formatted
and are saved as file with the correct name
make sure the values are updated correctly

Test if new users are added expected output is captured
'''
def test_send_thankyou():
    email_template = send_thankyou("Paul Allen",100)
    assert donors_list["Paul Allen"]["donation_total"] == 808.42
    assert email_template == "\n".join((f"Dear Paul Allen,\n\nThank you for your very kind donation of $100.00.\n",
                        "It will be put to very good use.\n",
                        "Sincerely,\n",
                        "-The Team"))
    assert os.path.isfile("Paul_Allen.txt") == True

    email_template = send_thankyou("Larry David",100)
    assert email_template == "\n".join((f"Dear Larry David,\n\nThank you for your very kind donation of $100.00.\n",
                        "It will be put to very good use.\n",
                        "Sincerely,\n",
                        "-The Team"))
    assert donors_list["Larry David"]["donation_total"] == 100.00
    assert os.path.isfile("Larry_David.txt") == True

'''
ensure all expected files are saved with the correct names
'''
def test_bulk_thankyou():
    email_output = bulk_thankyou(a_dict)
    for i in email_output:
        assert os.path.isfile(i) == True
    
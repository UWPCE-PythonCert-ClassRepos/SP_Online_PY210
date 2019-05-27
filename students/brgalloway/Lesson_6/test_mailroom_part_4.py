from mailroom_part_4 import *

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

def test_list_names():
    names = list_names()
    assert type(names) is str

def test_sort_donors():
    output = sorted(a_dict.items(), key=sort_donors, reverse=True)
    assert type(output) is list

def test_generate_report():
    donors_list = generate_report(a_dict)
    assert donors_list["Paul Allen"]["donation_total"] == 708.42

def test_send_thankyou():
    email_template = send_thankyou("Paul Allen",100)
    assert donors_list["Paul Allen"]["donation_total"] == 808.42
    assert email_template == "\n".join((f"Dear Paul Allen,\n\nThank you for your very kind donation of $100.00.\n",
                        "It will be put to very good use.\n",
                        "Sincerely,\n",
                        "-The Team"))
    
    email_template = send_thankyou("Larry David",100)
    assert email_template == "\n".join((f"Dear Larry David,\n\nThank you for your very kind donation of $100.00.\n",
                        "It will be put to very good use.\n",
                        "Sincerely,\n",
                        "-The Team"))
    assert donors_list["Larry David"]["donation_total"] == 100.00

def test_bulk_thankyou():
    email_template = bulk_thankyou()
    # donors_list["Larry David"]["donation_total"]
    assert email_template == "\n".join((f"Dear Larry David,\n\nThank you for your very kind donation of $100.00.\n",
                        "It will be put to very good use.\n",
                        "Sincerely,\n",
                        "-The Team"))
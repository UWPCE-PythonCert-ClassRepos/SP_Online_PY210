from mailroom import Report, Donor
from mailroom import send_thank_you, send_thank_you_multiple
import os

def test_donor_init():
    test_donor = Donor("Kristy Martini", 0, 3, 3000)
    assert test_donor.name == "Kristy Martini"
    assert test_donor.gift_value == 0
    assert test_donor.num_gifts == 3
    assert test_donor.average_gift == 3000/3

def test_donor_add_gift():
    test_donor = Donor("Kristy Martini", 0, 3, 3000)
    test_donor.add_gift(300)
    assert test_donor.total_gift_value == 3000 + 300
    assert test_donor.num_gifts == 3 + 1
    assert test_donor.average_gift == 3300/4

def test_report_init():
    test_report = Report()
    donor_names = ["Kristy Martini", "Mike Martini", "Nick Martini", "Bill Martini", "Cathy Martini"]
    for donor in test_report.donors.keys():
        assert donor in donor_names
    
def test_report_add_donor():
    test_report = Report()
    test_donor = Donor("Katie Edwards")
    test_report.add_donor(test_donor)
    assert "Katie Edwards" in test_report.donors.keys()

def test_report_sort_donors():
    test_report = Report()  
    test_report.sort_donors(new_report=None)
    sorted_order = ["Nick Martini", "Mike Martini", "Cathy Martini", "Bill Martini", "Kristy Martini"]
    i = 0
    for donor in test_report.sorted_dict.keys():
        assert donor == sorted_order[i]
        i += 1

def test_create_report():
    test_report = Report()
    output_lines = test_report.create_report(new_report=None)
    test_lines = []
    test_lines.append("Donor Name          | Total Given   | Num Gifts | Average Gift")
    test_lines.append("--------------------------------------------------------------")
    test_lines.append("Nick Martini         $      47484949          50 $   949698.98")
    test_lines.append("Mike Martini         $       3424834           7 $    489262.0")
    test_lines.append("Cathy Martini        $         63833           7 $      9119.0")
    test_lines.append("Bill Martini         $         60000          10 $      6000.0")
    test_lines.append("Kristy Martini       $          3000           3 $      1000.0")
    test_lines.append("\n")

    for i in range(8):
        assert output_lines[i] == test_lines[i]
    
def test_send_thank_you():
    test_donor = Donor("Kristy Martini", 0, 1, 1000)
    send_thank_you(test_donor)
    output_file = os.path.join(os.getcwd(), "Kristy Martini.txt")
    assert os.path.exists(output_file)

def test_thank_you_text():
    test_donor = Donor("Kristy Martini", 0, 1, 1000)
    send_thank_you(test_donor)
    output_text = []
    output_text.append("Thank you Kristy Martini for your charitable gift to our organization.\n")
    output_text.append("We could not operate without the generosityy of donors like yourself.\n")
    output_text.append("Your generous gift of $1000 will allow us to continue to serve our community in the hopes of a better world.\n")
    output_text.append("   -Kristy Martini")
    output_file = os.path.join(os.getcwd(), "Kristy Martini.txt")
    with open(os.path.join(output_file), 'r') as f:
        lines = f.readlines()
    for i in range(4):
        assert output_text[i] == lines[i]

def test_send_thank_you_multiple():
    new_report = Report()
    send_thank_you_multiple(new_report)
    for donor in new_report.donors.keys():
        file_name = str(donor) + ".txt"
        output_file = os.path.join(os.getcwd(), file_name)
        assert os.path.exists(output_file)
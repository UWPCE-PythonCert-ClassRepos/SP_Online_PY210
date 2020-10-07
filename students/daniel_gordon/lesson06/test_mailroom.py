import pytest
import mailroom as UUT

testbench = {"Nick Esen": [1800, 720],
          "Sabina": [1500],
          "Marceline Theodosia": [30000, 500000, 100],
          "Rafat Rein": [1500000],
          "Kevin Both": [150, 1200, 750]}

#test create_a_report first
def test_get_total():
    #test ability to make a sum
    assert UUT.get_total(testbench["Nick Esen"]) == 2520
    assert UUT.get_total(testbench["Sabina"]) == 1500
    assert UUT.get_total(testbench["Marceline Theodosia"]) == 530100
    assert UUT.get_total(testbench["Rafat Rein"]) == 1500000
    assert UUT.get_total(testbench["Kevin Both"]) == 2100

def make_text(name, total, num, avg):
    return f"{name:<25}  ${total:>11.2f} {num:>11}  ${avg:>12.2f}"

def make_letter(name, money):
    letter  = f"Dear {name},\n\n"
    letter += f"\tThank you for your donation of {money}\n\n"
    letter += "\tSincerly,\n"
    letter += "\t\tThe Team"
    return letter
    
def test_report_entry():
    #test generated text
    assert UUT.report_entry(("Nick Esen", testbench["Nick Esen"])) == make_text("Nick Esen", 2520, 2, 1260)
    assert UUT.report_entry(("Sabina", testbench["Sabina"])) == make_text("Sabina", 1500, 1, 1500)
    assert UUT.report_entry(("Marceline Theodosia", testbench["Marceline Theodosia"])) == make_text("Marceline Theodosia", 530100, 3, 176700)
    assert UUT.report_entry(("Rafat Rein", testbench["Rafat Rein"])) == make_text("Rafat Rein", 1500000, 1, 1500000)
    assert UUT.report_entry(("Kevin Both", testbench["Kevin Both"])) == make_text("Kevin Both", 2100, 3, 700)
    
def test_create_a_report():
    #test that the function can run without error
    assert UUT.create_a_report() is True

    
def test_add_donation():
    #test new donation for existing donor
    assert UUT.add_donation("Sabina", 30600)
    testbench["Sabina"].append(30600)
    assert testbench == UUT.donors
    #test new donor
    assert UUT.add_donation("Chadash", 3600)
    testbench["Chadash"] = [3600]
    assert testbench == UUT.donors

def test_thank_you():
    #test that the thank you text is as expected
    assert UUT.thank_you("Kevin Both", testbench["Kevin Both"][-1]) == "Thank you Kevin Both for your generous donation of 750"
    assert UUT.thank_you("Name", 1234) == "Thank you Name for your generous donation of 1234"
    
def test_send_letters():
    #test ability to create the correct path
    assert UUT.make_path("./letters")
    #test that the letter reads as expected
    assert UUT.write_letter("Rafat Rein") == make_letter("Rafat Rein", 1500000)
    #test that the function runs correctly
    assert UUT.send_letters()
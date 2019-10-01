import os 
import numpy as np
os.chdir(r'C:\Users\Gemini\UW_PYTHON\SP_Online_PY210\students\philip_behrend\lesson06')
from mailroom_pt4 import get_name, donor_logic, donation, send_thanks, thank_you, create_metrics,send_all_letters


donor_dict = {'Marge':[50,40],'Harold':[100,1000,10000],'Henry':[2],'Myrtle':[5,0.5,.05],'Mitchell':[3,6,9]}    
name = 'Bill'

def test_name(donor_dict,name):
    get_donor = get_name(donor_dict)
    assert get_donor == name

def test_donor(donor_dict,name,donation_amt = 34):
    donor_logic(donor_dict,name)
    assert name in donor_dict.keys()
    assert donation_amt in donor_dict[name]
    
def test_ty(name):
    message = "Esteemed {}, thank you for your generous donation".format(name)
    assert thank_you(name = message)
    
def test_metrics(donor_dict):
    metrics = create_metrics(donor_dict)
    temp = metrics
    assert metrics.keys() == donor_dict.keys()
    for i in temp:
        temp[i] = [sum(donor_dict[i]),np.mean(donor_dict[i]),len(donor_dict[i])]
    assert metrics == temp

def test_letter_creation(donor_dict):
    send_all_letters(donor_dict)
    donors = donor_dict.keys()
    for i in donors:
        assert "{}.txt".format(i) in os.listdir()
    
def test_letter_contents(donor_dict):
    send_all_letters(donor_dict)
    donors = donor_dict.keys()
    filenames = ["{}.txt".format(i) for i in donors]
    for donor,filename in zip(donors, filenames):
        with open(filename, 'r') as f:
            assert "Esteemed {}, thank you for your generous donation".format(donor) == f.read()
    
test_name(donor_dict,name = 'Bill')
test_donor(donor_dict,name,donation_amount = 34)
test_ty(name)
test_metrics(donor_dict)
test_letter_creation(donor_dict)
test_letter_contents(donor_dict)    


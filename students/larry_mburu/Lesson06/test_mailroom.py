import mailroom
import os
from operator import itemgetter


#test functions for Send Thank You!!

def test_get_donor_list(): 
    actual  = mailroom.get_donor_list('list')
    expected = ['William Gates III', 'Mark Zuckerberg', 'Jeff Bezo', 'Paul Allen', 'Bill Gates']
    assert actual == expected

def test_add_donor_to_list(): 
    '''
    test new user not in DB
    '''
    mailroom.add_donar_to_list('James Comey')
    assert mailroom.donations_per_individual['James Comey'] == [100.0]

def test_add_to_donation_database(): 
    assert mailroom.add_to_donation_database('James Comey', 100) == None

def test_send_thank_you_email(): 
    name = 'James Comey'
    amount = 100
    expected = f"Thank you {name} for your generous donation of $ {amount:.2f} dollars"
    assert mailroom.send_thank_you_email(name, amount) == expected


#test function get_report

def test_get_report(): 
    #test contents of donor DB.
    actual = [ 
        (
            donor, 
            sum(mailroom.donations_per_individual[donor]), 
            len(mailroom.donations_per_individual[donor]), 
            sum(mailroom.donations_per_individual[donor]) / len(mailroom.donations_per_individual[donor]) 
        ) 
        for donor in list(mailroom.donations_per_individual) 
    ]

    expected = [
        ('William Gates III', 50500.12, 2, 25250.06),
        ('Mark Zuckerberg', 28500.989999999998, 2, 14250.494999999999),
        ('Jeff Bezo', 140700.99, 3, 46900.329999999994),
        ('Paul Allen', 201740.0, 3, 67246.66666666667),
        ('Bill Gates', 100450.0, 3, 33483.333333333336),
        ('James Comey', 200.00, 2, 100.00)
    ]

    assert actual == expected

    # test the sort feature
    actual_sorted = sorted(actual, key=itemgetter(3), reverse=True)

    expected_sorted = [
        ('Paul Allen', 201740.0, 3, 67246.66666666667),
        ('Jeff Bezo', 140700.99, 3, 46900.329999999994),
        ('Bill Gates', 100450.0, 3, 33483.333333333336),
        ('William Gates III', 50500.12, 2, 25250.06),
        ('Mark Zuckerberg', 28500.989999999998, 2, 14250.494999999999),
        ('James Comey', 200.00, 2, 100.0)
        ]

    assert actual_sorted == expected_sorted

    # test the create_report() returned results.
    padding = 20
    actual_summary = [ 
        f"{name:{padding}} $ {total:10.2f} {num_gifts:14} $ {average:10.2f}" 
        for name, total, num_gifts, average in expected_sorted
        ]
    assert actual_summary == mailroom.get_report()

#test send_thank_you_letters() function

def test_send_thank_you_letters(): 
    donor_names = list(mailroom.donations_per_individual)
    expected_list = [ '_'.join(donor.split()) for donor in donor_names ] 
    for expected in expected_list: 
        assert os.path.isfile(expected + '.txt') == True

def test_get_text_letter():
    donor_names = list(mailroom.donations_per_individual)
    for donor_name in donor_names: 
        expected = f"""Dear {donor_name},
        Thank you for your kind donation of ${mailroom.donations_per_individual[donor_name][-1]}. 
            
        It will be put to very good use. 
            
        Sincerely, 
            
        - The Cloud Squad"""
        assert mailroom.get_letter_text(donor_name) == expected
    
            

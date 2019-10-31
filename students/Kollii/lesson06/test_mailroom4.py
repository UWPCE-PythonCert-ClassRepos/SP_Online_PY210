import mailroom4 as mailroom
import os.path
import pathlib


mailroom.donor_dict = mailroom.donors()

def test_donors_history():
    """ Test History of dictionary of donors created """
    history = mailroom.donors()
    assert history['Jeff Bezos'] == [877.33]
    assert history['William Gates, III'] == [653772.32, 12.17]

def test_donors_list():
    """ Test all donor names are returned"""
    
    thislist = ('William Gates, III\n Jeff Bezos\n Paul Allen\n Mark Zuckerberg')
    assert mailroom.donors_list() == thislist

def test_donation_update():
   
    mailroom.donation('Indu', 100)
    
    assert mailroom.donor_dict.get('Indu') == [100.00]

def test_thankyou_note():
    """ Test  Thank you Note """
    note = (f'\nDear Jeff Bezos,'
            f'\nThank you for your generous donation of $877.33'
            '\nWe appreciate your support.'
            '\n\nRegards,\nXYZ Charity Team\n')

    assert mailroom.print_thanksnote('Jeff Bezos') == note

def test_send_letters():
    dirpath = pathlib.Path('./').absolute()
    file1 = os.path.join(dirpath,'Mark Zuckerberg.txt')
    file2 = os.path.join(dirpath, 'Paul Allen.txt')
    mailroom.send_letters_all()
    assert os.path.exists(file1)
    assert os.path.exists(file2)

if __name__== "__main__":
    test_donors_history()
    test_donation_update()
    test_thankyou_note()
    test_send_letters()
    print("All TESTS PASS")

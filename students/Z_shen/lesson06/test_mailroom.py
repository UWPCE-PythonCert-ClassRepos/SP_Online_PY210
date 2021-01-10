
import mailroom_4 as mr
import os.path
import pathlib

donor = {'William Gates': [1500.99, 3500, 800.25],
         'Jeff Bezos': [145.72, 1350.25],
         'Paul Allen': [250.00, 57.00],
         'Mark Zuckerberg': [600.00],
         }
test_donor = donor.copy()

def test_donor_name_list():
    result = {'William Gates', 'Jeff Bezos', 'Paul Allen', 'Mark Zuckerberg'}
    assert mr.donor_name_list(donor) == result


def test_add_new_donor():
    result = {'William Gates': [1500.99, 3500, 800.25],
         'Jeff Bezos': [145.72, 1350.25],
         'Paul Allen': [250.00, 57.00],
         'Mark Zuckerberg': [600.00],
         'peter chen': [123],
         }
    assert mr.add_new_donor('peter chen', 123, test_donor) == result


def test_add_amount_same_donor():
    result = {'William Gates': [1500.99, 3500, 800.25],
         'Jeff Bezos': [145.72, 1350.25],
         'Paul Allen': [250.00, 57.00],
         'Mark Zuckerberg': [600.00, 123],
         }
    assert mr.add_amount_same_donor('Mark Zuckerberg', 123, donor) == result



def test_print_letter():
    thx = {'Name': 'peter chen', 'Donation': float(123)}
    letter = ('''Dear peter chen, 
    Thank you for your generous donation of $123.00 to us.
    It will be put to very good use.

                        Sincerely,
                            -The Team
                                    ''')
    assert mr.print_letter(thx) == letter


def test_send_letter_to_all():
    path = pathlib.Path('./').absolute()
    file1 = os.path.join(path, 'Mark_Zuckerberg.txt')
    file2 = os.path.join(path, 'Paul_Allen.txt')
    file3 = os.path.join(path, 'Jeff_Bezos.txt')
    file4 = os.path.join(path, 'William_Gates.txt')
    mr.send_letters_to_all()
    assert os.path.exists(file1)
    assert os.path.exists(file2)
    assert os.path.exists(file3)
    assert os.path.exists(file4)


if __name__ == '__main__':
    test_donor_name_list()
    test_add_new_donor()
    test_add_amount_same_donor()
    test_print_letter()
    test_send_letter_to_all()


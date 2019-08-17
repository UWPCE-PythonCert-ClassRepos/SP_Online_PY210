'''
Andrew Garcia
Mailroom Tests
8/7/19
'''

import Mailroom4 as mr
import os.path

def test_sorting_donors():
    """Tests sorting donors by highest donation amount"""
    assert mr.sorting_donors() == [['Bryan Fultan', 1, 1236.28, 1236.28], ['Jayson Black', 3, 584.04, 194.67999999999998], ['Danica Dolores', 3, 450.15, 150.04999999999998], ['Roy Max', 2, 365.6, 182.8], ['Skylar Odell', 2, 319.52, 159.76]]

def test_thank_all():
    """Tests file creation for donors"""
    mr.thank_all()
    assert os.path.exists('Bryan Fultan.txt')
    assert os.path.exists('Danica Dolores.txt')
    assert os.path.exists('Jayson Black.txt')
    assert os.path.exists('Roy Max.txt')
    assert os.path.exists('Skylar Odell.txt')

def test_thank_all_files():
    """Tests content in a file created"""
    text = (f'Dear Skylar Odell, \nThank you for your 2 donations, totaling $319.52. \nFrom, Your Local Charity')
    with open('Skylar Odell.txt', 'r+') as file:
        fileinfo = ''
        for line in file:
            line.strip('\n')
            fileinfo += line
    assert fileinfo == text

def test_format_thank_you():
    """Tests a single thank you for one donor"""
    text = (f'''\nDear Mark, \nThank you for donating $500.00! \nYour contribution greatly helps us! \nFrom, Your Local Charity''')
    assert mr.format_thank_you('Mark', 500) == text


def test_add_donation():
    """Tests adding a donation for exsiting donor"""
    mr.add_donation('Bryan Fultan', 209.66)
    assert mr.all_donations == {'Jayson Black': [156.8, 207.32, 219.92],
                                'Bryan Fultan': [1236.28, 209.66],
                                'Danica Dolores': [163.51, 100.42, 186.22],
                                'Skylar Odell': [167.9, 151.62],
                                'Roy Max': [137.97, 227.63]}

def test_add_donation2():
    """Tests adding a new donor"""
    mr.add_donation('Mark Wright', 250.36)
    assert mr.all_donations == {'Jayson Black': [156.8, 207.32, 219.92],
                                'Bryan Fultan': [1236.28, 209.66],
                                'Danica Dolores': [163.51, 100.42, 186.22],
                                'Skylar Odell': [167.9, 151.62],
                                'Roy Max': [137.97, 227.63],
                                'Mark Wright': [250.36]}

if __name__ == '__main__':
    test_sorting_donors()
    test_thank_all()
    test_thank_all_files()
    test_format_thank_you()
    test_add_donation()
    test_add_donation2()
    print('Working')


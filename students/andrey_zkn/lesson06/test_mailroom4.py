
import mailroom4 
import os.path
import pathlib


mailroom4.donors_data = mailroom4.donors()

def test_donors():
    """ Test initial donors list and amounts """
    donors_data = mailroom4.donors()
    assert donors_data['Leo Tolstoy'] == [150, 250, 100]
    assert donors_data['Alexander Pushkin'] == [200, 100, 340]


def test_list_of_donors():
    """ Test all donor names are returned """
    donors_list = ('Alexander Pushkin\nMikhail Lermontov\nLeo Tolstoy\nFyodor Dostoevsky\nAnton Chekhov\nNikolai Gogol')
    assert mailroom4.list_of_donors() == donors_list


def test_donations():
    """ Test donor name and donation amount update """
    mailroom4.donations('Vladimir Mayakovsky', 300)
    assert mailroom4.donors_data.get('Vladimir Mayakovsky') == [300]


def test_thank_you_message():
    """ Test  Thank you Message """
    message = (f'\nDear Leo Tolstoy,'
               f'\n\nThank you for your generous donation of $500.00.' 
               '\nWe value your contribution and support.' 
               '\n\nSincerely,\n\nNew Horizon Charity Director\n')   
    assert mailroom4.thank_you_message('Leo Tolstoy') == message


def test_send_letters_to_all():
    dirpath = pathlib.Path('./').absolute()
    file1 = os.path.join(dirpath,'Mikhail Lermontov.txt')
    file2 = os.path.join(dirpath, 'Anton Chekhov.txt')
    mailroom4.send_letters_to_all()
    assert os.path.exists(file1)
    assert os.path.exists(file2)

if __name__== "__main__":
    test_donors()
    test_list_of_donors()
    test_donations()
    test_thank_you_message()
    test_send_letters_to_all()
    print("All tests were successfully passed. Congratulations!!!")


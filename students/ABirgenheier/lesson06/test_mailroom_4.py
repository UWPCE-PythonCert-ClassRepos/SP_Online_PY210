import mailroom_4
import os.path
import pathlib


mailroom_4.donars_data = mailroom_4.donars()


def test_donars():
    """ Test initial donars list and amounts """
    donars_data = mailroom_4.donars()
    assert donars_data['Mike'] == [200, 150, 50]
    assert donars_data['Sarah'] == [150, 150, 150]


def test_list_of_donars():
    """ Test all donor names are returned """
    donars_list = ('Mike\nTony\nSarah')
    assert mailroom_4.list_of_donars() == donars_list


def test_donations():
    """ Test donor name and donation amount update """
    mailroom_4.donations('Mike', 200)
    assert mailroom_4.donars_data.get('Mike') == [200]


def test_thank_you_message():
    """ Test  Thank you Message """
    message = (f'\nDear Mike,'
               f'\n\nThank you for your generous donation of $500.00.'
               '\nWe value your contribution and support.'
               '\n\nSincerely,\n\nNew Horizon Charity Director\n')
    assert mailroom_4.thank_you_message('Mike') == message


def test_send_letters_to_all():
    dirpath = pathlib.Path('./').absolute()
    file1 = os.path.join(dirpath, 'Sarah.txt')
    file2 = os.path.join(dirpath, 'Tony.txt')
    mailroom_4.send_letters_to_all()
    assert os.path.exists(file1)
    assert os.path.exists(file2)


if __name__ == "__main__":
    test_donars()
    test_list_of_donars()
    test_donations()
    test_thank_you_message()
    test_send_letters_to_all()
    print("All tests were successfully passed. Congratulations!!!")

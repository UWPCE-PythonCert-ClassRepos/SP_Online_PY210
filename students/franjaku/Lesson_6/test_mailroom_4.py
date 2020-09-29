import mailroom_4 as ml
import os

"""
Uses pytest to test all the code in the mailroom_4 module.


"""


def test_initialize_database():
    assert ml.initialize_database() == {'John Smith': [5000, 52048, 20],
                                        'Jane Adams': [25000, 5498, 3333, 87469],
                                        'Brett Johnson': [50, 6584, 20, 68, 9857, 5412],
                                        'Sofia Pippy': [623, 98, 40658],
                                        'Maddy North': [85426, 10, 25]}


def test_add_new_donation():
    # Test Existing Donor
    database = ml.initialize_database()
    ml.add_new_donation(database, 'John Smith',50)
    assert sum(database['John Smith']) == 5000+52048+20+50

    # Test New Donor
    ml.add_new_donation(database, 'Wiggle Jiggle', 500)
    assert sum(database['Wiggle Jiggle']) == 500


def test_sort_key():
    database = ml.initialize_database()
    assert ml.sort_key(database.popitem()) == 85426+10+25


def test_prompt_user():
    pass


def test_prompt_donation_amount():
    pass


def test_get_donation_amount():
    donation = ml.get_donation_amount(100)
    assert type(donation) == float


def test_prompt_donor_name():
    pass


def test_generate_thank_you_email():
    email = ml.generate_thank_you_email('John Smith', 5205)
    assert email == 'John Smith, thank you for your generous donation of $5205.00'


def test_driver_send_thank_you_note():
    pass


def test_send_letters():
    database = ml.initialize_database()
    for donor, data in database.items():
        assert os.path.isfile(f"{donor}.txt")


def test_create_report():
    database = ml.initialize_database()
    lines = ml.create_report(database)
    assert lines[0] == '-----Donation Report-----'
    assert lines[1] == '\n{:<15} | {:>14} | {:>11} | {:>16}'.format('Donor Name', 'Total Donation', '# donations', 'Average Donation')
    assert lines[2] == '-'*66
    assert lines[3] == '{:<15} | ${:>13.2f} | {:^11} | ${:>15.2f}'.format('Jane Adams', 121300.00, 4, 30325.00)
    assert lines[5] == '{:<15} | ${:>13.2f} | {:^11} | ${:>15.2f}'.format('John Smith', 57068.00, 3, 19022.67)
    assert lines[7] == '{:<15} | ${:>13.2f} | {:^11} | ${:>15.2f}'.format('Brett Johnson', 21991.00, 6, 3665.17)


def test_mail_room():
    pass

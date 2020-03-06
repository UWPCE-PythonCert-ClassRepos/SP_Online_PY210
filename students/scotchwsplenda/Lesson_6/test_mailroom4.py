#!/usr/bin/python

import os
import MailRoom_4 as mail

'''1. Send Thank You: generating thank you text,
adding or updating donors, and listing donors.'''


'''listing donors'''


def test_print_donors():
    assert(mail.print_donors() == ['Gordian', 'Tiberius', 'Maximus',
                                   'Tacitus', 'Commodus'])


'''generating thank you text'''


def test_send_thanks():
    a = 'butt'
    b = 69.0
    assert mail.send_thanks(a, b) == ('Wow butt, only $69.0? Give'
                                      ' til it hurts you capitalist swine')


'''adding new donor'''


def test_update_dons():
    a = 'butt'
    b = 69
    assert mail.update_dons(a, b) == {'butt': [69]}


'''2. Create Report: return the report string already
formatted or return a list of formatted rows'''


def test_data_metrics():
    data_set = mail.data_metrics()
    assert any(item == ('Gordian', 75.0, 2, 37.5)
               for item in data_set)
    assert any(item == ('Tiberius', 60.0, 1, 60.0)
               for item in data_set)


'''3. Send Letters: assert that a file is created per donor
and that the file content contains text as expected.'''


''' assert that a file is created per donor'''


def test_sent():
    mail.mass_mail()
    assert os.path.exists("./Tacitus.txt")
    assert os.path.exists("./Gordian.txt")
    assert os.path.exists("./Tiberius.txt")


'''file content contains text as expected'''


def test_text():
    mail.mass_mail()
    file = open('Tacitus.txt', 'r')
    assert file.read() == ('Thanks Tacitus for '
                           'donating $80.0. Your mother would be so proud.')

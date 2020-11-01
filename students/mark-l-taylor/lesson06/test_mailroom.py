"""Mailroom Testing"""

import mailroom


def check_get_donor_names():
    assert mailroom.get_donor_names() == ['Homer Simpson', 'Charles Burns', 'Kent Brockman', 'Ned Flanders',
                                          'Barney Gumble']

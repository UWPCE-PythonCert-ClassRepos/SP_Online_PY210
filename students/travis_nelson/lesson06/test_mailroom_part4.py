

import mailroom_part4


def test_initial_donor_db():
    assert len(mailroom_part4.donor_db) == 5

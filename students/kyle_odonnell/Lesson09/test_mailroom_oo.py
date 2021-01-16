"""
test code for mailroom.py
"""


from donor_models import *


def test_donor_init():
    d = Donor("Paul Allen")
    assert d.name == "Paul Allen"
    print(d.name)


def test_donor_str():
    d = Donor("Paul Allen")
    assert str(d) == "Donor: Paul Allen"
    print(str(d))


# def test_donor_repr():
#     d = Donor("Paul Allen")
#     assert repr(d) == Donor("Paul Allen")
#     print(repr(d))


def test_donor_amount():
    d = Donor("Paul Allen")
    d.donation = 100
    assert d.donation == 100
    print(d.donation)


def test_donor_number():
    d = Donor("Paul Allen")
    d.number = 3
    assert d.number == 3
    print(d.number)


def test_donor_average():
    d = Donor("Paul Allen")
    d.donation = 100
    d.number = 3
    assert d.average == 33.33
    print(d.average)


def test_donor_eq():
    d = Donor("Paul Allen")
    d.donation = 100
    c = Donor("Kelby Doggy")
    c.donation = 20
    assert d != c


def test_donor_lt():
    d = Donor("Paul Allen")
    d.donation = 100
    c = Donor("Kelby Doggy")
    c.donation = 20
    assert c < d


def test_write_letter():
    d = Donor("Marge Simpson")
    d.donation = 150.43
    text = d.write_letter
    expected = """
        Dear Marge Simpson,
        Thank you for your collective contributions of $150.43 over the years.
        Your generous donations have been put to good use!
        Sincerely,
        Kyle at Kelby Doggo, Inc\n"""
    assert text == expected
    print(text)
    print(expected)


def test_send_letter():
    d = Donor("Marge Simpson")
    d.donation = 150.43
    d.send_letter
    assert os.path.isfile("Marge_Simpson.txt")








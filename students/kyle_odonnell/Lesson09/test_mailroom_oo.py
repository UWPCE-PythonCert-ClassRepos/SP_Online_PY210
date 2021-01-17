"""
test code for mailroom.py
"""

from donor_models import *


def test_donor_init():
    """Test Donor objects rendered correctly with valid/invalid inputs"""
    d = Donor("Paul Allen", amount=800.87, number=3)
    c = Donor("Mark Zuckerberg", amount=-5, number=4.3)
    e = Donor("Jeff Bezos")

    assert d.name == "Paul Allen"
    assert d.donation == 800.87
    assert d.number == 3
    assert c.name == "Mark Zuckerberg"
    assert c.donation == 0
    assert c.donation == 0
    assert e.name == "Jeff Bezos"
    assert e.donation == 0
    assert e.number == 0
    print(d.name)


def test_donor_str():
    """Test Donor str return correct string"""
    d = Donor("Paul Allen")
    c = Donor("Mark Zuckerberg", amount=-5, number=4.3)

    assert str(d) == "Donor: Paul Allen"
    assert str(c) == "Donor: Mark Zuckerberg"
    print(str(d))


def test_add_donation():
    """Test add_donation method"""
    d = Donor("Paul Allen")
    e = Donor("Mark Zuckerberg", 23, 1)
    d.add_donation(100)
    e.add_donation(34)

    assert d.donation == 100
    assert d.number == 1
    assert e.donation == 57
    assert e.number == 2

    print(d.donation)


def test_donor_number():
    """Test donor number attribute"""
    e = Donor("Mark Zuckerberg", 23, 3)

    assert e.number == 3
    print(e.number)


def test_add_number():
    """Test add donor number method"""
    d = Donor("Paul Allen", amount=80, number=3)
    d.add_number(1)

    assert d.number == 4
    d.add_number(1.5)
    assert d.number == 4
    print(d.number)


def test_donor_average():
    """Test donor average method"""
    d = Donor("Paul Allen")
    d.donation = 100
    d.number = 3

    assert d.average == 33.33
    print(d.average)


def test_donor_eq():
    """Test Donor equals operator"""
    c = Donor("Paul Allen", amount=800.87, number=3)
    d = Donor("Mark Zuckerberg", amount=-5, number=4.3)
    m = Donor("Marge Simpson")
    m.donation = 100
    k = Donor("Kelby Doggy")
    k.donation = 100

    assert d != c
    assert m == k


def test_donor_lt():
    """Test Donor less than operator"""
    d = Donor("Paul Allen")
    d.donation = 100
    c = Donor("Kelby Doggy")
    c.donation = 20

    assert c < d
    assert c != d


def test_write_letter():
    """Test write letter method"""
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
    """Test send letter method"""
    d = Donor("Jon Snow")
    w = Donor("William Gates, III")
    d.donation = 150.43
    Donor.send_letter(d)
    Donor.send_letter(w)

    assert os.path.isfile("Jon_Snow.txt")
    assert os.path.isfile("William_Gates_III.txt")


def test_donor_collections_init():
    """Test DonorCollections Initializer"""
    w = Donor("William Gates, III", amount=400, number=1)
    m = Donor("Mark Zuckerberg", amount=600, number=5)
    j = Donor("Jeff Bezos", amount=877.33, number=2)
    db = DonorCollections((w, m, j))

    assert w in db.list
    assert m in db.list
    assert j in db.list
    print(db.list)


def test_donor_collection_str():
    """Test DonorCollections string"""
    w = Donor("William Gates, III", amount=400, number=1)
    m = Donor("Mark Zuckerberg", amount=600, number=5)
    j = Donor("Jeff Bezos", amount=877.33, number=2)
    db = DonorCollections((w, m, j))

    assert str(db) == "Donor Collection: ['Jeff Bezos', 'Mark Zuckerberg', 'William Gates, III']"
    print(db)


def test_add_donor():
    """Test add donor method"""
    w = Donor("William Gates, III", amount=400, number=1)
    m = Donor("Mark Zuckerberg", amount=600, number=5)
    db = DonorCollections((w, m))
    j = Donor("Jeff Bezos", amount=877.33, number=2)
    db.add_donor(j)

    assert j in db.list


def test_format_collection():
    """Test format collection method"""
    w = Donor("William Gates, III", amount=400, number=1)
    m = Donor("Mark Zuckerberg", amount=600, number=5)
    donor_db = DonorCollections((w, m))
    d = DonorCollections.format(donor_db)
    row = "| {dn:<20s} \t| {ds:<1s} {tg:>14.2f} \t|" \
          "{ng:>10d}\t| {ds2:<1} {ag:>14.2f} |".format

    assert d[2] == row(dn="Mark Zuckerberg", ds="$", tg=600,
                       ng=5, ds2="$", ag=120)
    print(d)


def test_send_letters():
    """Test send letters method"""
    w = Donor("William Gates, III", amount=400, number=1)
    m = Donor("Mark Zuckerberg", amount=600, number=5)
    j = Donor("Jeff Bezos", amount=877.33, number=2)
    db = DonorCollections((w, m, j))
    DonorCollections.send_letters(db)

    assert os.path.isfile("Mark_Zuckerberg.txt")
    assert os.path.isfile("Jeff_Bezos.txt")
    assert os.path.isfile("William_Gates_III.txt")


def test_get_names():
    """Test get names method"""
    w = Donor("William Gates, III", amount=400, number=1)
    m = Donor("Mark Zuckerberg", amount=600, number=5)
    j = Donor("Jeff Bezos", amount=877.33, number=2)
    db = DonorCollections((w, m, j))

    assert db.get_names == ['Jeff Bezos', 'Mark Zuckerberg', 'William Gates, III']
    print(db.get_names)

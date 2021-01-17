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
    d = Donor("Jon Snow")
    d.donation = 150.43
    Donor.send_letter(d)
    assert os.path.isfile("Jon_Snow.txt")


def test_data_collection_init():
    w = Donor("William Gates, III", amount=400, number=1)
    m = Donor("Mark Zuckerberg", amount=600, number=5)
    j = Donor("Jeff Bezos", amount=877.33, number=2)
    db = DonorCollections((w, m, j))
    assert w in db.list
    assert m in db.list
    assert j in db.list
    print(db.list)


def test_donor_collection_str():
    w = Donor("William Gates, III", amount=400, number=1)
    m = Donor("Mark Zuckerberg", amount=600, number=5)
    j = Donor("Jeff Bezos", amount=877.33, number=2)
    db = DonorCollections((w, m, j))
    assert str(db) == "Donor Collection: ['Jeff Bezos', 'Mark Zuckerberg', 'William Gates, III']"
    print(db)


def test_add_donor():
    w = Donor("William Gates, III", amount=400, number=1)
    m = Donor("Mark Zuckerberg", amount=600, number=5)
    db = DonorCollections((w, m))
    j = Donor("Jeff Bezos", amount=877.33, number=2)
    db.add_donor(j)
    assert j in db.list


def test_format_collection():
    w = Donor("William Gates, III", amount=400, number=1)
    m = Donor("Mark Zuckerberg", amount=600, number=5)
    donor_db = DonorCollections((w, m))
    d = DonorCollections.format(donor_db)
    row = "{dn:<20s} \t {ds:<1s} {tg:>14.2f} \t " \
          "{ng:>10d} \t {ds2:<1} {ag:>14.2f} ".format
    assert d[1] == row(dn="Mark Zuckerberg", ds="$", tg=600,
                                                ng=5, ds2="$", ag=120)
    print(d)

def test_send_letters():
    w = Donor("William Gates, III", amount=400, number=1)
    m = Donor("Mark Zuckerberg", amount=600, number=5)
    j = Donor("Jeff Bezos", amount=877.33, number=2)
    db = DonorCollections((w, m, j))
    Donor.send_letter(db)
    assert os.path.isfile("Mark_Zuckerberg.txt")


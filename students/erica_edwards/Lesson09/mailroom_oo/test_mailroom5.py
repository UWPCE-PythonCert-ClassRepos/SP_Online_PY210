#!/usr/bin/env python
from pytest import approx
from donor_models import Donor, DonorCollection
import os


def test_donor_init_type():
    donor = Donor('Some Name')
    assert type(donor) is Donor


def test_donor_init_name():
    donor = Donor('Some Name')
    assert donor.name == 'Some Name'


def test_donor_init_single_donation():
    donor = Donor('Some Name', [1.23])
    assert len(donor.donations) == 1
    assert sum(donor.donations) == 1.23


def test_donor_init_multi_donation():
    donor = Donor('Some Name', [1.23, 2.10])
    assert len(donor.donations) == 2
    assert sum(donor.donations) == 3.33


def test_donor_multi_donation_single_letter():
    donor = Donor('Some Name', [1.23, 2.10])
    assert '2.10' in donor.single_donation_letter()


def test_donor_multi_donation_multi_letter_sum():
    donor = Donor('Some Name', [1.23, 2.10])
    print(donor.multi_donation_letter())
    assert '3.33' in donor.multi_donation_letter()


def test_donor_multi_donation_multi_letter_name():
    donor = Donor('Some Name', [1.23, 2.10])
    print(donor.multi_donation_letter())
    assert 'Some Name' in donor.multi_donation_letter()


def test_donor_multi_donation_report_values_name():
    donor = Donor('Some Name', [1.23, 2.10])
    name, total, count, avg = donor.report_values()
    print(f'name = {name}, total = {total}, count = {count}, avg = {avg}')
    assert name == 'Some Name'


def test_donor_multi_donation_report_values_total():
    donor = Donor('Some Name', [1.23, 2.10])
    name, total, count, avg = donor.report_values()
    print(f'name = {name}, total = {total}, count = {count}, avg = {avg}')
    assert total == 3.33


def test_donor_multi_donation_report_values_count():
    donor = Donor('Some Name', [1.23, 2.10])
    name, total, count, avg = donor.report_values()
    print(f'name = {name}, total = {total}, count = {count}, avg = {avg}')
    assert count == 2


def test_donor_multi_donation_report_values_average():
    donor = Donor('Some Name', [1.23, 2.10])
    name, total, count, avg = donor.report_values()
    print(f'name = {name}, total = {total}, count = {count}, avg = {avg}')
    assert avg == approx(1.66, rel=1e-2)


def test_collection_init():
    donors = DonorCollection()
    assert type(donors) is DonorCollection


def test_collection_add():
    donor = Donor('Some Name', [1.23])
    donors = DonorCollection()
    donors.add(donor)
    assert 'Some Name' in donors.donors.keys()


def test_collection_list_donors():
    donors = DonorCollection()
    donors.add(Donor('Foo', [1.23]))
    donors.add(Donor('Bar', [4.56]))
    print(donors.list_donors())
    assert 'Foo' in donors.list_donors()
    assert 'Bar' in donors.list_donors()
    assert 'Foo\nBar' in donors.list_donors()


def test_collection_generate_letters():
    email_output_path = "C:\\Users\\erica\\Desktop\\python210\\SP_Online_PY210\\students\\erica_edwards\\"
    donors = DonorCollection()
    donors.add(Donor('Foo', [1.23]))
    donors.add(Donor('Bar', [4.56]))
    donor_count = len(donors.donors)
    donors.generate_letters()
    donor_file_count = len([x for x in os.listdir(email_output_path) if x.endswith('.txt')])
    assert donor_file_count == donor_count


def test_create_report():
    donors = DonorCollection()
    donors.add(Donor('Some Name', [2.00, 6.00]))
    expected = ("\nDonor Name                | Total Given | Num Gifts | Average Gift\n"
                "------------------------------------------------------------------\n"
                "Some Name                  $       8.00           2  $       4.00\n")
    actual = donors.create_report()
    print(actual)
    assert actual == expected


def test_collection_donor_exists():
    donors = DonorCollection()
    donors.add(Donor('Foo', [1.23]))
    donors.add(Donor('Bar', [4.56]))
    assert donors.donor_exists('Foo')


def test_collection_from_dict():
    given = {'Sandy Pie': [75],
             'Judy Smith': [75, 100, 1000],
             'Mike Jones': [75, 1000],
             'Joe Smith': [75, 100, 2000],
             'Kelly Blue': [75, 150, 275]}
    donors = DonorCollection.from_dict(given)
    assert len(donors.donors) == 5


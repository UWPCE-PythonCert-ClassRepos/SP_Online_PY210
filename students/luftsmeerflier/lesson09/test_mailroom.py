#/usr/bin/env python3
import sys
import contextlib
from io import StringIO

from donor_models import Donor, DonorCollection

donations = DonorCollection(Donor("Natasha Singer", 120, '02-08-2010'))
donations.add_donation("Bob Marquardt", 40, '05-08-1994')


def test_send_thank_you():
	temp_stdout = StringIO()
	with contextlib.redirect_stdout(temp_stdout):
		donations.send_thank_you("Natasha Singer")
	output = temp_stdout.getvalue().strip()
	assert "Natasha Singer" in output

def test_get_report():
	temp_stdout = StringIO()
	with contextlib.redirect_stdout(temp_stdout):
		donations.get_report()
	output = temp_stdout.getvalue().strip()
	assert "Natasha Singer" in output

def test_send_letter_all():
	donations.send_letters()
	with open('Natasha_Singer.txt', 'r') as f:
		assert "Natasha Singer" in f.read()
	with open('Bob_Marquardt.txt', 'r') as f:
	 	assert "Bob Marquardt" in f.read()


test_send_thank_you()
test_get_report()
test_send_letter_all()

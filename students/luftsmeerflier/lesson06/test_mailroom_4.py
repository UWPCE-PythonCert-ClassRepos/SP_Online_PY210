#/usr/bin/env python3
import sys


from mailroom_4 import write_letters

from mailroom_4 import send_thank_you

from mailroom_4 import send_letter_all


# test for send_thank_you
def test_send_thank_you():
	assert "John Quigley" in send_thank_you(first_name = "John", last_name = "Quigley")

def test_write_letters():
	write_letters("John Quigley", 2000, '10-2-2020')
	with open('John_Quigley.txt', 'r') as f:
		assert "John Quigley" in f.read()

def test_send_letter_all():a
	send_letter_all()
	with open('John_Quigley.txt', 'r') as f:
		assert "John Quigley" in f.read()
	with open('Jacob_van_der_Schmidt.txt', 'r') as f:
		assert "Jacob van der Schmidt" in f.read()
	with open('Sara_Smith.txt', 'r') as f:
		assert "Sara Smith" in f.read()
	with open('Ogden_Nash.txt', 'r') as f:
		assert "Ogden Nash" in f.read()

test_write_letters()
test_send_letter_all()


# Jacob van der Schmidt         $ 5420.0         3         $ 1806
# John Quigley                  $ 12250.0        3         $ 4083
# Ogden Nash                    $ 5550000.0      3         $ 1850000
# Sara Smith                    $ 76000.0        3         $ 25333

#/usr/bin/env python3
import sys


from mailroom_4 import print_heading

from mailroom_4 import print_info

from mailroom_4 import write_letters

from mailroom_4 import send_thank_you

from mailroom_4 import send_letter_all


# test for send_thank_you
def test_send_thank_you():
	assert "John Quigley" in send_thank_you(first_name = "John", last_name = "Quigley")


# Part of create_report
def test_print_heading():
	assert "Donor Name" in print_heading()

# Also part of create_report
def test_print_info(): 
	l = [entry.split('      ') for entry in print_info()]
	flat_list = [item for sublist in l for item in sublist]
	assert "John Quigley" in flat_list
	assert "Jacob van der Schmidt" in flat_list

# part of send_thank_you, send_thank_you_all

def test_write_letters():
	assert "John Quigley" in write_letters("John Quigley", 2000, '10-2-2020')

def test_send_letter_all():
	assert "John Quigley" in send_letter_all()
	assert "Jacob van der Schmidt" in send_letter_all()
	assert "Sara Smith" in send_letter_all()
	assert "Ogden Nash" in send_letter_all()


#tests for create_report
test_print_heading()
test_print_info()
test_write_letters()
test_send_letter_all()


# Jacob van der Schmidt         $ 5420.0         3         $ 1806
# John Quigley                  $ 12250.0        3         $ 4083
# Ogden Nash                    $ 5550000.0      3         $ 1850000
# Sara Smith                    $ 76000.0        3         $ 25333

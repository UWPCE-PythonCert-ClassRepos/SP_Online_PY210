#/usr/bin/env python3
import sys
from donor_models import Donor, DonorCollection

donations = None

# Your user interaction code will interact wtih DonorCollection class instance like below:
# donations = DonorCollection(Donor("Natasha Singer", 100, '02-08-1994'))

# donations.add_donation("Bob Marquardt", 40, '05-08-1994')
# donations.add_donation("Bob Marquardt", 50, '06-08-2010')
# donations.add_donation("John Quigley", 40, '05-08-1994')
# donations.add_donation("Jacob van der Schmidt", 40, '05-08-1994')
# donations.add_donation("Sara Smith", 40, '05-08-1994')
# donations.add_donation("Ogden Nash", 40, '05-08-1994')


def send_thank_you(name):
	donations.send_thank_you(name)

def create_report():
	donations.get_report()

def send_letter_all():
	donations.send_letters()

def exit_program():
	print("Adieu, auf wiedersehen, goodbye!")
	sys.exit()	

# def input_first_donation():
# 	print("Add a donor to the list")
# 	first_name = input("Enter donor first name> ")
# 	last_name = input("Enter donor last > ")
# 	full_name = first_name + ' ' + last_name
# 	donation_amount = int(input("Enter a donation amount>"))
# 	date = input("Enter a donation date (DD-MM-YYYY)> ")
# 	donations = DonorCollection(Donor(full_name, donation_amount, date))

def add_update_donor(donation_num):
	global donations
	first_name = input("Enter donor first name> ")
	last_name = input("Enter donor last > ")
	full_name = first_name + ' ' + last_name	
	donation_amount = int(input("Enter a donation amount>"))
	date = input("Enter a donation date (MM-DD-YYYY)> ")
	if donation_num == "first":
		donations = DonorCollection(Donor(full_name, donation_amount, date))
	elif donation_num == "add":
		donations.add_donation(full_name, donation_amount, date)

arg_dict = {
    1: send_thank_you,
    2: create_report,
	3: send_letter_all,
	4: add_update_donor,
	5: exit
}

prompt = "\n".join(("Please input one of the numbers below:",
	"1 - Send a Thank You",
	"2 - Create a Report",
	"3 - Send letters to all donors.",
	"4 - Add new donor or update a donor field",
	"5 - quit"
	))

def main():
	if donations is None:
		add_update_donor("first")

	while True:
		try:
			response = int(input(prompt + "\n")) # continuously collect user selection

			if response > 0 and response < 6:
				#now redirect to feature functions based on the user selection
				if arg_dict[response] == send_thank_you:
					name = input("enter name> ").title()
					send_thank_you(name)
				elif arg_dict[response] == create_report:
					create_report()
				elif arg_dict[response] == send_letter_all:
					send_letter_all()
				elif arg_dict[response] == add_update_donor:
					add_update_donor("add")
				elif arg_dict[response] == exit:
					exit()
				else:
					print("Please enter a number between 1 and 4")
					return
			else:
				print("Input a valid selection")
				return 1
		except ValueError:
			print("\nIncorrect input\n")

			


if __name__ == "__main__":
	main()

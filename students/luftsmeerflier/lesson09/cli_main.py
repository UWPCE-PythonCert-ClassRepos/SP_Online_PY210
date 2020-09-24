#/usr/bin/env python3
import sys
from donor_models import Donor, DonorCollection

# Your user interaction code will interact wtih DonorCollection class instance like below:
donations = DonorCollection(Donor("Natasha Singer", 100, '02-08-1994'))

donations.add_donation("Bob Marquardt", 40, '05-08-1994')
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

arg_dict = {
    1: send_thank_you,
    2: create_report,
	3: send_letter_all,
	4: exit
}

prompt = "\n".join(("Please input one of the numbers below:",
	"1 - Send a Thank You",
	"2 - Create a Report",
	"3 - Send letters to all donors.",
	"4 - quit"
	))

def main():
	while True:
		try:
			response = int(input(prompt + "\n")) # continuously collect user selection

			if response > 0 and response < 5:
				#now redirect to feature functions based on the user selection
					if arg_dict[response] == send_thank_you:
						name = input("enter name> ").title()
						send_thank_you(name)
					elif arg_dict[response] == create_report:
						create_report()
					elif arg_dict[response] == send_letter_all:
						send_letter_all()
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

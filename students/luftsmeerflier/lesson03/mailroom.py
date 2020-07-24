#/usr/bin/env python3
import sys

donors = [
	#The actual donations themselves are a list of objects: Donations.date and Donations.amount
	[
		"John",
		"Quigley",
		"555 Camelot RD N London, Ontario",
		[
			("2019-02-04", 5000.00),
			("2019-02-04", 4250.00),
			("2019-02-04", 3000.00)
		]
	],
	[
		"Sara",
		"Smith",
		"256 Camden RD N London, UK",
		[
			("2020-04-02", 2000.00),
			("2019-02-04", 42000.00),
			("2019-02-04", 32000.00)
		]
	],
	[
		"Jacob",
		"van der Schmidt",
		"2001 Space Oddysey RD SW Los Angeles, CA",
		[
			
			("2012-04-20", 20.00),
			("2019-02-04", 2000.00),
			("2019-02-04", 3400.00)
		]
	],
	[
		"Jason Quigley",
		"Quigley",
		"12 Camden RD N London, UK",
		[
			("2012-02-04", 12.00),
			("2013-02-04", 240.00),
			("2014-02-05",120.00)
		]
	],
	[
		"Ogden",
		"Nash",
		"256 Camden RD N London, UK",
		[
			("2019-02-04", 5000000.00),
			("2019-02-04", 500000.00),
			("2019-02-04", 50000.00)
		]
	]
]

prompt = "\n".join(("Please select from the following options:",
					"1 - Send a Thank You",
					"2 - Create a Report",
					"3 - quit"
					))

def send_thank_you():
	list = input("Type `list` for a list of donors or press the carriage key to skip")
	if list == "list":
		for donor in donors:
			print(donor[0], donor[1])
		return
	else:
		pass

	first_name = input('What is the first name of the donor?\n').title()
	last_name = input('What is the last name of the donor?\n').title()

	for donor in donors:
		if donor[0] ==  first_name and donor[1] == last_name:
			amount = donor[3][0][1]
			date = donor[3][0][0]
			print("\n\n")
			print(f"Dear {first_name} {last_name},\n\n    Thank you for your donation in the amount of {amount} on {date}. Please keep this letter for your records.\n\n")
			return
		else:
			print("We are unable to locate that donor")
			return


def create_report():
	#print(donor_list[0].ljust(20) + donor_list[1].ljust(10) + donor_list[2].ljust(20) + donor_list[3].ljust(8))
	# print(donor_list[0].ljust(20))
	print("Donor Name".ljust(28) + '|'.ljust(2) + "Total Given" + '|'.rjust(2) + "Num Gifts".rjust(10) + "|".ljust(2) + "Average Gift")
	print('-' * 70)

	donor_list = []
	for donor in donors:
		first_name = donor[0]
		last_name = donor[1]
		total = 0
		# get total
		amount = []
		donations = donor[3]
		for num in donations:
			amount.append(num[1])
		total += sum(amount)
		num_gifts = len(amount)
		average = total / num_gifts

		name_length = len(first_name) + len(last_name)
		
		print((first_name + ' ' + last_name).ljust(30) + '$'.ljust(2) + str(total).ljust(15) + str(num_gifts).ljust(10) + '$'.ljust(2) + str(round(average, 2)))
	
def exit_program():
	print("Adieu, auf wiedersehen, goodbye!")
	sys.exit()

def main():
	while True:
		response = input(prompt + "\n") # continuously colelct user selection
		# now redirect to feature functions based on the user selection
		if response == "1":
			send_thank_you()
		elif response == "2":
			create_report()
		elif response == "3":
			exit_program()
		else:
			print("Not a valid option")

	
if __name__ == "__main__":
	main()
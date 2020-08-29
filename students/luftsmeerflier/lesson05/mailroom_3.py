#/usr/bin/env python3
import sys

donors = {
	"John Quigley": {"2019-02-04": 5000.00, "2019-02-05": 4250.00, "2019-02-07": 3000.00},
	"Sara Smith": {"2020-01-02": 2000.00, "2019-02-08": 42000.00, "2019-02-02": 32000.00},
	"Jacob van der Schmidt": {"2012-01-20": 20.00, "2019-02-24": 2000.00, "2019-12-1": 3400.00},
	"Ogden Nash": {"2019-06-04": 5000000.00, "2019-04-04": 500000.00, "2019-12-04": 50000.00}
}

def send_thank_you(first_name='', last_name=''):
	names_list = list(donors.keys())

	_list = input("Type `list` for a list of donors or press the carriage key to skip\n")

	if _list == "list":
		for donor in names_list:
			print(donor)
		print('\n')
	else:
		pass

	name = input('What is the name of the donor?\n').title()
	donor = donors.get(name)

	if donor:
		amount = list(donor.values())[0]
		date = list(donor.keys())[0]
		write_letters(name, amount, date)
	else:
		amount = input("How much did {} donate?\n".format(name))
		date = input("When was the donation? YYYY-MM-DD\n")
		try: 
			print(amount > 0)
		except:
			print("That is an invalid donation amount")

		write_letters(name, amount, date)


def write_letters(name, amount, date):	

	text = "Dear {},\n\n    Thank you for your donation in the amount of {} on {}. Please keep this letter for your records.\n\n"

	letterhead = "{}.txt".format(name).replace(" ", "_")
	# open a letter template
	formatted = text.format(name, amount, date)

	with open("{}".format(letterhead), "w+") as thank_you:
		thank_you.write(formatted)

	print('\n')
	print("Thank you letter has been created")
	print('\n')


def create_report():
	print('\n')
	print("Donor Name".ljust(28) + '|'.ljust(2) + "Total Given" + '|'.rjust(2) + "Num Gifts".rjust(10) + "|".ljust(2) + "Average Gift")
	print('-' * 70)

	def key(item):
		return sum(item[1].values())

	# list of tuples
	sorted_donors = sorted(donors.items(), key=key, reverse=True)

	for donor in sorted_donors:
		name = donor[0]
		total = sum(list(donor[1].values()))
		num_gifts = len(donor[1].values())
		average = total / num_gifts
		
		print((name).ljust(30) + '$'.ljust(2) + str(total).ljust(15) + str(num_gifts).ljust(10) + '$'.ljust(2) + str(round(average, 2)))
		
	print('\n')


def send_letter_all():
	for donor in donors:
		name = donor
		amount = list(donors[name].values())[0]
		date = list(donors[name].keys())[0]
		write_letters(name, amount,date)

def exit_program():
	print("Adieu, auf wiedersehen, goodbye!")
	sys.exit()	

arg_dict = {
    1: send_thank_you,
    2: create_report,
	3: send_letter_all,
	4: exit
}

prompt = "\n".join(("Please select from the following options:",
	"1 - Send a Thank You",
	"2 - Create a Report",
	"3 - Send letters to all donors.",
	"4 - quit"
	))


def main():
	while True:
		response = int(input(prompt + "\n")) # continuously collect user selection
		try:
			isinstance(response, int)
			reponse > 0
			response < 5
			#now redirect to feature functions based on the user selection
			arg_dict.get(response)()

		except:
			print("Please input a valid selection")
			return
			


if __name__ == "__main__":
	main()

#/usr/bin/env python3
import sys

donors = {
	"John Quigley": [
		("2019-02-04", 5000.00),
		("2019-02-04", 4250.00),
		("2019-02-04", 3000.00)
	],
	"Sara Smith": [
		("2020-04-02", 2000.00),
		("2019-02-04", 42000.00),
		("2019-02-04", 32000.00)
	],
	"Jacob van der Schmidt": [			
		("2012-04-20", 20.00),
		("2019-02-04", 2000.00),
		("2019-02-04", 3400.00)
	],
	"Ogden Nash": [
		("2019-02-04", 5000000.00),
		("2019-02-04", 500000.00),
		("2019-02-04", 50000.00)
	]
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

	if name in names_list:
		index = names_list.index(name)
		name = names_list[index]
		donor = donors[name]
		date = donor[0][0]
		amount = donor[0][1]
		write_letters(name, amount, date)
	

def write_letters(name, amount, date):	

	text = "Dear {},\n\n    Thank you for your donation in the amount of {} on {}. Please keep this letter for your records.\n\n"

	letterhead = "{}.txt".format(name).replace(" ", "_")
	# open a letter template
	formatted = text.format(name, amount, date)
	thank_you = open("{}".format(letterhead), "w+")
	thank_you.write(formatted)
	thank_you.close()
	print('\n')
	print("Thank you letter has been created")
	print('\n')


def create_report():
	#print(donor_list[0].ljust(20) + donor_list[1].ljust(10) + donor_list[2].ljust(20) + donor_list[3].ljust(8))
	# print(donor_list[0].ljust(20))
	print('\n')
	print("Donor Name".ljust(28) + '|'.ljust(2) + "Total Given" + '|'.rjust(2) + "Num Gifts".rjust(10) + "|".ljust(2) + "Average Gift")
	print('-' * 70)

	names_list = list(donors.keys())
	names_list.sort()

	for name in names_list:
		index = names_list.index(name)
		name = names_list[index]
		donor = donors[name]
		date = donor[0][0]
		total = 0
		num_gifts = 0
		for donation in donor:
			total += donation[1]
			num_gifts += 1
		average = int(total / num_gifts)

		name_length = len(name)
		
		print((name).ljust(30) + '$'.ljust(2) + str(total).ljust(15) + str(num_gifts).ljust(10) + '$'.ljust(2) + str(round(average, 2)))

	print('\n')


def send_letter_all():
	text = "Dear {},\n Thank you very much for your very kind donation of ${}.\n It will be put to good use.\n Sincerely,\n-The Team"

	for donor in donors:
		name = donor
		donation = donors[donor]
		amount = donation[0][1]
		date = donation[0][0]
		write_letters(name, amount,date)


	# write to the template

	
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
		response = int(input(prompt + "\n")) # continuously colelct user selection
		# now redirect to feature functions based on the user selection
		try:
			arg_dict.get(response)()
		except:
			print("Error")


if __name__ == "__main__":
	main()
#/usr/bin/env python3
import sys

donors = [
	#The actual donations themselves are a list of objects: Donations.date and Donations.amount
	{
		"first_name": "John",
		"last_name": "Quigley",
		"address": "555 Camelot RD N London, Ontario",
		"donations": 
			[
				("2019-02-04", 5000.00),
				("2019-02-04", 4250.00),
				("2019-02-04", 3000.00)
		
			]
	},
	{
		"first_name": "Sara",
		"last_name": "Smith",
		"address": "256 Camden RD N London, UK",
		"donations": [
			("2020-04-02", 2000.00),
			("2019-02-04", 42000.00),
			("2019-02-04", 32000.00)
		]
	},
	{
		"first_name": "Jacob",
		"last_name": "van der Schmidt",
		"address": "2001 Space Oddysey RD SW Los Angeles, CA",
		"donations":[
			("2012-04-20", 20.00),
			("2019-02-04", 2000.00),
			("2019-02-04", 3400.00)
		]
	},
	{
		"first_name": "Jason",
		"last_name": "Quigley",
		"address": "12 Camden RD N London, UK",
		"donations": [
			("2012-02-04", 12.00),
			("2013-02-04", 240.00),
			("2014-02-05",120.00)
		]
	},
	{
		"first_name": "Ogden",
		"last_name": "Nash",
		"address": "256 Camden RD N London, UK",
		"donations": [
			("2019-02-04", 5000000.00),
			("2019-02-04", 500000.00),
			("2019-02-04", 50000.00)
		]
	}
]

def send_thank_you(first_name='', last_name=''):
	list = input("Type `list` for a list of donors or press the carriage key to skip\n")
	if list == "list":
		print('\n')
		for donor in donors:
			print(donor['first_name'], donor['last_name'])
		print('\n')
		return
	else:
		pass

	first_name = input('What is the first name of the donor?\n').title()
	last_name = input('What is the last name of the donor?\n').title()


	for donor in donors:
		if donor['first_name'] ==  first_name and donor['last_name'] == last_name:
			amount = donor['donations'][0][1]
			date = donor['donations'][0][0]
			write_letters(first_name, last_name, amount, date)
			return
		else:
			print("We are unable to locate that donor")
			return

def write_letters(first_name, last_name, amount, date):	

	text = "Dear {} {},\n\n    Thank you for your donation in the amount of {} on {}. Please keep this letter for your records.\n\n"

	letterhead = "{}_{}.txt".format(first_name, last_name)
	# open a letter template
	formatted = text.format(first_name, last_name, date, amount)
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

	donor_list = []
	for donor in donors:
		first_name = donor['first_name']
		last_name = donor['last_name']
		total = 0
		# get total
		amount = []
		donations = donor['donations']
		for num in donations:
			amount.append(num[1])
		total += sum(amount)
		num_gifts = len(amount)
		average = total / num_gifts

		name_length = len(first_name) + len(last_name)
		
		print((first_name + ' ' + last_name).ljust(30) + '$'.ljust(2) + str(total).ljust(15) + str(num_gifts).ljust(10) + '$'.ljust(2) + str(round(average, 2)))

	print('\n')


def send_letter_all():
	text = "Dear {} {},\n Thank you very much for your very kind donation of ${}.\n It will be put to good use.\n Sincerely,\n-The Team"

	for donor in donors:
		write_letter(donor['first_name'], donor['last_name'], donations[0][1], donations[0][0])

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
		arg_dict.get(response)()


if __name__ == "__main__":
	main()
#/usr/bin/env python3
import datetime

donors = [
	#The actual donations themselves are a list of objects: Donations.date and Donations.amount
	{
		"first" : "John",
		"last" : "Quigley",
		"address" : "555 Camelot RD N London, Ontario",
		"donations" : [
			{
				"date" : "2019-02-04",
				"amount" : 5000.00
			},
			{
				"date" : "2019-02-04",
				"amount" : 4250.00
			},
			{
				"date" : "2019-02-04",
				"amount" : 3000.00
			}
		]
	},
	{
		"first" : "Sara",
		"last" : "Smith",
		"address" : "256 Camden RD N London, UK",
		"donations" : [
			{
				"date" : "2020-04-02",
				"amount" : 2000.00
			},
			{
				"date" : "2019-02-04",
				"amount" : 42000.00
			},
			{
				"date" : "2019-02-04",
				"amount" : 32000.00
			}
		]
	},
	{
		"first" : "Jacob",
		"last" : "van der Schmidt",
		"address" : "2001 Space Oddysey RD SW Los Angeles, CA",
		"donations" : [
			{
				"date" : "2012-04-20",
				"amount" : 20.00
			},
			{
				"date" : "2019-02-04",
				"amount" : 2000.00
			},
			{
				"date" : "2019-02-04",
				"amount" : 3400.00
			}
		]
	},
	{
		"first" : "Jason Quigley",
		"last" : "Quigley",
		"address" : "12 Camden RD N London, UK",
		"donations" : [
			{
				"date" : "2012-02-04",
				"amount" : 12.00
			},
			{
				"date" : "2013-02-04",
				"amount" : 240.00
			},
			{
				"date" : "2014-02-05",
				"amount" : 120.00
			}
		]
	},
	{
		"first" : "Ogden",
		"last" : "Nash",
		"address" : "256 Camden RD N London, UK",
		"donations" : [
			{
				"date" : "2019-02-04",
				"amount" : 5000000.00
			},
			{
				"date" : "2019-02-04",
				"amount" : 500000.00
			},
			{
				"date" : "2019-02-04",
				"amount" : 50000.00
			}
		]
	}
]

def total_amount():
	total = 0
	for donation in donor['donations']:
		total += int(donation['amount'])
	return total

def lookup(first_name, last_name):
	for donor in donors:
		if donor['first'] == first_name and donor['last'] == last_name:
			return donor
		else:
			print("That donor is not on the list")
			main()


#def create_report():

def send_thank_you():
	# prompt = input("Type 'list' to see the donors, or lookup to find donors by name\n")
	# if prompt == "list":
	# 	names = [ f"{donor['first']} {donor['last']}" for donor in donors]
	# 	for name in names:
	# 		print(name) 
	# elif prompt == "lookup":
	# 	first_name = input('What is the first name of the donor?\n')
	# 	last_name = input('What is the last name of the donor?\n')
	first_name = input('What is the first name of the donor?\n').title()
	last_name = input('What is the last name of the donor?\n').title()
	donor = lookup(first_name, last_name)
	amount = input("How much has the donor just given?")	
	donor['donations'].append({
		"date" : "{}".format(datetime.date.today()),
		"amount": amount
	})
	date = (donor['donations'][-1]['date'])
	print(f"Dear {first_name} {last_name}. Thank you for your donation in the amount of ${amount} on {date}. Please keep this letter for your records.")


def create_report():
	donor_list = []
	for donor in donors:
		total = 0
		num_gifts = 0
		for donation in donor['donations']:
			num_gifts += 1
			total += int(donation['amount'])
		average_gift = round(total / num_gifts, 2)
		donor_list.append([donor['first'], donor['last'], total, num_gifts, average_gift])
	donor_list.sort(key = lambda donor_list: donor_list[2])
	donor_list = donor_list[::-1]

	#print(donor_list[0].ljust(20) + donor_list[1].ljust(10) + donor_list[2].ljust(20) + donor_list[3].ljust(8))
	# print(donor_list[0].ljust(20))
	print("Donor Name".ljust(28) + '|'.ljust(2) + "Total Given" + '|'.rjust(2) + "Num Gifts".rjust(10) + "|".ljust(2) + "Average Gift")
	print('-' * 70)

	for donor in donor_list:
		print(str((donor[0]) + ' ' + str(donor[1])).ljust(30) + '$'.ljust(2) + str(donor[2]).ljust(15) + str(donor[3]).ljust(10) + '$'.ljust(2) + str(donor[4]))
	print("\n")

	main()


def main():
	select = input("Would you like to:\na: Send a Thank You\nb: Create a Report\nc: quit\n(Type either a, b, or c, then press enter)\n").lower()
	if select not in ['a', 'b', 'c']:
		print("Come again?\n")
		main()

	if select == 'a':
	 	send_thank_you()
	elif select == 'b':
		print(create_report())
	elif select == 'c':
		quit()


	
if __name__ == "__main__":
	main()
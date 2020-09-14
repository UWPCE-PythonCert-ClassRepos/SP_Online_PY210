#/usr/bin/env python3
import sys
import donor_models


Donor = donor_models.Donor

names = "John Quigley", 
donors = ["John Quigley", "Sara Smith", "Jacob van der Schmidt", "Ogden Nash"]

Donor()

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


# donors = {
# 	"John Quigley": [
# 		("2019-02-04", 5000.00),
# 		("2019-02-04", 4250.00),
# 		("2019-02-04", 3000.00)
# 	],

		# names_list = list(donors.keys())

		# _list = input("Type `list` for a list of donors or press the carriage key to skip\n")
		# if _list == "list":
		# 	for donor in names_list:
		# 		print(donor)
		# 	print('\n')
		# else:
		# 	pass

		# # for send_thank_you()
		# name = input('What is the name of the donor?\n').title()

#/usr/bin/env python3
import sys

# write_letter mixin, since both Donor() and DonorCollection() use it
class write_letter_mixin():

	def write_letter(self):
		text = "Dear {},\n\n    Thank you for your donation in the amount of {} on {}. Please keep this letter for your records.\n\n"

		letterhead = "{}.txt".format(self.name).replace(" ", "_")
		# open a letter template
		formatted = text.format(self.name, self.amount, self.date)

		make_letter(letterhead, formatted)
		return formatted


class Donor():
	# Anything dealing with a single donor, such as
	# send_thank_you()

	def __init__(self, params): # ex "John Quigley", "2019-02-04", 5000.00
		# create a dictionary like so:
		# {
		# "John Quigley": [
		# 	("2019-02-04", 5000.00),
		# 	("2019-02-04", 4250.00),
		# 	("2019-02-04", 3000.00)
		# ],
		# }
		# the name will be the key
		self.name = { params.get('name'): [] }
		# the date and amount will append as tuples to a list
		list_key = next(iter(self.name))
		list_ = self.name[list_key]
		list_.append(tuple((params.get('date'), params.get('amount'))))

	#getter 
	@property 
	def donor_name(self):
		name = next(iter(self.name))
		print("Donor's name is {}".format(name))

	@property
	def dates(self):
		#name of donor
		list_key = next(iter(self.name))
		list_ = self.name[list_key]
		name = list_key
		dates = [entry[0] for entry in list_]
		
		print("{} donated on these dates: ".format(name))
		for date in dates:
			print(date)

	@property
	def amounts(self):
		#name of donor
		list_key = next(iter(self.name))
		list_ = self.name[list_key]
		name = list_key
		amounts = [entry[1] for entry in list_]
		
		print("\n{} donated these amounts ".format(name))
		for amount in amounts:
			print(str(amount) + "\n")
		print("For a total of:")
		print(sum([amount for amount in amounts]))
		print()

	# #setter
	# # update a donor with a donation
	# @name.setter
	# def name(self, value):
	# 	self.name = value
	# # edit the 
	# @amount.setter
	# def amount(self, value):
	# 	self.amount = value











	def __repr__(self):
		return "Donor()"

	def __str__(self):
		return "{}".format(self.name)


	# def send_thank_you(self):
	# 	write_letters(self.name, self.amount,self.date)





	#{"John Quigley", "2019-02-04", 5000.00}


	
	# @date.setter
	# def date(self, value):
	# 	self.date = value
	# #edit the donor name

	#deleter
	# @name.deleter
	# def name(self):
	# 	del self.name
	# @date.deleter
	# def date(self):
	# 	del self.date
	# @amount.deleter
	# def amount(self):
	# 	del self.amount


#class DonorCollection(Donor):
	# send_letter_all()
	# create_report()
		# print_heading()
		# print_info()
	# works with Donor objects
	#Anything relating to multiple donors goes here
	#holds all donor objects

	# holds code that generates reports about multiple donors //run create_report() on multiple donors

	# 


# donors = {
# 	"John Quigley": [
# 		("2019-02-04", 5000.00),
# 		("2019-02-04", 4250.00),
# 		("2019-02-04", 3000.00)
# 	],

a = Donor({'name': "John Quigley", 'date': "2019-02-04", 'amount': 5000.00})
#print(a)
#print(a.name)
print(a.donor_name)
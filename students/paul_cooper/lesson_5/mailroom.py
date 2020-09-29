Mike_Tomlin = [164.33, 175.00, 750,50]
Bill_Gates = [100000.00]
Charles_Barkley = [1130.80, 100.00]
Bill_Clinton = [250.00, 800.00, 1200.00]
Rosanne_Barr = [86.98, 124.30]
Donors_names = ['Mike Tomlin', 'Bill Gates', 'Charles Barkley', 'Bill Clinton', 'Rosanne Barr']
Donnors_dict = {'Mike Tomlin': Mike_Tomlin,
				'Bill Gates': Bill_Gates,
				'Charles Barkley': Charles_Barkley,
				'Bill Clinton': Bill_Clinton,
				'Rosanne Barr': Rosanne_Barr}

# this will allow a person to donate and automaticly generate a thankyou letter
def send_a_thankyou():
	print('Send a Thank You card')
	users_thank_choice = input('Please enter a full name or type list: ')
	if users_thank_choice == 'list':
		print(Donors_names)
		send_a_thankyou()
		

	elif users_thank_choice in Donors_names:
		donation_amount = input('Enter the donation amount: ')
		while True:
			try:
				donation_amount = float(donation_amount)
				Donnors_dict[users_thank_choice].extend([donation_amount])
				break
			except ValueError:
				print("That is not a number! ")
				donation_amount = input('Enter the donation amount: ')
				continue


	else:
		donation_amount = input('Enter the donation amount: ')
		while True:
			try:
				donation_amount = float(donation_amount)
				Donors_names.append(users_thank_choice)
				Donnors_dict[users_thank_choice] = [donation_amount]
				break
			except ValueError:
				print("That is not a number! ")
				donation_amount = input('Enter the donation amount: ')
				continue

	
	letter = 'Thank you so much {} for the generous donation of ${:.2f}'.format(users_thank_choice, donation_amount)
	print(letter)
	maincode()
	

# creates a report of the donors, total amout given, number of gifts, and average amout given
def create_a_report():
	donor_total = []
	donor_ave = []
	donor_length = []
	count = 0

	for j in Donnors_dict:
		total = sum(Donnors_dict[j])
		print(total)
		donor_total.append(total)
		donor_length.append(len(Donnors_dict[j]))
		ave = total/donor_length[count]
		donor_ave.append(ave)
		count += 1


	print('{:22}{:>10}{:10}{:>10}'.format('Donor Name ','| Total Given |',' Num Gifts |',' Average Gift'))

	print('-' * 64)
	for x in range(len(Donors_names)):
		print('{:24}{}{:>10.2f}{:12}{:>4}{:>10.2f}'.format(Donors_names[x], '$', donor_total[x], donor_length[x], '$', donor_ave[x]))
	maincode()

#this will send out thand you letters to all that have donated
def write_to_all():
	for name in Donors_names:
		name = name.replace(' ','_')
		with open('{}.txt'.format(name), 'w') as f:
			name = name.replace('_', ' ')
			f.write('Thank you so much {} for the generous donation.'.format(name))
			f.close()
	print("Files have been written")
	maincode()




if __name__ == '__main__':
	def maincode():
		print('menu: ''\n' , '1: Send a Thank You','\n'' 2: Create a Report', '\n',
			'3: Write txt file to all', '\n', '4: quit')
		choice = input('Please enter # 1, 2, 3, or 4: ')
		while choice != '1' and choice != '2' and choice != '3' and choice != '4':
			print('Invalad choice please choose again')
			choice = input('Please enter # 1, 2, 3, or 4: ')

		menu_choice_dict = {'1': send_a_thankyou, '2': create_a_report, '3': write_to_all,  '4': exit}
		menu_choice_dict.get(choice)()

maincode()







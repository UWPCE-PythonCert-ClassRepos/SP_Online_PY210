Mike_Tomlin = [164.33, 175.00, 750,50]
Bill_Gates = [100000.00]
Charles_Barkley = [1130.80, 100.00]
Bill_Clinton = [250.00, 800.00, 1200.00]
Rosanne_Barr = [86.98, 124.30]
Donors = [Mike_Tomlin, Bill_Gates, Charles_Barkley, Bill_Clinton, Rosanne_Barr]
Donors_names = ['Mike Tomlin', 'Bill Gates', 'Charles Barkley', 'Bill Clinton', 'Rosanne Barr']



def send_a_thankyou():
	print('Send a Thank You card')
	users_thank_choice = input('Please enter a full name or type list: ')
	if users_thank_choice == 'list':
		print(Donors_names)
		users_thank_choice = input('Please enter a full name: ')

	elif users_thank_choice in Donors_names:
		pass

	else:
		Donors_names.append(users_thank_choice)
		add_to_donors = users_thank_choice.replace(' ','_')
		add_to_donors = []
		Donors.append(add_to_donors)
		
	donation_amount = input('Enter the donation amount: ')
	donation_amount = float(donation_amount)
	for i in Donors:
		if Donors.index(i) == Donors_names.index(users_thank_choice):
			i.insert(0 , donation_amount)
	
	#print(Donors_names)
	#print(Donors)

	letter = 'Thank you so much {} for the generous donation of ${:.2f}'.format(users_thank_choice, donation_amount)
	print(letter)
	maincode()
	



def create_a_report():
	donor_total = []
	donor_ave = []
	for j in Donors:
		total = sum(j)
		donor_total.append(total)
		ave = total/len(j)
		donor_ave.append(ave)

	print('{:22}{:>10}{:10}{:>10}'.format('Donor Name ','| Total Given |',' Num Gifts |',' Average Gift'))

	print('-' * 64)
	for x in range(len(Donors_names)):
		print('{:24}{}{:>10.2f}{:12}{:>4}{:>10.2f}'.format(Donors_names[x], '$', donor_total[x], len(Donors[x]), '$', donor_ave[x]))

	#print(donor_total)
	#print(donor_ave)
	maincode()



if __name__ == '__main__':
	def maincode():
		print('menu: ''\n' , '1: Send a Thank You','\n'' 2: Create a Report', '\n',
			'3: Quit')
		choice = input('Please enter # 1, 2, or 3: ')
		while choice != '1' and choice != '2' and choice != '3':
			print('Invalad choice please choose again')
			choice = input('Please enter # 1, 2, or 3: ')
		if choice == '1':
			send_a_thankyou()
		if choice == '2':
			create_a_report()
		if choice == '3':
			print("quitting")
			exit()

maincode()







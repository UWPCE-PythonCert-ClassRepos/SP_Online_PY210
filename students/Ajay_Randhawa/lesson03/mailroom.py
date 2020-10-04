#Lesson 3 assignment
#Initial donor list
donorlist = [("William Gates", [150, 2, 75]), ("Mark Zuckerburg", [300, 3, 100]), ("Jeff Bezos", [100, 2, 50]),("Paul Allen", [200, 2, 100]), ("Elon Musk", [500, 2, 250])]

#Prompt Text
prompt = "\n".join(("Please choose from the below options",
	"1 - Send a Thank You", 
	"2 - Create a Report", 
	"3 - Quit",
	">>> "))

def send_thankyou():
	#Store input from user
	response = input("Enter Full Name:")
	donorlist_names = []
	for i in range(len(donorlist)):
		donorlist_names.append(donorlist[i][0])
	#displays the list of all donors if the user inputs list
	#inital value of 'found' set to 0.
	found = 0
	if response == "list":
		print(donorlist_names)
		print('\n')
		#variable "found" is set when a known function is called and not a name of the donor.
		found = 1
	#scrolling through the list to find a match
	#storing the donation amount and updating the database
	for i in range(len(donorlist)):
		#'found1' value of '0' tells that its a new donor
		#Case where the name already exists in donorlist
		found1 = 0
		if response == donorlist_names[i]:
			#if donor name is found in the database, 'found1' variable is updated to 1.
			found1 = 1
			response1 = input("Donation amount:")
			response1 = int(response1)
			#update to the Total Amount Given
			donorlist[i][1][0] =  donorlist[i][1][0] + response1
			#Update to the Num of Gifts
			donorlist[i][1][1] = donorlist[i][1][1] + 1
			#Update to the average amount
			donorlist[i][1][2] = round(((donorlist[i][1][2])*((donorlist[i][1][1])-1) + response1)/donorlist[i][1][1])
			#Thank you email using f strings
			name = donorlist[(i)][0]
			amount = response1
			print('\n')
			print(f'Thank you {name} for your generous donation of {amount}')
			print('\n')
			break
	#if the value of found and found1 is 1, we know to create a new user in the donorlist
	#case where name does not exist in donor list
	if (found or found1) == 0:
		donorlist.append(tuple())
		donorlist[len(donorlist)-1] += (response, [0,0,0])
		j = len(donorlist)
		response2 = input("Donation amount:")
		response2 = int(response2)
		donorlist[(j-1)][1][0] = int(donorlist[(j-1)][1][0])
		#update to the Total Amount Given
		donorlist[(j-1)][1][0] = donorlist[(j-1)][1][0] + response2
		#Update to the Num of Gifts
		donorlist[(j-1)][1][1] = donorlist[(j-1)][1][1] + 1
		#Update to the average amount
		donorlist[(j-1)][1][2] = donorlist[(j-1)][1][0]
		#Thank you email using f strings
		name = donorlist[(j-1)][0]
		amount = response2
		print('\n')
		print(f'Thank you {name} for your generous donation of {amount}')
		print('\n')
		


def create_report():
	# defining common symbols
	symbol = '$'
	symbol1 = '|'
	#displaying header text for the table
	string_header = '{:19}{:1}{:13}{:1}{:10}{:1}{:10}'.format("Donor Name", symbol1, " Total Given ", symbol1, " Num Gifts ", symbol1, " Average Gift ")
	print("\n")
	print(string_header)
	print("-----------------------------------------------------------")
	#printing the values in the donorlist
	for i in range(len(donorlist)):
		string = '{:20}{:>2}{:10}{:11}{:>5}{:11}'.format(donorlist[i][0], symbol, donorlist[i][1][0], donorlist[i][1][1], symbol, donorlist[i][1][2])
		print(string)
	print("\n")

def exit_program():
	#exits the script
	print("Exiting....")
	sys.exit()


def main():
	while(True):
		response = input(prompt)
		#redirect to feature functions based on user selections
		if response == "1":
			send_thankyou()
		elif response == "2":
			create_report()
		elif response == "3":
			exit_program()
		else:
			print("Not a valid option! \n")


if __name__ == "__main__":
	main()

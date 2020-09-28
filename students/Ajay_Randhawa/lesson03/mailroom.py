donorlist = [("William Gates", [150, 2, 75]), ("Mark Zuckerburg", [300, 3, 100]), ("Jeff Bezos", [100, 2, 50]),("Paul Allen", [200, 2, 100]), ("Elon Musk", [500, 2, 250])]

prompt = "\n".join(("Please choose from the below options",
	"1 - Send a Thank You", 
	"2 - Create a Report", 
	"3 - Quit",
	">>> "))

def send_thankyou():
	response = input("Enter Full Name:")
	donorlist_names = []
	for i in range(len(donorlist)):
		donorlist_names.append(donorlist[i][0])
	print(donorlist_names)
	print(donorlist)
	
	if response == "list":
		print(donorlist_names)
	for i in range(len(donorlist)):
		found = 0
		if response == donorlist_names[i]:
			found = 1
			response1 = input("Donation amount:")
			response1 = int(response1)
			donorlist[i][1][0] =  donorlist[i][1][0] + response1
			donorlist[i][1][1] = donorlist[i][1][1] + 1
			donorlist[i][1][2] = round(((donorlist[i][1][2])*((donorlist[i][1][1])-1) + response1)/donorlist[i][1][1])
			name = donorlist[(i)][0]
			amount = response1
			print(f'Thank you {name} for your generous donation of {amount}')
			break
	if found == 0:
		donorlist.append(tuple())
		donorlist[len(donorlist)-1] += (response, [0,0,0])
		print(donorlist)
		print(donorlist[len(donorlist)-1])
		j = len(donorlist)
		response2 = input("Donation amount:")
		response2 = int(response2)
		donorlist[(j-1)][1][0] = int(donorlist[(j-1)][1][0])
		donorlist[(j-1)][1][0] = donorlist[(j-1)][1][0] + response2
		donorlist[(j-1)][1][1] = donorlist[(j-1)][1][1] + 1
		donorlist[(j-1)][1][2] = donorlist[(j-1)][1][0]
		name = donorlist[(j-1)][0]
		amount = response2
		print(f'Thank you {name} for your generous donation of {amount}')
		


def create_report():
	symbol = '$'
	symbol1 = '|'
	string_header = '{:19}{:1}{:13}{:1}{:10}{:1}{:10}'.format("Donor Name", symbol1, " Total Given ", symbol1, " Num Gifts ", symbol1, " Average Gift ")
	print("\n")
	print(string_header)
	print("-----------------------------------------------------------")
	for i in range(len(donorlist)):
		string = '{:20}{:>2}{:10}{:11}{:>5}{:11}'.format(donorlist[i][0], symbol, donorlist[i][1][0], donorlist[i][1][1], symbol, donorlist[i][1][2])
		print(string)
	print("\n")

def exit_program():
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

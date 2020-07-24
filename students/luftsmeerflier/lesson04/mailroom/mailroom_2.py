#/usr/bin/env python3

import benefactors

def write_letter(benefactor, first_name, last_name):
	letterhead = "{}_{}.txt".format(first_name, last_name)
	# open a letter template
	letter = open('./thank_you.txt')
	formatted = letter.read().format(**benefactor)
	letter.close()
	# write to the template
	thank_you = open("{}".format(letterhead), "w+")
	thank_you.write(formatted)

def send_thanks():
	first_name = input('What is the first name of the benefactor? ')
	last_name = input('What is the surname of the benefactor? ')

	for benefactor in benefactors.list:
		if first_name in benefactor.values() and last_name in benefactor.values():
			write_letter()
			print("\n\n*****Letter has printed*****\n\n")
			get_input()

		else:
			print("try that again")
			send_thanks()

# 
def create_report():
	for benefactor in benefactors.list:
		print("{first_name} {last_name} donated {amount}\n".format(**benefactor))

#
def send_letter_all():
	for benefactor in benefactors.list:
		write_letter(benefactor, benefactor['first_name'], benefactor['last_name'])


def get_input():

	prompt = input("Choose an action:\n\n1 - Send Thank You to a single donor.\n2 - Create a Report.\n3 - Send letters to all donors.\n4 - Quit\n")

	if int(prompt) == 1:
		send_thanks()
	elif int(prompt) == 2:
		create_report()
	elif int(prompt) == 3:
		send_letter_all()
	elif int(prompt) == 4:
		exit()
	else:
		pass


def main():
	get_input()





	
if __name__ == "__main__":
	main()
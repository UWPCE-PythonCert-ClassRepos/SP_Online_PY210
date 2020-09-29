#!/usr/bin/env python3

data = [
    ["Tom Hanks", 1000, 500],
    ["Leonardo DiCaprio", 300, 1200, 500],
    ["Natalie Portman", 5000],
    ["Harrison Ford", 500, 2000, 100],
    ["Scarlett Johansson", 1500, 1000],
    ["Jennifer Aniston", 2000, 2000, 2000],
]

#Converting original list to dict
"""
for i in data:
    name = i[0]
	sumDonation = sum(i[1:])
	ind = (data.index(i)+1)
    print(("don0%i={'name':'%s','don':%i}")%(ind,name,sumDonation))
"""
"""
don01={'name':'Tom Hanks','don':1500}
don02={'name':'Leonardo DiCaprio','don':2000}
don03={'name':'Natalie Portman','don':5000}
don04={'name':'Harrison Ford','don':2600}
don05={'name':'Scarlett Johansson','don':2500}
don06={'name':'Jennifer Aniston','don':6000}
"""

def mailroom02(reply, action):
    while True:
	    resp = input(reply)
		if action[resp]()=="exit menu":
		    break

def print_list():
    print(don01['name'])
	print(don02['name'])
	print(don03['name'])
	print(don04['name'])
	print(don05['name'])
	print(don06['name'])

def add_donation():
    while True:
        print("Print 'list' to view donor names.")
        donName = str(input("Please enter full name of the donor: "))
        if donName == "list":
            for i in data:
                print(i[0])
        else:
            for i in data:
                if donName == i[0]:
                    donation = int(input("Please enter the donation amount: "))
                    i.append(donation)            
                    break
            else:
				newDonation = int(input("This is a new donor, please enter the donation amount: "))
				data.append([donName, newDonation])
				print("Letter for the donor: ")
                print("Hello {}, thank you for your generous donation of ${} to support our cause.".format(donName, newDonation))
            break    
	
def create_report():
    tags = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    print("{:20s}| {:10s} | {:10s} | {:10s}".format(*tags))
    print(("-")*61)
    for i in data:
        dname = (i[0])
        tgiven = sum(i[1:])
        ngifts = len(i[1:])
        agift = ((sum(i[1:]))/(len(i[1:])))
        data2 = (dname, tgiven, ngifts, agift)
        print("{:20s} $ {:10d}   {:10d}  $ {:.2f}".format(*data2))

def send_ty_note_all():
    for i in data:
	    filename = (i[0]+".txt")
		tDonation = sum(i[1:])
		import tempfile
		import os.path
		location = tempfile.gettempdir()
		lfile = os.path.join(location, filename)
		with open(lfile, "w") as f:
		    f.write("\nDear "+i[0]+",")
			f.write("\n"*2)
			f.write(" "*8+"Thank you for your very kind donation of $"+str(tDonation)+".")
			f.write("\n"*2)
			f.write(" "*8+"It will be put to very good use.")
			f.write("\n"*2)
			f.write(30*" "+"Sincerely,")
			f.write(34*" "+"-The Team")

def quit():
    print("Quiting this menu now!")
	return "exit menu"

def send_ty_note():
    mailroom02(send_ty_note_reply,send_ty_note_action)

def don01_letter():
	print(letter.format(**don01))


def don02_letter():
	print(letter.format(**don02))

def don03_letter():
	print(letter.format(**don03))

def don04_letter():
	print(letter.format(**don04))

def don05_letter():
	print(letter.format(**don05))

def don06_letter():
	print(letter.format(**don06))

letter = ("Hello {name}, thank you for your generous donation of ${don} to support our cause.")
main_reply = ("\nChoose an action:\n"
               "\n"
			   "1 - Send a Thank You note to a single donor.\n"
			   "2 - Add new donation.\n"
			   "3 - Create a Report.\n"
			   "4 - Send letters to all donors.\n"
			   "5 - To see the LIST of donor names.\n"
			   "q - Quit\n"			   
			   ">>>")

main_action = {"1":send_ty_note,
               "2":add_donation,
               "3":create_report,
			   "4":send_ty_note_all,
			   "5":print_list,
			   "q":quit
			   }
send_ty_note_reply = ("\nPlease enter full name.\n"
                    "q - to exit this menu.\n" 
                    ">>>")
send_ty_note_action = {"Tom Hanks":don01_letter,
                     'Leonardo DiCaprio':don02_letter,
					 'Natalie Portman':don03_letter,
					 'Harrison Ford':don04_letter,
					 'Scarlett Johansson':don05_letter,
					 'Jennifer Aniston':don06_letter,
					 "q":quit
                     }
argument = 1
don01={'name':'Tom Hanks','don':1500}
don02={'name':'Leonardo DiCaprio','don':2000}
don03={'name':'Natalie Portman','don':5000}
don04={'name':'Harrison Ford','don':2600}
don05={'name':'Scarlett Johansson','don':2500}
don06={'name':'Jennifer Aniston','don':6000}


if __name__=="__main__":
    mailroom02(main_reply, main_action)



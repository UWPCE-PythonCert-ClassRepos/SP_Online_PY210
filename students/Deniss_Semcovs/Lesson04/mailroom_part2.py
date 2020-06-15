#!/usr/bin/env python3
data = [
    ["Tom Hanks", 1000, 500],
    ["Leonardo DiCaprio", 300, 1200, 500],
    ["Natalie Portman", 5000],
    ["Harrison Ford", 500, 2000, 100],
    ["Scarlett Johansson", 1500, 1000],
    ["Jennifer Aniston", 2000, 2000, 2000],
]

def mailroom02(reply, action):
    while True:
	    resp = input(reply)
		if action[resp]()=="exit menu":
		    break
			
def sendTYnote():
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
                    print("Hello {}, thank you for your generous donation of ${} to support our cause.".format(donName, donation))
                    break
            else:
				newDonation = int(input("This is a new donor, please enter the donation amount: "))
				data.append([donName, newDonation])
				print("Letter for the donor: ")
                print("Hello {}, thank you for your generous donation of ${} to support our cause.".format(donName, newDonation))
            break

def createReport():
    tags = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    print("{:20s}| {:10s} | {:10s} | {:10s}".format(*tags))
    print(("-")*61)
    for i in data:
        dName = (i[0])
        tGiven = sum(i[1:])
        nGifts = len(i[1:])
        aGift = ((sum(i[1:]))/(len(i[1:])))
        data2 = (dName, tGiven, nGifts, aGift)
        print("{:20s} $ {:10d}   {:10d}  $ {:.2f}".format(*data2))

def sendTYnoteALL():
    for i in data:
	    name = i[0]
		tDonation = sum(i[1:])
		print(" ")
		print("Hello {}, thank you for your generous donation of ${} to support our cause.".format(name, tDonation))

def quit():
    print("Quiting this menu now!")
	return "exit menu"

main_reply = ("\nChoose an action:\n"
               "\n"
			   "1 - Send a Thank You to a single donor.\n"
			   "2 - Create a Report.\n"
			   "3 - Send letters to all donors.\n"
			   "4 - Quit\n"
			   ">>>")

main_action = {"1":sendTYnote,
               "2":createReport,
			   "3":sendTYnoteALL,
			   "4":quit
			   }


if __name__=="__main__":
    mailroom02(main_reply, main_action)
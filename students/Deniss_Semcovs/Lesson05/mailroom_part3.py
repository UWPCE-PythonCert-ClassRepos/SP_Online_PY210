#!/usr/bin/env python3

import tempfile
import os.path


def mailroom02(reply, action):
    while True:
        resp = input(reply)
        if action[resp]()=="exit menu":
            break
# Complerssed "list"
def print_list():
    [print(i["name"]) for i in donor]

def add_donation():
    while True:
        print("Print 'list' to view donor names or 'q' to quit.")
        full_name = str(input("Please enter full name of the donor: "))
        if full_name == "list":
            print_list()
        elif full_name == "q":
            break
        else:
            for i in data:
                if full_name == i[0]:
                    i.append(int(input("Please enter the donation amount: ")))            
                    break          
            else:
                new_donation = int(input("This is a new donor, please enter the donation amount: "))
                data.append([full_name, new_donation])
                print("Letter for the donor: ")
                print("Hello {}, thank you for your generous donation of ${} to support our cause.".format(full_name, new_donation))
            break    

def create_report():
    tags = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    print("{:20s}| {:10s} | {:10s} | {:10s}".format(*tags))
    print(("-")*61)
    for i in data:
        data2 = (i[0], sum(i[1:]), len(i[1:]), ((sum(i[1:]))/(len(i[1:]))))
        print("{:20s} $ {:10d}   {:10d}  $ {:.2f}".format(*data2))

def send_ty_note_all():
    for i in data:
        total_donation = sum(i[1:])
        letter_file = os.path.join(tempfile.gettempdir(), (i[0]+".txt"))
        with open(letter_file, "w") as f:
            f.write("\nDear "+i[0]+",")
            f.write("\n"*2)
            f.write(" "*8+"Thank you for your very kind donation of $"+str(total_donation)+".")
            f.write("\n"*2)
            f.write(" "*8+"It will be put to very good use.")
            f.write("\n"*2)
            f.write(30*" "+"Sincerely,")
            f.write(34*" "+"-The Team")
    print("<<< Letters have been created in the temp folder! >>>")

def quit():
    print("Quiting this menu now!")
    return "exit menu"

def send_ty_note():
    don_name = str(input("Enter donor's name: "))
    for i in donor:
        if don_name == i["name"]:
            print("Hello {}, thank you for your generous donation of ${} to support our cause.".format(i['name'], i['don']))
        else:
            print("The donor's name is not on the list")
            break
data = [
    ["Tom Hanks", 1000, 500],
    ["Leonardo DiCaprio", 300, 1200, 500],
    ["Natalie Portman", 5000],
    ["Harrison Ford", 500, 2000, 100],
    ["Scarlett Johansson", 1500, 1000],
    ["Jennifer Aniston", 2000, 2000, 2000],
]
# Generating dictionary from the list - complressed
donor = [{"name":i[0], "don":sum(i[1:])} for i in data]

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

#argument = 1

if __name__=="__main__":
    mailroom02(main_reply, main_action)



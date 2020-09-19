#!/usr/bin/env python3

import tempfile
import os.path

# KeyError exception added
def mailroom02(reply, action):
    while True:
        try:
            resp = input(reply)
            if action[resp]() is None or False:
                pass
            elif action[resp]() == "exit menu":
                break
        except KeyError:
            keyerror()
        except KeyboardInterrupt:
            keyboardinterrupt()

# Complerssed "list"
def print_list():
    new_data = dict_donor()
    [print(i["name"]) for i in new_data]

# add_donation() input function
def add_donation():
    print()
    full_name = str(input("Please enter 'list' to view donor names or 'q' to quit or full name of the donor: "))
    new_donation(full_name)
# add_donation() logic code + input
def new_donation(full_name):
    try:
        if full_name == "list":
            print_list()
        elif full_name == "q":
            return
        else:
            for i in data:
                if full_name == i[0]:
                    i.append(int(input("Please enter the donation amount: ")))            
                    print("Donation has been submitted! You can see new donation total in the report.")
                    return
                else:
                    new_donar(full_name)
    except ValueError:
        valueerror()
    except KeyboardInterrupt:
        keyboardinterrupt()
# new_donar() input function
def new_donar(full_name):
    new_don = int(input("This is a new donor, please enter the donation amount or 'q' to exit: "))
    if new_don == "q":
        return
    else:
        adding_donor(full_name, new_don)

# new_donar() logic code
def adding_donor(full_name, new_don):
    if new_don is None or False:
        pass
    else:
        data.append([full_name, new_don])
        print()
        print("Letter for the donor: ")
        print("Hello {}, thank you for your generous donation of ${} to support our cause.".format(full_name, new_don))
        return

def create_report():
    tags = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    print("{:20s}| {:10s} | {:10s} | {:10s}".format(*tags))
    print(("-")*61)
    new_data = dict_donor()
    report_data(new_data)
# create_report() data logic
def report_data(new_data):
    for i in new_data:
        data2 = (i["name"], i["don"], i["count"], i["average"])
        print("{:20s} $ {:10d}   {:10d}  $ {:.2f}".format(*data2))
# create files
def send_ty_note_all():
    for i in data:
        total_donation = sum(i[1:])
        letter_file = os.path.join(tempfile.gettempdir(), (i[0]+".txt"))
        d_name = i[0]
        create_letter(letter_file, d_name)
    print()
    print("<<< Letters have been created in the temp folder! >>>")
# writing text in created files
def create_letter(letter_file, d_name):
    with open(letter_file, "w") as f:
       f.write("\nDear "+d_name+" , thank you for your donation!")
#       f.write("\nDear "+i[0]+",")
#       f.write("\n"*2)
#       f.write(" "*8+"Thank you for your very kind donation of $"+str(total_donation)+".")
#       f.write("\n"*2)
#       f.write(" "*8+"It will be put to very good use.")
#       f.write("\n"*2)
#       f.write(30*" "+"Sincerely,")
#       f.write(34*" "+"-The Team")


def quit():
    return "exit menu"

#send_ty_note() input function
def send_ty_note():
    try:
        don_name = input("Enter donor's name: ")
        ty_note(don_name)              
    except KeyboardInterrupt:
        keyboardinterrupt()
#send_ty_note() logic code
def ty_note(don_name):
    new_data = dict_donor()
    for i in new_data:
        if don_name == i["name"]:
            print("Hello {}, thank you for your generous donation of ${} to support our cause.".format(i['name'], i['don']))
        else:
            print()
            print("The name you entered is not on the list!")
            return

# Generating dictionary data from the list
def dict_donor():
    donor = [{"name" : i[0], "don" : sum(i[1:]), "count" : len(i[1:]), "average" : ((sum(i[1:]))/(len(i[1:])))} for i in data]
    sort_donor = sorted(donor, key = lambda d: d["don"], reverse = True)
    return sort_donor

def valueerror():
    print()
    print("The donation amount has been incorrect or not entered.")
    print()

def keyerror():
    print()
    print("Wrong entery, please try again!")
    
def keyboardinterrupt():
    print()
    print("Keyboard interrupt doesn't work here ;)")
    print("please use apropriate method to exit this program")
    print(">>>> Hint: 'q'")

data = [
    ["Tom Hanks", 1000, 500],
    ["Leonardo DiCaprio", 300, 1200, 500],
    ["Natalie Portman", 5000],
    ["Harrison Ford", 500, 2000, 100],
    ["Scarlett Johansson", 1500, 1000],
    ["Jennifer Aniston", 2000, 2000, 2000],
]

main_reply = ("\nChoose an action: \n"
               "\n"
			   "1 - Send a Thank You note to a single donor.\n"
			   "2 - Add new donation.\n"
			   "3 - Create a Report.\n"
			   "4 - Send letters to all donors.\n"
			   "5 - To see the LIST of donor names.\n"
			   "q - Quit\n"			   
			   ">>>")

main_action = {"1" : send_ty_note,
               "2" : add_donation,
               "3" : create_report,
               "4" : send_ty_note_all,
               "5" : print_list,
               "q" : quit
               }

if __name__ == "__main__":
    mailroom02(main_reply, main_action)



# ------------------------------------------#
# !/usr/bin/env python3
# Title: mailroom_lab.py
# Desc: Assignment 1
# Tian Xie, 2020-04-10, Created File
# ------------------------------------------#

donor_list = []

def menu_selection(prompt, dispatch_dict):
    while True:
            response = input(prompt)  # continuously collect user selection
            if dispatch_dict[response]()== "Exit Menu":
                break

main_prompt = "\n".join(("-------------Main Menu-------------]\n",
          "Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Exit",
          ">>> "))

def send_thankyou():
    print("You selected the 1st option!")
    pass
def create_report():
    pass
def quit():
    print("Exiting the menu now")
    return "Exit Menu"

main_dispatch = {"1": send_thankyou,
               '2': create_report,
               '3': quit,
                 }

if (__name__ == '__main__'):
    menu_selection(main_prompt, main_dispatch)

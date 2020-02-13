#!/usr/bin/env python3


doners_list = [
    ['Bubbles Trailer',['150', '25', '300']],
    ['Julien Park',['25', '86']],
    ['Ricky Boys',['7', '3', '5']],
    ['Jack Anderson',['1001', '22', '45']],
    ['Lacey Coffin Greene',['750', '325', '1050']]
    ]

def start():
    action = input("Select a number to perform one of the following actions...\n"
                   "1. Send a Thank You Email \n"
                   "2. Create a Report \n"
                   "3. Quit \n")

    if action.isnumeric():
        action = int(action)
        if action > 3 or action < 1:
            print("Please select a number 1, 2 or 3")
            start()

        elif action == 1:
            send_thanks()

        elif action == 2:
            create_report()

        elif action == 3:
            print("Quitting program ....")
            return
    else:
        print("Please enter a numerical value")
        start()


def send_thanks():
    print("Sending Thanks")
    start()

def create_report():
    print("this is report option")
    start()


start()
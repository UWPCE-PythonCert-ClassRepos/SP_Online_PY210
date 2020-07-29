#!/usr/bin/env python3

"""
Lesson 3: Mail Room Part 1
Course: UW PY210
Author: Jason Jenkins
"""


# Global Variables
run_program = True


def send_thanks():
    response = ""
    while(True):
        print("You want to send a thank you.")
        response = input('Input persons full name or view list my inputing "list": ')

        if(response == "list"):
            print("Print the List of names")
        elif(response != ""):
            print(response)
            break
        else:
            break


def donate():
    print("add donation")


def create_report():
    print("create_report")


def startup_prompt():
    global run_program

    print()
    print("Do you want to:")
    print("\t1. Send a thank you")
    print("\t2. Create a report")
    print("\t3. Quit")

    response = input("Input number option you wish to do: ")

    # Add Error checking
    response = int(response)
    if(response == 1):
        send_thanks()
    elif(response == 2):
        create_report()
    elif(response == 3):
        run_program = False
    else:
        print(f"{response} is not a valid input.")


if __name__ == "__main__":
    # testing
    print("Program Started")
    while(run_program):
        startup_prompt()
    print("Program Completed")

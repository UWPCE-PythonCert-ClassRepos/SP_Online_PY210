#! /usr/bin/env python3

## Lesson 3.3 Mailroom Part 1
## By: B. Matthews
## 9/28/2020
## This is the first of a four-part assignment that will keep track of an imaginary charity's
## donors, the donation amounts, and will print a thank you message if desired.
## It's a bit simple, but will add more improvements later

import sys

prompt = "\n".join(("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nMailroom for Lazy Fundraisers\n",
          "Please choose an option:",
          "1) Send a Thank-you",
          "2) Create a Report",
          "3) Quit",
          "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n>>> "))

def exit_menu():
    print("Ok, get back to asking for donations.")
    sys.exit()  # exit the interactive script

def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        if response == "1":
            thanks()
        elif response == "2":
            report()
        elif response == "3":
            exit_menu()
        else:
            print("\n" * 100)
            print("Try again. What option?")

if __name__ == "__main__":
    main()
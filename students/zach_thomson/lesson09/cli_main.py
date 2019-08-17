#!/usr/bin/env python3
from donor_models import *
import sys

prompt = '\n'.join(('Welcome to the mailroom',
         'Please choose from the following options:',
         '1 - Send a Thank You',
         '2 - Create a Report',
         '3 - Quit',
         '> '))

#send a thank you tasks
def initial_input():
    ty_prompt = input('Please enter a full name or type list to see all the current donors: ')
    return ty_prompt


def thank_you():
    thank_you_logic(initial_input())


def thank_you_logic(name):
    if name.lower() == 'list':
        print('This will eventually print a list of donors')
    else:
        return Donor(name)


#Create a report tasks
def create_report():
    pass


#make a function to exit the program
def exit_program():
    print('Have a nice day!')
    sys.exit() # exit the interactive script


switch_dict = {1: thank_you,
               2: create_report,
               3: exit_program,
               }


def main():
    while True:
        response = input(prompt)
        switch_dict.get(int(response))()


if __name__ == "__main__":
    main()

from mailroom import Donor as D
from mailroom import DonorCollection as DC
import os.path as path


def thank_you(donor_collection):
    #Record single donation and thank donor
    fullname = input('What is the full name of the donor? Type list to see donors. Type exit to quit task \n')
    give_thanks(donor_collection,fullname)

def give_thanks(donor_collection,fullname):
    #Executes the thank you note, isolating data from input
    if fullname.lower() == 'list':
        #Print donor names
        print(donor_collection.print_donors())
    elif fullname.lower() == "exit":
        return None
    else:
        new_donation = float(input('What is the value of the donation (numbers only)?\n'))
        donor_collection.add_to_list(fullname,new_donation)
        #Print the thank you email
        print(thank_you_text(fullname))

def thank_all(donor_collection):
    #Generates .txt files of Thank Yous for all donors
    directory = input('What file path do you want the Thank You notes to be in? \n')
    many_thanks(donor_collection,directory)

def many_thanks(donor_collection,directory):
    #Try-except block ensures valid file path input
    try:
        for donor in donor_collection:
            filename = donor.name.replace(" ","") + ".txt"
            full_filename = path.join(directory,filename)
            with open(full_filename,'w') as f:
                f.write(thank_you_text(donor.name)) #same thing with donor.name
    except FileNotFoundError:
        print('File not found. Please enter an existing file path')
    except PermissionError:
        print('Permission error. Please enter a valid file path')

def thank_you_text(donor):
    return f'Dear {donor}, \n Thank you for your generous donation. We appreciate the support from people like you. \n Thank you,\n Charity Name'

def quit_program():
    #Terminates the program
    print('Goodbye!')
    exit()

def print_report(donor_collection):
    #Prints report
    print(donor_collection.create_report())


if __name__ == "__main__":

    #Donors
    donors = [D('Luke Skywalker',[10,20,30]),D('Leslie Knope',[100,300]),D('Dwight Schrute',[345,345345]),D('Freddie Mercury',[23532,32]),D('Jennifer Aniston',[235,2352])]
    donor_collection = DC()
    for person in donors:
        donor_collection.add_donor(person)

    #MAIN
    switch_dict = {1: thank_you, 2: print_report, 3: thank_all}

    while True:
        print("Options: \n 1 - Send a Single Thank You \n 2 - Create Report \n 3 - Send all donors Thank You \n 4 - Exit ")
        response = input('What would you like to do? Select a number\n')

        #Try-except block to catch user inputting a non-number
        try:
            response = int(response)
            if response in switch_dict:
                switch_dict[response](donor_collection)
                # Exit Program
            elif response == 4:
                quit_program()
            else:
                print('Number not recognized as an option')

        except ValueError:
            print('Please enter a whole number! No words or letters allowed')

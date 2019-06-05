import os.path as path

def thank_you(donor_dict):
    #Record single donation and thank donor
    fullname = input('What is the full name of the donor? Type list to see donors. Type exit to quit task \n')
    give_thanks(donor_dict,fullname)

def give_thanks(donor_dict, fullname):
    #Executes the thank you note, isolating data from input
    if fullname.lower() == 'list':
        print(list(donor_dict.keys()))
    elif fullname.lower() == "exit":
        return None
    else:
        new_donation = float(input('What is the value of the donation (numbers only)?\n'))
        add_to_list(donor_dict,fullname,new_donation)
        #Print the thank you email
        print(thank_you_text(fullname))

def add_to_list(donor_dict,fullname,new_donation):
    # Find donor in list or create a new one
    if fullname not in donor_dict:
        donor_dict[fullname] = []
    donor_dict[fullname].append(new_donation)

def calculate_report(name,donor_dict):
    #Calculate key metrics for donor report
    donations = len(donor_dict[name])
    # Add up all donations
    total_given = sum(donor_dict[name])
    avg_gift = total_given / donations
    return total_given,donations, avg_gift

def create_report(donor_dict):
    # Create report data from donor list
    format_report(*form_report(donor_dict))

def form_report(donor_dict):
    #Use a comprehension to create the report
    donor_report = dict()
    donor_report = {name : calculate_report(name,donor_dict) for name in donor_dict}
    name_lst = list(donor_report.keys())
    name_lst_sorted = sorted(name_lst, key = lambda name:donor_report[name][0],reverse=True)
    return name_lst_sorted, donor_report

def format_report(name_lst_sorted, donor_report):
    # Format report
    header = ['Name', 'Total Given', '# of Gifts', 'Average Gift']
    header_format = "{:<20}" + "{:^15}" + "{:^15}" + "{:^10}"
    row_name_format = "{:<20}"
    row_data_format = "${:>15.2f}" + "{:^15}" + "${:>10.2f}"

    print(header_format.format(*header))
    print('-' * 70)
    for name in name_lst_sorted:
        print(row_name_format.format(name) + row_data_format.format(*donor_report[name]))

def thank_all(donor_dict):
    #Generates .txt files of Thank Yous for all donors
    directory = input('What file path do you want the Thank You notes to be in? \n')
    many_thanks(donor_dict,directory)

def many_thanks(donor_dict,directory):
    #Try-except block ensures valid file path input
    try:
        for donor in donor_dict:
            filename = donor.replace(" ","") + ".txt"
            full_filename = path.join(directory,filename)
            with open(full_filename,'w') as f:
                f.write(thank_you_text(donor))
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

if __name__ == "__main__":

    #Donors
    donor_dict = {'Luke Skywalker':[10,20,30], 'Leslie Knope':[100,300],'Dwight Schrute':[345,345345],'Freddie Mercury':[23532,32],'Jennifer Aniston':[235,2352]}

    #MAIN
    switch_dict = {1: thank_you, 2: create_report, 3: thank_all}

    while True:
        print("Options: \n 1 - Send a Single Thank You \n 2 - Create Report \n 3 - Send all donors Thank You \n 4 - Exit ")
        response = input('What would you like to do? Select a number\n')

        #Try-except block to catch user inputting a non-number
        try:
            response = int(response)
            if response in switch_dict:
                switch_dict[response](donor_dict)
                # Exit Program
            elif response == 4:
                quit_program()
            else:
                print('Number not recognized as an option')

        except ValueError:
            print('Please enter a whole number! No words or letters allowed')


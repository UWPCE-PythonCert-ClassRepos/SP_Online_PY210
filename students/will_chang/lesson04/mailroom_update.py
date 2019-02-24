import datetime
import os.path
import pathlib

initial_donor_list = [
    {"name": "Warren Buffett", "total_don": 650.00, "number_don": 2, "avg_don": 325.00},
    {"name": "Jack Bogle", "total_don": 15000.50, "number_don": 1, "avg_don": 15000.50},
    {"name": "William Boeing", "total_don": 450.45, "number_don": 3, "avg_don": 150.15},
    {"name": "George Clooney", "total_don": 10000.00, "number_don": 2, "avg_don": 5000.00},
    {"name": "Orville Wright", "total_don": 95000000.00, "number_don": 1, "avg_don": 950000.00}
]

def list_data():
    """Provides formatted and updated list of donors, total donations, number of donations, and average donation."""
    global initial_donor_list
    initial_donor_list = sorted(initial_donor_list, key=lambda x: x["total_don"], reverse = True)
    max_len_str = [0]*4 # List providing the lengths of the longest items in each column

    for row in initial_donor_list: # Loop to fill in max_len_str with lengths of the longest items in each column
        count = 0
        for item in row:
            if len(str(row[item])) > max_len_str[count]:
                max_len_str[count] = len(str(row[item]))
            count += 1
                
    format_string = f'{{:<{max_len_str[0]+10}}}${{:<{max_len_str[1]+9}}}{{:<{max_len_str[2]+15}}}${{:<{max_len_str[3]+10}}}' # Format string taking into account the longest item in each column.
    format_string_header = f'{{:<{max_len_str[0]+10}}}{{:<{max_len_str[1]+10}}}{{:<{max_len_str[2]+15}}}{{:<{max_len_str[3]+10}}}'
    print("\n")
    print(format_string_header.format(*("Donor Name", "Total Given", "Num Gifts", "Average Gift")))
    print("-"*(max_len_str["name"]+max_len_str["total_don"]+max_len_str["number_don"]+max_len_str["avg_don"]+39))
    for row in initial_donor_list:
        print(format_string.format(*row.values()))

def thank_you():
    """Prompts user to input new donor information."""
    ask_name = input("\nPlease enter a full name or type 'list' for a list of the donor names: ")
    name_in_list = False
    while ask_name.lower() == "list":
        print([donor["name"] for donor in initial_donor_list])
        ask_name = input("\nPlease enter a full name or type 'list' for a list of the donor names: ")
    for donor in initial_donor_list:
        if ask_name == donor["name"] : # Check if the entered name is already in the list
            name_in_list = True
            ask_donor = float(input("Please enter a donation amount: "))
            donor["total_don"] += ask_donor
            donor["number_don"] += 1
            donor["avg_don"] = donor["total_don"]/donor["number_don"]
            print("\nDear {},\n\nThank you for your generous donation of ${:,.2f}.\n\nSincerely,\nThe Best Charity Ever".format(donor["name"],ask_donor))
            break
    else: # Check if the entered name is not in the list 
        ask_donor = float(input("Please enter a donation amount: "))
        initial_donor_list.append({"name": ask_name,"total_don": ask_donor,"number_don": 1,"avg_don": ask_donor})
        print("\nDear {},\n\nThank you for your generous donation of ${:,.2f}.\n\nSincerely,\nThe Best Charity Ever".format(ask_name,ask_donor))

def write_letter():
    """Function to generate letters for each donor in the list with their total donation amount and stores the letters in a new directory."""
    current = datetime.datetime.now()
    abs_path = pathlib.Path('./').absolute()
    final_path = os.path.join(abs_path, "letter_storage/")
    if not os.path.exists(final_path):
        os.makedirs(final_path)
    for line in initial_donor_list:
        with open("{}{}_{:02}_{:02}_{:02}.txt".format(final_path, line["name"], current.month, current.day, current.year), 'w') as thank_you_file:
            thank_you_file.write("Dear {},\n\nThank you for your continuous support over the years\nand for your total donation amount of ${:,.2f}.\n\nSincerely,\nThe Best Charity Ever".format(line["name"],line["total_don"]))
    

if __name__ == '__main__':
    option_select = {'1': thank_you, '2': list_data, '3': write_letter}
    while True: # loop until ended by user input '3'
        user_prompt = input("\nPlease choose from the following menu of actions:\n[1] Send a Thank You\n[2] Create a Report\n[3] Send letters to everyone\n[Press any other key to quit.]\n\nInput: ")
        if(user_prompt != '1' and user_prompt != '2' and user_prompt != '3'):
            break
        option_select.get(user_prompt)()
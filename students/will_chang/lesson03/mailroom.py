initial_donor_list = [
    ["Warren Buffett", 650.00, 2, 325.00],
    ["Jack Bogle", 15000.50, 1, 15000.50],
    ["William Boeing", 450.45, 3, 150.15],
    ["George Clooney", 10000.00, 2, 5000.00],
    ["Orville Wright", 95000000.00, 1, 950000.00]
]

def list_data(input_tuple):
    """Provides formatted and updated list of donors, total donations, number of donations, and average donation."""
    input_tuple.sort(key=lambda donor: int(donor[1]), reverse = True)
    max_len_str = [0]*len(input_tuple) # List providing the lengths of the longest items in each column
    
    for row in input_tuple: # Loop to fill in max_len_str with lengths of the longest items in each column
        for item in range(len(row)):
            if(len(str(row[item]))) > max_len_str[item]:
                max_len_str[item] = len(str(row[item]))
                
    format_string = f'{{:<{max_len_str[0]+10}}}${{:<{max_len_str[1]+9}}}{{:<{max_len_str[2]+15}}}${{:<{max_len_str[3]+10}}}' # Format string taking into account the longest item in each column.
    format_string_header = f'{{:<{max_len_str[0]+10}}}{{:<{max_len_str[1]+10}}}{{:<{max_len_str[2]+15}}}{{:<{max_len_str[3]+10}}}'
    print("\n")
    print(format_string_header.format(*("Donor Name", "Total Given", "Num Gifts", "Average Gift")))
    print("-"*(max_len_str[0]+max_len_str[1]+max_len_str[2]+max_len_str[3]+38))
    for row in input_tuple:
        print(format_string.format(*row))

def thank_you():
    """Prompts user to input new donor information."""
    ask_name = input("\nPlease enter a full name or type 'list' for a list of the donor names: ")
    name_in_list = False
    while(ask_name.lower() == "list"):
        print([donor[0] for donor in initial_donor_list])
        ask_name = input("\nPlease enter a full name or type 'list' for a list of the donor names: ")
    for donor in initial_donor_list:
        if(ask_name == donor[0]): # Check if the entered name is already in the list
            name_in_list = True
            ask_donor = int(input("Please enter a donation amount: "))
            donor[1] += ask_donor
            donor[2] += 1
            donor[3] = donor[1]/donor[2]
            print("\nDear {},\n\nThank you for your generous donation of ${:,}.\n\nSincerely,\nThe Best Charity Ever".format(donor[0],ask_donor))
    if(not name_in_list): # Check if the entered name is not in the list 
        ask_donor = int(input("Please enter a donation amount: "))
        initial_donor_list.append([ask_name,ask_donor,1,ask_donor])
        print("\nDear {},\n\nThank you for your generous donation of ${:,}.\n\nSincerely,\nThe Best Charity Ever".format(ask_name,ask_donor))

if __name__ == '__main__':
    quit_criteria = False # while loop flag
    while(not quit_criteria): # loop until ended by user input
        user_prompt = input("\nPlease choose from the following menu of actions:\n[1] Send a Thank You\n[2] Create a Report\n[3] Quit\n\nInput: ")
        if(user_prompt == '1' or user_prompt.lower() == "send a thank you"):
            thank_you()
        elif(user_prompt == '2' or user_prompt.lower() == "create a report"):
            list_data(initial_donor_list)
        elif(user_prompt == '3' or user_prompt.lower() == "quit"):
            quit_criteria = True
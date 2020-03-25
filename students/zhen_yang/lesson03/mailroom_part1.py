######################
# Mail Room Part One #
######################
# Data Sturcture for Mail Room
donors_list = ['Adan','Peter','Sara','Jason','Zooe']
donors_amount = ['10,120,32',
                  '25.25,225.25',
                  '45',
                  '150.00,35.50,80.75',
                  '10,20']
# prompt the three options for user 
def Ori_Prompt():
    input_str = input("Please choose from the following three options: 1.Send_ThankYouLetter 2.Create_Report,3.Quit")
    return input_str

# prompt the user to input full name of the donor
def Fullname_Prompt()
    input_str = input("Please input donor's full name or input 'list' or input 'quit' to quit`."))
    if input_str == 'quit':
       return -1 
    return input_str

# prompt the user to input a donation amount 
def Amount_Prompt():
    input_str = input("Please input the donation amount:  or input 'quit' to quit.")
    if input_str == 'quit':
       return -1 
    # Convert the amount into a number
    input_amount = float(input_str)
    return input_amount 


# find the name from donors_list 
def Found_Name(my_name):
    for i in donors_list:
        if i == my_name:
            return True
    return False

# add the amount to the donors_amount list
def Add_Amount(d_name,amount):
    donors_amount[donor_list.index(d_name)].append(amount) 

# add the name to the donors_list
def Add_Name(d_name,amount):
    donors_list.append(d_name) 
    donors_amount.append(amount) 

#################################
# define Send_ThankYou() Option #
#################################
def Send_ThankYou():
    # if user input 'list' we will list all the donor's name and ask full name again.
    while d_name == 'list':
        print(f"The donor list: {donors_list}")
        if Fullname_Prompt() == -1:
            return -1
    else:# user input a name
        if Found_Name(d_name):
            amount = Amount_Prompt()
            Add_Amount(d_name, amount)
        else:
            amount = Amount_Prompt()
            #add the name and amount to the lists.
            Add_Name(d_name,amount)

    # print ThankYou_Letter()
    # ThankYou_Letter()



#################################
# define Create_Report() Option #
#################################
def Create_Report():




# put main interaction into the __main__ block 
if __name__ == '__main__':
    #Forever loop for letting user choose one of three options.
    while:
        input_str = ""
        # keep asking the user for choose one of three options
        while not(input_str == 1 or input_str == 2 or input_str ==3):
            input_str = Ori_Prompt()
        if input_str == 1:
            d_name = Fullname_Prompt()
            if d_name == -1 :
                input_str = ""
            else:
                Send_ThankYou(d_name)

        elif input_str == 2:
            Create_Report()

        elif input_str == 3:
            exit()




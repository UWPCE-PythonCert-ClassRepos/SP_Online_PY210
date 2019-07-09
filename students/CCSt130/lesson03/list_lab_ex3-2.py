# -*- coding: utf-8 -*-
""" This code will allow the user to append, insert or delete list contents. """

"""
Lesson03
Exercise 3.2 :: List Lab
Parts 1-4
Please note:
Some requirements were 'combined' by this student, and requirements may not be \
presented following the order in the assignment. Should that be a problem, \
please let me know.
@author: Chuck Stevens :: CCSt130
Created on Thu May 30 10:17:02 2019
"""

import sys

def list_printer(our_list):
    """ This generic function will print any list with index. """
    
    print()
    print("Here's our current list: ")
    for item in our_list:
        print()
        # Find index in list
        position = our_list.index(item)
        # Start at '1' rather than '0'
        position += 1 
        # Print items with desired formatting        
        print("{}".format(position), end = ". ")
        print(item)

def list_checker(item_list, find_char):
    """ Generic function that finds items in list beginning with 'X'. """
    
    # List to hold items found with search char
    temp_list = [] 
    
    for item in item_list:
        if item.startswith(find_char):
            # print(item)
            # Add found items to a list
            temp_list.append(item)

    print()
    print("Printing a list of all items containing '{}'.".format(find_char))
    # Call print function
    list_printer(temp_list)

def choose_sequence(): 
    """ Take input to display and return 1 of 3 choices. """

    input_msg = "Please enter 'A' to Append to the list, or 'I' to Insert: "
    
    choice1 = 'A' # append
    choice2 = 'I' # insert
    choice3 = '+' # hidden option

    choice1_msg = "You've chosen to Append to the list."
    choice2_msg = "You've chosen to Insert at the beginning of the list."
    choice3_msg = "Clearly, you are an insider."
    
    while True:
        # Note: change input to upper to make error handling easier
        seq_choice = input(input_msg).title() 
   
        print()
        print("You entered: '{}'.".format(seq_choice))
        print()
        # Note: Error handling could be more robust       
        if(seq_choice == choice1):
            # print()
            print(choice1_msg)
            break
        elif(seq_choice == choice2):    
            # print()
            print(choice2_msg)
            break
        elif(seq_choice == choice3):    
            # print()
            print(choice3_msg)
            break
        else:            
            print()
            # print("Invalid Entry, please enter '{}' or '{}'.".format(choice1, choice2))
            print("Invalid Entry--try again!")

    return(seq_choice)

def copy_list(item_list):
    
    # List to swap values of original list
    temp_list = item_list[:]
    
    # Empty list to append to
    backward_list =[]
    
    print()
    print("We'll now print the list sdrawkcab, because that's the kind of crazy were are.")
    
    for item in temp_list:
        # Reverse letters in each item
        item = item[::-1]
        backward_list.append(item)

    # Call function to print modified string
    list_printer(backward_list)        
        
    # This could be its own separate function
    # For readibility
    # Find list length and assign value to a name
    list_len = len(item_list)
    # print("List length: ", end = "")
    list_len-=1 # Offset index by 1
    
    print()
    print("We'll now delete the last element in the original list, for fun.")
    
    # Remove the last element from original list
    item_list.remove(item_list[list_len])

    # Call function to print modified string
    list_printer(item_list)

def do_you_like(sm_list): 
    """ Take input and delete if user doesn't like item. """
    
    # This code is similar to choose_sequence and could probably be genericized
    input_msg = "Please enter 'Y' if you Like an item, or 'N' to Delete it: "
    
    choice1 = 'Y' # likes
    choice2 = 'N' # Doesn't like, delete

    choice1_msg = "Ok, we'll keep that in the list."
    choice2_msg = "Ok, we'll delete that from the list."

    # Temp list is required as the for loop will 'skip' an item... 
    # if the item before it is deleted. This must have something
    # ...to do with indexing

    # Empty swap list
    temp_list = [] 

    for element in sm_list:
        
        print()
        print("Do you like {}?".format(element))
        
        # Note: change input to upper to make error handling easier
        seq_choice = input(input_msg).title() 
   
        print()
        print("You entered: '{}'.".format(seq_choice))
        print()
        # Note: Error handling could be more robust       
        if(seq_choice == choice1):
            # print()
            print(choice1_msg)
            # Populate a new list to avoid skipping an element if 'No'
            temp_list.append(element)
        elif(seq_choice == choice2):    
            # print()
            print(choice2_msg)
            # Below will fail if n-1 has been deleted
            # Remove element from list
            # sm_list.remove(element)
        else:            
            print()
            print("Invalid Entry, please enter '{}' or '{}'.".format(choice1, choice2))
            # print("Invalid Entry--try again!")

    # Should the user delete the entire list
    if not(temp_list):
        print()
        print("The list is empty!")
    else:
        list_printer(temp_list)

def fruity_list(sm_list):
    """ This function asks for user input to modify list. """
    
    # For fun and comparison purposes
    big_fruit_list = ['Açaí','Apple','Akee','Apricot','Avocado','Banana','Bilberry','Blackberry',\
                      'Blackcurrant','Black sapote','Blueberry','Boysenberry','Buddhas hand',\
                      'Fingered citron','Crab apples','Currant','Cherry','Cherimoya','Custard Apple',\
                      'Chico fruit','Cloudberry','Coconut','Cranberry','Cucumber','Damson','Date',\
                      'Dragonfruit','Pitaya','Durian','Elderberry','Feijoa','Fig','Goji berry',\
                      'Gooseberry','Grape','Raisin','Grapefruit','Guava','Honeyberry','Huckleberry',\
                      'Jabuticaba','Jackfruit','Jambul','Japanese plum','Jostaberry','Jujube',\
                      'Juniper berry','Kiwano','Horned melon','Kiwifruit','Kumquat','Lemon','Lime',\
                      'Loquat','Longan','Lychee','Mango','Mangosteen','Marionberry','Melon','Cantaloupe',\
                      'Honeydew','Watermelon','Miracle fruit','Mulberry','Nectarine','Nance','Orange',\
                      'Blood orange','Clementine','Mandarine','Tangerine','Papaya','Passionfruit',\
                      'Peach','Pear','Persimmon','Plantain','Plum','Prune','Dried plum','Pineapple',\
                      'Pineberry','Plumcot','Pluot','Pomegranate','Pomelo','Purple mangosteen',\
                      'Quince','Raspberry','Salmonberry','Rambutan','Mamin Chino','Redcurrant',\
                      'Salal berry','Salak','Satsuma','Soursop','Star apple','Star fruit','Strawberry',\
                      'Surinam cherry','Tamarillo','Tamarind','Ugli fruit','White currant',\
                      'White sapote','Yuzu']    
    
    # Get user input regarding the list
    # Please note: attempted try-except here but couldn't get it to operate as expected
    while True:
        # Print current items in list
        print()
        list_printer(sm_list) 
        # Ask user to type in name of favorite fruit        
        user_fav = input("Hey, what's your favorite fruit? Enter it please (e.g. 'Pear'): ")
        
        # Change to title case for comparison with big_fruit_list
        new_fruit = user_fav.title()
            
        # Check if already in the list
        if(new_fruit in sm_list):
            print()
            print("Your entry is already in our list! Good choice!")
            break
        # Check against Wikipedia exhaustive fruit list
        # This is by no means 'error-proof', but imho a reasonable way of validating input
        elif(new_fruit in big_fruit_list):
            print()
            print("Ok, we'll add '{}' to the list!".format(new_fruit))
            # print()
            # launch function to present and return choice            
            apnd_or_ins = choose_sequence()
            
            if(apnd_or_ins == 'A'):
                # Adding input to list
                sm_list.append(new_fruit) # append to end of list
            elif(apnd_or_ins == 'I'):
                sm_list.insert(0, new_fruit) # insert at index 0 of list
            elif(apnd_or_ins == '+'):
                print()
                print("This seems non-pythonic but we'll do it anyway.")
                # Clunky, but...can't add str to list
                temp_fruits = [new_fruit]
                # Concatenate 2 lists
                sm_list+=temp_fruits 
            # Minimal error handling...quit if invalid value passed.
            else:
                print()
                print("Invalid input. Please rerun.")
                sys.exit()
            # Output revised list to screen
            list_printer(sm_list)
            break
        else:
            print()
            print("Are you sure that's a fruit? Please check your spelling and try again.")  

    while True:
        # Ask user for delete choice
        # Doesn't cast input to int for str error handling
        del_fruit = input("Please enter a number corresponding to the item you would like to delete: ")
        # Ask user for delete choice and cast to int
        # del_fruit = int(input("Please enter a number corresponding to the item you would like to delete: "))
        
        print()
        print("You entered '{}'".format(del_fruit), end = " :: ")
        
        # Find list length
        list_len = len(sm_list)
        
        # Error handling of non-numeric entry
        if(del_fruit.isalpha()):
            print("Invalid entry--try again.")
        else:
            # Casting to int as input is str
            del_fruit = int(del_fruit) 
            # Is user input out of range?
            if((del_fruit < 1) or (del_fruit > list_len)):
                print("Please enter a numeric value between 1 and {}.".format(list_len))
            else: # Remove item based on valid input-1
                del_fruit-=1 # Offset index by 1
                # Print name of fruit
                print("'{}' will be removed.".format(sm_list[del_fruit]))
                # Remove item from list
                sm_list.remove(sm_list[del_fruit])
                # print()
                list_printer(sm_list) # Call print function
                break

if __name__ == "__main__":

    def main():
        
        search_char = "P" # Search_char could be a menu option
        
        sm_fruit_list = ['Apple', 'Pear', 'Orange', 'Peach'] # removed plural
    
        # Call function to modify list based on input
        fruity_list(sm_fruit_list)
        # Function iterates over list for 'X'
        list_checker(sm_fruit_list, search_char)
        # For test
        # list_checker(big_fruit_list, search_char)
        # Call function to reverse letters
        copy_list(sm_fruit_list)
        # Call function to determine user's likes or dislikes
        do_you_like(sm_fruit_list)
        
        print()
        print("### End ###")

### Program entry point ###
main()

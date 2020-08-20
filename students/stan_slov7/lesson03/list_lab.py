#!/usr/bin/env python3


def series1(lst_orig):

    lst = lst_orig[:]
    print("Our starting list is as follows: \n", lst, "\n") 
    
    prompt1 = input("Please enter a Fruit value to be added to the list, as a string of characters:\n")    
    another_fruit1 = prompt1.lower().capitalize()
    lst.append(another_fruit1)
    print("Append Fruit: {:s} to the back of the starting list.\n".format(another_fruit1), lst, "\n")
    
    prompt2 = input("Please enter an integer value between 1 to 5 for position of a fruit in the list, "
                    "where the first starts at pos '1', the second at pos '2', etc. (Current list has 5 elements)\n")     
    pos = int(prompt2) 
    print("The chosen position number: {:d} corresponds to the fruit: {:s}\n".format(pos, lst[(pos-1)]))
    
    another_fruit2 = "Pineapples"
    lst += [another_fruit2]
    print("Added the fruit: {:s} to the end of the list using '+' list concatenation.\n".format(another_fruit2), lst, "\n")
    
    another_fruit3 = "Bananas" 
    lst.insert(0, another_fruit3)
    print("Added the fruit: {:s} to the beginning of the list using .insert()\n".format(another_fruit3), lst, "\n")
    
    check_letter = "P"
    lst_start_with_P = []
    for idx in lst:
        if idx.startswith(check_letter):
            lst_start_with_P.append(idx)                      
    print("List of all fruits that start with the letter 'P':\n", lst_start_with_P, "\n")
    print("------------------------------End of Series1------------------------------\n")



def series2(lst_orig):

    lst = lst_orig[:]
    #to start with copy of original list to be  
    print("This is the Original list: \n", lst, "\n")
    last_fruit = lst.pop()
    print("The Original list with its last fruit: {:s} removed.\n".format(last_fruit), lst, "\n")
    
    idx = 0
    while not idx:
        ans = input("Enter a Fruit to delete from the list above:\n")
        fruit = ans.lower().capitalize()
        try:
            idx = (lst.index(fruit) + 1) 
            #returns index+1 as position if such string exists in list and breaks loop as a result  
        except ValueError: #>>>ValueError: no such value in list      (TypeError for if int instead of string?) (NameError?)
            print("ValueError: {:s} is not an exact string match for any of the Fruit values in the list above...\n".format(ans))
    
    lst.pop(idx-1)
    #(lst.pop(idx-1) == fruit) --> True   #fruit found at index same value as specified by user
    
    print("Deleted the Fruit specified by the user: {:s}, found at position #{:d} of the list above.\n".format(fruit, idx))
    print("Updated list consists of the following Fruit values: ", lst, "\n")
    
    lst_cpy = lst_orig[:]  #copy of initial list that will be multiplied x2 and used further
    lst_2x = lst_cpy *2
    print("Repeat the same task with the following 2x length list:\n", lst_2x, "\n")
    
    #use a loop that breaks when an existing string is found in list
    match_found = False  #can use this flag to run the loop break proper input given then use to initiate delete of all instances
    amt_deleted = 0
    while not match_found:
        ans2x = input("Enter a Fruit value to delete from the latest 2x list above.\n")
        fruit2x = ans2x.lower().capitalize()
        if fruit2x in lst_2x:
            match_found = True   
        else: 
            print("{:s} was not found in list, please enter an actual Fruit value in the 2x list above...\n".format(ans2x))
    while match_found:
        if fruit2x in lst_2x:
            lst_2x.remove(fruit2x)
            amt_deleted += 1
            print("Deleting instance #{:d} of Fruit: {:s}...\n".format(amt_deleted, fruit2x))
        else:
            match_found = False
            print("No additional instances of Fruit: {:s} remain, ending procedure.\n".format(fruit2x))
    print("Located and deleted {:d} total instance(s) of Fruit: {:s} specified by user, "
          "for removal of any and all its occurances within the 2x list above.\n".format(amt_deleted, fruit2x))
    print("Updated 2x list now consists of the following Fruit values:\n", lst_2x, "\n")
    print("------------------------------End of Series2------------------------------\n")



def series3(lst_orig):

    lst = lst_orig[:]
    print("The Original starting list is:\n", lst, "\n")
    for fruit in lst[:]:  #iterate over a copy
        while True: #input check for each value in the list till user chooses to keep or delete Fruit value 
            ans = input("Do you like {:s}?\n".format(fruit.lower()))
            if ans == "no":
                lst.remove(fruit)
                break
            if ans == "yes":
                break
            else:   
                print("Please give an answer in the form either 'yes' or 'no' only. "
                      "No other form of input will allow the program script to continue.\n")
    print("The resulting list of Fruit values remaining is based on the input given by user regarding "
          "their 'yes'/'no' preference of each Fruit from the Original list:\n", lst, "\n")        
    print("------------------------------End of Series3------------------------------\n")



if __name__ == "__main__":
    
    #initialize the Original list used to begin each of the series scripts
    #keeping the Original intact by manipulating instead copies made with slicing, thus any actions 
    #performed on the Original list don't keep the changes made to it with each series script
    
    lst_original = ["Apples", "Pears", "Oranges", "Peaches"]

    series1(lst_original)
    series2(lst_original)
    series3(lst_original)
    
    
    
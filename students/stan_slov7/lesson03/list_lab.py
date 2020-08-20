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



if __name__ == "__main__":
    
    #initialize the Original list used to begin each of the series scripts
    #keeping the Original intact by manipulating instead copies made with slicing, thus any actions 
    #performed on the Original list don't keep the changes made to it with each series script
    
    lst_original = ["Apples", "Pears", "Oranges", "Peaches"]

    series1(lst_original)
    
    
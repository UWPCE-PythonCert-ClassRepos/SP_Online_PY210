#!/usr/bin/env python3

# Dictionary and Set Lab
# Dev: Roslyn Melookaran
# Date: 9/17/20
# Change Log: (Who, When, What)
# R. Melookaran, 9/9/20, created script
#---------------------------------------------------------------------------------#
def t_count(dict):
    list_values=[]
    #values=
    # list_values=list(values)
    # print(list_values)
    for item in dict.values():
        count=0
        for index in item:
            if index=="t":
                count=count+1
            else:
                count=count
        item=count
        print(item)

#----------DICTIONARIES 1 ------------#
# Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
dict_info={"Name":"Chris","City":"Seattle","Cake":"Chocolate"}
# Display the dictionary.
print(dict_info)
# Delete the entry for “cake”.
#dict_info.popitem() #<--- This one removes an arbitrary value
dict_info.pop("Cake") #<-- This one you can specify
# Display the dictionary.
print(dict_info)
# Add an entry for “fruit” with “Mango” and display the dictionary.
dict_info.update({"Fruit":"Mango"})
# Display the dictionary keys.
print(dict_info.keys())
# Display the dictionary values.
print(dict_info.values())
# Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
print("Cake" in dict_info)
# Display whether or not “Mango” is a value in the dictionary (i.e. True).
print("Mango" in dict_info.values())

#----------DICTIONARIES 2 ------------#
# for value in dict_info:
t_count(dict_info)


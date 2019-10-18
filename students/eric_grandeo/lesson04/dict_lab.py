#!/usr/bin/env python3

#Dictionary 1
dict_1 = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}

#Display the dict
print(dict_1)

#Delete the entry for cake, display the dict
dict_1.pop("cake")
print(dict_1)

#add fruit, display dict
dict_1["fruit"] = "Mango"
print(dict_1)

#display dict keys
print(dict_1.keys())

#display the dict values
print(dict_1.values())

#is cake in dict
print("cake" in dict_1)

#is mango in dict
print("Mango" in dict_1.values())

print("-" * 100)

#Dictionaries 2
dict_1 = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}

def count_letters(dictionary, letter):
    dict_2 = {}
    for x,y in dictionary.items():
        dict_2[x] = y.lower().count(letter)
    return dict_2

print(count_letters(dict_1, "t"))





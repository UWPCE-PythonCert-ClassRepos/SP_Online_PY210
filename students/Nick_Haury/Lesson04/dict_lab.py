#!/usr/bin/env python3
'''

'''

# Dictionaries 1

print("Dictionaries 1:\n")

my_dict = {
    "name":"Chris", 
    "city":"Seattle", 
    "cake":"Chocolate"
    }

print(my_dict)
my_dict.pop("cake")
print(my_dict)
my_dict["fruit"] = "Mango"
print(my_dict.keys())
print(my_dict.values())
print("Is 'cake' a key in the dictionary?: " + str(("cake" in my_dict)))
print("Is 'Mango' a value in the dictionary?: " + str(("Mango" in my_dict.values())))

# Dictionaries 2

print("\nDictionaries 2:\n")

dict_t = dict()
for key in my_dict:
    dict_t[key] = my_dict[key].count("t")
print(dict_t)

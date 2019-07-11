# Author: Brian Minsk

""" Dictionaries 1
Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
Display the dictionary.
Delete the entry for “cake”.
Display the dictionary.
Add an entry for “fruit” with “Mango” and display the dictionary.
Display the dictionary keys.
Display the dictionary values.
Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
Display whether or not “Mango” is a value in the dictionary (i.e. True).
"""
a_dict = {"name":"Chris", "city":"Seattle", "cake": "Chocolate"}
print(a_dict)

a_dict.pop("cake")
print(a_dict)

a_dict["fruit"] = "Mango"
print(a_dict)

print(a_dict.keys())
print(a_dict.values())
print("cake" in a_dict)
print("Mango" in a_dict.values())



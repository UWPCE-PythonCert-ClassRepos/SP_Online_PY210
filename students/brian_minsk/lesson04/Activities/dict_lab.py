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

""" Dictionaries 2
Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value 
as the value (consider upper and lower case?).

The result should look something like:

{"name": 0
 "city": 2
 "cake": 2
}
"""
a_dict_original = {"name":"Chris", "city":"Seattle", "cake": "Chocolate"}
b_dict = {}

for k,v in a_dict_original.items():
    num_t = 0
    if type(v) == str:
        for letter in v:
            if letter.lower() == "t":
                num_t += 1
    b_dict[k] = num_t

print(b_dict)

""" Sets
Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4 (figure out a way to compute those – don’t just type them in).
Display the sets.
Display if s3 is a subset of s2 (False)
and if s4 is a subset of s2 (True).
"""
s2 = set({})
s3 = set({})
s4 = set({})

for i in range(0, 21):
    if i % 2 == 0:
        s2.add(i)
    if i % 3 == 0:
        s3.add(i)
    if i % 4 == 0:
        s4.add(i)

print(s2)
print(s3)
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))

""" Sets 2
Create a set with the letters in ‘Python’ and add ‘i’ to the set.
Create a frozenset with the letters in ‘marathon’.
Display the union and intersection of the two sets.
"""
set_letters = set({"P", "y", "t", "h", "o", "n"})
set_letters.add("i")
frozenset_letters = frozenset({"m", "a", "r", "a", "t", "h", "o", "n"})
print(set_letters.union(frozenset_letters))
print(set_letters.intersection(frozenset_letters))




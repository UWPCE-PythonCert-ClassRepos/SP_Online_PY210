#!/usr/bin/env python3
#-------------------------------------------#
#Tittle: dict_lab, PYTHON210 - Exercise 4.1
#Desc: Dictionary Practice Lab
#Change Log: (Who, When, What)
#Brent Kieszling, <2020-Nov-15>, created file
#-------------------------------------------#

#DATA---------------------------------------

notes = {"Name": "Chris", "City": "Seattle", "Cake": "Chocolate"}
notes_2 = notes.copy()

s2 = set()
s3 =set()
s4 = set()
#PROCESS------------------------------------
def count_by(skip):
    """Return a list of numbers 0-20 that are divisible by 'skip'
    
    Args:
        skip (int): Integer for checking divisibility
        
    Returns:
        nums (list): List of numbers divisible by skip (0-20)
    """
    nums = []
    x = 0
    for x in range(21):
        division = x / skip
        if division.is_integer():
            nums.append(x)
        x += 1
    return nums



    

#PRESENTATION INPUT/OUTPUT------------------


print("Task 1:")
print(notes)
print("Removing Cake.")
notes.pop("Cake")
print(notes)
print("Adding Fruit.")
notes["Fruit"] =  "Mango"
print(notes)
print("Just the keys.")
print(notes.keys())
for key in notes:
    print(key)
print("Just the values.")
print(notes.values())
for key in notes:
    print(notes[key])
print("Is Cake still here?")
print("Cake" in notes)
print("Is Mango in the dictionary?")
print("Mango" in notes.values())
print()

print("Task 2:")
print(notes_2)
print("Updating list based on the number of 't's in the value.")
for key in notes_2:
    notes_2[key] = (notes_2[key]).lower().count("t")
print(notes_2)
print()


print("Task 3:")
print("S2:")
s2.update(count_by(2))
print(s2)
print("S3:")
s3.update(count_by(3))
print(s3)
print("S4:")
s4.update(count_by(4))
print(s4)
print("Is S3 a subset of S2?")
print(s3.issubset(s2))
print("Is S4 a subset of S2?")
print(s4.issubset(s2))
print()

print("Task 4:")
py = set(["p", "y", "t", "h", "o", "n"])
py.update(["i"])
fs = frozenset(("m","a","r","a","t","h","o","n"))
print("Union")
print(py.union(fs))
print("intersection")
print(py.intersection(fs))







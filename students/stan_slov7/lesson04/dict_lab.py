#!/usr/bin/env python3


#Dictionaries1
print("-------------------------- Dictionaries 1 --------------------------\n")

dict1 = {"name" : "Chris", "city" : "Seattle", "cake" : "Chocolate"}

print("The starting contents of dict1 (Key : Value) pairs:\n")

for item, value in dict1.items():
    print("{:s} : {:s}".format(item, value))

print("")
dict1.pop("cake")
print("removed entry for 'cake' from dict1...\n")
for item, value in dict1.items():
    print("{:s} : {:s}".format(item, value))

print("")
dict1["fruit"] = "Mango"
print("Added 'fruit' : 'Mango' (Key : Value) pair to dict1...\n")
for item, value in dict1.items():
    print("{:s} : {:s}".format(item, value))

print("")
print("Keys currently in dict1:")
for item in dict1:
    print(item)

print("")
print("Values currently in dict1:")
for val in dict1.values():
    print(val)

print("")
print("Check if 'cake' is a Key thats currently in dict1:")
print("cake" in dict1.keys())

print("")
print("Check if 'Mango' is a Value thats currently in dict1:")
print("Mango" in dict1.values())

#Dictionaries2
print("-------------------------- Dictionaries 2 --------------------------\n")

dict1_tmp = {"name" : "Chris", "city" : "Seattle", "cake" : "Chocolate"}

print("")
print("Now using the Keys from dict1 a new dict2 is created with "
      "respective Values set to the number of letters 't' in each of the Values of the Original dict1:\n")
dict2 = {}
for key, value in dict1_tmp.items():
    #use .count() method of String type:  value.count("t")
    dict2[key] = value.lower().count("t") #account for uppercase as well
    
#OR use for loop to update count variable, but theres a method just for this..
    #count = 0
    #for letter in value:
        #if(letter == 't'):
            #count += 1
    #dict2[key] = count
    #print("{} : {}".format(key, count))        

for item, value in dict2.items():
    print("{:s} : {:d}".format(item, value))
print("")

#Sets1
print("------------------------------ Sets 1 ------------------------------\n")

s2 = set()
for num in range(2, 21, 2):
    s2.update([num])
print("set s2 formed of all numbers divisible by 2 in the range of 0 to 20:\n", s2, "\n")

s3 = set()
for num in range(3, 21, 3):
    s3.update([num])
print("set s3 formed of all numbers divisible by 3 in the range of 0 to 20:\n", s3, "\n")

s4 = set()
for num in range(4, 21, 4):
    s4.update([num])
print("set s4 formed of all numbers divisible by 4 in the range of 0 to 20:\n", s4, "\n")

print("Is set s3 a subset of s2?")
print(s3.issubset(s2), "\n")

print("Is set s4 a subset of s2?")
print(s4.issubset(s2), "\n")

#Sets2
print("------------------------------ Sets 2 ------------------------------\n")

set1 = set(["P", "y", "t", "h", "o", "n"])
print("Formed set1 containing the letters in 'Python' :\n", set1, "\n")

set1.update(["i"])
print("Added letter 'i' to the set of letters in 'Python' from above set:\n", set1, "\n")

frznset1 = frozenset(("m", "a", "r", "a", "t", "h", "o", "n"))
print("Immutable set (frozenset) of the letters in 'marathon' :\n", frznset1 , "\n")

union1 = set1 | frznset1
print("Union of the above defined sets, containing all the unique letters in each set and their intersect:\n", union1, "\n") 

intersect1 = set1 & frznset1
print("Intersection of above sets, containing the unique letters found in both sets simultaneously:\n", intersect1, "\n") #consists of only the common letters "t h o n"


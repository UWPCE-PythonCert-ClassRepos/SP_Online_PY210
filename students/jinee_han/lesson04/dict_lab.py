
# Dictionaries 1
print ("Dictionaries 1\n")
dic = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
print (dic)
dic.pop ("cake") # Delete "cake"
print (dic)
dic.update({"fruit": "Mango"})
print (dic)

print (dic.keys()) # Display the dictionary keys
print (dic.values()) # Display the dictionary values

print ("\nIs cake in the key?")
cake_key = False   # Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
if "cake" in dic.keys():
    cake_key = True
print (cake_key)

print ("\nIs Mango in the value?")
mango_value = False   #Display whether or not “Mango” is a value in the dictionary (i.e. True).
if "Mango" in dic.values():
    mango_value = True
print (mango_value)



# Dictionaries 2
def t_count(string):
    count = 0
    t_string = string.lower()
    for ch in t_string:
        if ch == 't':
            count += 1

    return count

dict2 = {}
for key in dic.keys():
    currentCount = t_count(dic[key])
    dict2.update({key: currentCount})
print ("\nDictionaries 2\n")
print ("How many 't's in the value?")
print (dict2)

# Sets

def divisible_by_(maxcount):
    two_list = []        # Create s2
    three_list = []          # Create s3
    four_list = []            # Create s4
    for int in range(maxcount):
        if int % 2 == 0:
             two_list.append(int)
        if int % 3 == 0:
              three_list.append(int)
        if int % 4 == 0:
              four_list.append(int)
    return two_list, three_list,four_list


two_list,three_list,four_list = divisible_by_(21)

# Converting the list to a set for a subset test
set_s2 = set((two_list))
set_s3 = set((three_list))
set_s4 = set((four_list))
print (" \nSets\n")
print ("s2: ",two_list)
print ('-'*100)
print ("s3: ",three_list)
print ('-'*100)
print ("s4: ",four_list)

print ("\nis s3 a subset of s2?")
print (set_s3.issubset(set_s2))
print ("\nis s4 a subset of s2?")
print (set_s4.issubset(set_s2))

# Sets 2


print ("\nset 2\n")
python_set = {"Python"}
python_set.add("i")
print (python_set)

marathon = ("marathon")
frozen_marathon = frozenset(marathon)
print ("frozenset is: ",frozen_marathon)

print ("Union: ", python_set | frozen_marathon)
print ("Intersection: ", python_set & frozen_marathon)



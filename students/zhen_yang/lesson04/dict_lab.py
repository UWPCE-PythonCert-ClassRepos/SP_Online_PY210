###################################
# Exercise for Dictionary and Set #
###################################


##################
# Dictionaries 1 #
##################
# create a dictionary
dic_1 = {'name':'Chris','city':'Seattle','cake':'Chocolate'}
print(f"1. The dic1 :{dic_1}")

# delete the entry for "cake"
dic_1.pop('cake')
print(f"2. The dic1 :{dic_1}")

# add an entry for "fruit" with "Mango"
dic_1['fruit']='Mango'
print(f"3. The dic1 :{dic_1}")

# display the dictionary keys.
for key in dic_1:
    print(f"dic_1 key: {key} ", end="")
print("\n")
# display the dictionary values.
for val in dic_1.values():
    print(f"dic_1 val: {val} ", end="")
print("\n")
# Display whether or not "cake" is a key in the dictonary 
print(f"Is cake in dic_1?: {'cake' in dic_1}")
# Display whether or not "Mango" is a value in the dictonary 
print(f"Is Mango in dic_1?: {'Mango' in dic_1.values()}")


##################
# Dictionaries 2 #
##################
# Based on the dictionary from Dictonaries 1,
# Make a new dictionary using the same keys but with the number of 't's 
# in each value as the value.
print(f"Old dic: {dic_1}")
dic_2 = {}
for key,val in dic_1.items():
    # get the number of 't's in value
    num = val.lower().count('t')
    dic_2[key] = num 

print(f"New dic: {dic_2}")

#Dictionaries 1

#creating the dictionary with given keys and values 
Chris_info = {'name' : 'Chris', 'city' : 'Seattle', 'cake' : 'Chocolate'}

#display the dictionary
print(Chris_info)

#Delete the entry for cake 
Chris_info.pop('cake')

#display the dictionary
print(Chris_info)

#add an entry for fruit with Mango as the value
Chris_info['fruit'] = 'Mango'

#display the dictionary keys
print(Chris_info.keys())

#display the dictionary values
print(Chris_info.values())

#display whether or  not 'cake' is in the dictionary
print('cake' in Chris_info)

#display whether or  not 'Mango' is in the dictionary
print('Mango' is Chris_info.get('fruit'))


#Dictionaries 2

#Reuse original dictionary from part 1
Chris_info = {'name' : 'Chris', 'city' : 'Seattle', 'cake' : 'Chocolate'}

#Create a new dictionary for counting the 't's
Chris_ts = {}

#Count the number of 't's in each value and assign that number as the value
for k,v in Chris_info.items():
    num_ts = v.lower().count('t')
    Chris_ts[k] = num_ts
    
print(Chris_ts)

#Sets
#Create s2, s3, s4 that contain numbers from 0 to 20 divisible by 2,3,4
#Create empty sets
s2 = set()
s3 = set()
s4 = set()

#define sets
for i in range(21):
    if i % 2 is 0:
        s2.add(i)
    if i % 3 is 0:
        s3.add(i)
    if i % 4 is 0:
        s4.add(i)

#display sets
print(f"{s2}\n{s3}\n{s4}")

#display if s3 is a subset of s2
print(s3.issubset(s2))

#display if s4 is a subset of s2
print(s4.issubset(s2))

#Sets 2
#Create set with the letters 'Python' and add 'i' to set
py_set = set(['p','y','t','h','o','n'])
py_set.add('i')

#Create a frozen set with the letters in 'marathon'
mar_fset = frozenset(['m','a','r','a','t','h','o','n'])

#Display the union of the sets
print(py_set.union(mar_fset))

#Display the intersection of the sets
print(py_set.intersection(mar_fset))


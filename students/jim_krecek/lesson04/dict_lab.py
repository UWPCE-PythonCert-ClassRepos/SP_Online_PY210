#dictionaries 1
print("Dictionaries 1")
#creates a dictionary
d1 = {'name':'Chris','city':'Seattle','cake':'Chocolate'}
print(d1)

#deletes the entry for 'cake'
d1.popitem()
print(d1)

#add 'fruit':'Mango' to dictionary
d1['fruit'] = 'Mango'
print(d1)

#display dictionary keys
print("Below are the keys for this dictionary:")
for x in d1.keys():
    print(x)
    
#display dictionary values
print("Below are the values for this dictionary:")
for x in d1.values():
    print(x)
    
#display whether or not 'cake' is a key in the dictionary
print("is 'cake' a key in this dictionary? {}".format('cake' in d1.keys()))

#display whether or not 'Mango' is a value in the dictionary
print("is 'Mango' a value in this dictionary? {}".format('Mango' in d1.values()))

#dictionaries 2
print("Dictionaries 2")
#using same dictionary, make the values equal to the number of lower case t's in each value
d2 = {}
for k,v in d1.items():
    d2[k] = v.lower().count('t')
print(d2)

#sets 1
print("Sets 1")
s2=set() #set containing numbers divisible by 2
s3=set() #set containing numbers divisible by 3
s4=set() #set containing numbers divisible by 4
for i in range(21):
    if i % 2 == 0:
        s2.update([i])
    if i % 3 == 0:
        s3.update([i])
    if i % 4 == 0:
        s4.update([i])
print("s2: ",s2)
print("s3: ",s3)
print("s4: ",s4)

#display whether or not s3 is a subset of s2
print("is s3 a subset of s2? {}".format(s3.issubset(s2)))

#display whether or not s4 is a subset of s2
print("is s4 a subset of s2? {}".format(s4.issubset(s2)))

#sets 2
print("Sets 2")

#create a set with the letters in "Python" and add "i" to the set
pyset = set('Python')
pyset.update(['i'])

#create a frozenset with the letters in 'marathon'
maraset = frozenset('marathon')

#display the union and intersection of these two sets
print('the union of these two sets is: {}'.format(pyset.union(maraset)))
print('the intersection of these two sets is: {}'.format(pyset.intersection(maraset)))

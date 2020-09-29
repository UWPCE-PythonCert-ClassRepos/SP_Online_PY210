#!/usr/bin/env python3

#Dictionaries 1

#definition of dict1
dict1={'name':'Chris','city':'Seattle','cake':'Chocolate'}
dict2=dict1.copy()
dict3=dict1.copy()
#displaying dict1

print(dict1)

#delete entry got cake

dict1.pop('cake')

#display dict1 after deleting cake

print(dict1)

#adding fruit mango
dict1['fruit']='Mango'

print(dict1)

#display keys
print(dict1.keys())

#display values
print(dict1.values())

print('cake' in dict1)

#find 'mango' as value in dict1

def find_value():
    for k,v in dict1.items():
        if v == 'Mango':
            return True


print(find_value())

#######Dictionaries 2
#method 1
for k,v in dict3.items():
    dict3[k]=v.count('t')

print(dict3)

#method 2
for value in dict2:
    dict2[value]=dict2[value].count('t')

print(dict2)

#Lesson 4 assignment 1 part 3
'''set assigmnet for checking the number divisible by 2,3,4'''
s2, s3 ,s4=set(),set(),set()

for i in range(21):
    if(i%2 ==0):
        s2.add(i)
    if(i%3 == 0):
        s3.add(i)
    if(i%4 == 0):
        s4.add(i)

print(s2,s3,s4)

print(s3.issubset(s2))
print(s4.issubset(s2))


#Sets 2
'''set assignment to check the union, intersection and frozenset'''

s5=set(['P','y','t','h','o','n'])
s5.add('i')
s6=frozenset(['m','a','r','a','t','h','o','n'])
print(s5.union(s6),s5.intersection(s6))

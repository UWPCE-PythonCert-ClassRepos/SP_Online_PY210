#!/usr/bin/env python3

##Change Log
## 11/21 - JH - Created File

##import constant

chrisDict = {
        'name' : 'Chris',
        'city' : 'Seattle',
        'cake' : 'Chocolate'
        }

print (chrisDict)

del chrisDict['cake']

print (chrisDict)

chrisDict['fruit']='Mango'

x = chrisDict.keys()
y = chrisDict.values()

print(x)
print(y)
z = 'cake' in x
j = 'Mango' in y
print(z)
print(j)

chrisDict2 = {
        'name' : 'Chris',
        'city' : 'Seattle',
        'cake' : 'Chocolate'
        } 

valA = list(chrisDict2['name'])
valB = list(chrisDict2['city'])
valC = list(chrisDict2['cake'])
valATot = 0
valBTot = 0
valCTot = 0

while True:
    if 't' in valA:
        valATot = valATot + 1
        valA.remove('t')
    else :
        break

while True:
    if 't' in valB:
        valBTot = valBTot + 1
        valB.remove('t')
    else :
        break
    
while True:
    if 't' in valC:
        valCTot = valCTot + 1
        valC.remove('t')
    else :
        break

chrisDict['name'] = valATot
chrisDict['city'] = valBTot
chrisDict['cake'] = valCTot

s2 = set() 
s3 = set()
s4 = set()

for i in range(0,20):
    if i % 2 == 0:
        s2.add(i)
    if i % 3 == 0:
        s3.add(i)
    if i % 4 == 0:
        s4.add(i)

print(s2)
print(s3)
print(s4)

zap = set.intersection(s3,s2) 
print(zap == s3)

nap = set.intersection(s4,s2) 
print(nap == s4)

python = 'Python'
pyNameVar = set(python)
pyNameVar.add('i')
print(pyNameVar)

marathon = 'marathon'
maraSet = set(marathon)
print(maraSet)
print(maraSet.union(pyNameVar))
print(maraSet.intersection(pyNameVar))





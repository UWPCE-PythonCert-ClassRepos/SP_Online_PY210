#!/usr/bin/env python3

mydict = {'name':'Chris','city':'seattle','cake':'chocolate'}
print(mydict)
mydict.pop('cake')
print(mydict)
mydict['fruit'] = 'mango'
print(mydict)
print(mydict.keys())
print(mydict.values())
print('cake' in mydict)
print('mango' in mydict.values())

mydict_cp = mydict.copy()
for k,v in mydict_cp.items():
    mydict_cp[k] = v.lower().count('t')
print(mydict_cp)
set3 = set()
set2 = set()
set4 = set()
for i in range(21):
     if not i%3:
        set3.update([i])
     if not i%2:
        set2.update([i])
     if not i%4:
        set4.update([i])

print(set4)
print(set2)
print(set3)

print(set3.issubset(set2))
print(set4.issubset(set2))
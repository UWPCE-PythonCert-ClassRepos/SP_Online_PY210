#!/usr/bin/env python3

#Function for part 3
def divisibilityset(divisor, maxnumber):
    temp_set=set()
    i=1
    while i<=maxnumber:
        if i%divisor==0:
            temp_set.update({i})
        i+=1
    return temp_set

#Dictonary 1
dictonary={"name":"Chris","city":"Seattle","cake":"Chocolate"}
print(dictonary,"\n")
del(dictonary["cake"])
print(dictonary,"\n")
dictonary["fruit"]="Mango"
print(dictonary.keys(),"\n")
print("or if you like this better\n")
print(','.join(dictonary),"\n")
print(dictonary.values(),"\n")
print("or if you like this better\n")
print(','.join(dictonary.values()),"\n")
print("Is cake a key in our dictionary anymore?\n","cake" in dictonary,"\n")
print("Is Mango a value in our dictionary anymore?\n","Mango" in dictonary.values(),"\n")

#Dictonary 2
print("How many ts are in our keys?")
dictonaryt=dictonary
for key in dictonaryt.keys():
    i=key.lower().count("t")
    dictonaryt[key]=i
print(dictonaryt,"\n")

#Dictionary3
s2=divisibilityset(2,20)
s3=divisibilityset(3,20)
s4=divisibilityset(4,20)
print("s2:\n",s2,"\n")
print("s3:\n",s3,"\n")
print("s4:\n",s4,"\n")
print("Is s3 a subset of s2?\n",s3.issubset(s2),"\n")
print("Is s4 a subset of s2?\n",s4.issubset(s2),"\n")

#Dictonary4
python_set=set("Python")
python_set.update("i")
frozen_set=frozenset("marathon")
print(python_set.union(frozen_set))
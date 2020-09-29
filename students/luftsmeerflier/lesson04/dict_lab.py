#!/user/bin/env python3

#Dictionaries 1
dictionary = {
	"name" : "Chris",
	"city" : "Seattle",
	"cake" : "Chocolate"
}

print(dictionary)

del dictionary['cake']

print(dictionary)


dictionary['fruit'] = "Mango"

print(dictionary)

print(dictionary.keys())

print(dictionary.values())

print("cake" in dictionary.keys())

print("Mango" in dictionary.values())

#Dictionaries 2

def count_t(word):
	return word.lower().count('t')


dictionary_2 = {}

for (i, key) in enumerate(dictionary):
	dictionary_2[key] = count_t(dictionary[key])

print(dictionary_2)

#Sets

s2 = set()
s3 = set()
s4 = set()

for i in range(1, 20):
	if i % 2 == 0:
		s2.add(i)

for i in range(1, 20):
	if i % 3 == 0:
		s3.add(i)

for i in range(1, 20):
	if i % 4 == 0:
		s4.add(i)

print("s2: ", s2)
print("s3: ", s3)
print("s4: ", s4)

print("Is s3 a subset of s2: ", s3.issubset(s2))
print("Is s4  a subset of s2: ", s4.issubset(s2))

#Set 2
Python = set()
for letter in "Python":
	print(letter)
	Python.add(letter)
#Python.add('i')
print(Python)
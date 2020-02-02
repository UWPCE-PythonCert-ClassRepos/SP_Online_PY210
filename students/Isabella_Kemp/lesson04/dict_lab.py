# Isabella Kemp
# Dictionary and Set Lab
# 1/29/2020


# Creating a dictionary
dict1 = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
# Prints dictionary
print(dict1)
# Element cake removed
print(dict1.pop('cake'))

# Add mango to dictionary
dict1["fruit"] = "Mango"
print(dict1)

# Display the dictionary Keys, for iterates over keys.
for x in dict1:
    print (x)

# Display the dictionary values
for x in dict1:
    print(dict1[x])

# Display the dictionary values and keys
for k, v in dict1.items():
    print("%s: %s" %(k,v))

print("Is cake in the dictionary dict1? {}".format("cake" in dict1.keys()))
print("is Mango in the dictionary dict1? {}".format("Mango" in dict1.values()))

# Dictionary 2
# Uses same keys from dict 1 but the values are number of times "t" appears in previous value.
dict2 = {"name": "Chris".count("t"), "city": "Seattle".count("t"), "cake": "Chocolate".count("t")}
print(dict2)

# Sets 1

s2 = set()
s3 = set()
s4 = set()

for x in range(0,20):
    if x%2 == 0:
        s2.update([x])
for x in range(0,20):
    if x%3 == 0:
        s3.update([x])
for x in range(0,20):
    if x%4 == 0:
        s4.update([x])

print(s2, s3, s4)

print("Is s3 a subset of s2?")
print(s3.issubset(s2))

print("Is s4 a subset of s2?")
print(s4.issubset(s2))

# Sets 2

py_set = {"P", "y", "t", "h", "o", "n"}
py_set.add("i") #add i to set above
set_marathon = frozenset({"m", "a", "r", "a", "t", "h", "o", "n" }) #create frozenset

# Displays the union and intersection of the two sets
print("union:", py_set.union(set_marathon))
print("intersection:", py_set.intersection(set_marathon))

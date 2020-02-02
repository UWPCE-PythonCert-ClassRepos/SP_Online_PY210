#!/user/bin/env/ python3
"""
Created on Thu Jan 23 18:21:24 2020

@author: Grant Dowell
Dictionary and Set Lab
"""


dict_1 = {"name":"Chris", "city":"Seattle", "cake":"Chocolate"}
print(dict_1)

dict_1.pop("cake")
print(dict_1)

dict_1["fruit"] = "Mango"
print(dict_1)
print(dict_1.keys())
print(dict_1.values())
print("cake" in dict_1)
print("fruit" in dict_1)
print("Mango" in dict_1.values())

dict_2 = dict_1.copy()
for key in dict_2:
    dict_2[key] = dict_1[key].lower().count('t')
print(dict_2)    

# Sets
def set_builder(max_val,div):
    s = set()
    for n in range(max_val):
        if n % div != 0:
            s.update([n])
    return(s)
    
s2 = set_builder(20,2)
print(s2)
s3 = set_builder(20,3)
print(s3)
s4 = set_builder(20,4)
print(s4)

print(s2.issubset(s3))
print(s2.issubset(s4))

# Sets 2
s_py = set('python')
print(s_py)
s_py.update('i')
print(s_py)
s_str2 = frozenset('marathon')
print(s_str2)
print(s_str2.intersection(s_py))
print(s_str2.union(s_py))

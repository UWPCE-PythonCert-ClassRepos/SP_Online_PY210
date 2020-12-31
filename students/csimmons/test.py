#!/usr/bin/env python3
# Craig Simmons
# Python 210
# trigram.py 
# Created 12/17/2020 - csimmons
# Edited: 12/27/2020 - csimmons

food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}
'''
Chris is from Seattle, and he likes chocolate cake, mango fruit, greek salad, and lasagna pasta

def func(d): 
      
    for key in d: 
        print("key:", key, "Value:", d[key]) 
          
# Driver's code 
D = {'a':1, 'b':2, 'c':3} 

d = {'a' : 1, 'b' : 2, 'c' : 3}
def f(dict):
    for k, v in dict.iteritems():
        print k, 2*v
f(d)
'''
def stupid(seq):
    for key, value in food_prefs.items():
        print('Value: ', value, ' Key: ', key)

stupid(food_prefs)
stupid_dict = dict(value: key for key, value in food_prefs}
print
'''

In [9]: d = {id: name for id, name in zip(ids, names)}

In [10]: d
Out[10]: {1: 'fred', 2: 'john', 3: 'mary'}

{name: Val} is from {city: Val}, and he likes {cake: Val Key}, {fruit: Val Key}, {salad: val key}, {pasta: val key}





print('{0} {1} cost ${2}'.format(6, 'bananas', 1.74))
6 bananas cost $1.74
'''
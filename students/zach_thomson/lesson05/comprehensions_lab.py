def count_evens(nums):
    return len([num for num in nums if num % 2 == 0])

#print(count_evens([2,5,3,4]))
#print(count_evens([2,4,5,6,8,10]))


food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}


#print(food_prefs.values())

#test = '{} is from {}, and he likes {} cake, {} fruit, {} salad, and lasagna {}'
#print(test.format(food_prefs.values()))
range15 = [i for i in range(15)]
hex15 = [hex(i) for i in range15]
new_dict_from_list = {i:v for i,v in zip(range15, hex15)}
#print(new_dict_from_list)

new_dict_oneliner = {i: hex(i) for i in range(15)}

#print(new_dict_oneliner)

food_copy = {k: v.count('a') for k, v in food_prefs.items()}
#print(food_copy)
#print(food_prefs)

s2 = {num for num in range(20) if num % 2 == 0}
s3 = {num for num in range(20) if num % 3 == 0}
s4 = {num for num in range(20) if num % 4 == 0}

print(s2)
print(s3)
print(s4)

a_list = [2, 3, 4]

test = {num for num in range(20) for a in a_list if num % a == 0}

print(test)

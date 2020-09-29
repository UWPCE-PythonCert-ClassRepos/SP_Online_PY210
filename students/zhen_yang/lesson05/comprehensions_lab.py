###############################
# Comprehensions Lab Exercise #
###############################
food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}
# Print the dict by passing it to a string format method
text = '{} is from {}, and he likes {} cake, {} fruit, {} salad, and {} pasta'
# Note!!! using * to unpacking the dictionary's value list
print(text.format(*food_prefs.values()))

print("-----------------")
num_hex_list = [(a, b) for a, b in zip([s for s in range(16)],
                [hex(s) for s in range(16)])]
print(f"-- num_hex_list:{num_hex_list}")

print("-----------------")

# dictionary version
num_hex_dic = {num: hex(num) for num in range(0, 16)}
print(f"-- num_hex_dic:{num_hex_dic}")

print("-----------------")
food_prefs_new = {key: val.count('a') for key, val in food_prefs.items()}
print(f" The new food_prefs dictionary: {food_prefs_new}")
print("-----------------")

s2 = {s for s in range(21) if not s % 2}
print(f" s2:{s2}")
s3 = {s for s in range(21) if not s % 3}
print(f" s3:{s3}")
s4 = {s for s in range(21) if not s % 4}
print(f" s3:{s4}")

# using dictionary data sturcture to hold all the divisors
# the value of each divisors key is a list of the coresspoinding
# numbers.
divisor_list = list(range(2, 11))
divisor_dic = {divisor: [s for s in divisor_list if not s % divisor] for
               divisor in divisor_list}
#for key, val in divisor_dic.items():
#    print(f"-- 1. Divisor: {key} List: {val} --")
# using Comprehension to print out dictorinary
[print(key, value) for key, value in divisor_dic.items()]

print("-----------------")
# do it all as a one-liner by nesting a set comprehension
# inside a list comprehension
divisor_dic = {divisor: [a for a in list(range(2, 11)) if not a % divisor]
               for divisor in list(range(2, 11))}
#for key, val in divisor_dic.items():
#    print(f"-- 2. Divisor: {key} List: {val} --")
# using Comprehension to print out dictorinary
[print(key, value) for key, value in divisor_dic.items()]

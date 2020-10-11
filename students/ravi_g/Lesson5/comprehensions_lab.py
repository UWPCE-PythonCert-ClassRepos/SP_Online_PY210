food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

###############
# Task 1
###############

print("{0} is from {1}, and he likes {2} cake, {3} fruit, {4} salad, and {5} pasta".format(food_prefs['name'], food_prefs['city'], food_prefs['cake'],food_prefs['fruit'], food_prefs['salad'],food_prefs['pasta']))

###############
# Task 2 - dict for hexadecimal from 0 to 15
###############

d = {}
for i in range(16):
    d[i] = hex(i)[2:]
print(d)

###############
# Task 3 - dict for hexadecimal from 0 to 15, one-liner
###############

print({i:hex(i)[2:] for i in range(16)})

###############
# Task 4 - Make dict for task 1
###############

d1 = {}
for k,v in food_prefs.items():
    d1[k] = v.lower().count('a')
print(d1)

###############
# Task 5
###############

s2 = {s for s in range(21) if s % 2 == 0}
s3 = {s for s in range(21) if s % 3 == 0}
s4 = {s for s in range(21) if s % 4 == 0}
print(s2, s3, s4)

###############
# Task 5 - using function
###############

def set_creater(n):
    '''
    :param n: int
    :return: set
    '''
    return {i for i in range(21) if i % n == 0}

out = [] # list of sets
for i in range(2,5):
    out.append(set_creater(i))
print(out)

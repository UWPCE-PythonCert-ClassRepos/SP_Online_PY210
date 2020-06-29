#! bin/user/env

import datetime

print("Script works!")

def get_name(alias):
    print(alias)

def get_time():
    x = datetime.datetime.now()
    print(x)

def get_age(age):
    print(age)

def dog_age(age):
    x = 7
    x.append(age)
    print(x)

# # TypeError
# get_name()

# # NameError
# get_time(now)

# #SyntaxError
# get_age(5

# AttributeError
dog_age(5)

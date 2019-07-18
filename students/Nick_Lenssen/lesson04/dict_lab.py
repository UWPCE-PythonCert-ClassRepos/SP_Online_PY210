#!/usr/bin/env python3

def dict_1(my_dict):
    my_dict_prac = my_dict.copy()
    print (my_dict_prac)
    my_dict_prac.pop('cake')
    print (my_dict_prac)
    my_dict_prac['fruit'] = 'Mango' 

    print ('cake' in my_dict_prac)
    print ('Mango' in my_dict_prac.values())

def dict_2(my_dict):
    my_dict_prac2 = my_dict.copy()
    count = 0
    for item in my_dict_prac2:
        for i in item:
            if i.lower() =='t':
                count+=1
            my_dict_prac2[item] = count
    print (my_dict_prac2)

def create_set(div):
    my_list = []
    for i in range(21):
        if i%div == 0:
            my_list.append(i)
    my_set = set(my_list)
    return my_set

def set_string(string):
    s = set()
    for i in string:
        s.update([i])
    #print (s)
    return s
def set_update(my_set, up_str):
    my_set.update([up_str])
    return my_set

my_dict = {'name': "Chris", 'city': "Seattle", 'cake': "Chocolate"}

dict_1(my_dict)
dict_2(my_dict)

s2 = create_set(2)
s3 = create_set(3)
s4 = create_set(4)
print (s2, s3, s4)

print (s3.issubset(s2))
print (s4.issubset(s2))

py_s = set_string('Python')
py_s = set_update(py_s, 'i')

py_s2 = frozenset(set_string('marathon'))
print (py_s2, py_s , '\n')
print (py_s2.union(py_s))
print (py_s2.intersection(py_s))






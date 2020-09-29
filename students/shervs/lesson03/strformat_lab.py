#!/usr/bin/env python

def formatter(in_tuple):  #function for task3
   
    tuple_len = len(in_tuple)
    form_string =f"the {tuple_len} numbers are: "+ "{:d}"+ (tuple_len-1)*\
                  ",{:d}"
   
    return form_string.format(*in_tuple)

#task 1
print("task1:\n")
a_tuple = (2, 123.4567, 10000, 12345.67)
print("file_{:0>3d} :   {:.2f}, {:.2e}, {:.3e}".format(*a_tuple))


#task 2
print("\ntask2:\n")
print(f"file_{a_tuple[0]:0>3d} :   {a_tuple[1]:.2f}, {a_tuple[2]:.2e},\
 {a_tuple[3]:.3e}")

#task 3
print("\ntask3:\n")
t = 1,2,3,4,4,5
print(formatter(t))

#task 4
print("\ntask4:\n")
t = ( 4, 30, 2017, 2, 27)
print(f"{t[3]:0>2d} {t[4]} {t[2]} {t[0]:0>2d} {t[1]}")

#task 5
print("\ntask5:\n")
l = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {l[0]}\b is {l[1]} and the weight of a {l[2]}\b is\
 {l[3]}")

print(f"""The weight of an {l[0].upper()}\b is {l[1]*1.2} and the weight of a\
 {l[2].upper()}\b is {l[3]*1.2}""")

#task 6
print("\ntask6:\n")
print('{:10}{:10}{:>3}{:>8}'.format('First',"Last", "Age" , "Cost" ))
print('{:10}{:10}{:>3}{:>8}'.format('John', 'Smith', "22" , "1.35"))
print('{:10}{:10}{:>3}{:>8}'.format('Tu', 'Vu', "5" , "35.35"))

t = 1,2,3,4,5,6,7,8,9,10
print("{:5d}\n{:5d}\n{:5d}\n{:5d}\n{:5d}\n{:5d}\n{:5d}\n{:5d}\n{:5d}\n{:5d}\n"
      .format(*t))
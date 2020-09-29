#Chris Dela Pena
#UW PCE PY210
#Lesson 3.3 String Formatting Lab


print('***Task 1***')
"""
Write a format string to take tuple:
( 2, 123.4567, 10000, 12345.67)
and produce
'file_002 :   123.46, 1.00e+04, 1.23e+04'
REF: https://mkaz.blog/code/python-string-format-cookbook/
"""
t1 = ( 2, 123.4567, 10000, 12345.67)
print("file_{:03}, {:.2f}, {:.2e}, {:.2e}".format(*t1))


print('***Task 2***')
"""
Repeat task 1 using alternate type
of format string
"""
print(f"file_{t1[0]:03}, {t1[1]:.2f}, {t1[2]:.2e}, {t1[3]:.2e}")


print('***Task 3***')
"""
Rewrite "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
to take an arbitrary number of values
"""
def formatter(in_tuple):
    form_string = "the {} numbers are: ".format(len(in_tuple))
    for num in in_tuple[0:]:
        form_string += "{}, ".format(num)
    return form_string
t2 = (2,3,5)
t3 = (2,3,5,7,9)
print(formatter(t2))
print(formatter(t3))


print('***Task 4***')
"""
Use index numbers to specify positions for tuple
( 4, 30, 2017, 2, 27) to print '02 27 2017 04 30'
"""
t4 = ( 4, 30, 2017, 2, 27)
print(f"{t4[3]:02}, {t4[4]}, {t4[2]}, {t4[0]:02}, {t4[1]}")

print('***Task 5***')
"""
Given ['oranges', 1.3, 'lemons', 1.1], write f-string
to display The weight of an orange is 1.3 and the weight of a lemon is 1.1.
Also, change f-string to display names of fruit in upper case
and weight 20% higher.
"""
t5 = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {t5[0][:-1]} is {t5[1]} and the weight of a {t5[2][:-1]} is {t5[3]}")
print(f"The weight of an {t5[0][:-1].upper()} is {t5[1]*1.2} and the weight of a {t5[2][:-1].upper()} is {t5[3]*1.2}")

print('***Task 6***')
"""
Write some Python code to print a table of several rows,
each with a name, an age and a cost. Make sure some of
the costs are in the hundreds and thousands to test your alignment specifiers.
And for an extra task, given a tuple with 10 consecutive numbers,
can you work how to quickly print the tuple in columns that are 5 charaters
wide? It can be done on one short line!
"""
t6 = (["Name", "Age", "Salary"], ["Duhamel", 35, 100000], ["Moriarty", 55, 85555],
["Steadrock", 34, 155500], ["Gumm", 21, 19000])

for i in range(len(t6)):
    print(f"{t6[i][0]:<12} {t6[i][1]:<8} {t6[i][2]:<10}")

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

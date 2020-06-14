#Chris Dela Pena
#UW PCE PY210
#Lesson 3.3 String Formatting Lab

"""
Task 1
Write a format string to take tuple:
( 2, 123.4567, 10000, 12345.67)
and produce
'file_002 :   123.46, 1.00e+04, 1.23e+04'
REF: https://mkaz.blog/code/python-string-format-cookbook/
"""
tuple1 = ( 2, 123.4567, 10000, 12345.67)
print("file_{.03}, {:.2f}, {:.2e}, {:.2e}".format(*tuple1))

"""
Task 2

"""

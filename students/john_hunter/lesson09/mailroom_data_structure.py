# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 16:33:42 2021

@author: johnh
"""
import datetime

total = int()
donations=[]
address = {'number': int(), 'street': str(), 'city': str(), 'state': str(), 'zipcodefive': int()}
name = 'Example Donor'
first = 'Example'
last = 'Donor'
phone_number = str()
date = [int(), int(), int()]
status = bool()

x = datetime.datetime.now()
xyear = x.year 
xday = x.day
xmonth = x.month

print(type(xyear))
print(type(xday))
print(type(xmonth))

#key is name, value is a list of data structures, 0 is donations, 1 is total, 
# 2 is list of fist and last names, 3 is address, 4 phone number,
# 5 is last donation date, 6 is status
standard_data_dict_template = {'name':[donations, total, [first, last], None, None, None, None]}
full_data_dict_template = {'name':[donations, total, [first, last], address, phone_number, date, status]}
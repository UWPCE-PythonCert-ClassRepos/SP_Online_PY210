#!/usr/bin/env python3
import time
# crete dictionary to hold data
studentsdict = {}
studentdatalist = []
firstlinekeys = []
languages = []
#studentsdict = {str(i):i for i in [studentdatalist]}

# open students file nad read contents
with open("students.txt","r") as f1:
    studentdatalist = f1.read().splitlines() # add students file contents to list
    firstline = studentdatalist[0].split(':') # grab first line of studentdatalist and split on :
    joinfirstline = (', '.join(firstline)) # join the items to remove ,
    print(firstline[1]) # test print
    splitfirstline = joinfirstline.split(',') # split list on ,
    print('1', joinfirstline) # test print
    cleanfirstline = splitfirstline[0].lstrip()
    print(len(splitfirstline)) # test print
    #value = None


remainingstudentdatalist = studentdatalist[1:]
for line in remainingstudentdatalist:
    data = line.split(",  ")
    joindata = (', '.join(data))
    #print(type(joindata)) # string
    doing = joindata.split(': ') # now a list
    print(doing)
    secondlist = []
    for i in doing:
        print("second", i)
        secondlist = (doing[0].split(', '))
        secondlist.append(i.split(','))

        #print(type(testing0))


        #print('0', testing0)
    print(secondlist[0])
    value0 = secondlist[0]
    print(secondlist[1])
    value1 = secondlist[1]
    print(secondlist[2])
    value2 = secondlist[2]
    # regular for loop
    #for d in doing:
        #print("non lc", doing)
    # list comprehension attempt
    [print("list comp test", d) for d in doing]
    [print("list comp test", doing) for d in doing]






    print('*****')
    #print(type(data)) # list
    print(data)
    print(data[0])
    for entry in data:
        print(entry)

    #print(remaining)

    #print('2',cleanfirstline)
    firstlinekeys = cleanfirstline
    #print('3',firstlinekeys)
    for i in cleanfirstline:
        studentsdict[cleanfirstline] = cleanfirstline
    #print(studentsdict[i])
    #studentsdict[]
    #selection = (studentdatalist[1]) # printing to verify output
    #studentsdict[selection] = selection

    #thing = (studentdatalist[1])
    #print(thing.split(":"))

    #studentdatalist = studentdatalist.split(':')
    #print([i.split(':', 1) for i in studentdatalist])
    #print(studentdatalist[1])
    studentsdict = studentsdict.fromkeys(studentdatalist) # create dictionary from list

    ini_string1 = studentdatalist[1]
    studentsdict = studentdatalist[1]
    #print(ini_string1)
    #print ("Initial String", studentdatalist[1])
    #es = dict(item.split(":") for item in ini_string1.split(", "))
    #for k, v in studentdatalist: D[k] = v
    #print(es)

    # print all keys in dictionary
    #for key in studentsdict.keys():
    #    print(key)

    # Display the dictionary values.
    #print('\nDisplaying Dictionary Values:')
    #for value in studentsdict.values():
    #    print(value)

    # use dictionary comprehension to convert list to dictionary
    # {str(i):i for i in [studentdatalist]}






    # loop to make keys for dictionary
    for entry in splitfirstline:
        studentsdict = {splitfirstline[0]: value0, splitfirstline[1]: value1, splitfirstline[2]:value2}
        print(studentsdict)
    time.sleep(3)

    # list comprehension to make keys for dictionary
    #studentsdict = [print({splitfirstline[0]: value, splitfirstline[1]: value, splitfirstline[2]:value} for entry in splitfirstline)]
    # getting <generator object <genexpr> at 0x10fcd19a8> print here with this list comprehension attempt
    #time.sleep(5)
    #for entry in entries_list:
    #case = {'key1': entry[0], 'key2': entry[1], 'key3':entry[2] }
    #case_list.append(case)
    #value = None

    # for loop to make keys for dictionary
    #for entry in splitfirstline:
    #    case = {splitfirstline[0]: value, splitfirstline[1]: value, splitfirstline[2]:value}

    # list comprehension to make keys for dictionary
    #case = [print({splitfirstline[0]: value, splitfirstline[1]: value, splitfirstline[2]:value} for entry in splitfirstline)]

        #splitfirstline[entryname] = case  #you will need to come up with the logic to get the entryname.
    #    print(case)

    # begin clean up of remaining data
    #print(studentdatalist[1:]) # test print line

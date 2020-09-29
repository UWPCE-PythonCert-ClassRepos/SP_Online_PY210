##############################################################
# 20200706    djm   File Exercise
#
#
#
# https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/file_lab.html
#
################################################################

# Write a program which prints the full path for all files in the
# current directory, one per line. Use either the os module or pathlib.

import os
def getFileListingForDirectory():
    spath = os.getcwd()
    print("Current path " + spath)
    for root, dirs, files in os.walk(spath, topdown=True):
        for fn in files:
            try:
                print(os.path.join(root, fn))
            except UnicodeEncodeError:
                print("can\'t encode file name of " + len(fn) + " chars at " + root + "\n")
            except (WindowsError, OSError):
                print("can't find the file " + os.path.join(root, fn))

getFileListingForDirectory()

######################################################################################################
#
# Write a program which copies a file from a source, to a destination (without using shutil,
# or the OS copy command (you are essentially writing a simple version of the OS copy command)).
#
#     This should work for any kind of file, so you need to open the files in binary mode: open(filename, 'rb')
# 	(or 'wb' for writing). Note that for binary files, you can’t use readline() – lines don’t have any meaning
# 	for binary files.
#     Test it with both text and binary files (maybe a jpeg or something of your choosing).
#     Advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once.
#     This should only be a few lines of code :-)
#
# test files, student.txt, boeing-747-space-shuttle-carrier-aircraft.jpg, Binder3.pdf

def copyfile(nm, source_dir, destination_dir):
    nm_src = source_dir + '\\' + nm
    nm_dest = destination_dir + '\\copy_' + nm
    fsource = open(nm_src)
    #assert isinstance(nm_src, object)
    #print(nm_src)
    try:
        fdest = open(nm_dest, 'w+')
        for x in fsource:
            fdest.write(x)
        fdest.close()
    except:
        i = 0
        fsource.close()
        fdest = open(nm_dest, 'wb')
        with open(nm_src, "rb") as f:
            byte = bytearray(f.read(1))
            fdest.write(byte)
            while byte:
                # Do stuff with byte.
                byte = bytearray(f.read(1))
                i =+ 1
                fdest.write(byte)
    fsource.close()
    fdest.close()


source_file_dir='C:\\Users\\djm4938\\Documents\\~~~~2020\\mygit\\students\\duanez2021\\lesson04'
destination = 'C:\\Users\\djm4938\\Documents\\~~~~2020\\mygit\\students\\duanez2021\\lesson04'
# JPG
copyfile('boeing-747-space-shuttle-carrier-aircraft.jpg', source_file_dir, destination)
# pdf
copyfile('Binder3.pdf', source_file_dir, destination)
# text file
copyfile('students.txt', source_file_dir, destination)

################################################################################################################

# students.txt
#
# In it, you will find a list of names and what programming languages they have used in the past.
# this may be similar to a list generated at the beginning of this class.
#
# Write a little script that reads that file and generates a list of all the languages that have been used.
#
# What might be the best data structure to use to keep track of bunch of values (the languages) without duplication?
#
#


# Write a little script that reads that file and generates a list of all the languages that have been used.
# change dir
import sys, os
print(os.getcwd())
os.chdir('lesson04')
# get file name
fname = 'thank_you_template.txt'
def open_and_read(fname):
    f = open(fname)
    tupleContents = tuple(x.split(":") for x in f)
    for i, j in enumerate(tupleContents):
        if len(tupleContents[i][1]) == 1:
            #print(tupleContents[i][0])
            tupleContents[i][1] = ' none_specified' + tupleContents[i][1]
    return(tupleContents)
x = open_and_read(fname)
len(x[8][0])
fname = "thank_you_template.txt"

def open_and_read_template(fname):
    outF = open("myOutFile.txt", "w")
    with open(fname) as fp:
        line = fp.readline()

        cnt = 1
        while line:
            if '<name>' in line:
            #    print(str(line[0:5]) + 'Duane' + str(line[len(line)-2]))
                #print(line[5:11])
                line = line.replace('<name>', 'donkeyknong')
                print(line)
            if '<donation>' in line:
                line = line.replace('<donation>', '$1,000,000.00')
                print(line)
            #print("Line {}: {}".format(cnt, line.strip()))
            outF.write(line)
            line = fp.readline()
            cnt += 1
    outF.close()
    fp.close()

    open_and_read_template("thank_you_template.txt")



def get_languages(fname):
    y = open_and_read(fname)
    lstContents = tuple()
    for i, j in enumerate(y):
        s = str(y[i][1:])
        lstContents += tuple((s[3:len(s)-4].split(', ')))
    # chop off first two elements
    lstContents = lstContents[2:]
    # copy as a list
    x = list(lstContents)
    # nicknames appear to start with a capital letter, remove them
    for i, j in enumerate(x):
        if j == 'nothing':
            x[i] = str('none_specified')
            #print(str(i), j, 'NONE SPECIFIED')
    for i, j in enumerate(x):
        if str(j[0:1]).isupper():
            x.remove(j)
    for i, j in enumerate(x):
        if ',' in str(j):
            # print(x[i])
            x[i] = trim_character(j, ',')
    for i, j in enumerate(x):
        if ' ' in str(j):
            # print(x[i])
            x[i] = trim_character(j, ' ')
    return list(x)

def trim_character(s, c):
    if c in s:
        s = s.replace(c, '')
    return s

    trim_character('matlab,', ',')
    # print a human read-able list
    unique_languages = set(get_languages(fname))
    for w in unique_languages:
        print(str(w))

# What might be the best data structure to use to keep track of bunch of values (the languages) without duplication?

# set data struct could easily get rid of dups
# dictionray might be best though long term and easiest to work with. last name, first name.
# nicknames are a problem in the original data. i would add semicolons to delinate the three members of each line.


#
# How can you tell the difference between a nickname and a language?
# nicknames all started with capital letters. as long as this rule is never
# violated, this code should work ok.

#
# Extra challenge: keep track of how many students specified each language.
#
x = tuple(get_languages(fname))
count_of_language_declarations = {}
for i in x:
    if i in count_of_language_declarations:
        count_of_language_declarations[i] += 1
    else:
        count_of_language_declarations[i] = 1

for name, countof in count_of_language_declarations.items():
    print('{} {}'.format(name, countof))


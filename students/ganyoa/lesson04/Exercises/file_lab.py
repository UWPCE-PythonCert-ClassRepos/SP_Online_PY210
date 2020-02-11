import sys
import pathlib
import os

#paths and file processing
for files in os.listdir(os.getcwd()):
    print(os.path.abspath(files))

with open('students.txt', 'rb') as og_file, open('students02.txt', 'wb') as newbie:
    newbie.write(og_file.read())

with open('lake.jpg', 'rb') as og_file, open('lake02.jpg', 'wb') as newbie:
    newbie.write(og_file.read())

#file reading and parsing
languages = set()
lang_list = list()
lang_count = {}

with open('students.txt', 'r') as infile: #open file as readable
    next(infile) #skip the header row
    for line in infile:
        newness = (line.strip('\n').split(':')) #split at # to create two items per line
        newness = newness[1].split(',') #split each language to stand alone

        for lang in newness:
            lang = lang.strip() #trim spaces
            if lang.islower(): #only if lower case, to avoid nicknames
                languages.add(lang) #add language to set
                lang_list.append(lang) #list all languages to count later
        for x in languages:
            lang_count[x] = lang_list.count(x) #build dictionary with languages and occurences
    #print(languages)
    print('\n''Number of programming languages students know:''\n')
    print(lang_count)


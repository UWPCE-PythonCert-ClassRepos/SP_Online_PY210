#!/usr/bin/env python3

''' Read a file that stores the name of students and the programming language and reports the langauages used.'''

import os

filename = 'students.txt'
fullname = os.path.join(os.getcwd(),filename)
lang = []
with open(fullname, 'r') as infile:
    for line in infile.readlines():
        name, data = line.split(':')
        if line.startswith('Name'):
            #Header line
            pass
        elif data:
            print(data)
            #Need to convert data, but strip line characters and spaces.
            data = [d.strip() for d in data.strip().split(',') if d.strip() and not d.strip()[0].isupper()]
            print(data)
            lang.extend(data)

lang_set = set(lang)
            
print('Programming languages used by students: {}'.format(set(lang)))

print('Number of students for each language:')
for l in sorted(lang_set):
    print(f'{l:<15}{lang.count(l):>4d}')
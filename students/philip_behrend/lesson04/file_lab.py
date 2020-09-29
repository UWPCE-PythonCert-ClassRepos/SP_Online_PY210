# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:18:18 2019

@author: Philip Behrend
"""

import os 

os.chdir(r'C:\Users\Gemini\UW_PYTHON\SP_Online_PY210\students\philip_behrend\lesson04\\')


# Print Path
print([os.getcwd() + '\\' + i for i in os.listdir()])

# Copy file from source to destination
for file in os.listdir():
    with open(file, 'rb') as f:
        contents = f.read()
    with open('outfile_'+ str(file), 'wb') as wf:
        wf.write(contents)
        
# Generate languages from students.txt
with open('students.txt', 'rb') as f:
    student_contents = f.readlines()
student_contents = [i.decode('utf-8') for i in student_contents]  

import re
lang_list = []
for i in student_contents:
    temp = re.search(r'[^:]*$',i).group(0).replace(',','').split()
    for j in temp:
        if ((j not in lang_list) and (j[0].isupper() == False) and (j != 'languages')):
            lang_list.append(j)
print(lang_list)
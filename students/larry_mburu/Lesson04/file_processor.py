#!/usr/bin/env python3

import os 

def list_files(): 
    print("[+] Listing files in current directory..")
    for file in os.listdir(os.curdir):
        print(file)

def copy(file_source, file_destination, size):
    """
    copies data from file to file by size bytes

    param: file_souce : file to copy from
    param: file_destination: file to copy to
    param: size: byte size to read from source
    """

    with open(file_source, 'rb') as f_source:
        with open(file_destination, 'wb') as f_destination:
            bytes_read = f_source.read(size)
            while bytes_read: 
                f_destination.write(bytes_read)
                bytes_read = f_source.read(size)

    print("[+] Copy complete!")

def file_processor(file): 
    """
    function consumes a file, split student name to a set of
    programming languages, then counts the most popular lang
    taken.

    param: file: a file containing students to programming
    languages taken.
    """
    student_db = {}

    with open(file) as f_obj: 
        for record in f_obj: 
            # skip file header
            if record.startswith('Name'):
                continue 
            student_name = record.split(':')[0]
            #split based on a comma, then a pesky space
            prog_languages = record.split(':')[1].strip().split(', ')
            # destroy nick_names in list. 
            # names are capitalized. program names are not!
            if prog_languages[0].istitle():
                del prog_languages[0]
            student_db[student_name] = set(prog_languages) # no duplicates

    # track language count per student
    count_lang_per_student = {} 

    for value in student_db.values(): 
        for lang in value: 
            if lang not in count_lang_per_student:
                count_lang_per_student[lang] = 1
            else:
                count_lang_per_student[lang] += 1

    print(count_lang_per_student)

if __name__ == '__main__':
    #list_files()
    #copy('test.txt', 'dtest.bin', 10)
    file_processor('students.txt')
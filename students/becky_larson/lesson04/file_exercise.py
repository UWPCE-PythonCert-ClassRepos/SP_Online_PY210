#!/usr/bin/env python3
import os


def Paths_Processing():
    print('******************* Paths Processing')
    cwd = os.getcwd()
    dirs = os.listdir(cwd)

    for file in dirs:
        print(cwd+'\\'+file)


def File_Processing():
    print('******************* File Processing')

    header_size = 128
    f = open('C:\\Users\\belarson\\Documents\\junk\\gbunny.jpg', 'rb')
    # f = open('C:\\Users\\belarson\\Documents\\junk\\junk.txt', 'rb')
    #    junk_data = f.read()
    junk_header = f.read(header_size)
    junk_rest = f.read()
    f.close()
    print(junk_header)


def copy_file():
    print('******************* copy_file')

    f = open('C:\\Users\\belarson\\Downloads\\students.txt')
    student_data = f.read()
    # student_header = f.read(header_size)
    # student_rest = f.read()
    f.close()
    print(student_data)


def create_student_records():
    in_file = 'C:\\Users\\belarson\\Downloads\\students.txt'

    student_no = 0
    all_languages = dict()

    with open(in_file, 'r') as f:
        for line in f:
            student_no += 1
            student_languages = []
            split_name = line.split(':')
            name = split_name[0]
            #  new student record
            student_record = {'id': student_no, 'name': name}
            remainder = split_name[1]
            # read thru remainder of line to check if nickname else language
            for word in split_name[1].split(','):
                word = word.strip()
                #  if first letter is a capital, its a nickname
                if word[:1].isupper():
                    # This is a nickname.  Add to record
                    student_record['nickname'] = word
                else:
                    # This is a language
                    # update language list for student
                    student_languages.append(word)
                    # either increment count or add language to list
                    if word in all_languages:
                        # language found in list. increment languate totals
                        all_languages.update({word: all_languages[word]+1})
                    else:
                        #  language not found in list. add and set count to 1
                        all_languages[word] = 1
        # add lang list to dict
        student_record['languages'] = student_languages
        print(f'\n\nfinal student_record is {student_record}')
        print(f'\n\nfinal **** all_languages is {all_languages}')

        for k, v in all_languages.items():
            print(f"{k}: {v}")


# Paths_Processing()
# File_Processing()
# copy_file()
create_student_records()

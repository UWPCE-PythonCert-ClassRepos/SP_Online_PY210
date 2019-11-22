#!/usr/bin/env python

"""
File Exercise

Allows user to specify any file path accessible, then returns to origin filepath.

File paths for Clemente Fortuna's personal testing:
    dst_dir = '/Users/fortucj/Documents/skoo/Python/L04_dst'
    src_dir = '/Users/fortucj/Documents/skoo/Python/L04_src'
"""

import os


def processing():
    """
    Execution of path and file processing.
    """

    # store origin directory
    orig_dir = os.getcwd()
    # prompt for user input
    src_dir = input("Please enter a source directory: \n")
    dst_dir = input("Please enter a destination directory: \n")
    os.chdir(src_dir)  # switch to source directory
    for item in os.listdir(src_dir):
        # first bullet, and also print file size.  Includes hidden files
        print(os.path.abspath(item) + '\n', os.path.getsize(item))
        # setup absolute paths
        file_copy = dst_dir + '/Copy_' + item
        file_source = src_dir + '/' + item
        # skips hidden files for copying
        if item.startswith('.'):
            pass
        else:
            # copy by line for text files
            try:
                with open(file_source, 'r') as source, open(file_copy, 'w') as copy:
                    for line in source:
                        copy.write(line)
            # copy by byte size for binary files
            except UnicodeDecodeError:
                with open(file_source, 'rb') as source, open(file_copy, 'wb') as copy:
                    while True:
                        chunk = source.read(1024)
                        if not chunk:
                            break
                        copy.write(chunk)
    # switch to destination directory
    os.chdir(dst_dir)
    # verify second bullet by printing copied items and their file size
    for item in os.listdir(dst_dir):
        print(os.path.abspath(item) + '\n', os.path.getsize(item))
    # change back to origin directory
    os.chdir(orig_dir)


def parsing():
    orig_dir = os.getcwd()
    src_dir = input("Pleae enter source directory of text file: \n")
    dst_dir = input("Please enter destination directory of language file: \n")
    language_file = dst_dir + '/languages.txt'
    os.chdir(src_dir)
    lang_dict = {}
    pass_list = ['', '\n', 'nothing', 'nothing\n']
    remove_objs = [',', '\n']
    with open('students.txt', 'r') as source, open(language_file, 'w') as new:
        next(source)
        for line in source:
            colon = line.index(':')
            ssv_nick_lang = line[colon + 1:].split(' ')
            for i, item in enumerate(ssv_nick_lang):
                list_item = list(item)
                if (item in pass_list) or (list_item[0].isupper()):
                    pass
                else:
                    for obj in remove_objs:
                        if obj in list_item:
                            list_item.remove(obj)
                    mod_item = "".join(list_item)
                    if mod_item not in lang_dict:
                        lang_dict[mod_item] = 1
                    elif mod_item in lang_dict:
                        lang_dict[mod_item] += 1
            #print(mod_item, lang_dict[mod_item])
        for key in lang_dict:
            new.write(key + ':' + str(lang_dict[key]) + '\n')
    os.chdir(orig_dir)

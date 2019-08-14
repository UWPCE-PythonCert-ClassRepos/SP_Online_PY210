#!/usr/bin/env python3
import pathlib

def main():
    pth = pathlib.Path('./')
    for f in pth.iterdir():
        print(pth.absolute() / f)

def languages(text_file):
    with open(text_file, mode='r', encoding='utf-8') as a_file:
        a_file.readline()
        lang_dict = {}

        for line in a_file:
            data = line[line.index(':') + 1 :].lstrip()
            data = data.replace('\n', '')
            a_list = data.split(',')

            for lang in a_list:
                if ' ' in lang:
                    lang = lang[lang.index(' ')+1:]
                if lang and not lang.istitle():
                    if lang not in lang_dict:
                        lang_dict[lang] = 1
                    else:
                        lang_dict[lang] += 1
    return lang_dict
    
            #for lang in a_list:

def language_tracker():
    pass


def copy_file(source, dest):
    with open(source, 'rb') as infile, open(dest, 'wb') as outfile:
        while True:
            data = infile.read(8)
            if not data:
                break
            outfile.write(data)



            
if __name__ == '__main__':
    main()
    languages('students.txt')
    #copy_file('students.txt', 'this_is_a_successful_test.txt')

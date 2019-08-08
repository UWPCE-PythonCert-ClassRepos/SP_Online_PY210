#!/usr/bin/env python3
import pathlib

def main():
    pth = pathlib.Path('./')
    for f in pth.iterdir():
        print(pth.absolute() / f)

def languages(text_file):
    with open(text_file, mode='r', encoding='utf-8') as a_file:
        a_file.readline()

        for line in a_file:
            data = line[line.index(':') + 1 :].lstrip()
            if data[:1].isupper():
                pass
            print(data)

def plus_one():
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

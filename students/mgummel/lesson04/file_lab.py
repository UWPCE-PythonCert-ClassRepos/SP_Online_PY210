#!/usr/bin/env python3
import pathlib

def main():
    pth = pathlib.Path('./')
    for f in pth.iterdir():
        print(pth.absolute() / f)

def copy_file(source, dest):
    with open(source, 'rb') as infile, open(dest, 'wb') as outfile:
        while True:
            data = infile.read(8)
            if not data:
                break
            outfile.write(data)
            
if __name__ == '__main__':
    main()
    copy_file('students.txt', 'this_is_a_successful_test.txt')
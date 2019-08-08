#!/usr/bin/env python3
import pathlib


def main():
    pth = pathlib.Path('./')
    
    for f in pth.iterdir():
        print(pth.absolute() / f)

def copy_file(source, dest):
    with open(source, 'rb') as infile, open(dest, 'wb') as outfile:
        while True:
            outfile.write(infile.read(255))
            if infile.read(32) == b'':
                break
    #with open(new_file, mode='wb') as any_file:
    #    new_file=.write(3)
        
    
if __name__ == '__main__':
    main()
    copy_file('students.txt', 'testing_what.txt')

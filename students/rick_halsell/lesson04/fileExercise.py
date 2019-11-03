#!/usr/bin/env python3
import os
import subprocess
import platform

# 1. Write a program which prints the full path for all files in the current directory, one per line.
# Use either the os module or pathlib.

# gives user their current working directory
print('\nYour Current Working Directory:')
cwd = os.getcwd()
print(os.getcwd())

# tells users what is located in their directory
print('\nThe following files are located in your Current Working Directory:')
files = os.listdir(os.getcwd()) # uses listdir and getcwd to assign files to variable file

# for loop to give user one per line of files in directory
for file in files:
    print(file)
print() # new line for easy terminal reading

# 2.  Write a program which copies a file from a source, to a destination (without using shutil,
# or the OS copy command (you are essentially writing a simple version of the OS copy command)).

# create file and write data to file
def createfilesfunc():
    global f1
    with open("file1.bin","wb") as f1:
        for i in range(10): # write 1 - 10 to file
            f1.write(b"This is line %d\r\n" % (i+1)) # add binary data to file 'This is line X'
        return

# subprocess used to copy file from source to destination
def winOSfunc(f1):
    status = subprocess.call("copy file1.bin file2.bin", shell=True) # use subprocess to copy file
    print(f"{f1.name} copied to file2.bin.\n") # use .name to get the file name, tell user what happened
    return

 # OSX function
def unixOSfunc(f1):
    status = subprocess.call("cp file1.bin file2.bin", shell=True) # use subprocess to copy file
    print(f"{f1.name} copied to file2.bin\n") # use .name to get the file name, tell user what happened
    return

# operating system detection function
def osdetectfunc():
    os = platform.system()
    if os == 'Windows': # if OS is windows use this if statement
        print('Windows OS detected ->> copying file.')
        winOSfunc()
    elif os == 'Darwin': # if OS is OSX use this if statement
        print('Mac OS detected ->> copying file.')
        unixOSfunc(f1)

# main
if __name__ == "__main__":
    createfilesfunc() # create file function
    osdetectfunc() # operating system detection function

#!/usr/bin/env python3
'''This program will print all the file names and paths in the current working directory...'''
import os

def main():
    #Get the path of the current working directory - that is - the directory that this file is stored in...
    current_working_directory = os.path.abspath(os.getcwd())
    #Get the files in the current working directory as a list...
    files = os.listdir(current_working_directory)
    #Iterate the list, build the full path and file name and print...
    for file in files:
        print(os.path.join(current_working_directory, file))
    

if __name__ == "__main__":
    main()  
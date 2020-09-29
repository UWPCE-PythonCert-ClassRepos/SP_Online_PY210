Part1
#Write a program that prints the path of all files in the current directory, one per line
#Use os or pathlib modules
import os, sys

#Define the current directory path
Current_Path = os.getcwd()
#List all the files in the current directory
Dir = os.listdir(Current_Path)

#Iterate through each file and print it's absolute path, moving to a new line each time
for File in Dir:
    print(f"{os.path.abspath(File)}\n")   

#Part 2
#Write a program which copies a file from a source to a destination

def Copy_File(File_Name):
    with open(File_Name, 'rb') as f:
        f.
    
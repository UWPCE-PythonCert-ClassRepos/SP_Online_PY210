#file exercise
import os

#write a program that prints the full path for all files in the current directory
print("These files are in the current directory:\n")
for file in os.listdir():
    print(os.path.abspath(file),'\n')


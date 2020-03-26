#################
# File Exercise #
#################

#############################
# Paths and File Processing #
#############################
import os

# Write a program which prints the full path for 
# all files in the current directory

# get the current directory
cur_dir = os.getcwd()
print(cur_dir)
# list the names of the files
file_list = os.listdir(cur_dir)
for i in file_list:
    print(f"{cur_dir}\{i}")


# Write a program which copies a file from a source to a destination.
source = cur_dir + '\my_file.txt'
dest = cur_dir + '\my_copy.txt'
file_size = 4000
# use with as block to open files, then don't need to close the files.
with open(source, 'rb') as in_file, open(dest, 'wb') as out_file:
        # read part of a file into memeory
        out_file.write(in_file.read(file_size))
        # read the rest part of a file into memeory
        out_file.write(in_file.read())


#############################
# File reading and parsing  #
# Write a little script that reads that file and generates 
# a list of all the languages that have been used.
#############################
# use dictionary data sturcture 
# key is the difference language, and value is the 
# number of studets use the language.
language_dic = {} 

def create_language_list(the_list):
    for i in the_list:
        # remove the whitespace in each string
        new_str = str(i).strip() 
        if len(new_str)!=0:
            # if the language is already on the dic, then add the value by one
            if new_str in language_dic:
                language_dic[new_str] = language_dic[new_str] + 1
            else:
                # if the language is not on the dic, then add the item
                language_dic[new_str] =  1
        

source = cur_dir + '\students.txt'
with open(source,'r') as in_file:
    # read in each line
    for line in in_file:
        # remove the newlines from each line
        line = line.rstrip("\n") 
        new_list_1 = line.split(": ")
        # skip the first title line and the line without nick name or language specification
        if new_list_1[0] != 'Name' and len(new_list_1) == 2:
            new_list_2 = new_list_1[1].split(',')
            # Note: check nothing is in the list using 'in' not '=='
            if 'nothing' in new_list_2 :
                #print("2. Nothing is here. {new_list_2}") 
                pass
            # nick name has the first uppercase letter 
            elif not new_list_2[0].islower():
                # remove nick name from the list
                #print(f"before nick {new_list_2}")
                new_list_3 = new_list_2[0].split(" ")
                if len (new_list_3) ==1:
                    new_list_2.pop(0)
                else:
                    new_list_2.pop(0)
                    new_list_2.append(new_list_3[1])

                #print(f"after nick {new_list_2}")
                create_language_list(new_list_2)
            else:
                create_language_list(new_list_2)


    for key, val in language_dic.items():
        print(f"Language: {key}, student speficed: {val}")


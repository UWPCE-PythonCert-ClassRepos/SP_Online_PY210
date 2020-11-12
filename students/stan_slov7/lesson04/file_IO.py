#!/usr/bin/env python3

from pathlib import Path

from operator import itemgetter




print("------------------------------------PART 1------------------------------------\n")

current_dir = Path.cwd()
print("Path of the Current Directory is:\n", current_dir, "\n")

print("Listed below are the full paths of all the files (of any type) located " 
      "within the current dir, as well as in any of its nested directories (if any):\n")
file_path_recurse = sorted(current_dir.glob('**/*'))
for item in file_path_recurse:
    if item.is_file():
        print(item)

print("------------------------------------Part 2------------------------------------\n")

filename = '2019-01-14.png' #swap with 'students.txt' to see that works just the same with text as binary .png file
dest_file = 'new_file' #whether binary (eg. .png file) or .txt file, will be readable by appropriate apps

#setting the open [modes] for read and write stream to '_b' for binary 
#resulting in binary file being read and written successfully, as well as .txt file
#which would not have been the case if binary mode wasnt specified in the binary file case.
with open(filename, 'rb') as infile, open(dest_file, 'wb') as outfile:
    outfile.write(infile.read())

print("")
print("Reading from 'filename' and copying contents (whether binary or text) to 'new_file'.\n")

print("------------------------------------PART 3------------------------------------\n")

#build up collection of unordered and unique elements as its reading in the file data

#lang_lst = []

lines_lst = []

#read in file 'students.txt' and output the formed set of unique languages 
with open('students.txt', 'r') as read_file:
    while True:
        next_line = read_file.readline()
        if not next_line:
            break
        start = next_line.find(":")
        end = next_line.find("\n")
        sub_str = next_line[start+2:end]
        temp_lst = sub_str.split(",")
        temp_str = "".join(temp_lst)
        sub_lst = temp_str.split(" ")
        print(sub_lst)
        lines_lst.append(sub_lst)
        #for word in sub_lst:
            #if word.islower():
                #lang_lst.append(word)
print("")
removed_header = lines_lst.pop(0)
fake_entry = lines_lst.remove(["nothing"])  
print("removed Header of data list, as not actual data...\n", removed_header, "\n")
print("removed fake language entry 'nothing'...\n")
lang_lst = []
for lst in lines_lst:
    print(lst)
    for word in lst:
        if word.islower():
            lang_lst.append(word)
print("")
print("All iterations of the languages listed:\n", lang_lst, "\n")

lang_set = set(lang_lst)
print("The Set of unique languages in 'students.txt' data:\n", lang_set, "\n")

freq_lst = []
for lang in lang_set:
    freq_lst.append(lang_lst.count(lang))

lang_dict = dict(list(zip(lang_set, freq_lst)))
#sorted((list(lang_dict)), key=itemgetter(1))

lst1 = list(zip(lang_set, freq_lst))

#sorted_lst_tuples = sorted(lst1, key=itemgetter(0))
print("List of (language, frequency) tuple pairs sorted alphabetically within their grouped frequencies, sorted in ascending order:\n")
print(sorted(sorted(lst1, key=itemgetter(0)), key=itemgetter(1))) #list of tuple pairs of (language, frequency)
    #sorting based on retrieval of each tuple item in list using the itemgetter and sorting
    #the alphabetically sorted list (that was based on index 0) using now the freq value at index 1 position 
    #to form alphabetically ordered clusters of tuples which are themselves based on increasing order of frequency.
    
    
#first sorted the list of tupes created from unique set of languages and their frequency
#Where the tuples are grouped based on associated frequency from low to high freq
#where within each cluster of a common freq count, the (lang, freq) tuples 
#are also sorted in alphabetical order of their languages throughout the various frequency groupings. 
print("")
print("Dict formed from Set of unique languages and the respective frequency in which"
      " they appeared in the data file, displayed as (Lang : Freq) pairs:\n")
for key, freq in lang_dict.items():
    print("{:s} : {:d}".format(key, freq))

print("")
print("(Lang : Freq) pairs sorted by ascending freq:\n")
print(sorted(lang_dict.items(), key=itemgetter(1)))  
#Ascending order i.e. sorted lowest to highest



#File entry example:
#Name: Nickname, languages
#Jagger, Michael: Mick, shell, python

#identify NickNames from languages using .isTitled() String method, 
#separate 'Name: Nickname,' from the rest and will have languages to .extend() set
#Bonus: add a count variable for each language to keep track # students listing each


#no write to file needed


#use f.writelines(seq) to write a sequence of prog languages built up.

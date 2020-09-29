#Christine Kim
#Lesson 4 File Exercise

#Paths and File Processing
import pathlib

pth = pathlib.Path("./")
print(pth.is_dir())

#get path
print(pth.absolute())

#call function for copy
def copy_file(in_name, out_name):
    #open source file and destination file
    with open(in_name, "rb") as source, open(out_name, "wb") as dest:
        #iterate through text file and copy line by line
        while True:
            line = source.readline()
            if not line:
                break
            dest.write(line)

        #read from source, write to destination by entire content
        #dest.write(source.read())

copy_file("deus ex achievement.txt", "first_copy.txt")
copy_file("Jane ball room.jpg", "second_copy.jpg")

#File reading and parsing
with open("students.txt", "rb") as f:
    #create a set for computing languages
    languages = set()
    #remove 2 from line count to offset category and last empty line
    student_num = -2
    while True:
        #take in line by line
        line = f.readline()
        student_num += 1
        #end at end of file
        if not line:
            break
        #split out name into list
        name = line.decode().split(": ")
        #remove \n from last element
        name[-1] = name[-1].strip()

        #remove empty languages
        if len(name) <= 1:
            pass
        else:
            #List with names removed
            name_gone = name[1]

        #sort out nick names and languages into list
        sort = name_gone.split(", ")

        #remove nicknames
        if any(map(str.isupper, sort[0])):
            sort.remove(sort[0])
        #remove category
        elif sort[0] == "languages":
            sort.remove(sort[0])
        languages.update(sort)
    #dispaly languages set
    print(languages)
    #num of students specified language
    print(student_num)
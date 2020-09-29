#Mark McDuffie
#File excercise
#3/31/20

#Prints the path for every file in the entire working directory
import os
def print_paths():
    dirpath = os.getcwd()
    print("current directory is : " + dirpath)

    for root, dirs, files in os.walk(os.path.abspath(dirpath)):
        for file in files:
            print(os.path.join(root, file))

#Copies a file from a source to a destination
def copyfile_example(source, dest):
    # Beware, this example does not handle any edge cases!
    with open(source, 'rb') as src, open(dest, 'wb') as dst:
        'students.txt'(src, dst)


#Formats and cleans up the student text file
def format_students():
    file = open("students.txt", 'r')
    header = file.readline()
    print("{:<25} {:<5} {:>37}".format("Name","(nickname)", "Languages Leared"))
    print("-"*74)
    for line in file:
        nickname = ""
        code = ""
        data = line.split(" ")
        last = data[0].strip()
        first = data[1].strip()
        codeIndex = 3
        try:
            nickname = data[2].strip()
            if(nickname[0].islower()):
                codeIndex = 2
                nickname = ""
            for item in data[codeIndex:]:
                code += item.strip()
        except IndexError:
            pass
        if(nickname.endswith(',')):
            nickname = nickname[:-1]
        print("{:<15} {:<10} {:<10} {:>35}".format(last, first[:-1], nickname, code))



format_students()



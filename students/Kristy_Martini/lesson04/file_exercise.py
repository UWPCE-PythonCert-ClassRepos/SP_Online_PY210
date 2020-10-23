import os
import pathlib

def print_filepaths():
    """ Prints the full path for all files in the current directory."""
    working_dir = pathlib.Path('./')
    for filepath in working_dir.iterdir():
        print(filepath.absolute())

def copy_file(source_path, dest_path):
    """ Copies file from a source to a destination.
    
    Inputs:
    source_path     the absolute path of the file to copied

    Outputs:
    dest_path       the absolute path of the location for the copied file
    """

    with open(source_path, 'rb') as infile, open(dest_path, 'wb') as outfile:
        outfile.write(infile.read())

def read_students_file(students):
    dict_languages = {}
    with open(students, 'r') as f:
        for line in f.readlines()[1:]:
            words = line.split(":",1)[-1]
            languages = words.split()
            for language in languages:
                language = language[:-1]
                if(language not in dict_languages):
                    dict_languages[language] = 1
                else:
                    dict_languages[language] += 1
    print(dict_languages)

if __name__ == "__main__":
    #print_filepaths()
    #copy_file("C:\\Users\\marti\\Documents\\Py210\\SP_Online_PY210\\students\\Kristy_Martini\\lesson04\\WolfCreekMay2020.jpg", "C:\\Users\\marti\\Documents\\Py210\\SP_Online_PY210\\students\\Kristy_Martini\\WolfCreekMay2020.jpg")
    students =  pathlib.Path('./') / "students.txt"
    read_students_file(students)
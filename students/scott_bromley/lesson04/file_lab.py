#!/usr/bin/env python3

import pathlib

# File Exercises described here: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/file_lab.html


def main():
    # print the full path of all files in the current directory, one per line
    print_curr_dir()
    # copy a file to a destination
    #copy_file('fletch.jpg', '/Users/scottbromley/Desktop/fletch.jpg')
    #copy_file('some_text.txt', '/Users/scottbromley/Desktop/some_text.txt')
    # read in a text file and return a list of all unique languages in text file
    parse_languages()


def print_curr_dir():
    """
    prints the absolute path of all files in current dir
    :return:
    """
    pth = pathlib.Path('./')
    [print(f.absolute()) for f in pth.iterdir()]


def copy_file(file, destination):
    """
    copies a file (from current dir) in any format to a destination folder
    :return:
    """
    with open(file, 'rb') as infile, open(destination, 'wb') as outfile:
        outfile.write(infile.read())


def parse_languages():
    """
    reads in students.txt; parses file for languages
    :return: set of languages appearing in students.txt; dict of language and occurrences
    """
    languages = set()
    with open('students.txt', 'r') as f:
        next(f)
        for line in f.readlines():
            language_list = [language.strip() for language in line.split(':')[1].split(',') if language.islower()]
            for language in language_list:
                languages.add(language)
    return languages


if __name__ == "__main__":
    print("Running", __file__)
    main()
else:
    print("Running %s as imported module", __file__)
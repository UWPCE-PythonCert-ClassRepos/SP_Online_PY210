#!/usr/bin/env python3

"""
Lesson 4: file lab
Course: UW PY210
Author: Jason Jenkins
"""
import pathlib

# Global Variables
language_list = dict()
known_languages = set()
known_languages.update({"python"})
known_languages.update({"java"})
known_languages.update({"perl"})
known_languages.update({"fortran"})
known_languages.update({"javascript"})
known_languages.update({"typescript"})
known_languages.update({"c++"})
known_languages.update({"shell"})
known_languages.update({"matlab"})
known_languages.update({"erlang"})
known_languages.update({"c"})
known_languages.update({"vb"})
known_languages.update({"sql"})
known_languages.update({"bash"})
known_languages.update({"rex"})
known_languages.update({"db"})
known_languages.update({"mysql"})
known_languages.update({"php"})
known_languages.update({"visualbasic"})


def print_files():
    pth = pathlib.Path('./')
    for f in pth.iterdir():
        print(f)


def copy_file(file, dest):
    with open(file, 'rb') as infile, open(dest, 'wb') as outfile:
        for line in infile:
            outfile.write(line)


def get_language_list(file):
    global language_list
    global known_languages

    with open(file, 'r') as f:
        for line in f:
            tmp_line = line.split(':')
            for word in tmp_line[1].split(','):
                word = word.strip().lower()
                if word in known_languages and not (word in language_list):
                    language_list.update({word: 1})
                elif word in language_list:
                    cur_count = language_list.get(word) + 1
                    language_list.update({word: cur_count})

    for k, v in language_list.items():
        print(f"{k}: {v}")


if __name__ == "__main__":

    print_files()
    copy_file('OrgFile.txt', 'NewFile.txt')
    copy_file('OrgPic.jpeg', 'NewIMG.jpeg')

    get_language_list('students.txt')

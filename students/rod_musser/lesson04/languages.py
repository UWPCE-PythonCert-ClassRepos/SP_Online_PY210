#!/usr/bin/env python3
filename = './students.txt'
languages = set()
lang_hist = {}

def readStudentFile(filename):
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            processStudent(line)


def processStudent(line):
    name_data = line.split(':')
    if name_data[0] != 'Name':
        langs_with_nickname = name_data[1].split(',')
        for l in langs_with_nickname:
            l_no_ws = l.strip()
            # If string starts with Capital letter, it's a nickname
            if len(l_no_ws) > 0 and not l_no_ws[0].isupper():
                languages.add(l_no_ws)
                lang_hist.setdefault(l_no_ws, 0)
                lang_hist[l_no_ws] = lang_hist[l_no_ws] + 1



if __name__ == "__main__":
    readStudentFile(filename)
    print(languages)
    print(lang_hist)

#!/usr/bin/env python3
# ==============================================================================
# Python210 | Fall 2020
# ------------------------------------------------------------------------------
# Lesson04
# File reading and parsing (file_parser.py)
# Steve Long 2020-10-15 | v0
#
# Requirements:
# =============
#
#   Write a little script that reads file "students.txt" and generates a list
#   of all the languages that have been used.
#
#   The file format:
#
#   The first line of the file is...
#
#       Name: Nickname, languages
#
#   ...and each line looks something like...
#
#       Jagger, Michael: Mick, shell, python
#
#   So a colon after the name, then the nickname, and then one or more
#   languages.
#
#   However, like real data files, the file is NOT well-formed. Only some
#   lines have nicknames, and other small differences, so you will need to
#   write some code to make sure you get it all correct.
#
#   How can you tell the difference between a nickname and a language?
#
#   Extra challenge: keep track of how many students specified each language.
#
# Implementation:
# ===============
#
#   The implementation uses a dictionary to map alternate names of programming
#   languages/tech often found on CVs and LinkedIn to common names. Functions
#   filter out data trash and count number of students using each tech.
#   Checked with flake8.
#
# Dependencies:
# -------------
#
#   Read access to data file "students.txt" in local directory "source".
# 
# Script Usage:
# -------------
#
#   ./file_parser.py executes show_student_tech_skills.
#
# Issues:
# -------
#
#   None
#
# History:
# --------
# 000/2020-10-16/sal/Created.
# =============================================================================

import pathlib


def load_sw_language_names():
    """
    Translation key between common alternate spellings or equivalent
    names and the actual name of a programming language, operating
    system, application, or process.
    """
    alternates_name = \
        ((("actionscript",), "ActionScript"),
         (("ada",), "Ada"),
         (("algol",), "ALGOL"),
         (("ansible",), "Ansible"),
         (("apl",), "APL"),
         (("applescript",), "AppleScript"),
         (("asp", "aspnet"), "ASP"),
         (("assemblylanguage",), "Assembly Language"),
         (("bash",), "Bash"),
         (("basic",), "Basic"),
         (("c",), "C"),
         (("cascadingstylesheets", "css"), "CSS"),
         (("clojure",), "Clojure"),
         (("cobol", "gnucobol"), "COBOL"),
         (("c++", "c+", "cplusplus"), "C++"),
         (("c#", "cs", "csharp"), "C#"),
         (("database", "db"), "Database"),
         (("ddl",), "DDL"),
         (("dos",), "DOS"),
         (("dxl",), "DXL"),
         (("erlang",), "Erlang"),
         (("forth",), "Forth"),
         (("fortran", "fortran66", "fortran77", "fortran90"), "FORTRAN"),
         (("f#",), "F#"),
         (("git", "gitlab", "github"), "Git"),
         (("go", "golang"), "Golang"),
         (("haskell",), "Haskell"),
         (("html", "dhtml"), "HTML"),
         (("hypertalk",), "HyperTalk"),
         (("idl",), "IDL"),
         (("java",), "Java"),
         (("javascript",), "JavaScript"),
         (("korn",), "Korn"),
         (("labview",), "LabVIEW"),
         (("lisp", "maclisp"), "Lisp"),
         (("logo",), "Logo"),
         (("matlab",), "MatLab"),
         (("modula2",), "Modula-2"),
         (("mysql",), "MySQL"),
         (("objectivec", "objc"), "Objective C"),
         (("pascal",), "Pascal"),
         (("perl",), "Perl"),
         (("php",), "PHP"),
         (("powershell",), "PowerShell"),
         (("prolog",), "Prolog"),
         (("python", "jython"), "Python"),
         (("r",), "R"),
         (("rexx", "rex"), "Rexx"),
         (("ringo",), "Ringo"),
         (("ruby", "rubyonrails"), "Ruby"),
         (("scala",), "Scala"),
         (("scheme",), "Scheme"),
         (("sed",), "Sed"),
         (("shell",), "Shell"),
         (("simula",), "Simula"),
         (("smalltalk",), "SmallTalk"),
         (("sql", "tsql", "plsql"), "SQL"),
         (("swift",), "Swift"),
         (("typescript",), "TypeScript"),
         (("vba", "visualbasicforapplications", "vbscript", "vb6"), "VBA"),
         (("visualbasic", "vb"), "Visual Basic"))
    d = {}
    for alts_name in alternates_name:
        alternate_names = alts_name[0]
        name = alts_name[1]
        for alternate_name in alternate_names:
            if (d.get(alternate_name, None) is None):
                d[alternate_name] = name
    return d


def student_file_to_array(pathname):
    """
    Convert a text file containing rows of the form

    <student-name> : <nickname-or-technology-csv>

    where the first char of <nickname-or-technology-csv>
    is uppercase when it is a nickname and the csv may be
    either a comma or a space.
    """
    file_lines = []
    with open(pathname, 'r') as file:
        line = file.readline()
        while (line):
            file_lines.append(line.strip())
            line = file.readline()
    return file_lines[1:]


def remove_extra_chars(s, c):
    """
    Remove duplicate adjacent characters from a string.
    """
    a = []
    for word in s.strip().split(c):
        if (len(word) > 0):
            a.append(word)
    return c.join(a)


def flatten_string(s):
    """
    Remove all space, ".", and "-" chars from a string and make lower
    case.
    """
    replaceable = (" ", ".", "-")
    s = s.strip().lower()
    for rep in replaceable:
        s = s.replace(rep, "")
    return s


def show_student_tech_skills(pathname):
    """
    Retrieve student programming language and tech skills list
    and print the number of students using each language.
    """
    langs = load_sw_language_names()
    d = {}
    lines = student_file_to_array(pathname)
    for line in lines:
        rest = remove_extra_chars((line.split(":"))[1], " ")\
                .replace(" ,", ",")\
                .replace(" ", ",")
        for name_or_tech in rest.split(","):
            if (len(name_or_tech) > 0):
                if (name_or_tech == name_or_tech.capitalize()):
                    print("{} is a nickname".format(name_or_tech))
                else:
                    key = flatten_string(name_or_tech)
                    tech = langs.get(key, name_or_tech.capitalize())
                    n = d.get(tech, 0)
                    d[tech] = n + 1
    for tech in sorted(d.keys()):
        count = d[tech]
        print("{} = {}".format(tech, count))


if (__name__ == "__main__"):
    show_student_tech_skills(
        str(pathlib.Path
            .cwd()
            .joinpath("source", "students.txt")))

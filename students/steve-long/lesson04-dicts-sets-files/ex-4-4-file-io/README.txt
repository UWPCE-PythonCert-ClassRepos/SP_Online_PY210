# Python210 | Fall 2020
# ----------------------------------------------------------------------------
# Lesson04 | File operations | ex-4-4-file-io/
# README
# Steve Long 2020-10-31


Contents:

copy_file_binary-screenshot.png ... Unit test output for copy_file_binary.

copy_file_binary.py ............... Source code for bin/text doc 
                                    read/write.

file_parser.py .................... Source code for text doc parsing.

source/ ........................... Folder for source data docs for 
                                    copy_file_binary.

    robot.jpg ..................... Small bin doc for copy_file_binary.

    samaritaine.jpg ............... Large(r) bin doc for copy_file_binary.

    students.txt .................. Semi-structured text doc used by 
                                    file_parser composed of newline
                                    delimited records consisting of 
                                    student name, optional nickname, and
                                    tech skills.

    widgets.txt ................... Text doc for copy_file_binary.

target/ ........................... A folder to hold output from 
                                    copy_file_binary.

README.txt ........................ This manifest document.


Directions:
-----------

copy_file_binary:

Run ./copy_file_binary.py from the terminal window. A series of functional tests
will be run that copies or writes new documents from the local source/ folder to the target/ folder. Tests that pass will print "OK" to the terminal.

file_parser:

Run ./file_parser.py from the terminal window. The app will read the file source/students.txt and perform a set of string parsing operations which are reflected back to the terminal window.

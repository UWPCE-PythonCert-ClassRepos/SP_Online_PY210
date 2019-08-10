"""
Programming In Python - Lesson 4 Exercise 2 (Part 1.2): Paths and File Processing (Part 2)
Code Poet: Anthony McKeever
Start Date: 08/05/2019
End Date: 08/05/2019
"""

import argparse

parser = argparse.ArgumentParser(description="Copy a file to a new destination.")
parser.add_argument("--source", metavar="src", type=str, help="The source file to copy.")
parser.add_argument("--destination", metavar="dest", type=str, help="The destination to copy the source to.")


def copy_file(src, dest):
    read_file = open(src, "rb")
    write_file = open(dest, "wb")

    content = read_file.read(1024)
    while len(content) > 0:
        write_file.write(content)
        content = read_file.read(1024)
    
    read_file.close()
    write_file.close()


if __name__ == "__main__":
    args = parser.parse_args()
    copy_file(args.source, args.destination)

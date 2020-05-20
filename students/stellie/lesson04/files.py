#!/usr/bin/env python3

f = open('students.txt')
# for line in f:
#     print(line)
read_data = f.read()
print(read_data)
f.close()
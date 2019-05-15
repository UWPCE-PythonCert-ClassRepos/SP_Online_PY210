#!/usr/bin/env python3
import os

# Print full path of all files in current directory
print('Printing files in current directory:')
for filex in os.listdir():
    print(os.path.abspath(filex))

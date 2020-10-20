#!/usr/bin/env python3

''' Prints the full path for all files in the current directory'''

import os
print('Listing contents of current directory')
for f in os.listdir():
    print(os.path.abspath(f))


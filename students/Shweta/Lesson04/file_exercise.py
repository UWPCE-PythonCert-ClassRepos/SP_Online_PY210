#!/usr/bin/env python3
#file excercise from lesson 04

import os
import pathlib
#part first - full path of each file in directory

for f in os.listdir():
    print(os.path.abspath(f))

          
#part two- copy file without using shutil or os module

source=pathlib.Path.home() /"Downloads\image.png"
destin=pathlib.Path.home() /"Downloads\ewimage.png"

with open(str(source),'rb') as infile, open(destin,'wb') as outfile:
    outfile.write(infile.read())



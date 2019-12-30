#!/usr/bin/env python
import os

os.chdir(r'C:\\Users\\ig408c\\Documents\\!SCHOOL\\!Python\\SP_Online_PY210-master\\students\\tim_lurvey')

for i in range(2,11):
    os.mkdir(".\\lesson{0:02d}".format(i))
"""
Programming In Python - Lesson 4 Exercise 2 (Part 1.1): Paths and File Processing (Part 1)
Code Poet: Anthony McKeever
Start Date: 08/05/2019
End Date: 08/05/2019
"""

import os

for root, dirs, files in os.walk("."):
    for file_name in files:
        print(file_name)

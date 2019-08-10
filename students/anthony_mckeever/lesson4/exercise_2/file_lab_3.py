"""
Programming In Python - Lesson 4 Exercise 2 (Part 2): File reading and parsing
Code Poet: Anthony McKeever
Start Date: 08/05/2019
End Date: 08/05/2019
"""

languages = set([])

f = open("students.txt")
for line in f.readlines():
    if line == "Name: Nickname, languages\n":
        continue

    splitted = line.split(":")
    splitted2 = splitted[-1].split(",")
    
    for l in splitted2:
        stripped = l.strip()

        #Nick names start with an upper case letter.  Ensure we find a language by finding strings that are lower. 
        if len(stripped) > 0 and stripped.islower():
            print(stripped)
            languages.add(stripped.strip())
    
print(languages)

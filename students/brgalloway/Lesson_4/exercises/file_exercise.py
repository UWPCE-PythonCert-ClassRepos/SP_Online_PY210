
d = {}
with open("students.txt") as file:
    for line in file:
        names, languages = line.split(':',1)
        
        d[names] = languages.strip()
print(d)
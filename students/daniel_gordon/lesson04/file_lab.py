import pathlib

#Paths and File Processing
p = pathlib.Path('./')
for f in p.iterdir():
    print(f.absolute())

with open("test.txt", "r") as infile, open("copy.txt", "w") as outfile:
    for line in infile:
        outfile.write(line)
    print("Copied test.txt")

with open("test.png", "rb") as infile, open("copy.png", "wb") as outfile:
    for byte in infile:
        outfile.write(byte)
    print("Copied test.png")

#used set to prevent repeted entries
languages = set()
with open("students.txt") as data:
    #throw away the first line
    data.readline()
    for raw in data:
        #throw away student name
        line = raw.split(':')[1].split(',')
        for word in line:
            #ignore nickname, and clean up whitespace and /n
            if word.islower(): languages.add(word.strip())

print(languages)
        
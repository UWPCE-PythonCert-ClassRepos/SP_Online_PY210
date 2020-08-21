import pathlib

#Paths and File Processing
p = pathlib.Path('./')
for f in p.iterdir():
    print(f.absolute())

with open("test.txt", "rb") as infile, open("copy.txt", "wb") as outfile"
    outfile.write(infile.read())

with open("text.jpg", "rb") as infile, open("copy.jpg", "wb") as outfile:
    outfile.write(infile.read())
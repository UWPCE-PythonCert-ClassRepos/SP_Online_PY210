import pathlib
"""
pth = pathlib.Path('./')

pth.is_dir()
print(f'Folder Pathway: {pth.absolute()}\n Contents:')

for f in pth.iterdir():
    print(f.absolute())
"""
source = 'students.txt'
dest = 'students_copy.txt'
with open(source, 'rb') as infile, open(dest, 'wb') as outfile:
    outfile.write(infile.read())
langs = []
nicknames = []
with open(source) as infile:
    line = infile.readline()
    while True:
        line = infile.readline()
        students = line.split(": ")
        if len(students) > 1:
            record = students[1].split()
        else:
            record = ""
        for ele in record:
            ele = ele.replace(",", "")
            if ele[0].isupper():
                nicknames.append(ele)
            else:
                if ele not in langs:
                    langs.append(ele)
        if not line:
            break
print("Languages found in Students.txt file:")
for lang in langs:
    print(lang)



import pathlib
p = pathlib.Path('./')
for item in p.iterdir():
    print(item.absolute())

f = open('falcon.jpg', 'rb')
data = f.read()
f.close()

m = open('blah.txt', 'wb')
m.write(data)
m.close()


list1 = []
with open('students.txt', 'r') as g:
    cnt = 0
    for line in g:
        lang = line.strip().split(':')[1]
        #data.strip().split(',')
        #lang.split(',')
        list1.append(lang.strip().split(','))
list1 = sum(list1, [])
l =set(list1)

print(l)
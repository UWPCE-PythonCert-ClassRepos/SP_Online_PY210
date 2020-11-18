'''
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
'''
#Create a empty list
list1 = []
#using open, read line by line in students.txt
with open('students.txt', 'r') as g:
    for line in g:
        #read only the text to the left of the ':' and store it in variable "lang"
        lang = line.strip().split(':')[1]
        #append 'lang' to empty list 'list1'
        list1.append(lang.strip().split(','))
#gets rid of nested list
list1 = sum(list1, [])
#converting the list to a set to get rid of duplicate values
set1 = set(list1)
set1 = list(set1)
#only adding list items that start with a lower case to a seperate list
finalList = []
for i in range(len(set1)):
    if (set1[i].islower()):
        finalList.append(set1[i])
#printing the new list with whitespace removed from front of text 
for i in range(len(finalList)):
    finalList[i] = finalList[i].lstrip()
    print(finalList[i])
    

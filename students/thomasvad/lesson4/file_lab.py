import os

files = os.listdir()
for file in files:
    print(os.path.abspath(file))


with open('random_text.txt', 'w') as f:
    for i in range(1,20):
        f.write('{}. this is random \n'.format(i))



# making text copy
with open('random_text.txt','r') as f1, open ('copy_random_text.txt','w') as f2:
    for line in f1.readlines():
        f2.write(line)

# binary copy
with open('random.png','rb') as f3, open ('copy_random.png','wb') as f4:
    for piece in f3:
        f4.write(piece)


# file parsing
student_langs = {}
with open('students.txt', 'r') as f:
    for line in f.readlines()[1:]:
        for word in (line.split(':')[-1]).split(' '):
            if word.islower():
                word = word.replace(',','').strip()
                if len(word)>0 and word not in student_langs:
                    student_langs[word] = 0
                student_langs[word]+=1
print(student_langs)

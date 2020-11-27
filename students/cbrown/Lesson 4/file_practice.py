#File Practice
import os

file_names = os.listdir()
for name in file_names:
    print(os.path.abspath(name))

#File Copy
file_to_copy = r'file_to_copy.txt'
destination = r"C:\Users\chris\Desktop\File_Path\output.txt"

with open(file_to_copy,'rb') as f:
    file = f.read()

des = open(destination,'wb')
des.write(file)
des.close()

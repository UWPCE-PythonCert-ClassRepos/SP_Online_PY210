import os

print("These are the files in the current directory:")
for file_name in os.listdir():
    print(os.path.abspath((file_name)))


with open('Koala.jpg', 'rb') as file_source:
    with open('Penguins.jpg', 'wb') as file_dest:
        for line in file_source:
            file_dest.write(line)

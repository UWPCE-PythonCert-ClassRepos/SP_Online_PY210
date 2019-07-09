import os
import io

# Write a program which prints the full path for all files in the current directory, one per line

for i in os.listdir('.'):
        print(i)

# Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command).
def crummy_copy(file_in, dest):
        f = open(file_in)
        copied_stuff = f.read()
        dest_path = os.path.join(dest, file_in)
        file_out = open(dest_path, 'w')
        file_out.write(copied_stuff)
        file_out.close()

# Advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once.

# all in memory
def crummy_copy2(file_in, dest):
        dest_path = os.path.join(dest, file_in)
        with open(file_in, 'rb') as infile, open(dest_path, 'wb') as outfile:
                outfile.write(infile.read())
                infile.close()


# This should work for any kind of file, so you need to open the files in binary mode: open(filename, 'rb') (or 'wb' for writing).
# in chunks
def crummy_copy2(file_in, dest):
        dest_path = os.path.join(dest, file_in)
        with open(file_in, 'rb') as infile, open(dest_path, 'wb') as outfile:
                while True:
                        copy_out = infile.read(1024)
                        outfile.write(copy_out)
                        if not copy_out:
                                break
                outfile.close()
                infile.close()

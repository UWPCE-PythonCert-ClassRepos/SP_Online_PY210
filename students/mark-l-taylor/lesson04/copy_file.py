#!/usr/bin/env python3

'''Simple copy file function'''

def copy_file(source, target):
    '''copy files from source to target'''
    with open(source, 'rb') as sf, open(target, 'wb') as of:
        print('Copying {} \n to \n{}'.format(source,target))
        while True:
            # to handle large files read and write batches of data
            batch = sf.read(1024)
            if batch:
                of.write(batch)
            else:
                break
                
if __name__ == '__main__':
    #copy files to a test directory
    import os
    source_dir = '/Users/taylo/UW_Python_Cert/SP_Online_PY210/students/mark-l-taylor/lesson04'
    file_list = ['students.txt', 'python-logo.png']
    
    for filename in file_list:
        source = os.path.join(source_dir, filename)
        target = os.path.join(source_dir, 'target', filename)
        copy_file(source, target)
    
    
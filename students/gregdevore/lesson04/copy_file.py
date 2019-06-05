#!/usr/bin/env python3
import os, sys

# Copy source file to target directory
def copy_file(source_file, target):
    """ Copy file to target directory

    Arguments:

    source_file -- Full path of source file to be copied
    target -- Destination directory for file to be copied to

    """

    # Extract file name from full path of source file
    file_name = os.path.basename(source_file)
    # Create file with same name in target directory
    target_file = os.path.join(target,file_name)
    print('Copying {} to {}'.format(file_name, target))

    # Open files for reading and writing in binary mode
    with open(source_file, 'rb') as infile, open(target_file, 'wb') as outfile:
        while True:
            # Write 1024 bytes at a time to accomodate larger files
            buffer = infile.read(1024)
            if buffer:
                outfile.write(buffer)
            else:
                break

if __name__ == "__main__":
    # Define target directory
    target_directory = '/Users/gdevore21/Documents/Certificate Programs/Python/PYTHON210/SP_Online_PY210/students/gregdevore/lesson04/target/'

    # Make sure target directory exists
    if not os.path.exists(target_directory):
        print('Target directory {} does not exist. Exiting.'.format(target_directory))
        sys.exit()

    # Test with text and image files
    source_files = ['/Users/gdevore21/Documents/Certificate Programs/Python/PYTHON210/SP_Online_PY210/students/gregdevore/lesson04/test_file.txt',
                    '/Users/gdevore21/Documents/Certificate Programs/Python/PYTHON210/SP_Online_PY210/students/gregdevore/lesson04/test_image.jpg']

    for source_file in source_files:
        # Verify that each file exists
        if os.path.exists(source_file):
            copy_file(source_file,target_directory)
        else:
            print('Source file \'{}\' not found. Skipping.'.format(source_file))

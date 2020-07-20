#!/user/bin/env python3

# Write a program which prints the full path for all files in the curent directory, one per line. use either the os module or pathlib.
import pathlib
import os

def iter_paths():
	from pathlib import Path
	p = Path('.')
	# create a dictionary of files to choose from in user prompt
	dict = {}
	files = [file.absolute() for file in p.iterdir()]
	for i, file in enumerate(files):
	 	dict[i] = file
	return dict

def user_prompt(dict):
	prompt = ""
	for key in dict:
		file_name = os.path.basename(dict[key])
		prompt += "{}: {}\n".format(key, file_name)
	print("Type one of the following integers and press enter")
	user_input = int(input(prompt))

	copy(dict[user_input])

# Open file in binary
def copy(file):

	f = open(file, mode='rb', buffering=0, encoding=None, errors=None, newline=None, closefd=True, opener=None)
	copy_of = "copy_of_{}".format(os.path.basename(f.name))
	
	read_file = f.read()

	with open(copy_of, "wb") as copy:
		copy.write(read_file)


def main():
	# a dictionary of present working directory paths
	pwd_paths = iter_paths()
	user_prompt(pwd_paths)
	print("File has copied")


if __name__ == "__main__":
	main()
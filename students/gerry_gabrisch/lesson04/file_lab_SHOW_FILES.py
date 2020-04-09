#!/usr/bin/env python3
import os
import sys


def get_files(the_directory):
	'''Prints the path and file names in a single directory.
	   Input parameter = a directory path as a string.'''
	files = []
	#walk the directory and get the file names...
	for (dirpath, dirnames, filenames) in os.walk(the_directory):
		#add file names to the list...
		files.extend(filenames)
		for f in files:
			print(the_directory + f)
		print()
		#Break out before this loop before printing the sub-directories...
		break
		
		
def get_path():
	'''Prompts the user for a file path...'''
	return input('Enter a valid file path. >> ')


def get_options():
	while True:
		options = input('Options\n1. Enter 1 to view files in a directory?\n2. Or 2 to quit. > ')
		if options =='1':
			the_directory = get_path()
			get_files(the_directory)
		elif options == '2':
			print('Thanks, bye.')
			sys.exit()
		else:
			#Reprompt for invalid answers...
			print("That's not a valid option. Try again.\n")


def main():
	get_options()
	
	
if __name__ == "__main__":
	main()  

#!/usr/bin/env python3
import os
import sys

def OnlyThisDirectory(theDirectory):
	'''prints the path and file names is a single directory...'''
	print('Print the file names in this directory only.\n')
	files = []
	#walk the directory and get the file names...
	for (dirpath, dirnames, filenames) in os.walk(theDirectory):
		#add file names to the list...
		files.extend(filenames)
		for f in files:
			print(theDirectory + f)
		print()
		#break out before this loop gets to sub-directories...
		break
		

def PrintItAll(theDirectory):
	'''this tool prints all the files and paths, including subdirectories...'''
	print('Print all the files, and files in sub directories.\n')
	#sift through all the directories and get the file paths...
	for root, dirs, files in os.walk(theDirectory):
		for file in files:
			print(os.path.join(root, file))	

def GetPath():
	'''prompts the user and returns a file path...'''
	return input('Enter a valid file path >> ')

def main():
	while True:
		print('Print file paths...')
		#give the user some options...
		options = input('Options\n1. View files in a directory only?\n2. View all files in this and all sub-directories?\n3. Or 3 to quit > ')
		if options =='1':
			print('Print the files in this directory only.\n')
			theDirectory = GetPath()
			OnlyThisDirectory(theDirectory)
		elif options == '2':
			print('Print all files in the directory (and all sub directories)\n')
			theDirectory = GetPath()
			PrintItAll(theDirectory)
		elif options == '3':
			print('Thanks, bye.')
			sys.exit()
		else:
			#if the user screws up...
			print("That's not a valid option. Try again.\n")


if __name__ == "__main__":
	main()  

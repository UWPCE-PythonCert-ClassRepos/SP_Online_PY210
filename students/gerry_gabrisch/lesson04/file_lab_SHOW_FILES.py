#!/usr/bin/env python3
import os
import sys

#def OnlyThisDirectory(theDirectory):
	#print('Print the files in this directory only.\n')
	#arr = next(os.walk('.'))[2]
	#print('\n'.join(arr))
	#print()
def OnlyThisDirectory(theDirectory):
	print('Print the file names in this directory only.\n')
	from os import walk
	files = []
	for (dirpath, dirnames, filenames) in walk(theDirectory):
		files.extend(filenames)
		print('\n'.join(files))
		print()
		break
		

def PrintItAll(theDirectory):
	print('Print all the files, and directories including paths.\n')
	for root, dirs, files in os.walk(theDirectory):
		for file in files:
			print(os.path.join(root, file))	
def GetPath():
	return input('Enter a valid file path >> ')

def main():
	while True:
		print('Print file paths...')
		options = input('Options\n1. View files in a directory only?\n2. View all files and folders in all sub-directories?\n3. To quit > ')
		
		
		if options =='1':
			print('Print the files in this directory only.\n')
			theDirectory = GetPath()
			OnlyThisDirectory(theDirectory)
		if options == '2':
			print('Print the full paths for all files in the directory (and all sub directories)\n')
			theDirectory = GetPath()
			PrintItAll(theDirectory)
		if options == '3':
			print('Thanks, bye.')
			sys.exit()		
		
if __name__ == "__main__":
	main()  

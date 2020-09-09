## Lesson 2 Assignment Grid Printer
## By: B. Matthews
## 9/8/2020

def printGrid(n):
	while n:			#iterate through the rows
		if n<0:
			break
		n-=1

		count=n
		print ('+ ', end='')
		count-=1

		i=n
		##while (i>0):
			while count:		#iterate through the columns
				if count<0:
					break
				print ('-', end=' ')
				count-=1
			print('+')
		##i-=1
	print()			#advance row

printGrid(3)



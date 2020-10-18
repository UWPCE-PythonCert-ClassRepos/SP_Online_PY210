#Write a function that draws a grid like the following:
#+ - - - - + - - - - +
#|         |         |
#|         |         |
#|         |         |
#|         |         |
#+ - - - - + - - - - +
#|         |         |
#|         |         |
#|         |         |
#|         |         |
#+ - - - - + - - - - +
 

#Define two different lines
full_line = '+ ' + 4*'- ' + '+ ' + 4*'- ' + '+'
side_line = '|' + 9*' ' + '|' + 9*' ' + '|'

#Print the lines to create the grid
for i in range(0,3):
	print(full_line)
	for j in range(0,4):
		if i < 2:
			print(side_line)
		else:
			pass
		
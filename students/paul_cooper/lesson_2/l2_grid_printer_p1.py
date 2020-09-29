# This prints the exact grid form the exercise

x = 11

for i in range(x):
	for j in range(x):
		if j%5==0 and i%5==0:
			print('+', end=' ')
		elif j%5==0:
			print('|', end=' ')
		elif i%5==0:
			print('-', end=' ')
		else:
			print(' ', end=' ')	
	print()
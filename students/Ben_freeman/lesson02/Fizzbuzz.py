def fizz_buzz(n,m,o):                #chose what integers you want to play with. n and m are the multiples and o is the max number you are going to.
	i=1                              #initialize i. (I think thats what doing this is called, forgive me if im just making up words.)
	while i<=o:
		if i%(n*m)==0:               #if i is divisable by two reletively prime numbers then it is divisable by their product, proof left for the reader)
			print("Fizz Buzz")
		elif i%n==0:                 #is i mod n is zero then i is a multiple of n
			print("Fizz")
		elif i%m==0:                 # same as above but for m
			print("Buzz")
		else:                        #how we print numbers
			print(i)
		i+=1                         #ticks up i by 1 each time we run the loop.
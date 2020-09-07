def formatString(a,b,c,d):
	A = str(a).zfill(3)
	A = "file_" + A
	print(A)
	B = float("{:.2f}".format(b))
	print(B)
	C = "{:.2e}".format(c)
	print(C)
	D = "{:.2e}".format(d)
	print(D)
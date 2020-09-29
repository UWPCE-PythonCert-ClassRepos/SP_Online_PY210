# too many lines but solves the problem
line1="+ - - - - + - - - - +"
line2="|         |         |"
print(line1)
print(line2)
print(line2)
print(line2)
print(line2)
print(line1)
print(line2)
print(line2)
print(line2)
print(line2)
print(line1)

# simplier way, but not super simplified
line1="+ - - - - + - - - - +"
line2="|         |         |"
line2n='\n'.join([line1,line2,line2,line2,line2]*2)
print(line2n)
print(line1)


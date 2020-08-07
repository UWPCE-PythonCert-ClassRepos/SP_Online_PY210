#Exercise2.2.py

#Creating Grid the "Hard way"
print("+ - - - - + - - - - +")
print("|         |         |")
print("|         |         |")
print("|         |         |")
print("|         |         |")
print("+ - - - - + - - - - +")
print("|         |         |")
print("|         |         |")
print("|         |         |")
print("|         |         |")
print("+ - - - - + - - - - +")

#Creating square grids of various widths
x = 5
y = 2
#header to generate columns
for w in range(y):
    #first row
    for z in range(x+1):
        line = ""
        if z == 0:
            line = line + "+"
        elif z == w*x:
            line = line + " +"
        else:
            line = line + " -"
        print(line, end= "")

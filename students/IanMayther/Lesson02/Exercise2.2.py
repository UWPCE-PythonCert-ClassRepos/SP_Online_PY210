#Exercise2.2.py

#CREATING STATIC GRID
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

#CREATING GRID WITH ARBITRARY WIDTHS
#arbitrary values
x = 5
y = 2
#header to generate columns
for t in range(y):
    line = ""
    #first row
    for z in range(y*x): 
        if z == 0:
            line = line + "+"
        elif z > 1 and x%z == 0:
            line = line + " +"
        else:
            line = line + " -"
    line = line + " +"
    print(line)

    #Vertical Rows.
    for r in range(x-1):
        line = ""
        for w in range(y):
            for z in range(x+1): 
                if z == 0:
                    line = line + "|"
                elif z == x:
                    line = line + " "
                else:
                    line = line + "  "
        line = line + "|"
        print(line)

#Footer
line = ""
for z in range(y*x):
    if z == 0:
        line = line + "+"
    elif z > 1 and x%z == 0:
        line = line + " +"
    else:
        line = line + " -"
line = line + " +"
print(line)
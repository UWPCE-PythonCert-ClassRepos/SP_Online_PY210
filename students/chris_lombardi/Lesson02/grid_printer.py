#UWPCE PY210
#Lesson02, Grid Printer

PLUS = "+"
MINUS ="-"
VERT_BAR = "|"

#Print Header/Footer Row
print(PLUS, end=" ")
for i in range(4):
    print(MINUS, end=" ")
print(PLUS, end = " ")
for i in range(4):
    print(MINUS, end = " ")
print(PLUS)

#Print Cell Rows
for i in range(4):
    print("|", end = " ")
    for j in range(4):
        print(" ", end = " ")
    print("|", end = " ")
    for j in range(4):
        print(" ", end = " ")
    print("|")

#Print Header/Footer Row
print(PLUS, end=" ")
for i in range(4):
    print(MINUS, end=" ")
print(PLUS, end = " ")
for i in range(4):
    print(MINUS, end = " ")
print(PLUS)

#Print Cell Rows
for i in range(4):
    print("|", end = " ")
    for j in range(4):
        print(" ", end = " ")
    print("|", end = " ")
    for j in range(4):
        print(" ", end = " ")
    print("|")

#Print Header/Footer Row
print(PLUS, end=" ")
for i in range(4):
    print(MINUS, end=" ")
print(PLUS, end = " ")
for i in range(4):
    print(MINUS, end = " ")
print(PLUS)
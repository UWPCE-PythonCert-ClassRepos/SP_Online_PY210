"""
Programming In Python - Lesson 1 Task 2: Puzzles - String-2
Code Poet: Anthony McKeever
Date: 07/20/2019
"""

# String-2 > double_char 
def double_char(inString):
    output = ""
    template = "{0}{0}"
    for c in inString:
        output = output + template.format(c)
    return output

# String-2 > count_hi 
def count_hi(inString):
  return inString.count("hi")

# String-2 > cat_dog
def cat_dog(inString):
    cat = inString.count("cat")
    dog = inString.count("dog")
    return cat == dog

# String-2 > count_code 
def count_code(inString):
    count = 0
    lenStr = len(inString)
    for i in range(lenStr):
        if inString[i] == 'c' and i < lenStr - 3:
            if inString[i + 1] == 'o' and inString[i + 3] == 'e':
                count += 1
    return count

# String-2 > end_other 
def end_other(a, b):
    endsWithB = a.lower().endswith(b.lower())
    endsWithA = b.lower().endswith(a.lower())
    return endsWithB or endsWithA

# String-2 > xyz_there 
def xyz_there(inString):
    xyzCount = inString.count("xyz")
    dotXyzCount = inString.count(".xyz")
    return xyzCount > dotXyzCount

#def ReturnNameError(inString):
    #error = inString + x
    #return error


#def ReturnTypeError(inString):
    #error = inString/5
    #return error

#def ReturnSyntaxError(inString):
    #error =instring %& 7
    #return error
    

def ReturnAttributeError(inString):
    error = inString.font_color
    return error


someString = 'foo'

#ReturnNameError(someString)

#ReturnSyntaxError(someString)

#ReturnTypeError(someString)

ReturnAttributeError(someString)
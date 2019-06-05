#!/usr/bin/python

# lesson01
# Exception exercise
# Chuck Stevens :: CCSt130

# need for exceptions
# import sys

#NameError

def nameErr():

    tee = 10
    #hee = 20
    teeHee = 0

    try:
        teeHee = tee + hee
    except NameError:
        print("\nSorry, variable 'hee' is not defined.")
    else:
        print("\nThe sum of '%d' plus '%d' is: '%d'." % (tee, hee, teeHee))
    finally:
        print("\nThat's all I have to say about that.")        

nameErr()

'''
#TypeError

def typeErr():

    tee = 50
    # hee = 100
    hee = "oops"

    try:
        teeHee = tee + hee
    except TypeError:
        print("\nSorry, despite the magic of python you can't add a str to an int.")
    else:
        print("\nThe sum of '%d' plus '%d' is: '%d'." % (tee, hee, teeHee))
    finally:
        print("\nThat's all I have to say about that.")        

typeErr()
'''

'''
#SyntaxError

def syntaxErr():

    tee = 200
    hee = 400
    
    try:
        eval('teeHee = [tee + hee]')
        #teeHee = (tee + hee)
    except SyntaxError:
        print("\nWhoa, beginner bracket mistake!")
    else:
        #print("\nThe sum of '%d' plus '%d' is: '%d'." % (tee, hee, teeHee))
        print("\nThe value of 'tee' is '%d' and the value of 'hee' is '%d'." % (tee, hee))        
    finally:
        print("\nThat's all I have to say about that.")        

syntaxErr()
'''

'''
#AttributeError

def attribErr():

    tee = 300
    hee = 500
    
    try:
        teeHee = (tee + hee)
        print(tee.teehee) #invalid!
    except AttributeError:
        print("\nWhoa, you can't do that!")
    else:
        print("\nThe sum of '%d' plus '%d' is: '%d'." % (tee, hee, teeHee))
    finally:
        print("\nThat's all I have to say about that.")        

attribErr()
'''














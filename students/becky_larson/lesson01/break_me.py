#!/usr/bin/env python

def Function1(parm):
    print ('-- should produce NameError')
    print (parm2)

def Function2(parm):
    print ('-- should produce TypeError')
    print (7/parm)

def Function3(parm):
    print ('Function3')
    print ('-- should produce SyntaxError')
    myint = 5
#    len(parm) = myint

def Function4(parm):
    print ('Function4')
    print ('-- should produce Attribute Error')
    x=10
    x.append(6)

#print ('**** calling Function1')
#Function1('test')

#print ('**** calling Function2')
#Function2('4')

#print ('**** calling Function3')
#Function3('tests')

print ('**** calling Function4')
Function4('test')

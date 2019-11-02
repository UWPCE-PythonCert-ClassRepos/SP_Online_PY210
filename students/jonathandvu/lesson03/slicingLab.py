#!/usr/bin/env python
# PY210 Lesson 3 Slicing Lab
# Jonathan Vu
#
def exchangeFirstAndLast(inputVariable):
    if isinstance(inputVariable, int):
        inputVariable = str(inputVariable)
    part1 = inputVariable[0:1]
    part2 = inputVariable[1:len(inputVariable) - 1]
    part3 = inputVariable[len(inputVariable) - 1:len(inputVariable)]
    outputVariable = part3 + part2 + part1
    return outputVariable

def removeEveryother(inputVariable):
    if isinstance(inputVariable, int):
        inputVariable = str(inputVariable)
    outputVariable = inputVariable[0::2]
    return outputVariable

def firstLastEveryother(inputVariable):
    if isinstance(inputVariable, int):
        inputVariable = str(inputVariable)
    outputVariable = inputVariable[4:len(inputVariable)-4:2]
    return outputVariable

def chaChaSlideReverseReverse(inputVariable):
    if isinstance(inputVariable, int):
        inputVariable = str(inputVariable)
    outputVariable = inputVariable[len(inputVariable)-1::-1]
    return outputVariable

def neverCutPizzaInThirds(inputVariable):
    if isinstance(inputVariable, int):
        inputVariable = str(inputVariable)
    thirdValue = int(len(inputVariable)/3)
    firstThird = inputVariable[0:thirdValue]
    middleThird = inputVariable[thirdValue:thirdValue*2]
    lastThird = inputVariable[thirdValue*2:]
    reStitch = lastThird + firstThird + middleThird
    return reStitch

def testSlicingFunctions():
    assert exchangeFirstAndLast('switcharoo') == 'owitcharos'
    assert removeEveryother('abcdefg') == 'aceg'
    assert firstLastEveryother('abcdefghijklmnop') == 'egik'
    assert chaChaSlideReverseReverse('reverse') == 'esrever'
    assert chaChaSlideReverseReverse(123456) == '654321'
    assert neverCutPizzaInThirds('123456789') == '789123456'
    print('All Tests Passed!');
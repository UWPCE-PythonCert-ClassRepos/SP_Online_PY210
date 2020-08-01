#!/usr/bin/env python3

def string_times(str, n):
    return n*str

def front_times(str,n):
    return n*str if len(str)< 3 else n*str[0:3]

def string_bits(str):
    str_new = ''
    for n in range (0,len(str)):
        if n%2 ==0:
            str_new += str[n]
    return str_new

def string_splosion(str):
    str_new = ''
    for n in range (0,len(str)+1):
        str_new += str[0:n]
    return str_new

def last2(str):
    if len(str) <=2:
        return ('invalid input')
    else:
        search_str = str[len(str)-2:len(str)]
    count = 0
    for i in range (0,len(str)-2):
        if str[i:i+2] == search_str:
            count += 1
    return count

def array_count9(nums):
    count = 0
    for i in range (0,len(nums)):
        count += 1 if nums[i] == 9 else 0
    return count

def array_front9(nums):
    front4_has9 = False
    search_band = len(nums) if len(nums) < 4 else 4
    for i in range (0,search_band):
        if nums[i] == 9:
            front4_has9 = True
    return front4_has9

def array123(nums):
    if len(nums) < 3:
        return False
    for i in range (0, len(nums)-2):
        if nums[i:i+3] == [1,2,3]:
            return True
    return False

def string_match(a,b):
    match_count = 0
    search_band = len(a) if len(a) < len(b) else len(b)
    for i in range (0, search_band-1):
        match_count += 1 if a[i:i+2] == b[i:i+2] else 0
    return match_count

#print out of solutions
print('string_times')
print(string_times('Hi',2))
print(string_times('Hi',3))
print(string_times('Hi',1))
print()
print('front_times')
print(front_times('Chocolate',2))
print(front_times('Chocolate',3))
print(front_times('Abc',3))
print()
print('string_bits')
print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))
print()
print('string_splosion')
print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))
print()
print('last2')
print(last2('hixxhi'))
print(last2('xaxxaxaxaxx'))
print(last2('axxxaaxx'))
print()
print('array_count9')
print(array_count9([1,2,9]))
print(array_count9([1,9,9]))
print(array_count9([1,9,9,3,9]))
print()
print('array_front9')
print(array_front9([1,2,9,3,4]))
print(array_front9([1,2,3,4,9]))
print(array_front9([1,2,3,4,5]))
print()
print('array123')
print(array123([1,2,3]))
print()
print('string_match')
print(string_match('xxcaazz','xxbaaz'))
print(string_match('abc','abc'))
print(string_match('abc','axc'))

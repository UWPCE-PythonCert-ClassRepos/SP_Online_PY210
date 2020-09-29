#Gerald (Gerry) Gabrisch
#UW Python PY210 - Lesson 1
#2020-03-25

##sleep_in
#def sleep_in(weekday, vacation):
    #if not weekday or vacation:
        #return True
    #else:
        #return False  
#isWeekday = False
#onVacation = True
#x = sleep_in(isWeekday, onVacation)
#print(x)
###############################################
##monkey_trouble
#def monkey_trouble(a_smile, b_smile):
    #if a_smile and b_smile or not a_smile and not b_smile:
        #return True
    #else:
        #return False
#a_smile = False
#b_smile = True
#x = monkey_trouble(a_smile, b_smile)
#print (x)
###############################################
##sum_double
#def sum_double(a, b):
    #if a == b:
        #return 2*(a+b)
    #else:
        #return a + b
    
#a = 2
#b = 2
#print (sum_double(a,b))
###############################################
##diff21
#def diff21(n):
    #if n > 21:
        #return abs(n - 21)*2
    #else:
        #return abs(n - 21)
#print (diff21(22))
###############################################
##parrot_trouble
#def parrot_trouble(talking, hour):
    #if talking == False:
        #return False
    #if 6 < hour <= 20 and talking :
        #return False
    #else:
        #return True
#talking = True
#hour = 7
#print(parrot_trouble(talking, hour))
###############################################
##makes10
#def makes10(a, b):
    #if a == 10 or b == 10 or a + b == 10:
        #return True
    #else:
        #return False
#a = 1
#b = 9
#print(makes10(a,b))
###############################################
##near_hundred
#def near_hundred(n):
    #if 90 <= n <= 110 or 190 <= n <= 210:
        #return True
    #else:
        #return False
    
    
#n = 201
#print(near_hundred(n))
###############################################
##pos_neg
#def pos_neg(a, b, negative):
    #if negative == False:
        #if a * b < 0 :
            #x = True
        #else:
            #x =  False
    #else:
        #if a < 0 and b < 0:
            #x = True
        #else:
            #return False
    #return x
#a = -1
#b = -10
#negative = True
#print(pos_neg(a, b, negative))
###############################################
##not_string()
#def not_string(x):
    #if x[:3] == 'not':
        #return x
    #else:
        #return 'not ' + x
#x = 'omething'
#print(not_string(x))
###############################################
##missing_char
#def missing_char(str, n):
    #newstring = str = str[0:n] + str[n+ 1:]
    #return newstring
#str = 'foobar'
#n = 3
#print(missing_char(str, n))
###############################################
##front_back
#def front_back(str):
    #if len(str) <= 1:
        #return str
    #else:
        #str = str[-1] + str[1:-1]+str[0]
        #return str
#str = "A shrubbery!"
#print(front_back(str))
###############################################
##front3
#def front3(str):
    #if len(str)>= 3:
        #return str[:3]+str[:3]+str[:3]
    #else:
        #return str+ str + str
#str = 'ab'
#print(front3(str))
###############################################

####                Warmup-2

##stringTimes
#def string_times(str, n):
    #'''Given a string and a non-negative int n, return a larger string that is n copies of the original string.'''    
    #if n > 0:
        #n = n-1
        #newstr = ''
        #count = 0
        #while count <= n:
            #newstr = newstr + str
            #count += 1
        #return newstr
    #else:
        #return ''
#n = 8
#str = 'Hi'
#print(string_times(str, n))
###############################################
#front_times
#def front_times(str, n):
    #'''Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;'''
    #n = n-1
    #if len(str)<3:
        #front = str
    #else:
        #front = str[:3]
    #newstr = ''
    #count = 0
    #while count <= n:
        #newstr = newstr + front
        #count += 1
    #return newstr
   
#str = "fubar"
#n = 2
#print(front_times(str, n))
###############################################
##string_bits
#def string_bits(str):
    #'''Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".'''
    #str = str[0::2]
    #return str
#str = "12121212"
#print(string_bits(str))
###############################################
##string_splosion
#def string_splosion(str):
    #'''Given a non-empty string like "Code" return a string like "CCoCodCode".'''  
    #strLength = len(str)
    #counter = 0
    #newStr = ''
    #while counter <= strLength:
        #newStr = newStr + str[:counter]
        #counter += 1
    #return newStr
#str = 'Code'
#print(string_splosion(str))
###############################################
##last2
#def last2(str):
    #'''Given a string, return the count of the number of 
    #times that a substring length 2 appears in the string 
    #and also as the last 2 chars of the string, so "hixxxhi" 
    #yields 1 (we won't count the end substring).'''
    #if str== "":
        #occuranceCounter = 1
    #else:
        #last2char = str[-2:]
        #placeCounter = 0
        #occuranceCounter = 0
        #for i in str:
            #if str[placeCounter:placeCounter+2] == last2char:
                #occuranceCounter += 1
            #placeCounter += 1
    #return (occuranceCounter-1)
#str = 'axxxaaxx'
#print(last2(str))
###############################################
##array_count9
#def array_count9(nums):
    #'''Given an array of ints, return the number of 9's in the array.'''
    #counter = 0
    #for i in nums:
        #if i == 9:
            #counter +=1
    #return counter
#nums = [9,2,3,4,9]
#print(array_count9(nums))
###############################################
##array_front9
#def array_front9(nums):
    #'''Given an array of ints, return True if one of the first 4 
    #elements in the array is a 9. The array length may be less than 4.'''
    #counter = 0
    #thecondition = False
    #for i in nums:
        #if i == 9 and counter <=3:
            #thecondition = True
        #counter +=1
    #return thecondition

#nums = [9]
#print(array_front9(nums))
###############################################
##array123
#def array123(nums):
    #'''Given an array of ints, return True if the sequence of numbers 1, 2, 3 
    #appears in the array somewhere.'''
    #counter = 0
    #for i in nums:
        #if nums[counter:counter +3] == [1,2,3]:
            #return True
        #counter += 1
    #else:
        #return False
       
#nums = [10,20,30,10,20,30]
#print(array123(nums))
###############################################
##string_match
#def string_match(a,b):
    #'''Given 2 strings, a and b, return the number of the positions 
    #where they contain the same length 2 substring. So "xxcaazz" and 
    #"xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear 
    #in the same place in both strings.'''
    #occurance = 0
    #shortList = min(len(a), len(b))
    #for i in range(shortList-1):
        #aa = a[i:i+2]
        #bb = b[i:i+2]
        #if aa == bb:
            #occurance +=1
    #return occurance  
#a = 'xx'
#b ='xx'
#print(string_match(a,b))
###############################################

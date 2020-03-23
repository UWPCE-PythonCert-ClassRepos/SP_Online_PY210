# sleep_in
def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False

# diff21
def diff21(num):
    if num <= 21:
        return abs(21 - num)
    else:
        return (abs(21 - num))*2

# near_hundred
def near_hundred(num):
    if abs(num-100) <= 10 or abs(num-200) <= 10:
        return True
    else:
        return False

# missing_char()
def missing_char(my_str,my_index):
    if my_index > len(my_str) - 1:
        print(f"The string index:{my_index} is invalid.")
        return (False)
    else:
        tmp_str ="" #define a new string
        for i in range(0,len(my_str)):
            if i != my_index:
                tmp_str = tmp_str + my_str[i]
        return (tmp_str)

# monkey_trouble()
def monkey_trouble(a_smile,b_smile):
    # if only one monkey is smiling then return False to indicate we are not in trouble.
    return not ((a_smile and not b_smile) or (not a_smile and b_smile))

# string_times()
def string_times(my_str,n):
    new_str = ""
    for i in range(0,n):
        new_str = new_str + my_str
    return new_str


# string_splosion()
def string_splosion(my_str):
    if my_str or my_str.strip():# test if a string is either None or Empty or Blank.
        new_str = ""
        str_len = len(my_str)
        for i in range(0,str_len):
            new_str = new_str  + my_str[:i+1]
        return new_str
    else:
        return False
"""my_str = 'Good'
new_str = string_splosion(my_str)
if new_str != False:
   print(f"'{my_str}' to '{new_str}'.")
else :
   print("Empty or Blank string!")"""

# array_front9()
def array_front9(num_array):
    my_len = len(num_array)
    if my_len > 4:
       my_len = 4

    for i in range(0,4):
        if num_array[i] == 9 :
            return True

    return False

"""if array_front9([1,2,5,0,8,1]):
    print("There is a 9 in the first 4 elements of the array")
else:
    print("No 9 in the first 4 elements of the array")
"""

# front_times()
def front_times(my_str, num):
    front_len = 3
    str_len = len(my_str)
    if str_len <= front_len:
        front_len = str_len
    front_str = my_str[:front_len] # !!!truncate the fix length of string to the new string.
    new_str = ""
    for i in range(0,num):
        new_str  = new_str + front_str
    return new_str
#my_str = 'ag'
#print(f"The Old str: {my_str}, new str: {front_times(my_str,2)} ")

# array123()
def array123(my_array):
    sub_array_len = 3
    sub_array = [1,2,3]
    my_array_len = len(my_array)
    if my_array_len < 3 :
        return False
    for i in range(0,my_array_len):
        if i + sub_array_len <= my_array_len:
            if sub_array[0] == my_array[i] :
                tmp_count = 0
                for j in range(0,sub_array_len):
                    if sub_array[j] != my_array[i+j]:
                        break
                    else:
                        tmp_count += 1 # count the matching number
                if tmp_count == sub_array_len:
                    return True
        else:
            return False

"""my_array = [1,2,3,1,2,3]
if array123(my_array):
    print(f"The string {my_array} has the 1,2,3 patten.")
else:
    print(f"The string {my_array} does not has the 1,2,3 patten.")
"""
# string_bits()
def string_bits(my_str):
   str_len = len(my_str)
   new_str = ""
   for i in range(0,str_len):
       if i % 2 == 0 :
           new_str = new_str + my_str[i]
   return new_str
#my_str = 'hellopy'
#print(f"The old str:{my_str}, new str: {string_bits(my_str)}")


# combo_string()
def combo_string(a_str,b_str):
    if len(a_str) == len(b_str):
           return(a_str + b_str + a_str)
    else:
       if len(a_str) < len(b_str):
           return(a_str + b_str + a_str)
       else:
           return(b_str + a_str + b_str)

"""a_str = 'Hel'
b_str = 'ABC'
print(f"'{a_str}' and '{b_str}' output: '{combo_string(a_str,b_str)}'")
"""

# has23()
def has23(num_array):
    for i in range(0,len(num_array)):
        if num_array[i] == 2 or num_array[i] == 3 :
            return True

    return False
# near_ten()
def near_ten(num):
    if num % 10 < 3 or num % 10 > 7 :
        return True
    else:
        return False


# xyz_there() with using library
def xyz_there(mystr):
    sub_str = 'xyz'
    sub_str_len = 3
    sub_array = [1,2,3]
    if len(mystr) < 3 :
        return False
    for i in range(0,len(mystr)):
        if mystr[i] == sub_str[0] and i+2 < len(mystr):
            if sub_str[0] == mystr[i] and sub_str[1] == mystr[i+1] and sub_str[2] == mystr[i+2] :
                if i==0 :
                    return True
                else:
                    if mystr[i-1] != '.':
                        return True
    return False

# using library re to code xyz_there()
import re
def xyz_there_1(mystr):
    for match in re.finditer(sub_str, mystr):
        if match.start() == 0 :
            return True
        elif str[match.start()-1] != '.':
            return True
        else :
            pass

my_str = 'ABC.xyzxy'
#if xyz_there(my_str):
#    print(f"Str: {my_str} has the 'xyz'.")
#else:
#    print(f"Str: {my_str} does not has the 'xyz'.")

# sum67()

def find_end_index(myindex, num_array):
    for j in range(myindex+1,len(num_array)):
          if num_array[j] == 7:
            return (j)  # find end_index
    print("Something is wrong! every 6 mush be followed by at least one 7 to end the section.")
    exit()

def sum67(num_array):
    end_index = -1
    tot = 0
    for i in range(0,len(num_array)):
        if end_index == -1 :
            if num_array[i] == 6:
                end_index = find_end_index(i, num_array)
            else:
                tot = tot + num_array[i]
        else :
            if i ==  end_index:
                end_index = -1 # reset the end_index
            else:# ignor the numbers between 6 to 7
                pass
    return tot

my_num =[1,2,2,6,1,2]
#my_num =[1,2,2,6, 98,99,7,2,5, 6, 1, 7]
#my_num =[1,2,2,8,9,7]
my_tot = sum67(my_num)
print(f"the sum of num array: {my_num} is {my_tot}")

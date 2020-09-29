# -*- coding: utf-8 -*-

"""
Lesson03 :: Slicing Lab
Exercise 3.1
@author: Chuck Stevens :: CCSt130
Created on Tue May 28 16:26:02 2019
"""

import math # for rounding
import random # PRNG for fun


test_str1 = ("The greatness of a man is not in how much wealth he acquires, but in his integrity and his ability to affect those around him positively...Bob Marley")

test_str2 = ('There is no charm equal to tenderness of heart...Jane Austen')

t_strings = (("All that we see or seem is but a dream within a dream...Edgar Allan Poe"),\
                ("Lord, make me an instrument of thy peace. Where there is hatred, let me sow love...Francis of Assisi"),\
                ("The only journey is the one within...Rainer Maria Rilke"),\
                ("Good judgment comes from experience, and a lot of that comes from bad judgment...Will Rogers"),\
                ("Think in the morning. Act in the noon. Eat in the evening. Sleep in the night...William Blake"),\
                ("Life without love is like a tree without blossoms or fruit...Khalil Gibran"),\
                ("No act of kindness, no matter how small, is ever wasted...Aesop"),\
                ("Love cures people--both the ones who give it and the ones who receive it...Karl A. Menninger"),\
                ("Dance like no one is watching...Satchel Paige"))

def first_is_last(my_str):
    """ Manipulate strings in various ways, such as swapping the first and last element. """
    # Exchange first and last char in str
    var_swap = my_str[-1:] + my_str[1:-1] + my_str[:+1]
   
    return(var_swap)

def every_other(my_str):    
    # Print str with every other letter removed
    
    new_str = my_str[::2]
    # print()
    # print(new_str)
    
    return(new_str)

def take_four(my_str):
    # Print all but first and last 4 char
    
    minus_four = my_str[4:-4]
    
    # print()
    # print(minus_four)
    
    return(minus_four)

def reverse_str(my_str):    
    # Print all strings (each char in str) in reverse order
    # print()
    # print("Test: ", end = "")
    # print(my_str[::-1])   

    new_str = my_str[::-1]

    # print()    
    # print(new_str)
    
    return(new_str)

def slice_thirds(my_string):
    """ Breaks a string into 3 nearly equal sections, prints and returns it. """
    
    str_length = (len(my_string))
    
    # determine the length of one third
    # round down to avoid float
    len_one_third = (math.floor((str_length)/3))
    
    n = len_one_third # new variable name that's shorter
    
    first_third = my_string[:n]
    # print(first_third)
    
    second_third = my_string[n:-n]
    # print(second_third)
    
    last_third = my_string[-n:]
    # print(last_third)
    
    three_thirds = [first_third, second_third, last_third]
    # print(three_thirds)
    
    # attempt to reorder string randomly
    wheel_of_random(three_thirds)
    
    return(three_thirds)

def wheel_of_random(my_str):
    """ This function will print each third of a string in random order. """

    # shuffle order in my_str
    # difficult to test
    random.shuffle(my_str)

def test_series():
    """ This is a test function. """
    
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    
    print()
    print("*** Running tests! ***")

    assert first_is_last(test_str1) == "yhe greatness of a man is not in how much wealth he acquires, but in his integrity and his ability to affect those around him positively...Bob MarleT"
    assert every_other(test_str1) == "Tegeteso  a snti o uhwat eaqie,bti i nert n i blt oafc hs rudhmpstvl..o aly"
    assert take_four(test_str1) == "greatness of a man is not in how much wealth he acquires, but in his integrity and his ability to affect those around him positively...Bob Ma"
    assert reverse_str(test_str1)== "yelraM boB...ylevitisop mih dnuora esoht tceffa ot ytiliba sih dna ytirgetni sih ni tub ,seriuqca eh htlaew hcum woh ni ton si nam a fo ssentaerg ehT"
    
    assert first_is_last(test_str2) == "nhere is no charm equal to tenderness of heart...Jane AusteT"
    assert every_other(test_str2) == "Teei ocameult edreso er..aeAse"
    assert take_four(test_str2) == "e is no charm equal to tenderness of heart...Jane Au"
    assert reverse_str(test_str2)== "netsuA enaJ...traeh fo ssenrednet ot lauqe mrahc on si erehT"
    
    assert first_is_last(a_string) == "ghis is a strint"
    assert first_is_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    print()
    print("*** Tests passed! ***")

if __name__ == "__main__":

    def main():

        # Run each function and assign to names
        first_var = first_is_last(test_str1)   
        every_var = every_other(test_str1)
        four_var = take_four(test_str1)
        reverse_var = reverse_str(test_str1)
        thirds_var = slice_thirds(test_str1)
        
        # Print names' values
        print()
        print("And the results are: ")
        print()
        print(first_var)
        print()
        print(every_var)
        print()
        print(four_var)
        print()
        print(reverse_var)
        print()
        print(thirds_var)
        print()
        
        test_series()
        
        # Test
        """        
        for my_str in t_strings:
            first_is_last(my_str)   
            every_other(my_str)
            take_four(my_str)
            reverse_str(my_str)
            slice_thirds(my_str)
        """

main()

###

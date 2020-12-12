#!/usr/bin/env python3
#-------------------------------------------#
#Tittle: trigram_stories, PYTHON210 - Assignemnt 3
#Desc: Create a story using trigrams
#Change Log: (Who, When, What)
#Brent Kieszling, <2020-Nov-21>, created file, wrote pseudo  code
#Brent Kieszling, <2020-Nov-22>, developed and tested: create_trigram(), new_story()
#-------------------------------------------#
import random

#TODO Add code to take in a book text file
#TODO remove all undesireable characters from the book string
#Trigram works well for current setup

#DATA---------------------------------------
book_file = "sherlock.txt"

#PROCESS------------------------------------
def get_book(file_name):
    """Get text from provided file
    
    Args:
        file_name(str): Name of file
        
    Returns:
        book(str): Text from file
    """
    with open(file_name, 'r') as file:
        book = file.read()
    return book

def get_story(book):
    """Find and return just the story contents of a text file
    
    Args:
        book(str): Unmodifed book text
    Returns:
        story(str): Story text conditioned for use in a trigram
    """
    start_key = "\n\n\n\n\n\n\n\n\n\n"
    end_key = "\n\n\n\n\n\n\n\n\n\nEnd"
    start_pos = book.find(start_key)
    end_pos = book.find(end_key)
    story = book[start_pos:end_pos]
    return story

def create_trigram(str_book):
    """Return a dictionary of trigrams based on sample text
    
    Args:
        str_book(str): Sample text to base trigram on
    
    Returns:
        book_seed(dict): Dictionary of word pairs and possible trailers
    """
    lst_book = str_book.split()
    book_seed ={}
    length = len(lst_book)
    x = 0
    for x in range(length-2):
        pair = (lst_book[x], lst_book[x+1])
        follow = lst_book[x+2]
        #Either finds the key and updates the value or creates a new key and value
        book_seed[pair] = book_seed.get(pair, []) + [follow]
        x += 1
    return book_seed

def new_story(book_seed, num_words):
    """Generate new story of specified length based on a trigram (book_seed)
    
    Args:
        book_seed(dict): Dictionary of word pairs and lists of possible trailers
        num_words(int): Number of words in new story.
    Returns:
        none
    """
    #Set starting pair
    lst_pairs = []
    for key in book_seed:
        lst_pairs.append(key)
    one, two = random.choice(lst_pairs)
    lst_story = [one.capitalize(), two]
    x = 0
    while x in range(num_words-2):
        try:
            follow = random.choice(book_seed[(one, two)])
        except:
            follow = "alternatively,"
        lst_story.append(follow)
        #Establish new starting words when options exhausted
        if follow =="alternatively,":
            one, two = random.choice(lst_pairs)
            lst_story.append(one)
            lst_story.append(two)
            x += 2
        else:
            one = lst_story[x + 1]
            two = lst_story[x + 2]
        x +=1
    print(" ".join(lst_story) + ".")





#PRESENTATION INPUT/OUTPUT------------------
if __name__ == "__main__":
    words = int(input("How many words would you like the story to contain?\n"))
    print()
    base_book = get_story(get_book(book_file))
    seed = create_trigram(base_book)
    new_story(seed, words)


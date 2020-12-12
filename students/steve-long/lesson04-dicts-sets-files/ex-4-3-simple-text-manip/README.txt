# Python210 | Fall 2020
# ----------------------------------------------------------------------------
# Lesson04 | Simple Text Manipulation | ex-4-3-file-simple-text-manip/
# README
# Steve Long 2020-10-31


Contents:

a-prefects-uncle.txt ... Project Gutenberg EBook text doc of story by P. G. 
                         Wodehouse used to run script trigrammatron.py.

trigrammatron.py ....... An application that turns a text doc into a trigram 
                         structure (with plenty of cleanup) and displays 
                         three kinds of results: A chain of three-word phrases
                         that looks like a Haiku, random three-word phrases
                         using the entire document, and a view of the 
                         trigram structure: the map of two-word keys to 
                         the list of third words.
                                    
README.txt ............. This manifest document.


Directions:
-----------

trigrammatron:

Trigrammatron.py is an interactive app that requires a text file (with text data) to work. The included file "a-prefects-uncle.txt" will serve this purpose or you can provide your own file (text; no other format.) 

Run the application from the terminal via command ./trigrammatron.py. When prompted, enter the name of the provided file or one of your own.

Once the file is loaded, there are three menu choices:

[1] "Haiku". Generate a series of chained 3-word phrases that looks like a crazy Haiku
    until the chain is broken (tuple key does not map to a third word.) A new chain is 
    initiated each time.

[2] "Random Key". Generate one random 3-word phrase for each mapped trigram tuple key 
    in the trigrams data structure.

[3] "A-to-Z". Retrieve all the 3-word phrases mapped to each trigram tuple key in  
    alphabetical order.

[:X] Exit from application.
 

# -*- coding: utf-8 -*-

"""
Lesson02 :: Reverse3
CodingBat Exercise 
@author: Chuck Stevens :: CCSt130
Please note: I chose to use strings instead, as they're more interesting.
Created on Sun Jun 30 23:17:38 2019
"""

"""
Given an array of ints length 3, return a new array with the elements in reverse order, 
so {1, 2, 3} becomes {3, 2, 1}.
"""

def reverse_str(my_str):    
    # Reverse string and assign to return name
    new_str = (my_str[::-1])
    # Return modified string
    return(new_str)

if __name__ == "__main__":

    def main():      
        # Empty list for modified strings
        quote_reversed = []
        # Quotes from famous people to reverse
        my_quotes = [("Strive not to be a success, but rather to be of value.--Albert Einstein"), \
                     ("Two roads diverged in a wood, and I—I took the one less traveled by, And that has made all the difference.  –Robert Frost"), \
                     ("I attribute my success to this: I never gave or took any excuse.--Florence Nightingale"), \
                     ("You miss 100% of the shots you don’t take.--Wayne Gretzky"), \
                     ("I`ve missed more than 9000 shots in my career. I`ve lost almost 300 games. 26 times I`ve been trusted to take the game winning shot and missed. I`ve failed over and over and over again in my life. And that is why I succeed.--Michael Jordan"), \
                     ("The most difficult thing is the decision to act, the rest is merely tenacity.--Amelia Earhart"), \
                     ("Every strike brings me closer to the next home run.--Babe Ruth"), \
                     ("Definiteness of purpose is the starting point of all achievement.--W. Clement Stone"), \
                     ("Life is what happens to you while you’re busy making other plans.--John Lennon"), \
                     ("We become what we think about.--Earl Nightingale"), \
                     ("Twenty years from now you will be more disappointed by the things that you didn’t do than by the ones you did do, so throw off the bowlines, sail away from safe harbor, catch the trade winds in your sails.  Explore, Dream, Discover.--Mark Twain"), \
                     ("Life is 10% what happens to me and 90% of how I react to it.--Charles Swindoll"), \
                     ("The most common way people give up their power is by thinking they don’t have any.--Alice Walker"), \
                     ("The best time to plant a tree was 20 years ago. The second best time is now.--Chinese Proverb"), \
                     ("An unexamined life is not worth living.--Socrates"), \
                     ("Your time is limited, so don’t waste it living someone else’s life.--Steve Jobs"), \
                     ("Winning isn’t everything, but wanting to win is.--Vince Lombardi"), \
                     ("I am not a product of my circumstances. I am a product of my decisions.--Stephen Covey"), \
                     ("Every child is an artist.  The problem is how to remain an artist once he grows up.--Pablo Picasso"), \
                     ("I’ve learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel.--Maya Angelou")]
        # Iterate over every quote in list
        for quote in my_quotes:
            print()
            print(quote)
            # Run string thru reverse function and assign to name
            quote_temp = reverse_str(quote)
            # Append reversed string to another list
            quote_reversed.append(quote_temp)
            # Print reversed string
            print(quote_temp)

        """
        # Print new list            
        for rev_str in quote_reversed:
            print()
            print(rev_str)
            """

#### Program Entry Point ####            
main()






            
from collections import Counter

def count_evens(nums):
    """Return the number of even integers in the given list"""
    return len([num for num in nums if num % 2 == 0])

def make_dict(old_dict):
    """Return a new dictionary using the same keys but with the number of ‘a’s in each value of the given dictionary"""
    # Get list of keys from given dictionary
    keys = old_dict.keys()
    # Get list of values from given dictionary
    # Use Counter() to count the number of 'a' in each value
    # Assign the new list of values
    values = [Counter(val)['a'] for val in old_dict.values()]
    # Use dictionary comprehension to create a new dict
    new_dict = {key: val for key, val in zip(keys, values)}

    return new_dict

def main():
    # Using a list comprehension, return the number of even integers in the given list.
    assert(count_evens([2, 1, 2, 3, 4]) == 3)
    assert(count_evens([2, 2, 0]) == 3)
    assert(count_evens([1, 3, 5]) == 0)

    # 1. Print the dict by passing it to a string format method, so that you get something like:
    # “Chris is from Seattle, and he likes chocolate cake, mango fruit, greek salad, and lasagna pasta”
    food_prefs = {"name": "Chris",
                "city": "Seattle",
                "cake": "chocolate",
                "fruit": "mango",
                "salad": "greek",
                "pasta": "lasagna"}
    print("{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta".format(**food_prefs))

    # 2. Using a list comprehension, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine).
    # (the hex() function gives you the hexidecimal representation of a number as a string)
    a_dict = dict([(num, hex(num)) for num in range(15)])
    print(f"a_dict = {a_dict}")

    # 3. Do the previous entirely with a dict comprehension – should be a one-liner
    b_dict = {num: hex(num) for num in range(15)}
    print(f"b_dict = {b_dict}")

    # 4. Using the dictionary from item (1): Make a dictionary using the same keys but with the number of ‘a’s in each value. 
    # You can do this either by editing the dict in place, or making a new one. If you edit in place make a copy first!
    new_food_prefs = make_dict(food_prefs)
    print(f"new_food_prefs = {new_food_prefs}")

    # 5. Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
    # 5a. Do this with one set comprehension for each set.
    s2 = {num for num in range(21) if num % 2 == 0}
    s3 = {num for num in range(21) if num % 3 == 0}
    s4 = {num for num in range(21) if num % 4 == 0}
    print(f"s2 = {s2}")
    print(f"s3 = {s3}")
    print(f"s4 = {s4}")
    # 5b. What if you had a lot more than 3? – Don’t Repeat Yourself (DRY).
    # 5bi. create a sequence that holds all the divisors you might want – could be 2,3,4, or could be any other arbitrary divisors.
    divisors = [2, 3, 4]
    # 5bii. loop through that sequence to build the sets up – so no repeated code. you will end up with a list of sets
    #  – one set for each divisor in your sequence.
    for divisor in divisors:
        s = {num for num in range(21) if num % divisor == 0}
        print(f"s = {s}")
    # 5c. Extra credit: do it all as a one-liner by nesting a set comprehension inside a list comprehension.
    result = [{num for num in range(21) if num % divisor == 0} for divisor in divisors]
    print(f"result = {result}")

if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()

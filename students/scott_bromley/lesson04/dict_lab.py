#!/usr/bin/env python3


def main():
    """
    Exercises listed here: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/dict_lab.html
    :return: None
    """
    # Dictionaries 1 exercises
    # Create dictionary containing name, city, cake w/ values Chris, Seattle, Chocolate
    dict_one = dict(name="Chris", city="Seattle", cake="Chocolate")
    # Display the dictionary
    print(f"{dict_one}")
    # Delete the entry for cake
    dict_one.pop("cake")
    # Display the dictionary
    print(f"{dict_one}")
    # Add entry for fruit w/ Mango as value and display
    dict_one["fruit"] = 'Mango'
    print(f"{dict_one}")
    # Display the dictionary keys
    print(f"{dict_one.keys()}")
    # Display the dictionary values
    print(f"{dict_one.values()}")
    # Display if cake is a key
    print(f"{'cake' in dict_one.keys()}")
    # Display if Mango is a value
    print(f"{'Mango' in dict_one.values()}")

    # Dictionaries 2 exercises
    dict_two = {k: v.count('t') for k, v in dict_one.items()}
    print(f"{dict_two}")

    # Sets 1 exercises: create sets s2, s3, s4 as numbers zero through twenty, divisible by 2, 3, and 4
    s2 = set(x for x in range(0, 21) if x % 2 == 0)
    s3 = set(x for x in range(0, 21) if x % 3 == 0)
    s4 = set(x for x in range(0, 21) if x % 4 == 0)
    # Display the sets
    print(f"{s2}")
    print(f"{s3}")
    print(f"{s4}")
    # Display if s3 is a subset of s2
    print(f"{s3.issubset(s2)}")
    # Display if s4 is a subset of s2
    print(f"{s4.issubset(s2)}")

    # Sets 2 exercises
    # Create a set w/ letters in 'Python'
    pythoni = set(x for x in 'Python')
    # Add 'i' to the set
    pythoni.add('i')
    marathon = frozenset(x for x in 'marathon')
    # Display union and intersection of two sets
    print(f"The union of 'Pythoni' and 'marathon': {pythoni.union(marathon)}\nThe intersection of" +
          f"'Pythoni' and 'marathon': {pythoni.intersection(marathon)}")


if __name__ == "__main__":
    print("Running", __file__)
    main()
else:
    print("Running %s as imported module", __file__)
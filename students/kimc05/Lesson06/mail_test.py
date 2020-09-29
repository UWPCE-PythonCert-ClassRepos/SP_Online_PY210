#!/usr/bin/env python

#Christine Kim
#Lesson 6
#Mailroom Part 4 Unit Test

import mailroom4 as charity
import os.path
import pathlib

#dict of donors for unit test
givers = {("Amell", "Solona"): [5, 10.5, 15],
            ("Hawke", "Garrette"): [5, 8.4],
            ("Trevelyan", "Jocelyn"): [2]}

expected_list = str("Solona Amell\n"
                    "Garrette Hawke\n"
                    "Jocelyn Trevelyan\n")

expected_email = str("\nDear Ser first last,\n"
    "Thank you for your generous donation of $0\n"
    "We will make certain your goodwill is directed to aid those affected by the Fifth Blight.\n"
    "With regards,\n"
    "The Blight Orphans Charity,\n")

expected_sort = [(('Amell', 'Solona'), [5, 10.5, 15]), 
                (('Hawke', 'Garrette'), [5, 8.4]), 
                (('Trevelyan', 'Jocelyn'), [2])]

#---Test Send a Thank You feature---

#test list feature
def test_list():
    assert charity.list_names(givers) == expected_list

#test thank you email
def test_email():
    assert charity.email() == expected_email

#---Test Create a Report feature---

#Test sort by total donation
def test_sort():
    assert charity.sort(givers) == expected_sort

#---Test Send Letters feature---

#Test letters
def test_letters():
    charity.letters()
    dirpath = pathlib.Path('./').absolute()
    letter_1 = os.path.join(dirpath, "Solona_Amell.txt")
    letter_2 = os.path.join(dirpath, "Alistair_Theirin.txt")
    letter_3 = os.path.join(dirpath, "Cullen_Rutherford.txt")
    assert os.path.exists(letter_1)
    assert os.path.exists(letter_2)
    assert os.path.exists(letter_3)

if __name__== "__main__":
    test_list()
    test_email()
    test_sort()
    test_letters()
    print("Pass")
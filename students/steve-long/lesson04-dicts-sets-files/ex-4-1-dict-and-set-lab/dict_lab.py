#!/usr/bin/env python3
# =============================================================================
# Python210 | Fall 2020
# -----------------------------------------------------------------------------
# Lesson04
# Dictionary and Set Lab (dict_lab.py)
# Steve Long 2020-10-13 | v0
#
# Requirements:
# =============
#
#   Dictionaries [D1]
#   -----------------
#
#   [D1.1] Create a dictionary containing "name", "city", and "cake" for
#          "Chris" from "Seattle" who likes "Chocolate" (so the keys should
#          be: "name", etc, and values: "Chris", etc.)
#   [D1.2] Display the dictionary.
#   [D1.3] Delete the entry for "cake".
#   [D1.4] Display the dictionary.
#   [D1.5] Add an entry for "fruit" with "Mango" and display the dictionary.
#   [D1.6] Display the dictionary keys.
#   [D1.7] Display the dictionary values.
#   [D1.8] Display whether or not "cake" is a key in the dictionary (i.e.
#          False) (now).
#   [D1.9] Display whether or not "Mango" is a value in the dictionary (i.e.
#          True).
#
#   Dictionaries [D2]
#   -----------------
#
#   [D2.1] Using the dic!onary from item 1: Make a dictionary using the same
#          keys but with the number of "t"’s in each value as the value
#          (consider upper and lower case?). The result should look something
#          like:
#
#          {"name": 0, "city": 2, "cake": 2}
#
#   Sets [S1]
#   ---------
#
#   [S1.1] Create sets s2, s3 and s4 that contain numbers from zero through
#          twenty, divisible by 2, 3 and 4 (figure out a way to compute those–
#          don't just type them in).
#   [S1.2] Display the sets.
#   [S1.3] Display if s3 is a subset of s2 (False)
#          and if s4 is a subset of s2 (True).
#
#   Sets [S2]
#   ---------
#
#   [S2.1] Create a set with the letters in 'Python' and add 'i' to the set.
#   [S2.2] Create a frozenset with the letters in 'marathon'.
#   [S2.3] Display the union and intersec!on of the two sets.
#
# Assumptions:
# ============
#
#   Minimalist solutions are satisfactory.
#
# Implementation:
# ===============
#
#   Function safe_input and demo_safe_input. Checked with flake8.
#
# Dependencies:
# =============
#
#   None
#
# Script Usage:
# =============
#
#   ./dict_lab.py
#
# Issues:
# =======
#
#   None.
#
# History:
# ========
# 000/2020-10-15/sal/Completed.
#
# =============================================================================

def solution_set_d1():
    """
    Run solution set D1 (dictionaries).
    """
    print("\nSolution Set [D1]")
    print("\nSolution [D1.12]")
    print("d = dict(name=\"Chris\", city=\"Seattle\", cake=\"Chocolate\")")
    d = dict(name="Chris", city="Seattle", cake="Chocolate")
    #
    print("\nSolution [D1.2]")
    print("d = {}".format(d))
    #
    print("\nSolution [D1.3]")
    print("del(d[\"cake\"])")
    del(d["cake"])
    #
    print("\nSolution [D1.4]")
    print("d = {}".format(d))
    #
    print("\nSolution [D1.5]")
    print("d[\"fruit\"] = \"Mango\"")
    d["fruit"] = "Mango"
    #
    print("\nSolution [D1.6]")
    print("d.keys() = {}".format(d.keys()))
    #
    print("\nSolution [D1.7]")
    print("d.values() = {}".format(d.values()))
    #
    print("\nSolution [D1.8]")
    key = "cake"
    found = (key in d)
    print("\"{}\" in d => {}".format(key, found))
    #
    print("\nSolution [D1.9]")
    value = "Mango"
    found = (value in d.values())
    print("\"{}\" in d.values() => {}".format(value, found))


def solution_set_d2():
    """
    """
    print("\nSolution Set [D2]")
    print("\nSolution [D2.1]")

    def t_count(s):
        return s.lower().count("t")

    print("d = dict(name=t_count(\"Chris\"),"
          " city=t_count(\"Seattle\"), cake=t_count(\"Chocolate\"))")
    d = dict(name=t_count("Chris"),
             city=t_count("Seattle"),
             cake=t_count("Chocolate"))
    print("d = {}".format(d))


def solution_set_s1():
    """
    """
    print("\nSolution Set [S1]")
    print("\nSolution [S1.1]\n(no output)")
    s234 = [[[], 2], [[], 3], [[], 4]]
    for j in range(0, 3):
        s = s234[j][0]
        n = s234[j][1]
        for i in range(0, 21):
            if ((i % n) == 0):
                s.append(i)
        s234[j][0] = set(s)
    set2 = s234[0][0]
    set3 = s234[1][0]
    set4 = s234[2][0]
    print("\nSolution [S1.2]")
    print("set2 = {}".format(set2))
    print("set3 = {}".format(set3))
    print("set4 = {}".format(set4))
    print("\nSolution [S1.3]")
    print("set3.issubset(set2) = {}".format(set3.issubset(set2)))
    print("set4.issubset(set2) = {}".format(set4.issubset(set2)))


def solution_set_s2():
    """
    """
    print("\nSolution Set [S2]")
    print("\nSolution [S2.1]")
    print("set1 = set(list(\"Python\"))")
    set1 = set(list("Python"))
    print("set1 = {}".format(set1))
    print("set1.add(\"i\")")
    set1.add("i")
    print("set1 = {}".format(set1))
    print("\nSolution [S2.2]")
    print("set2 = frozenset(set(list(\"marathon\")))")
    set2 = frozenset(set(list("marathon")))
    print("set2 = {}".format(set2))
    print("\nSolution [S2.3]")
    u_set1_set2 = set1.union(set2)
    print("set1.union(set2) = {}".format(u_set1_set2))
    i_set1_set2 = set1.intersection(set2)
    print("set1.intersection(set2) = {}".format(i_set1_set2))


def main():
    """
    """
    solution_set_d1()
    solution_set_d2()
    solution_set_s1()
    solution_set_s2()


if __name__ == "__main__":
    main()

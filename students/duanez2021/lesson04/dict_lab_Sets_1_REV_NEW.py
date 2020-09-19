#!/usr/bin/env python3
import sys

##############################################################
# 20200706    djm   Dictionary and Set Lab
#
#
#
#
# https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/dict_lab.html
#
#
# Sets
#
#     Create sets s2, s3 and s4 that contain numbers from zero through twenty,
#     divisible by 2, 3 and 4 (figure out a way to compute those – don’t just type them in).
#     Display the sets.
#     Display if s3 is a subset of s2 (False)
#     and if s4 is a subset of s2 (True).
#
################################################################
x = range(0, 20)

s2=set()
for n in x:
  if n % 2 == 0:
    s2.add(n)

s3 = set()
for n in x:
    if n % 3 == 0:
        s3.add(n)

s4 = set()
for n in x:
    if n % 4 == 0:
        s4.add(n)

print(s2)
print(s3)
print(s4)

#     Display if s3 is a subset of s2 (False)
print(s3.issubset(s2))
#     and if s4 is a subset of s2 (True).
print(s4.issubset(s2))

# Sets 2
#
#     Create a set with the letters in ‘Python’ and add ‘i’ to the set.
#     Create a frozenset with the letters in ‘marathon’.
#     Display the union and intersection of the two sets.
#
#

s5 = set()
for i, j in enumerate('Python'):
    s5.add(j)
s5.add('i')

frz = set()
for i, j in enumerate('marathon'):
    frz.add(j)
type(frz)
frz = frozenset(frz)
type(frz)

print(s5)
print(frz)

print(s5.union(frz))
print(s5.intersection(frz))










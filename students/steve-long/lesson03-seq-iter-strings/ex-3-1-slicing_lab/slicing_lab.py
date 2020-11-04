#!/usr/bin/env python3
# =============================================================================
# Python210 | Fall 2020
# -----------------------------------------------------------------------------
# Lesson03
# Slicing Lab (slicing_lab.py)
# Steve Long 2020-09-27 | v0
#
# Requirements:
# -------------
#
# Write some functions that take a sequence as an argument, and return a copy
# of that sequence:
#
#   [3-1] with the first and last items exchanged.
#   [3-2] with every other item removed.
#   [3-3] with the first 4 and the last 4 items removed, and then every other
#         item in the remaining sequence.
#   [3-4] with the elements reversed (just with slicing).
#   [3-5] with the last third, then first third, then the middle third in the
#         new order.
#
# Implementation:
# ---------------
#
#   [3-1] seq_swap_first_last
#   [3-2] seq_odd_elements and seq_even_elements
#   [3-3] seq_trim4_odd_elements and seq_trim4_even_elements
#   [3-4] seq_reverse
#   [3-5] seq_rotate_thirds_right
#
#   - See sections below for notes.
#   - Function names, variables, block comments, line continuation, and
#     operator spacing per PEP8 guidelines. Checked with flake8.
#
# Script Usage:
# -------------
#
#   Script only runs assertions, print 'nAll asserts passed.' if successful.
#
# Issues:
# -------
#
#   [3-2] The term "every other item" is ambiguous. Should this have started
#         with the 0th or 1st item?
#   [3-3] Same ambiguity as [3-2].
#   [3-5] The term "in the new order" is ambiguous. I had to ask the instructor
#         what this meant. My first implementation was quite different.
#
# History:
# --------
# 000/2020-09-27/sal/Created.
# =============================================================================

import math

# Solution [3-1]:
# ----------------------------------------------------------------------------
# Assumption: Return a sequence of the same type.


def seq_swap_first_last(seq):
    """
    seq_swap_first_last(<seq>)
    --------------------------
    Swap the first and last element of a sequence.

    Entry: <seq> ::= A string, list, or tuple.
    Exit:  Returns a copy of <seq> with the first and last element
    swapped.
    """
    return (seq if (len(seq) < 2) else seq[-1:] + seq[1:-1] + seq[0:1])


# Verify seq_swap_first_last with a string.
assert(seq_swap_first_last("frammitz") == "zrammitf")

# Verify seq_swap_first_last with an empty string.
assert(seq_swap_first_last("") == "")

# Verify seq_swap_first_last with a single-element string.
assert(seq_swap_first_last("A") == "A")

# Verify seq_swap_first_last with a 2-element string.
assert(seq_swap_first_last("AB") == "BA")

# Verify seq_swap_first_last with a list.
assert(seq_swap_first_last(["a", "e", "i", "o", "u", "sometimes", "y"])
       == ["y", "e", "i", "o", "u", "sometimes", "a"])

# Verify seq_swap_first_last with an empty list.
assert(seq_swap_first_last([]) == [])

# Verify seq_swap_first_last with a single-element list.
assert(seq_swap_first_last(["A"]) == ["A"])

# Verify seq_swap_first_last with a 2-element list.
assert(seq_swap_first_last(["A", "B"]) == ["B", "A"])

# Verify seq_swap_first_last with a tuple.
assert(seq_swap_first_last((1, 1, 2, 3, 6, 5, 3, 6))
       == (6, 1, 2, 3, 6, 5, 3, 1))

# Verify seq_swap_first_last with an empty tuple.
assert(seq_swap_first_last(()) == ())

# Verify seq_swap_first_last with a single-element tuple.
assert(seq_swap_first_last(("A")) == ("A"))

# Verify seq_swap_first_last with a 2-element tuple.
assert(seq_swap_first_last(("A", "B")) == ("B", "A"))

# Solution 3-2:
# ----------------------------------------------------------------------------
# Assumption: Return a sequence of the same type.
#
# Because the requirement "every other item" is ambiguous, two functions were
# implemented: One returns the odd elements and the other the even elements.
# Even and odd are determined by the sequence indices.


def seq_odd_elements(seq):
    """
    seq_odd_elements(<seq>)
    --------------------------
    Retrieve the odd-indexed elements of a sequence.

    Entry: <seq> ::= A string, list, or tuple.
    Exit:  Returns a copy of <seq> with every other element removed
           starting with element 0.
    """
    return seq[1::2]


def seq_even_elements(seq):
    """
    seq_even_elements(<seq>)
    --------------------------
    Retrieve the even-indexed elements of a sequence.

    Entry: <seq> ::= A string, list, or tuple.
    Exit:  Returns a copy of <seq> with every other element removed
           starting with element 1.
    """
    return seq[0::2]


# Verify seq_odd_elements with a string.
assert(seq_odd_elements("abcdefg") == "bdf")

# Verify seq_odd_elements with a single element string.
assert(seq_odd_elements("Z") == "")

# Verify seq_odd_elements with a zero element string.
assert(seq_odd_elements("") == "")

# Verify seq_odd_elements with a list.
assert(seq_odd_elements([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
       == [1, 3, 5, 7, 9])

# Verify seq_odd_elements with a single element list.
assert(seq_odd_elements([0]) == [])

# Verify seq_odd_elements with a zero element list.
assert(seq_odd_elements([]) == [])

# Verify seq_odd_elements with a tuple.
assert(seq_odd_elements((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
       == (1, 3, 5, 7, 9))

# Verify seq_odd_elements with a single element tuple.
assert(seq_odd_elements((0,)) == ())

# Verify seq_odd_elements with a zero element tuple.
assert(seq_odd_elements(()) == ())

# Verify seq_even_elements with a string.
assert(seq_even_elements("abcdefg") == "aceg")

# Verify seq_even_elements with a single element string.
assert(seq_even_elements("Z") == "Z")

# Verify seq_even_elements with a zero element string.
assert(seq_even_elements("") == "")

# Verify seq_even_elements with a list.
assert(seq_even_elements([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
       == [0, 2, 4, 6, 8])

# Verify seq_even_elements with a single element list.
assert(seq_even_elements([0]) == [0])

# Verify seq_even_elements with a zero element list.
assert(seq_even_elements([]) == [])

# Verify seq_even_elements with a tuple.
assert(seq_even_elements((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
       == (0, 2, 4, 6, 8))

# Verify seq_even_elements with a single element tuple.
assert(seq_even_elements((0,)) == (0,))

# Verify seq_even_elements with a zero element tuple.
assert(seq_even_elements(()) == ())

# Solution 3-3:
# ----------------------------------------------------------------------------
# Assumption: Return a sequence of the same type.
#
# Because the requirement "every other item" is ambiguous, two functions were
# implemented: Both trim the leading and trailing four elements but one
# returns the remaining odd element and the other the remaining even elements.
# Even and odd are determined by the sequence indices.


def seq_trim4_even_elements(seq):
    """
    seq_trim4_even_elements(<seq>)
    ------------------------------
    Trim the leading and trailing four elements of a sequence, then
    remove the remaining odd-indexed elements of a sequence.

    Entry: <seq> ::= A string, list, or tuple.
    Exit:  Returns the even elements of <seq> with the leading and
           trailing four elements removed.
    """
    return seq_even_elements(seq[4:-4])


def seq_trim4_odd_elements(seq):
    """
    seq_trim4_odd_elements(<seq>)
    ------------------------------
    Trim the leading and trailing four elements of a sequence, then
    remove the remaining even-indexed elements of a sequence.

    Entry: <seq> ::= A string, list, or tuple.
    Exit:  Returns the odd elements of <seq> with the leading and
           trailing four elements removed.
    """
    return seq_odd_elements(seq[4:-4])


# Verify seq_trim4_even_elements with a 14 element string.
assert(seq_trim4_even_elements("0000ABCDEF0000") == "ACE")

# Verify seq_trim4_even_elements with a 9 element string.
assert(seq_trim4_even_elements("0000A0000") == "A")

# Verify seq_trim4_even_elements with an 8 element string.
assert(seq_trim4_even_elements("00000000") == "")

# Verify seq_trim4_even_elements with a 1 element string.
assert(seq_trim4_even_elements("0") == "")

# Verify seq_trim4_even_elements with a 0 element string.
assert(seq_trim4_even_elements("") == "")

# Verify seq_trim4_even_elements with a 14 element list.
assert(seq_trim4_even_elements(
            ["0", "0", "0", "0", "A", "B", "C", "D", "E",
             "F", "0", "0", "0", "0"])
       == ["A", "C", "E"])

# Verify seq_trim4_even_elements with a 9 element list.
assert(seq_trim4_even_elements(["0", "0", "0", "0", "A", "0", "0", "0", "0"])
       == ["A"])

# Verify seq_trim4_even_elements with a 8 element list.
assert(seq_trim4_even_elements(["0", "0", "0", "0", "0", "0", "0", "0"])
       == [])

# Verify seq_trim4_even_elements with a 1 element list.
assert(seq_trim4_even_elements([0]) == [])

# Verify seq_trim4_even_elements with a 0 element list.
assert(seq_trim4_even_elements([]) == [])

# Verify seq_trim4_even_elements with a 14 element tuple.
assert(seq_trim4_even_elements(
            ("0", "0", "0", "0", "A", "B", "C", "D", "E", "F",
             "0", "0", "0", "0"))
       == ("A", "C", "E"))

# Verify seq_trim4_even_elements with a 9 element tuple.
assert(seq_trim4_even_elements(("0", "0", "0", "0", "A", "0", "0",
                                "0", "0"))
       == ("A",))

# Verify seq_trim4_even_elements with a 8 element tuple.
assert(seq_trim4_even_elements(("0", "0", "0", "0", "0", "0", "0", "0")) == ())

# Verify seq_trim4_even_elements with a 1 element tuple.
assert(seq_trim4_even_elements((0,)) == ())

# Verify seq_trim4_even_elements with a 0 element tuple.
assert(seq_trim4_even_elements(()) == ())

# Verify seq_trim4_odd_elements with a 14 element string.
assert(seq_trim4_odd_elements("0000ABCDEF0000") == "BDF")

# Verify seq_trim4_odd_elements with a 9 element string.
assert(seq_trim4_odd_elements("0000A0000") == "")

# Verify seq_trim4_odd_elements with an 8 element string.
assert(seq_trim4_odd_elements("00000000") == "")

# Verify seq_trim4_odd_elements with a 1 element string.
assert(seq_trim4_odd_elements("0") == "")

# Verify seq_trim4_odd_elements with a 0 element string.
assert(seq_trim4_odd_elements("") == "")

# Verify seq_trim4_odd_elements with a 14 element list.
assert(seq_trim4_odd_elements(
            ["0", "0", "0", "0", "A", "B", "C", "D", "E", "F", "0",
             "0", "0", "0"])
       == ["B", "D", "F"])

# Verify seq_trim4_odd_elements with a 9 element list.
assert(seq_trim4_odd_elements(["0", "0", "0", "0", "A", "0", "0", "0", "0"])
       == [])

# Verify seq_trim4_odd_elements with an 8 element list.
assert(seq_trim4_odd_elements(["0", "0", "0", "0", "0", "0", "0", "0"])
       == [])

# Verify seq_trim4_odd_elements with a 1 element list.
assert(seq_trim4_odd_elements([0])
       == [])

# Verify seq_trim4_odd_elements with a 0 element list.
assert(seq_trim4_odd_elements([])
       == [])

# Verify seq_trim4_odd_elements with a 14 element tuple.
assert(seq_trim4_odd_elements(
            ("0", "0", "0", "0", "A", "B", "C", "D", "E", "F", "0", "0",
             "0", "0"))
       == ("B", "D", "F"))

# Verify seq_trim4_odd_elements with a 9 element tuple.
assert(seq_trim4_odd_elements(("0", "0", "0", "0", "A", "0", "0", "0", "0"))
       == ())

# Verify seq_trim4_odd_elements with an 8 element tuple.
assert(seq_trim4_odd_elements(("0", "0", "0", "0", "0", "0", "0", "0")) == ())

# Verify seq_trim4_odd_elements with a 1 element tuple.
assert(seq_trim4_odd_elements((0,)) == ())

# Verify seq_trim4_odd_elements with a 0 element tuple.
assert(seq_trim4_odd_elements(()) == ())

# Solution 3-4:
# -----------------------------------------------------------------------------
# Assumption: Return a sequence of the same type.


def seq_reverse(seq):
    """
    seq_reverse(<seq>)
    ------------------------------
    Reverse the order of a sequence.

    Entry: <seq> ::= A string, list, or tuple.
    Exit:  Returns a copy of <seq> in reverse order.
    """
    return seq[::-1]


# Verify seq_reverse with a 6 element string.
assert(seq_reverse("ABCDEF") == "FEDCBA")

# Verify seq_reverse with a 2 element string.
assert(seq_reverse("AF") == "FA")

# Verify seq_reverse with a 1 element string.
assert(seq_reverse("A") == "A")

# Verify seq_reverse with a 0 element string.
assert(seq_reverse("") == "")

# Verify seq_reverse with a 6 element list.
assert(seq_reverse([0, 1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1, 0])

# Verify seq_reverse with a 2 element list.
assert(seq_reverse([0, 1]) == [1, 0])

# Verify seq_reverse with a 1 element list.
assert(seq_reverse([0]) == [0])

# Verify seq_reverse with a 0 element list.
assert(seq_reverse([]) == [])

# Verify seq_reverse with a 6 element tuple.
assert(seq_reverse((0, 1, 2, 3, 4, 5)) == (5, 4, 3, 2, 1, 0))

# Verify seq_reverse with a 2 element tuple.
assert(seq_reverse((0, 1)) == (1, 0))

# Verify seq_reverse with a 1 element tuple.
assert(seq_reverse((0,)) == (0,))

# Verify seq_reverse with a 0 element tuple.
assert(seq_reverse(()) == ())

# Solution 3-5:
# -----------------------------------------------------------------------------
# Assumption: Return a sequence of the same type.
#
# Due to the ambiguity of the requirement, functionality was implemented with
# the goal of having non-zero "thirds" except when the element count does not
# support this (count less than 2). All element counts except for 4 recognize
# "thirds" having larger, equal first and third subsequences than the second
# subsequence. Element count 4 yields subsequence counts of 1, 2, and 1,
# respectively.


def seq_rotate_thirds_right(seq):
    """
    seq_rotate_thirds_right(<seq>)
    ------------------------------
    Rotate each third of a sequence to the right (first moves to the
    second position, second moves to the third position, and third
    moves to the first position). For <seq> having an element count
    less than two, there is effectively no rotation. For <seq> having
    an element count that is not a multiple of 3, the second 'third'
    will be smaller than the first and third unless the element count
    is 4, in which case the second will be larger than the first and
    third.

    Entry: <seq> ::= A string, list, or tuple.
    Exit:  Returns a copy of <seq> (same type) rotated as described.
    """
    result = seq
    L = len(seq)
    if (L > 1):
        #
        # The following is a conditional assignment expression. See
        # https://docs.python.org/2.5/whatsnew/pep-308.html.
        #
        end_count = (1 if (L == 4) else math.ceil(L/3))
        middle_count = L - (2 * end_count)
        first = seq[0:end_count]
        second = seq[end_count:(end_count + middle_count)]
        third = seq[(end_count + middle_count):]
        result = third + first + second
    return result


# Verify seq_rotate_thirds_right for 14 element string, list, and tuple.
assert(seq_rotate_thirds_right("----ABCDEF++++") == "F++++----ABCDE")
assert(seq_rotate_thirds_right([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                "A", "B", "C", "D"])
       == [9, 'A', 'B', 'C', 'D', 0, 1, 2, 3, 4, 5, 6, 7, 8])
assert(seq_rotate_thirds_right((0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                "A", "B", "C", "D"))
       == (9, 'A', 'B', 'C', 'D', 0, 1, 2, 3, 4, 5, 6, 7, 8))

# Verify seq_rotate_thirds_right for 13 element string, list, and tuple.
assert(seq_rotate_thirds_right("----ABCDE++++") == "E++++----ABCD")
assert(seq_rotate_thirds_right([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C"])
       == [8, 9, 'A', 'B', 'C', 0, 1, 2, 3, 4, 5, 6, 7])
assert(seq_rotate_thirds_right((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C"))
       == (8, 9, 'A', 'B', 'C', 0, 1, 2, 3, 4, 5, 6, 7))

# Verify seq_rotate_thirds_right for 12 element string, list, and tuple.
assert(seq_rotate_thirds_right("----ABCD++++") == "++++----ABCD")
assert(seq_rotate_thirds_right([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B"])
       == [8, 9, 'A', 'B', 0, 1, 2, 3, 4, 5, 6, 7])
assert(seq_rotate_thirds_right((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B"))
       == (8, 9, 'A', 'B', 0, 1, 2, 3, 4, 5, 6, 7))

# Verify seq_rotate_thirds_right for 5 element string, list, and tuple.
assert(seq_rotate_thirds_right("-AB+0") == "+0-AB")
assert(seq_rotate_thirds_right([0, 1, 2, 3, 4]) == [3, 4, 0, 1, 2])
assert(seq_rotate_thirds_right((0, 1, 2, 3, 4)) == (3, 4, 0, 1, 2))

# Verify seq_rotate_thirds_right for 4 element string, list, and tuple (
# special case).
assert(seq_rotate_thirds_right("-AB+") == "+-AB")
assert(seq_rotate_thirds_right([0, 1, 2, 3]) == [3, 0, 1, 2])
assert(seq_rotate_thirds_right((0, 1, 2, 3)) == (3, 0, 1, 2))

# Verify seq_rotate_thirds_right for 3 element string, list, and tuple.
assert(seq_rotate_thirds_right("-AB") == "B-A")
assert(seq_rotate_thirds_right([0, 1, 2]) == [2, 0, 1])
assert(seq_rotate_thirds_right((0, 1, 2)) == (2, 0, 1))

# Verify seq_rotate_thirds_right for 2 element string, list, and tuple.
assert(seq_rotate_thirds_right("AB") == "BA")
assert(seq_rotate_thirds_right([0, 1]) == [1, 0])
assert(seq_rotate_thirds_right((0, 1)) == (1, 0))

# Verify seq_rotate_thirds_right for 1 element string, list, and tuple (de-
# generate end-condition case).
assert(seq_rotate_thirds_right("A") == "A")
assert(seq_rotate_thirds_right([0]) == [0])
assert(seq_rotate_thirds_right((0,)) == (0,))

# Verify seq_rotate_thirds_right for 0 element string, list, and tuple (de-
# generate end-condition case).
assert(seq_rotate_thirds_right("") == "")
assert(seq_rotate_thirds_right([]) == [])
assert(seq_rotate_thirds_right(()) == ())

print("\nAll asserts passed\n")

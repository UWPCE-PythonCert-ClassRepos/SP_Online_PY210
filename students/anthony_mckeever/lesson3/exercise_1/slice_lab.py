"""
Programming In Python - Lesson 3 Exercise 1: Slice Lab
Code Poet: Anthony McKeever
Start Date: 07/28/2019
End Date: 07/28/2019
"""

def exchange_first_last(seq):
    """
    Return a copy of a sequence where the first and last items are swapped.

    :seq: The sequence to copy and swap the first and last items from.
    """
    return seq[-1:] + seq[1:len(seq)-1] + seq[:1] if len(seq) >= 2 else seq[:]

def remove_every_other_item(seq):
    """
    Return a copy of a sequence where every other item is removed.

    :seq: The sequence to copy and remove the items from.
    """
    return seq[::2]

def remove_first_and_last_four(seq):
    """
    Return a copy of a sequence where the first four, last four, and every other items are removed.

    :seq: The sequence to copy and remove items from.
    """
    return seq[4:-4:2]

def reverse_sequcne(seq):
    """
    Return a copy of a sequence where the sequence has been reversed.
    
    :seq: The sequence to copy and reverse.
    """
    return seq[::-1]

def reorder_sequence(seq):
    """
    Return a copy of a sequence where the it has been reordered to the last third, first third, and middle third.
    Or [1, 2, 3] becomes [3, 1, 2]
    
    :seq: The sequence to copy and reorder.
    """
    one_third = int(len(seq) / 3)
    return seq[-one_third:] + seq[:-one_third]

if __name__ == "__main__":
    print("Validate exchange_first_last")
    print("\tTesting Strings")
    assert exchange_first_last("stuff in a box") == "xtuff in a bos"
    assert exchange_first_last("xy") == "yx"
    assert exchange_first_last("x") == "x"

    print("\tTesting Lists")
    assert exchange_first_last([0, 1, 2, 3, 4]) == [4, 1, 2, 3, 0]
    assert exchange_first_last([0, 1]) == [1, 0]
    assert exchange_first_last(["coffee"]) == ["coffee"]

    print("\tTesting Tuples")
    assert exchange_first_last(("stuff", "in", 0, True)) == (True, "in", 0, "stuff")
    assert exchange_first_last(("sophie", "loaphie")) == ("loaphie", "sophie")
    assert exchange_first_last((1,)) == (1,)

    print("Validate remove_every_other_item")
    print("\tTesting Strings")
    assert remove_every_other_item("sophie loaphie") == "spi opi"
    assert remove_every_other_item("sl") == "s"
    assert remove_every_other_item("s") == "s"
    assert remove_every_other_item("") == ""

    print("\tTesting Lists")
    assert remove_every_other_item([0, 1, 2, 3, 4, 5, 6]) == [0, 2, 4, 6]
    assert remove_every_other_item([0, 1]) == [0]
    assert remove_every_other_item([0]) == [0]
    assert remove_every_other_item([]) == []

    print("\tTesting Tuples")
    assert remove_every_other_item((True, "is", "never", 0, False)) == (True, "never", False)
    assert remove_every_other_item(("Cresenta", "Starchelle")) == ("Cresenta",)
    assert remove_every_other_item(("Cresenta",)) == ("Cresenta",)

    print("Validate remove_first_and_last_four")
    print("\tTesting Strings")
    assert remove_first_and_last_four("Cresenta Starchelle") == "et trh"
    assert remove_first_and_last_four("012345678") == "4"
    assert remove_first_and_last_four("1") == ""

    print("\tTesting Lists")
    assert remove_first_and_last_four([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [4, 6, 8]
    assert remove_first_and_last_four([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [5]
    assert remove_first_and_last_four([1]) == []

    print("\tTesting Tuples")
    assert remove_first_and_last_four((True, "Python", "is", "Cool", "and", "its", "fun", 2, "code", "in", "<3", "snake", 3)) == ("and", "fun", "code")
    assert remove_first_and_last_four((0, 1, True, False, "Coffee", "Cheesecake", "Pie", "Brownies", "Cookies")) == ("Coffee",)
    assert remove_first_and_last_four(("Coffee",)) == ()

    print("Validate reverse_sequence")
    print("\tTesting Strings")
    assert reverse_sequcne("tacocat") == "tacocat" # A palindrome should always reverse to itself.
    assert reverse_sequcne("Alpaca") == "acaplA"
    assert reverse_sequcne("xy") == "yx"

    print("\tTesting Lists")
    assert reverse_sequcne([1, 2, 3, 4, 3, 2, 1]) == [1, 2, 3, 4, 3, 2, 1]
    assert reverse_sequcne([0, 1, 2, 4, 8, 16, 32]) == [32, 16, 8, 4, 2, 1, 0]
    assert reverse_sequcne(["Starchelle", "Cresenta"]) == ["Cresenta", "Starchelle"]

    print("\tTesting Tuples")
    assert reverse_sequcne(("taco", 0, True, 0, "taco")) == ("taco", 0, True, 0, "taco")
    assert reverse_sequcne((True, False, 3.14, "taco")) == ("taco", 3.14, False, True)
    assert reverse_sequcne(("Four", 4)) == (4, "Four")

    print("Validate reorder_sequence")
    print("\tTesting Strings")
    assert reorder_sequence("Cresenta Starchelle") == "chelleCresenta Star"
    assert reorder_sequence("abc") == "cab"
    assert reorder_sequence("12") == "12"   # Since less than 3 items exist, it cannot reorder this string.

    print("\tTesting Lists")
    assert reorder_sequence([0, 1, 2, 3, 4, 5, 6, 7, 8]) == [6, 7, 8, 0, 1, 2, 3, 4, 5]
    assert reorder_sequence([1, 2, 3]) == [3, 1, 2]
    assert reorder_sequence([1, 2]) == [1, 2]

    print("\tTesting Tuples")
    assert reorder_sequence(("Pikachu", "Mareep", "Voltorb", "Rotom", "MissingNo.", "Pichu")) == ( "MissingNo.", "Pichu", "Pikachu", "Mareep", "Voltorb", "Rotom")
    assert reorder_sequence(("Mareep", "Flaafy", "Ampharos")) == ("Ampharos", "Mareep", "Flaafy")
    assert reorder_sequence((True, False)) == (True, False)

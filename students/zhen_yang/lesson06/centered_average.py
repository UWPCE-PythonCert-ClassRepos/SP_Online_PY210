# centered average #
"""
centerted_average.py returns the "centered" average of an array of ints,
which we'll say is the mean averge of the values, except ignoring the largest
and smallest values in the array. If there are multiple copies of the smallest
value, ignore just one copy, and likewise for the largest value. Use int
int division to produce the final average. You may assume that the array is
length 3 or more.
"""

def centered_average(the_list):
    the_sorted_list = sorted(the_list)
    the_sorted_list.pop(0)# remove the smallest one
    the_sorted_list.pop()# remove the largest one
    return int(sum(the_sorted_list) / len(the_sorted_list))

def first_last_exchange(n):
    if len(n) > 1:
        result = n[-1] + n[1:-1] + n[0]
        print(result)
        return result
    else:
        print(n)
        return n

# Works
# first_last_exchange("hamburger")


def every_other_removed(n):
    if len(n) > 2:
        # Uses length of string to find end point of start, stop, step function
        # Creates dynamic ability to process many different lengths of strings.
        result = n[0: len(n): 2]
        print(result)
        return result
    else:
        print(n)
        return(n)


# Works
# every_other_removed("hamburger")

def remove_first_four_last_four(n):
    if len(n) > 8:
        result = n[4: (len(n) - 5)]
        print(result)
        return result
    else:
        return False


# Works
# remove_first_four_last_four("hamburger_helper")


def reverse_with_slicing(n):
    reverseSlicing = []
    i = 0
    while i < len(n):
        letter = n[-(i) - 1]
        reverseSlicing.extend(letter)
        i += 1
    print(reverseSlicing)


# Works
# reverse_with_slicing("hamburger")


def reverse_thirds(n):
    if len(n) > 9:
        first = n[:len(n)/3]
        middle = n[len(n)/4: - len(n) / 3]
        last = n[-len(n)/3:]
        print(last + middle + first)
    else:
        print(n)


# Works
# reverse_thirds("hamburger_helper")

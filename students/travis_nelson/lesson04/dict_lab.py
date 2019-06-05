#!/usr/bin/env python3


def main():

    dicto = {'name': 'Travis',
             'city': 'Seattle',
             'cake': 'chocolate'}
    print(dicto)
    del dicto['cake']
    print(dicto)
    dicto['fruit'] = 'mango'
    print(dicto)
    print(dicto.keys())
    print(dicto.values())
    print('cake' in dicto)
    print('cake' in dicto.keys())
    print('mango' in dicto.values())

    # Using the dictionary from item 1: Make a dictionary using the same keys
    # but with the number of ‘t’s in each value as the value
    # (consider upper and lower case?).

    dicto['cake'] = 'chocolate'
    dicto_copy_ts = {}
    for k, v in dicto.items():
        num_ts = v.lower().count('t')
        dicto_copy_ts[k] = num_ts
    print(dicto_copy_ts)

    # Create sets s2, s3 and s4 that contain numbers from zero through twenty,
    # divisible by 2, 3 and 4
    # (figure out a way to compute those – don’t just type them in).
    # Display the sets.
    # Display if s3 is a subset of s2 (False)
    # and if s4 is a subset of s2 (True).

    s2 = set()
    s3 = set()
    s4 = set()
    for i in range(0, 21):
        if i % 2 == 0:
            s2.update([i])
        if i % 3 == 0:
            s3.update([i])
        if i % 4 == 0:
            s4.update([i])
    print(f"{s2}\n{s3}\n{s4}")
    print(s3.issubset(s2))
    print(s4.issubset(s2))

    # Create a set with the letters in ‘Python’ and add ‘i’ to the set.
    # Create a frozenset with the letters in ‘marathon’.
    # Display the union and intersection of the two sets.

    s5 = set()
    for i in 'Python':
        s5.add(i)
    s5.add('i')
    temp_list = []
    for i in 'marathon':
        temp_list.append(i)
    s6 = frozenset(temp_list)
    print(s6)
    print(s5.union(s6))
    print(s5.intersection(s6))

if __name__ == "__main__":
    main()

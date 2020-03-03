#!/usr/bin/env python3


####################################


def series1(in_lst):
    result_lst = in_lst
    print(result_lst)

    fruit = input("Enter fruit name: ")
    result_lst.append(fruit)
    print('{0}'.format(result_lst))

    num = input("Enter a number 1-5: ")
    ix = int(num) - 1
    print('{0}'.format(result_lst[ix]))

    result_lst = ["BlueBerry"] + result_lst
    result_lst.insert(0, "BlackBerry")
    print('{0}'.format(result_lst))

    for item in result_lst:
        s = str(item)
        s.startswith('P')
        if item.startswith('P'):
            print('Fruit starting with P => {0}'.format(item))

    return result_lst


####################################


# main, test funcs

if __name__ == "__main__":
    # run some tests
    dataLst = ["Apples", "Pears", "Oranges", "Peaches"]
    result_lst1 = series1(dataLst)



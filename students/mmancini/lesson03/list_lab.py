#!/usr/bin/env python3


####################################


def series1(in_lst):
    result_lst = in_lst.copy()
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


def series2(in_lst):
    result_lst = in_lst.copy()
    print(f"series 2, original list ", result_lst)

    ix = len(result_lst)
    item = result_lst[ix-1]
    result_lst.remove(item)
    print(f"remove last item ", result_lst)
    result_lst.pop()
    print(f"remove again last item ", result_lst)

    fruit = input("Enter fruit name to remove: ")
    result_lst.remove(fruit)
    print(f"remaining fruit ", result_lst)

    return result_lst


def series3(in_lst):
    result_lst = in_lst.copy()
    print(f"series 3, original list ", result_lst)

    for item in in_lst:
        ans = input("\nDo you like " + item.lower() + "? > ")
        while ans != 'yes' and ans != 'no':
            ans = input("\nPlease specify yes or no > ")
        if ans == 'no':
            print(f"removing fruit ", item)
            result_lst.remove(item)

    print(f"series 3, all fruits remaining ", result_lst)

    return result_lst


def series4(in_lst):
    result_lst = []
    print(f"series 4, original list ", result_lst)

    for item in in_lst:
        result_lst.append(item[::-1])

    print(f"series 4, fruit names reversed ", result_lst)

    return result_lst


####################################


# main, test funcs

if __name__ == "__main__":
    # run some tests
    data_lst = ["Apples", "Pears", "Oranges", "Peaches"]
    result_lst1 = series1(data_lst)
    result_lst2 = series2(result_lst1)
    result_lst3 = series3(result_lst1)
    result_lst4 = series4(result_lst1)



#!/usr/bin/env python3




def task1(tup):
    print("task 1 output without padding ==> " + 'file{:03d} : {:.2f}, {:.2E} , {:.2E}'.format(*tup))
    print("task 1 output with padding ==> " + 'file{:>03d} : {:.2f}, {:.2E} , {:.2E}'.format(*tup))


def task2(tup):
    print("task 2 output ==> " + 'file{:>03d} : {:.2f}, {:.2E} , {:.2E}'.format(*tup))
    print("task 2 output with f string ==> " + f'file00{tup[0],2} : {tup[1]:.2f}, {tup[2]:.2E}, {tup[3]:.2E}')




####################################


# main, test funcs

if __name__ == "__main__":
    # run some tests
    xTup = (2, 123.4567, 10000, 12345.67)
    task1(xTup)
    task2(xTup)

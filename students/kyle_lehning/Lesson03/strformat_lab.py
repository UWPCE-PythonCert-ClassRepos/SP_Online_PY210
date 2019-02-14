#!/usr/bin/env python3


def task1(input_tuple):
    formatted_string = "file_{:0>3d} :   {:.2f}, {:.2e}, {:.3g}".format(*input_tuple)
    print(formatted_string)


def task2(seq):
    formatted_string = f"file_{seq[0]:0>3d} :   {seq[1]:.2f}, {seq[2]:.2e}, {seq[3]:.3g}"
    print(formatted_string)


if __name__ == '__main__':
    start_tuple = (2, 123.4567, 10000, 12345.67)
    task1(start_tuple)
    task2(start_tuple)

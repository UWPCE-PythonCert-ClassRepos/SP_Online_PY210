#!/usr/bin/env python3

#'file_002 ,   123.46, 1.00e+04, 1.23e+04'


tuple = (2, 123.4567, 10000, 12345.67)


def format_string():
    return "file_{:0>3d}, {:.2f}, {:.2e}, {:.3e}".format(*tuple)

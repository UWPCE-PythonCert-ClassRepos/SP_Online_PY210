#!/usr/bin/env python3
import sys
##############################################################
# 20200620    djm list lab series 4
#
# Duane McCollum Python self-paced winter 2020
#
# String Formatting Exercise
#  given ( 2, 123.4567, 10000, 12345.67)
#  create a format string to output
# 'file_002 :   123.46, 1.00e+04, 1.23e+04'
# #
#############################################################

# Task One
t = (2, 123.4567, 10000, 12345.67)
#out_text= "file_00{}:  {:.2f}, {:.2e},  {:.2e}".format(t[0], t[1], t[2], t[3])
out_text= "file_{:03d} :  {:.2f}, {:.2e},  {:.2e}".format(t[0], t[1], t[2], t[3])
print(out_text)


# task two



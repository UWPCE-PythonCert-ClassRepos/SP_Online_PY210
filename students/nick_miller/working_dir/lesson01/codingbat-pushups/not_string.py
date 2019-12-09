#!/usr/bin/env python


# def not_string(str):
#     if "not" in str:
#         return str
#     else:
#         return "not " + str


def not_string(str):
    if len(str) >= 3 and str[:3] == "not":
        return str
    return "not " + str

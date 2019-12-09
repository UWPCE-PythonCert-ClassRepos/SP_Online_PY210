#!/usr/bin/env python


def string_splosion(str):
    result = ""
    for i in range(len(str)):
        result = result + str[:i + 1]
    return result

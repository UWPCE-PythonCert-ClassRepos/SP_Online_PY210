#!/usr/bin/python
# -*- coding: utf-8 -*-

def make_out_word(out, word):
    if len(out) == 4:
        return out[0:2] + word + out[2:4]

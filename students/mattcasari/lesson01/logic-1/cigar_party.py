#!/usr/bin/python
# -*- coding: utf-8 -*-

def cigar_party(cigars, is_weekend):
    if is_weekend:
        if 40 <= cigars:
            return True
    else:
        if 40 <= cigars <= 60:
            return True    
    return False
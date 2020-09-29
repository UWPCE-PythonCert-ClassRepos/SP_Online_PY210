#!/usr/bin/python
# -*- coding: utf-8 -*-

def cat_dog(str):
    dog_cnt = 0
    cat_cnt = 0

    for i in range(len(str)):
        if str[i:].find('cat') == 0:
            cat_cnt += 1
        if str[i:].find('dog') == 0:
            dog_cnt += 1

    if cat_cnt == dog_cnt:
        return True
    else:
        return False
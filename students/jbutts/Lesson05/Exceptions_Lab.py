#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def safe_input(text):
    output = None
    try:
        output = input(text)
    except KeyboardInterrupt:
        print("Keyboard Interrupt: control-C pressed")
    except EOFError as e:
        print("EOF: Control-D pressed")
    return output


safe_input("Kill Me!!!!!! (ctrl-c or ctrl-d) >>>")

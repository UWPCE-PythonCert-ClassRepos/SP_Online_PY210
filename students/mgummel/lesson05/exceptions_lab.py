#!/usr/bin/env python3

def safe_input():
    """ Gets a file name from the user. Raises exceptions 
    if the user tries to quit ungracefully
    """

    try:
        get_file = input("Enter filename:\n>>>")
    except KeyboardInterrupt:
        return None
    except EOFError:
        return None
    else:
        print("No errors encountered!")

if __name__=='__main__':
    safe_input()
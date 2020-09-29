#!/usr/bin/env python3

def safe_input():
    try:
        safe_input = input("Try ^C or ^D >>> ")
    except KeyboardInterrupt:
        print("None")
    except EOFError:
        print("None")
    
if __name__ == "__main__": 
    print(safe_input())
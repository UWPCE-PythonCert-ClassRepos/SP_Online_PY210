#!/usr/bin/env python3
import pathlib


def main():
    pth = pathlib.Path('./')
    
    for f in pth.iterdir():
        print(pth.absolute() / f)


if __name__ == '__main__':
    main()
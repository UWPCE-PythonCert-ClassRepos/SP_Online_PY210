#!/usr/bin/env python3


def main():
    assert diff21(-10) == 31
    assert diff21(0) == 21
    assert diff21(10) == 11
    assert diff21(-1) == 22


def diff21(n):
    return abs(n - 21) if n < 21 else abs(n - 21) * 2


if __name__ == "__main__":
    print("Running", __file__)
    main()
else:
    print("Running %s as imported module", __file__)
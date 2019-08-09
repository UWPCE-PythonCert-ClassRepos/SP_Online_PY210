#!/usr/bin/env python3

from pathlib import Path

textfile = Path("./sherlock_small.txt")

with textfile.open() as fileio: words = fileio.read().split()

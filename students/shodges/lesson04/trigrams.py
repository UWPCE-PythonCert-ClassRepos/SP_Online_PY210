#!/usr/bin/env python3

from pathlib import Path

textfile = Path("./sherlock.txt")

with textfile.open() as fileio: text = fileio.read()

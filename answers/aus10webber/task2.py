#!/usr/bin/env python
# utf-8

"""
BIOL 7800 Assignment 17, Task 2
Austen T. Webber
2016_4_4
"""

import argparse
import os
import glob
from Bio import AlignIO


def askingforfiles():
    parser = argparse.ArgumentParser(
        description="Directory of output folder")
    parser.add_argument(
        "--directory",
        required=True,
        help="Directory path for output phylip file ",
        type=str
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Provide the forward alignment input files in nexus format",
        type=str
    )
    return parser.parse_args()


def makedirectory(directory_file):
    newdir = os.path.join(directory_file, 'Phylip_Aligned')
    print(newdir)
    if not os.path.exists(newdir):
        os.makedirs(newdir)
    return newdir


def align(aligned):
    x = os.path.basename(aligned)
    x = os.path.splitext(x)[0]
    x = os.path.join(x + "." + "phylip")
    with open(aligned) as nexalign:
        with open(x, "w") as output:
            for aligned in AlignIO.parse(nexalign, "nexus"):
                AlignIO.write(aligned, output, "phylip-relaxed")


def main():
    path = askingforfiles()
    X = makedirectory(path.directory)
    os.chdir(X)
    nex_files = glob.glob(os.path.join(path.input, "*.nexus"))
    for files in nex_files:
        align(files)


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# encoding: utf-8

"""
My 2nd program for Assignment 17

Created by Michael Henson on 4 April 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""
import argparse
import os
import glob
from Bio import AlignIO


def askingforfiles():
    parser = argparse.ArgumentParser(
        description="Directory for your output folder")
    parser.add_argument(
        "--directory",
        required=True,
        help="Provide the desired directory path please ",
        type=str
    )
    parser.add_argument(
        "--align",
        required=True,
        help="Provide the forward alignment files directory",
        type=str
    )
    return parser.parse_args()


def makedirectory(directory_file):
    newpath = os.path.join(directory_file, 'Alginment_output')
    print(newpath)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath


def alignment(aln_read):
    x = os.path.basename(aln_read)
    x = os.path.splitext(x)[0]
    x = os.path.join(x + "." + "phylip")
    with open(aln_read) as align:
        with open(x, "w") as outfile:
            for aln in AlignIO.parse(align, "nexus"):
                AlignIO.write(aln, outfile, "phylip-relaxed")


def main():
    path = askingforfiles()
    X = makedirectory(path.directory)
    os.chdir(X)
    my_files = glob.glob(os.path.join(path.align, "*.nexus"))
    for files in my_files:
        alignment(files)


if __name__ == '__main__':
    main()

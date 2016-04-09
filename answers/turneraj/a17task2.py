#!/usr/bin/env python
# encoding: utf-8

"""
My second task for Assignment 17.

Created by A.J. Turner on April 4, 2016
Copyright 2016 A.J. Turner. All rights reserved. Collaboration/helpful hints
provided by Mikey Henson.

"""
from Bio import AlignIO
import argparse
import glob
import os


def get_location():
    """"user to specify input directory and ouput directory--easiest to drop
    each file path into command line"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--in_directory", help="input directory of interest", type=str)
    parser.add_argument("--out_directory", help="output directory of interest", type=str)
    args = parser.parse_args()
    return args


def name_files(in_directory):
    a = os.path.basename(in_directory)  # linking to files in input dir
    a_split = os.path.splitext(a)[0]  # splitting filename before doc type
    convert_a = os.path.join(a_split + "." + "phylip")  # converting to phylip
    with open(in_directory) as infile:
        with open(convert_a, "w") as outfile:
            for things in AlignIO.parse(infile, "nexus"):
                AlignIO.write(things, outfile, "phylip-relaxed")  # keep sp name


def main():
    path = get_location()
    my_files = glob.glob(os.path.join(path.in_directory, "*.nexus"))
    for files in my_files:
        name_files(files)


if __name__ == '__main__':
    main()

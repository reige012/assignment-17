#!/usr/bin/env python
# encoding: utf-8

"""
Assignment 17
Task 2 Program: Converting to PHYLIP format
Jessie Salter
3 April 2016
"""

import argparse
import os
import glob
from Bio import AlignIO


def parser():
    '''Takes user input'''
    parser = argparse.ArgumentParser(
        description="Gets the paths to the input and output directories")
    parser.add_argument(
        "--input",
        required=True,
        help="Enter the path to the directory you want to work from.",
        type=str
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Enter the path to the output directory you want to create.",
        type=str
    )
    return parser.parse_args()


def converter(path_input, path_output):
    '''Converts NEXUS files to PHYLIP format'''
    for filename in glob.glob(os.path.join(path_input, '*.nexus')):
        # This gets the input file name + ext:
        base = os.path.basename(filename)
        # This creates the output file name with a new ext:
        root = os.path.splitext(base)[0]+'.phylip'
        # This creates the path to the new file:
        newpath = os.path.join(path_output, root)
        with open(filename, 'r') as infile:
            with open(newpath, 'w') as output:
                nex = AlignIO.read(infile, 'nexus')
                AlignIO.write(nex, output, 'phylip-relaxed')


def main():
    args = parser()
    if args.input[-1] != '/':
        path_input = args.input + '/'
    else:
        path_input = args.input
    # If the output directory does not already exist, this will create it:
    if os.path.isdir(args.output) is False:
        os.makedirs(args.output)
    converter(path_input, args.output)


if __name__ == '__main__':
    main()

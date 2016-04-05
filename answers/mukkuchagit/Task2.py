#!/usr/bin/env python
# encoding: utf-8
"""
assignment 17.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""
from Bio import AlignIO
import glob
import argparse
import os


def convert_format(in_file, out_file):
    open_file = glob.glob(os.path.join(in_file, '*.nexus'))
    for file in open_file:
        input_handle = open(file, 'r')
        output_handle = os.path.splitext(file)
        alignments = AlignIO.parse(input_handle, "nexus")
        new_file = AlignIO.write(alignments, output_handle, "nexus")
        os.makedirs(out_file)
        out_file.write(new_file)
        output_handle.close()
        input_handle.close()


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("input_directory", help="Enter Input Directory where the .nexus files are located")
    parse.add_argument("output_directory", help="Enter Output File Directory where you want output files to be")

    dirs = parse.parse_args()
    input_dir = dirs.input_directory
    output_dir = dirs.output_directory

    convert_format(input_dir, output_dir)



if __name__ == '__main__':
    main()

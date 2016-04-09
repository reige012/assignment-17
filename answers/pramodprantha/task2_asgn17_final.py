#!/usr/bin/env python
# utf-8


"""
task 2 of assignment 17
Created by Pramod Pantha on April 3, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
reference:
http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc65
class slides
"""

from Bio import AlignIO
import glob
import argparse
import os


def alignformat_change(input_directory, output_directory):
    for filename in glob.glob(os.path.join(input_directory, '*.nexus')):
        with open(filename, 'w') as output_directory:
            AlignIO.write.format(output_directory, 'phylip')
    # http://stackoverflow.com/questions/18262293/python-open-every-file-in-a-folder


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("input_directory", help="Enter Input Directory")
    parse.add_argument("output_directory", help="Enter Output File Directory")
    dirs = parse.parse_args()
    input_dir = dirs.input_directory
    output_dir = dirs.output_directory
    alignformat_change(input_dir, output_dir)

if __name__ == '__main__':
    main()

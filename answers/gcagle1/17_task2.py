#! /usr/bin/env python
# encoding: utf-8

'''
Grace Cagle
Assignment 17 Task 2

Write a program that uses glob, os, and biopython to read these files and
convert each, individual file to the PHYLIP file format. Use argparse to get
the name of the input directory that contains the alignments and the name of
some output directory where the transformed alignments will be written.
Use BioPython to read/write/convert the input and output alignments, and write
the output alignments to the output directory provided by the user. Be sure to
maintain the full species name.
'''


import argparse
import glob
import os
from Bio import AlignIO


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', "--directory",
        required=True,
        help="The input file in FASTQ format"
    )
    parser.add_argument(
        '-o', "--output",
        required=True,
        help="The output directory name"
    )
    return parser.parse_args()


def read_directory(args):
    list_of_files = glob.glob(os.path.join(args.directory, "*"))
    return list_of_files


def convert_files(args, list_of_files):
    os.mkdir(args.output)
    for a_file in list_of_files:
        fname1 = os.path.basename(a_file)
        fname = os.path.splitext(fname1)
        outfile_name = args.output + '/' + fname[0] + '.phylip'
        with open(a_file, 'r') as f:
            with open(outfile_name, 'w') as outfile:
                aln_read = AlignIO.read(f, 'nexus')
                AlignIO.write(aln_read, outfile, 'phylip-relaxed')


def main():
    args = get_args()
    list_of_files = read_directory(args)
    convert_files(args, list_of_files)


if __name__ == '__main__':
    main()

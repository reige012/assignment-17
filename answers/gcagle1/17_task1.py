#! /usr/bin/env python
# encoding: utf-8

'''
Grace Cagle
Assignment 17 Task 1

Write a program that reads in the FASTQ file, reverse complements each sequence,
and writes the reverse complemented sequences out as a FASTA-formatted file.
Use argparse to get the name of the input file (the FASTQ file) and the name of
some output file name from the user. Use BioPython to read/write/convert the
input and output files
'''

import argparse
import glob
import os
from Bio import Seq
from Bio import SeqRecord
from Bio import SeqIO


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
        help="The output file name"
    )
    return parser.parse_args()


def read_directory(args):
    list_of_files = glob.glob(os.path.join(args.directory, "*"))
    return list_of_files


def parse_fastq(args, list_of_files):
    for item in list_of_files:
        with open(item, 'r') as f:
            outfile_name = args.output + ".fasta"
            with open(outfile_name, 'w') as outfile:
                for record in SeqIO.parse(f, 'fastq'):
                    outfile.write(record.format('fasta'))


def main():
    args = get_args()
    list_of_files = read_directory(args)
    parse_fastq(args, list_of_files)

if __name__ == '__main__':
    main()

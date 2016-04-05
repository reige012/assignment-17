#!/usr/bin/env python
# encoding: utf-8

"""
Assignment 17
Task 1 Program: FASTQ to FASTA file
Jessie Salter
3 April 2016
"""

import argparse
from Bio import SeqIO


def parser():
    '''Takes user input'''
    parser = argparse.ArgumentParser(
        description='''Gets the input FASTQ file and the output FASTA files''')
    parser.add_argument(
        "--input",
        required=True,
        help="Enter the name of a FASTQ file",
        type=str
        )
    parser.add_argument(
        "--output",
        required=True,
        help="Enter the name of FASTA output file you want to create",
        type=str
        )
    return parser.parse_args()


def reverse_complement(input_file, output):
    '''Reads in FASTQ input file and writes of the reverse complement of each
    sequence in FASTA format.'''
    with open(input_file, 'r') as infile:
        with open(output, 'w') as outfile:
            for record in SeqIO.parse(infile, 'fastq'):
                rc = record.reverse_complement()
                # This replaces other SeqRecord data with input values:
                rc.id = record.id
                rc.name = record.name
                rc.description = record.description
                outfile.write(rc.format('fasta'))


def main():
    args = parser()
    reverse_complement(args.input, args.output)

if __name__ == '__main__':
    main()

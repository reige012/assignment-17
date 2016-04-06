#!/usr/bin/env python
# utf-8

"""
Assignment 17, Task 1
Jon Nations on 3 April 2016
This program that reads in the FASTQ file, reverse complements each sequence,
and writes the reverse complemented sequences out as a FASTA-formatted file.
User determines input file and output file name.
"""

# for a Seq object, seq.reverse.compliment() does the trick.

from Bio import SeqIO
import argparse


def file_in():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infile', required=True, type=str,
                        help="give input fastq file name where the data are stored. MUST USE filename.fastq format")
    parser.add_argument('-o', '--outfile', required=True, help="give output                 fasta file name. MUST USE filename.fasta format")
    return parser.parse_args()


def conversion(args):
    with open(args.infile, 'r') as infile:
        with open(args.outfile, 'w') as outfile:
            for record in SeqIO.parse(infile, 'fastq'):
                outfile.write(record.format('fasta'))


def main():
    args = file_in()
    file_in()
    conversion(args)


if __name__ == '__main__':
    main()

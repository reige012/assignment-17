#!/usr/bin/env python
# encoding: utf-8

"""
My first task for Assignment 17.

Created by A.J. Turner on April 1, 2016
Copyright 2016 A.J. Turner. All rights reserved. Collaboration/helpful hints
provided by Mikey Henson.

"""
from Bio import SeqIO
import argparse


def file_info():
    """get input file path and create output file name--easiest to drop input
    file into command line"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_in", help="Drop file into command line", type=str)
    parser.add_argument("--file_out", help="Name your file output", type=str)
    return parser.parse_args()


def rev_complement(args):
    ''' get the reverse completement of (only) DNA sequences from fastq file'''
    revs_seqs = []
    with open(args, 'r') as filein:
        for record in SeqIO.parse(filein, 'fastq'):
            rev_com = record.reverse_complement(record.seq)
            revs_seqs.append(rev_com)
    return revs_seqs


def main():
    args = file_info()
    reverse = rev_complement(args.file_in)
    with open(args.file_out, 'w') as outfile:
        SeqIO.write(reverse, outfile, 'fasta')


if __name__ == '__main__':
    main()

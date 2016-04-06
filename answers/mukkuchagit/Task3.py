#!/usr/bin/env python
# encoding: utf-8
"""
assignment 17.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""
from Bio import SeqIO
from Bio import Restriction
import argparse


def cut_mt_DNA(input):
    with open(input, 'r') as infile:
        record = SeqIO.read(infile, 'fasta')
    return record.seq


def write_a_file(out_file):
    my_batch = Restriction.RestrictionBatch(first=[], suppliers="N")
    my_batch.search(record.seq)
    f = open(out_file, 'w')


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("input_file", help="Give the name of the FASTQ file")
    parse.add_argument("output_file", help="Give the name of the output file.")
    file = parse.parse_args()
    in_file1 = file.input_file
    in_file = in_file1 + '.fasta'
    out_file1 = file.output_file
    out_file = out_file1 + '.txt'

    cut_mt_DNA(in_file)
    write_a_file(out_file)


if __name__ == '__main__':
    main()

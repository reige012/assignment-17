#!/usr/bin/env python
# encoding: utf-8
"""
assignment 17.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""
from Bio import SeqIO
import argparse


def get_reverse_complementary(input_file, output_file):
    records = (rec.reverse_complement(id="rc_"+rec.id,
            description="reverse complement")
                        for rec in SeqIO.parse(input_file, "fastq"))
    SeqIO.write(records, output_file, "fasta")


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("input_file", help="Give the name of the FASTQ file")
    parse.add_argument("output_file", help="Give the name of the output file.")
    file = parse.parse_args()
    in_file1 = file.input_file
    in_file = in_file1 + '.fastq'
    out_file1 = file.output_file
    out_file = out_file1 + '.fasta'

    get_reverse_complementary(in_file, out_file)


if __name__ == '__main__':
    main()

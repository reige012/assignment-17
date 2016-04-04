# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 17
Oscar Johnson 3 April 2016

Copyright Oscar Johnson 2016

program takes input fastq file, reverse-complements the sequence
and write sequence records out to a fasta file
"""

import os
from Bio import SeqIO
import argparse


def get_args():
    parser = argparse.ArgumentParser(
            description="""provide input fastq file""")
    parser.add_argument('--in_file',
                        type=str,
                        required=True,
                        help="enter a fastq file",
                        )
    parser.add_argument('--out_file',
                        type=str,
                        required=True,
                        help="enter an output file name for fasta file",
                        )
    return parser.parse_args()


def seq_converter(args):
    """
    uses basic format of @brantfaircloth in Lecture 17
    http://biolprogramming.s3.amazonaws.com/Lecture17.pdf
    """
    # rename outfile to .fasta if needed
    if args.out_file[-6:] != '.fasta':
        args.out_file += '.fasta'
    else:
        pass
    with open(args.in_file, 'r') as infile:
        with open(args.out_file, 'w') as outfile:
            for record in SeqIO.parse(infile, 'fastq'):
                # create new SeqRecord object with reverse complement
                # but retain original id, name, and description
                rc_record = record.reverse_complement(id=record.id+"_rc",
                                                      name=record.name,
                                                      description=record.description)
                # print(rc_record)
                SeqIO.write(rc_record, outfile, 'fasta')
                # outfile.write(rc_record.format('fasta'))  # also works


def main():
    args = get_args()
    os.chdir(os.path.dirname(args.in_file))
    seq_converter(args)

if __name__ == '__main__':
    main()

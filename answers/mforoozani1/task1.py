#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task1 to Write a program to reads in the FASTQ file, reverse
complements each sequence, and writes the reverse complemented sequences out as
a FASTA-formatted file
"""
from Bio import SeqRecord
from Bio import SeqIO
import argparse


def get_parser():
    """
   using argparse to takes the list  as input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputfile", required=True)
    parser.add_argument("--outputfile", required=True)
    args = parser.parse_args()
    return args


def main():
    args = get_parser()
    outfile = open(args.outputfile, "w")
    with open(args.inputfile, "r") as infile:
        for record in SeqIO.parse(infile, 'fastq'):
                SeqIO.write([SeqRecord.SeqRecord(
                                             record.seq.reverse_complement(),
                                             id=record.id, name=record.name,
                                             description=record.description)],
                            outfile, 'fasta')

if __name__ == '__main__':
    main()

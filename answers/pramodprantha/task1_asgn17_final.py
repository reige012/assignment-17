#!/usr/bin/env python
# utf-8


"""
task 1 of assignment 17
Created by Pramod Pantha on April 3, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
reference:http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc65
http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc23
"""


from Bio import SeqIO
import argparse


def reversecomplement_fasta(infile, outfile):
    records = (rec.reverse_complement(id="rc_"+rec.id,
                description="reverse complement")
                        for rec in SeqIO.parse(infile, "fastq"))
    SeqIO.write(records, outfile, "fasta")


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("infile", help="give name of your fastq file")
    parse.add_argument("outfile", help="give your output file name")
    args = parse.parse_args()
    fastqfile = args.infile
    fastareversedfile = args.outfile
    reversecomplement_fasta(fastqfile, fastareversedfile)


if __name__ == '__main__':
    main()

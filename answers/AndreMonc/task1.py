# !/usr/bin/env python
# encoding: utf-8

"""
My assignment 17 task1 program
Created by Andre Moncrieff on 4 April 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""

import argparse
import os
from Bio import SeqIO


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--in_filename", required=True,
                        help="Enter filename (without the extension) for the" +
                        " original FASTQ file. Also, within the program,"
                        " personalize the path in the file_conversion function"
                        " to the assignment-17 task1-files folder as found on"
                        " your computer.",
                        type=str)
    parser.add_argument("--out_filename", required=True,
                        help="Enter filename (without the extension) for the"
                        " reverse complement FASTA file.",
                        type=str)
    args = parser.parse_args()
    return args


def file_conversion(in_filename, out_filename):
    os.chdir("/Users/Andre/Documents/aa_LSU_Files/3_Spring_2016/Comp_Prog_for_Biologists/assignment-17/task1-files")
    with open(in_filename + ".fastq", "r") as infile:
        os.chdir("/Users/Andre/Documents/aa_LSU_Files/3_Spring_2016/Comp_Prog_for_Biologists/assignment-17/answers/AndreMonc/task1_output")
        with open(out_filename + ".fasta", "w") as outfile:
            for record in SeqIO.parse(infile, "fastq"):
                record.seq.reverse_complement()
                record.format('fasta')
                outfile.write(record.format("fasta"))


def main():
    args = parser()
    file_conversion(args.in_filename, args.out_filename)

if __name__ == '__main__':
    main()

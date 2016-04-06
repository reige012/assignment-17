#!/usr/bin/env python

"""
Assignment 17_Task1:
In the task1-files directory, there is a file named \
10k-reads-S100_L004_R1_001.fastq that contains 10,000 FASTQ reads. Write a \
program that reads in the FASTQ file, reverse complements each sequence, and \
writes the reverse complemented sequences out as a FASTA-formatted file. Use \
argparse to get the name of the input file (the FASTQ file) and the name of \
some output file name from the user. Use BioPython to read/write/convert the \
input and output files. Your program should contain a main loop and an ifmain \
statement, and it should be formatted correctly.

Credit url: http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc66
Date accessed on: April 4th, 2016

Note for users: Make sure that this Python program, input fastq file and the \
output fasta files are in the same folder/location.

Created by Shraddha Shrestha on April 4th, 2016.
Copyright 2016 Shraddha Shrestha. All rights reserved.

"""

from Bio import SeqIO
import argparse


def parser():
    parser = argparse.ArgumentParser(description='open fastq file, get reverse\
    complement of sequences and output in fasta format')
    parser.add_argument("-i", "--input",
                        type=str,
                        required=True,
                        help="input fastq file name, make sure to add '-i' \
                            before input file name. eg: -i test.fastq"
                        )

    parser.add_argument("-o", "--output",
                        type=str,
                        required=True,
                        help="output fasta file name, make sure to add '-o' \
                        before output file name. eg: -o test.fasta"
                        )
    args = parser.parse_args()
    return args


def fastq_rev_comp_fasta(infile, outfile):
    # This will take the user input fastq file and then reverse complement each
    # sequence and write it to an output fasta file. If you need to store the
    # reverse complements then we need to create record oject and write it to
    # an output file of any format.

    record = [rec.reverse_complement(id="rev_comp_"+rec.id, description="rever\
se complement") for rec in SeqIO.parse(infile, "fastq")]
    SeqIO.write(record, outfile, "fasta")


def main():
    arg = parser()
    # argparse command for input file
    input_file = arg.input
    # argparse command for output file
    output_file = arg.output
    fastq_rev_comp_fasta(input_file, output_file)


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 17 Task 1

Amie Settlecowski
5 Apr. 2016

This program reverse complements the sequences in a file, re-formats them, and
saves them to a new file.

python ../task1_settlecowski.py --i ../pathto/input.fastq --o output.fna
"""
import argparse
import os

from Bio import SeqIO
from Bio import SeqRecord


def get_args(parserr):
    '''
    Requires --i flag for user to specify path to input file
    Requires --o flag for user to name output file
    '''
    parserr.add_argument("--i",
        required=True,
        help="Path to input file",
        type=str)

    parserr.add_argument("--o",
        required=True,
        help="Name output file",
        type=str)


def convert_file(infile, outfile, in_format, out_format):
    '''Iterate through input file, converting each record to new format and
       and writing to output file.'''
    with open(infile, 'r') as in_f:
        with open(outfile, 'w') as out_f:
            for record in SeqIO.parse(in_f, in_format):
                record = rev_comp(record)
                record = convert_record(record, out_format)
                write_record(record, out_f)


def rev_comp(record):
    '''Reverse complement the sequence of specified seqrecord object.'''
    rcomp_record = SeqRecord.SeqRecord(record.seq.reverse_complement(),
                                        id=record.id,
                                        name=record.name,
                                        description=record.description)
    return rcomp_record


def convert_record(record, frmt):
    '''Converts specified seqrecord object to new format.'''
    fasta_record = record.format(frmt)
    return fasta_record


def write_record(record, out_file):
    '''Writes specified seqrecord object out to specified file.'''
    out_file.write(record)


def main():
    # Create Parser with arguments for input and output files
    file_name_parser = argparse.ArgumentParser()
    get_args(file_name_parser)
    file_args = file_name_parser.parse_args()
    # Change to directory with input file
    working_dir = os.path.split(file_args.i)[0]
    os.chdir(working_dir)

    # Specify input and output file formats
    in_format = 'fastq'
    out_format = 'fasta'
    # Convert input file into output file of specified format
    convert_file(file_args.i, file_args.o, in_format, out_format)

if __name__ == '__main__':
    main()

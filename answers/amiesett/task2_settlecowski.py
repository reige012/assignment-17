#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 17 Task 2

Amie Settlecowski
5 Apr. 2016

This program creates a directory and re-formats a set of input files, saving
each as a new file in that directory.

python ../task2_settlecowski.py --idir ../input_dir/ --odir ../output_dir/
"""
import argparse
import os
import glob

from Bio import AlignIO


def get_args(parserr):
    '''
    Requires --idir flag for user to specify path to input directory
    requires --odir flag for user to name output directory
    '''
    parserr.add_argument("--idir",
        required=True,
        help="Path to input directory",
        type=str)

    parserr.add_argument("--odir",
        required=True,
        help="Name output file",
        type=str)


def convert_file(infile, outfile, in_format, out_format):
    '''Iterate through input file, converting each record to new format and
       and writing to output file.'''
    with open(infile, 'r') as in_f:
        with open(outfile, 'w') as out_f:
            for record in AlignIO.parse(in_f, in_format):
                record = convert_record(record, out_format)
                write_record(record, out_f)


def convert_record(record, out_format):
    '''Converts specified seqrecord object to new format.'''
    record = record.format(out_format)
    return record


def write_record(record, f):
    '''Writes specified seqrecord object out to specified file.'''
    f.write(record)


def main():
    # Create Parser with arguments for paths to input and output directories
    path_name_parser = argparse.ArgumentParser()
    get_args(path_name_parser)
    path_args = path_name_parser.parse_args()
    # Change to directory with input files
    os.chdir(path_args.idir)
    # Collect all input files with specified file extension
    input_files = glob.glob('*.nexus')
    # Create output directory
    os.mkdir(path_args.odir)
    # Specify input and output file formats
    in_format = 'nexus'
    out_format = 'phylip-relaxed'
    # Iteratively convert format of each input file into output file
    for in_file in input_files:
        # Name output file
        out_file = os.path.splitext(in_file)[0] + '.phy'
        out_file = os.path.join(path_args.odir, out_file)
        convert_file(in_file, out_file, in_format, out_format)

if __name__ == '__main__':
    main()

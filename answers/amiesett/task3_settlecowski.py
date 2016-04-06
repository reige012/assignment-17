#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 17 Task 3

Amie Settlecowski
5 Apr. 2016

This program creates a directory and re-formats a set of input files, saving
each as a new file in that directory.

python ../task3_settlecowski.py --i ../pathto/input.fna --o output.txt
"""
import argparse
import os

from operator import itemgetter

from Bio import SeqIO
from Bio import Restriction


def get_args(parserr):
    '''
    Requires --i flag for user to specify path to input file
    Requires --o flag for user to name output file    '''
    parserr.add_argument("--i",
        required=True,
        help="Path to input file",
        type=str)

    parserr.add_argument("--o",
        required=True,
        help="Name output file",
        type=str)


def digest(supplier, in_file, in_format):
    '''Run analysis of digestion by all enzymes available from supplier and
    return dictionary of enzymes as keys with list of cut sites as values.'''
    # Create restriction batch of all enzymes available from supplier
    restr_batch = Restriction.RestrictionBatch([], suppliers=[supplier])
    # Create seqrecord object for sequence that will be digested
    with open(in_file, 'r') as f:
        record = SeqIO.read(f, in_format)
    # Set up restriction analysis
    analysis = Restriction.Analysis(restr_batch, record.seq, linear=False)
    # analysis.print_that(analysis.with_sites())
    return analysis.with_sites()


def sort_enzymes(enzyme_dict):
    '''Convert dictionary of enzymes with cut lists as sorted list of lists.'''
    cut_count_list = []
    for key, value in enzyme_dict.items():
        cut_count_list.append((key, len(value), value))
    cut_count_list = sorted(cut_count_list, key=itemgetter(1))[::-1]
    return cut_count_list


def write_summary(out_file, enzyme_cut_list):
    '''Write out summary file'''
    total = len(enzyme_cut_list)
    most = enzyme_cut_list[0][1]
    least = enzyme_cut_list[total-1][1]
    with open(out_file, 'w') as out_f:
        out_f.write('Number of REs with cut sites: {}\n'.format(str(total)))
        out_f.write('REs with most and fewest cut sites:\n')
        for index in enzyme_cut_list:
            if index[1] == most or index[1] == least:
                out_f.write('{}:\t\t{}\n'.format(index[0], str(index[1])))


def main():
    # Create Parser with arguments for paths to input and output directories
    file_name_parser = argparse.ArgumentParser()
    get_args(file_name_parser)
    file_args = file_name_parser.parse_args()
    # Change to directory with input file
    working_dir = os.path.split(file_args.i)[0]
    os.chdir(working_dir)

    # Specify restriction enzyme supplier code and input file format
    supplier = 'N'
    in_format = 'fasta'
    # Create dictionary of enzymes and their cut sites
    enzymes = digest(supplier, file_args.i, in_format)
    ranked_enzymes = sort_enzymes(enzymes)
    write_summary(file_args.o, ranked_enzymes)

if __name__ == '__main__':
    main()

# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 17
Oscar Johnson 3 April 2016

Copyright Oscar Johnson 2016

Finds New England Biolabs enzymes that cut the
mitochondrial genome of Gallus gallus
Returns various information about those enzymes to outfile supplied by user
"""

import os
import argparse
import pdb
from Bio.Restriction import *
from Bio import SeqIO


def get_args():
    parser = argparse.ArgumentParser(
            description="""provide input fasta file""")
    parser.add_argument('--in_file',
                        type=str,
                        required=True,
                        help="enter fasta file of Gallus gallus mtDNA genome"
                        )
    parser.add_argument('--out_file',
                        type=str,
                        required=True,
                        help="enter an output file name for enzyme data",
                        )
    return parser.parse_args()


def open_file(args):
    """
    open fasta file to do stuff
    """
    with open(args.in_file, 'r') as infile:
        record = SeqIO.read(infile, 'fasta')
        return record


def enzymes(record):
    """
    Cuts circular mitochondrial genome with
    all restriction enzymes from New England Biolabs

    Uses some bits of code (somewhat edited)
    straight from the BioPython cookbook:
    http://biopython.org/DIST/docs/cookbook/Restriction.html

    Returns dictionary of enzymes and all cut sites
    """
    # all restriction enzymes from New England Biolabs
    rb_neb = RestrictionBatch(first=[], suppliers=['N'])
    cut_sites = {}
    for e in rb_neb:
        cut = e.search(record.seq, linear=False)
        if len(cut) > 0:
            cut_sites[str(e)] = cut
        else:
            pass
    return cut_sites


def dict_to_tuples(d):
    """
    takes dictionary of enzymes and cut sites
    and returns sorted list of tuples containing
    (number of cut sites, string of enzyme name, list of all cut sites)
    but sorted by the number of cut sites
    """
    l = []
    for key, value in d.items():
        l.append((len(value), key, value))
    l.sort()
    return l


def write(args, data):
    """
    Takes data from dict_to_tuples and writes the
    information that El Jefe wants to a user-specified .txt outfile
    """
    # rename outfile to .txt if needed
    if args.out_file[-4:] != '.txt':
        args.out_file += '.txt'
    else:
        pass
    fewest_sites = []
    for val in data:
        if val[0] == 1:
            fewest_sites.append(val[1:])
    with open(args.out_file, 'w') as outfile:
        outfile.write('info about Gallus gallus mitochondrial genome\n\n')
        outfile.write('number of enzymes that cut the genome: {}'
                      .format(len(data)))
        outfile.write("""\n\nthere are {} enzymes cutting the genome
    at a single site ('enzyme' and [site]): {}"""
                      .format(len(fewest_sites), str(fewest_sites)))
        outfile.write("""\n\nenzyme cutting the genome in the most places is {}
    which cuts at {} sites"""
                      .format(data[-1][1], data[-1][0]))


def main():
    args = get_args()
    os.chdir(os.path.dirname(args.in_file))
    seq_record = open_file(args)
    # pdb.set_trace()
    sites = enzymes(seq_record)
    sorted_tups = dict_to_tuples(sites)
    write(args, sorted_tups)

if __name__ == '__main__':
    main()

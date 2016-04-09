#! /usr/bin/env python
# encoding UTF-8

'''
Assignment17Task3 biol7800
ZacCarver 04/05/2016
'''
import argparse
from Bio import Restriction
from Bio import SeqIO


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gen", type=str,
                        help="provide file containing a genome(circular)")
    return parser.parse_args()


def site_search(infile):
    with open(infile, 'r') as f:
        record = SeqIO.read(f, 'fasta')
        new_seq = record.seq
        #http://biopython.org/DIST/docs/cookbook/Restriction.html#mozTocId255275
        rb = Restriction.RestrictionBatch([], ['N'])
        Analong = Restriction.Analysis(rb, new_seq, linear=False)
        Analong.print_as('number')
        Analong.print_that()


#def fxn writes to txt file


def main():
    arg = args()
    site_search(arg.gen)
if __name__ == '__main__':
    main()

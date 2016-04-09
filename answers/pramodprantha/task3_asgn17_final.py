#!/usr/bin/env python
# utf-8


"""
task 3 of assignment 17
Created by Pramod Pantha on April 3, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
#reference:
http://biopython.org/DIST/docs/cookbook/Restriction.html#mozTocId129244
class slide
"""

from Bio import Restriction
import argparse


def NEB_restrictioncite(infile, outfile):
    rb_supp = Restriction.RestrictionBatch(first=[], suppliers=['N'])
    print(rb_supp)
    # This will create a RestrictionBatch with the all enzymes from NEB


def rb_search():
    rb_search(infile, linear=False)
    # consider input as a circular DNA file


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("infile", help="give name of your fasta file")
    parse.add_argument("outfile", help="give your output file name")
    args = parse.parse_args()
    fastafile = args.infile
    Restriction.rb.search(fastafile)
    # it will cut circular infile for all NEB enzymes
    restrictioncite = args.outfile
    NEB_restrictioncite.print_as('map')
    NEB_restrictioncite.print_that()
    # it will print cut site as a map with name and frequency on it
    NEB_restrictioncite(fastafile, restrictioncite)

    if __name__ == '__main__':
        main()

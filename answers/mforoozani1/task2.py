#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task2 to read nexus files and convert each, individual file
to the PHYLIP file format.
"""
import argparse
import glob
import os
from Bio import AlignIO


def get_parser():
    """
   using argparse to takes the list  as input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--indirectory", help='directory to use', type=str)
    parser.add_argument("--outputfile1", help='outputfiles_name', type=str)
    parser.add_argument("--outputfile2", help='outputfiles_name', type=str)
    parser.add_argument("--outputfile3", help='outputfiles_name', type=str)
    args = parser.parse_args()
    return args


def main():
    args = get_parser()
    outfile1 = open(args.outputfile1, "w")
    file1 = glob.glob(os.path.join(args.indirectory, "*.nexus"))
    with open(file1[0], "r") as infile1:
        aln = AlignIO.read(infile1, 'nexus')
        AlignIO.write(aln, outfile1, 'phylip-relaxed')
    outputfile2 = open(args.outputfile2, "w")
    with open(file1[1], "r") as infile2:
        aln = AlignIO.read(infile2, 'nexus')
        AlignIO.write(aln, outputfile2, 'phylip-relaxed')
    outputfile3 = open(args.outputfile3, "w")
    with open(file1[2], "r") as infile3:
        aln = AlignIO.read(infile3, 'nexus')
        AlignIO.write(aln, outputfile3, 'phylip-relaxed')


if __name__ == '__main__':
    main()

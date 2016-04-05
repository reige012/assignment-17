#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task1 to Write a program to reads in the FASTQ file, reverse
complements each sequence, and writes the reverse complemented sequences out as
a FASTA-formatted file
"""
from Bio import Restriction
import argparse
from Bio import SeqIO
import collections


def get_parser():
    """
   using argparse to takes the list  as input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputfile", required=True)
    parser.add_argument("--outputfile", required=True)
    args = parser.parse_args()
    return args


def number_enzyme(record):
    my_batch = Restriction.RestrictionBatch(first=[], suppliers="N")
    A = my_batch.search(record.seq, linear=False)
    B = collections.OrderedDict(sorted(A.items(), key=lambda t: len(t[1])))
    KK = []
    for v in B.values():
        KK.append(len(v))
    return(KK)


def number_enzyme2(record):
    my_batch = Restriction.RestrictionBatch(first=[], suppliers="N")
    A = my_batch.search(record.seq, linear=False)
    B = collections.OrderedDict(sorted(A.items(), key=lambda t: len(t[1])))
    print(len(B))
    C = []
    for k in B.keys():
        C.append(k)
    return(C)


def main():
    args = get_parser()
    outfile = open(args.outputfile, "w")
    with open(args.inputfile, "r") as infile:
        record = SeqIO.read(infile, 'fasta')
    A = number_enzyme(record)
    B = number_enzyme2(record)
    print(A)
    print(B)
    for x in range(1, len(A)):
        outfile.write("%s %s\n" % (B[x], A[x]))


if __name__ == '__main__':
    main()

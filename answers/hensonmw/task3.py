#!/usr/bin/env python
# encoding: utf-8

"""
My 3rd program for Assignment 17

Created by Michael Henson on 4 April 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""
import argparse
from Bio import Restriction
from Bio import SeqIO
from operator import itemgetter


def askingforfiles():
    parser = argparse.ArgumentParser(
        description="Directory for your output folder")
    parser.add_argument(
        "--fna",
        required=True,
        help="Provide the forward alignment files directory",
        type=str
    )
    return parser.parse_args()


def enzymes(read):
    rb_supp = Restriction.RestrictionBatch(first=[], suppliers=['N'])
    with open(read) as read:
        record = SeqIO.read(read, 'fasta')
        x = Restriction.Analysis(rb_supp, record.seq, linear=False)
        print("There are {} enzymes in NEBs order list".format(len(rb_supp)))
        y = x.with_sites()
        print("\nThere are {} enzymes in NEBSs order list that cut {}".format((len(y)), record.id))
        length = {key: len(value) for key, value in y.items()}
        sort = sorted(length.items(), key=itemgetter(1), reverse=True)
        print("\n{}(Enzyme, cuts) cuts {}".format(sort[0], record.id))
        z = x.with_N_sites(1)
        length = {key: len(value) for key, value in z.items()}
        sort_1cut = sorted(length.items(), key=itemgetter(1))
        zero = x.without_site()
        length_zero = {str(key): len(value) for key, value in zero.items()}
        sort_0cut = sorted(length_zero.items(), key=itemgetter(1))
        print("\nThese enzmes cut {} the fewest(>=1):\n{}\n{}".format(record.id, sort_1cut,
        sort_0cut))


def main():
    path = askingforfiles()
    enzymes(path.fna)


if __name__ == '__main__':
    main()

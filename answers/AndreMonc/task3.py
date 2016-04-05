# !/usr/bin/env python
# encoding: utf-8

"""
My assignment 17 task3 program
Created by Andre Moncrieff on 4 April 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""


import os
import glob
import argparse
import os.path
from Bio import SeqIO
from Bio import Restriction


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--in_path", required=True,
                        help="Enter path for the directory containing Gallus"
                        "gallus mtDNA genome FASTA formatted file",
                        type=str)
    parser.add_argument("--out_name", required=True,
                        help="Enter the name you wish for the answer output" +
                        " file",
                        type=str)
    args = parser.parse_args()
    return args


def readin(in_path):
    os.chdir(in_path)
    filename = glob.glob("*.fasta")[0]
    with open(filename, "r") as infile:
        record = SeqIO.read(infile, 'fasta')
    return record


def res_enz_stuff(record):
    new_eng_enz = Restriction.Restriction.RestrictionBatch(first=[],
                                                           suppliers=["N"])
    enzyme_cuts = []
    for enzyme in new_eng_enz:
        # possible to for the enzyme variable to work as attribute??
        # Did not figure out yet.
        number_of_cuts = Restriction.enzyme.search(record.seq, linear=false)
        if number_of_cuts == []:
            enzyme_cuts.append(int(0))
        if number_of_cuts[0] > 0:
            enzyme_cuts.append(number_of_cuts[0])
    return new_eng_enz, enzyme_cuts

"""
def write_to_new_file(tuple_lists):
    maxval_cuts = max(tuple_lists[1])
    max_cut_indices = [ind for ind, val in enumerate(tuple_lists[1]) if val == maxval_cuts]
    minval_cuts = min(tuple_lists[1])
    min_cut_indices = [ind for ind, val in enumerate(tuple_lists[1]) if val == minval_cuts]
    with open("answers.txt", "w") as outfile:





Did not have time to finish
"""


def main():
    args = parser()
    record = readin(args.in_path)
    tuple_lists = res_enz_stuff(record)
    write_to_new_file(tuple_lists)


if __name__ == '__main__':
    main()

#! /usr/bin/env python
# encoding: utf-8

'''
Grace Cagle
Assignment 17 Task 3
A program that uses BioPython to determine all possible restriction enzymes
from NEB that cut the chicken mtDNA sequence. Write the number of these enzymes
that cut the chicken mtDNA to a text file that also contains the name of the
enzyme cutting the chicken mtDNA sequence in the fewest places as well as the
name of the enzyme cutting the chicken mtDNA sequence in the largest number of
places. Be sure to also output the exact number(s) of cuts provided by the
most and least agressive restriction enzyme.
'''

import argparse
import glob
import os
from Bio import SeqIO
from Bio.Restriction import *
import operator


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', "--input",
        required=True,
        help="The input file in FASTA format"
    )
    parser.add_argument(
        '-o', "--output",
        required=True,
        help="The output file name"
    )
    return parser.parse_args()


def read_file(args):
    with open(args.input, 'r') as infile:
        record = SeqIO.read(infile, 'fasta')
        return record


def restrict(record):
    rb_supp = RestrictionBatch(first=[], suppliers='N')
    result = rb_supp.search(record.seq, linear=False)
    return result


def make_dict(result):
    d = result
    length_dict = {str(key): len(value) for key, value in d.items()}
    return length_dict


def get_largest(length_dict):
    sd = sorted(length_dict.items(), key=operator.itemgetter(1), reverse=True)
    largest = sd[0]
    return largest


def get_smallest(length_dict):
    smallest = []
    for k, v in length_dict.items():
        if v == 0:
            smallest.append({k: v})
    return smallest


def write_file(args, largest, smallest):
    with open(args.output, 'w') as my_output:
        my_output.write("The largest is:\n\n{!s:<10} cuts {!s:<10}\n\n".format(*largest))
        my_output.write("The smallest are:\n")
        for item in smallest:
            for k, v in item.items():
                my_output.write("\n{!s:<10} cuts {!s:<10}".format(k, v))


def main():
    args = get_args()
    record = read_file(args)
    result = restrict(record)
    length_dict = make_dict(result)
    smallest = get_smallest(length_dict)
    largest = get_largest(length_dict)
    write_file(args, largest, smallest)

if __name__ == '__main__':
    main()

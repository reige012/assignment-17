#!/usr/bin/env python
# utf-8

"""
Assignment 17, Task 3
Jon Nations on 3 April 2016
Chicken mtDNA Genome. Remembering that this is a circular genome and assuming that NEB (New Englang Biolabs) is the only supplier of restriction enzymes in the entire world, write a program that uses BioPython to determine all possible restriction enzymes from NEB that cut the chicken mtDNA sequence. Write the number of these enzymes that cut the chicken mtDNA to a text file that also contains the name of the enzyme cutting the chicken mtDNA sequence in the fewest places as well as the name of the enzyme cutting the chicken mtDNA sequence in the largest number of places. Be sure to also output the exact number(s) of cuts provided by the most and least agressive restriction enzyme. As above, use argparse to get the input and output file names from the user. Your program should contain a main loop and an ifmain statement, and it should be formatted correctly.
"""
"""Need three things in the .txt. file
1) number of enzymes that can cut the chicken mt genome
2) enzyme that makes the most cuts and number of cuts it makes like:
    ASS1 makes the most cuts: 6421

    ASS2 makes the least cuts: 1"""

from Bio import Restriction
from Bio import SeqIO
import argparse
from collections import Counter
import operator



def file_in():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, type=str,
                        help="give input file name.")
    parser.add_argument('-o', '--output', required=True, help="give output file (.txt format) where enzyme list is going.")
    return parser.parse_args()


def get_seq(args):
    with open(args.input, 'r') as infile:
        chicken = SeqIO.read(infile, 'fasta')
        # print(chicken)  works!
        return chicken


def get_enzymes(chicken):
    r_batch = Restriction.RestrictionBatch(first=[], suppliers=['N'])
    # r_batch.search(chicken.seq)
    Ana = Restriction.Analysis(r_batch, chicken.seq, linear=False)
    Ana_dict = Ana.full()  # turn Ana from RestrictionAlalysis type to dict
    Ana_dict = {k: sum(1 for x in v if x) for k, v in Ana_dict.items()}
    # Dict sort method comes from iCodez answer from the page http://stackoverflow.com/questions/19843457/counting-how-many-values-were-attributed-to-a-key-an-a-python-3-2-dictionary
    return Ana_dict


def get_low(args, Ana_dict):
    with open(args.output, 'a') as output:
        for key, value in Ana_dict.items():
            if value == max(Ana_dict.values()) or 1 == value:
                print('enzyme:', key, 'number of cuts:', value, file=output)


def main():
    args = file_in()
    file_in()
    chicken = get_seq(args)
    Ana_dict = get_enzymes(chicken)
    # Ana_top = get_top(Ana_dict)
    get_low(args, Ana_dict)
    # print(Ana_top)
    # file_out(args, Ana_dict)
    # Ana.print_that()
    # print(Ana)

if __name__ == '__main__':
    main()

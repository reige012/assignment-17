#!/usr/bin/env python
# encoding: utf-8

"""
Gets a sequence file and output file name from the user. Searches New England
Biosystems restriction enzymes to determine which cut that sequence.  Then
creates an output file telling how many enzymes cut the sequence, which of
those that do cut cut the least amount of times(1) and which cuts the most
amount of times.

Edited by Alicia Reigel. 4 April 2016.
Copyright Alicia Reigel. Louisiana State University. 4 April 2016. All
rights reserved.

"""


import argparse
from Bio import Restriction
from Bio import SeqIO


def parser_get_args():
    """Collects the path to the file"""
    parser = argparse.ArgumentParser(
        description="""Input the full path to the file of interest"""
        )
    parser.add_argument(
            '--filepath',
            required=True,
            type=str,
            help='Enter the path to the file of interest.'
        )
    parser.add_argument(
            '--outputfile',
            required=True,
            type=str,
            help='Enter the desired name for the output file'
        )
    return parser.parse_args()


def search_for_cuts(enzymes_list, sequence_file, an_outputfile):
    """searches the sequence for all enzymes in the list that cut it and
        creates a dictionary with the enzyme and the number of times it cuts"""
    with open(sequence_file, 'r') as input_file:
        for record in SeqIO.parse(input_file, 'fasta'):
            sequence = record.seq
        cut = Restriction.Analysis(enzymes_list, sequence, linear=False)
        # makes a specific type of dictionary from the analysis
        cut_dict = cut.full()
        # changes it to a normal dictionary (source: http://biopython.org/DIST/docs/cookbook/Restriction.html#mozTocId255275)
            # cut.print_that(); reminder to self that this source above does
            # this cool funtion that makes a lovely list of all cute places
        cut_dict = {k: sum(1 for x in v if x) for k, v in cut_dict.items()}
        return cut_dict


def get_max_cuts(a_dict):
    """gets the enzyme with the most cuts"""
    v = list(a_dict.values())
    k = list(a_dict.keys())
    key_most_cuts = k[v.index(max(v))]
    # source:http://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
    return (key_most_cuts, max(v))


def get_least_cuts(a_dict):
    """gets the enzyme(s) with the least cuts and makes them into a list"""
    low_list = []
    for key, value in a_dict.items():
        if value == 1:
            low_list.append(key)
        else:
            pass
    return low_list


def make_cut_set(a_cut_dict):
    """creates a set of the enzymes that actually cut the sequence"""
    good_list = []
    for key, value in a_cut_dict.items():
        if value >= 1:
            good_list.append(key)
    cut_set = set(good_list)
    return cut_set


def print_it_to_file(o_file, cut_set, least_list, most_cuts, value_most_cuts):
    """prints all of the information to one output file"""
    with open(o_file, 'a') as output_file:
        output_file.write('Based on restriction enzymes available from New England Biosystems:\n\n')
        output_file.write('There are {} enzymes that will cut Gallus gallus mtDNA.'.format(len(cut_set)))
        output_file.write('\n\nThe following enzymes only cut the mtDNA 1 time, which is the fewest possible cuts:\n')
        for item in least_list:
            output_file.write('{}\n'.format(item))
        output_file.write('\n\nThe enzyme that cuts the most times is {} with {} cuts.'.format(most_cuts, value_most_cuts))


def main():
    args = parser_get_args()
    all_N_enzymes = Restriction.RestrictionBatch(first=[], suppliers="N")
    # list of all New England Bio's available restriction enzymes
    cut_dict = search_for_cuts(all_N_enzymes, args.filepath, args.outputfile)
    most_cuts_key, cuts = get_max_cuts(cut_dict)
    cut_set = make_cut_set(cut_dict)
    least_cuts_list = get_least_cuts(cut_dict)
    print_it_to_file(args.outputfile, cut_set, least_cuts_list, most_cuts_key, cuts)


if __name__ == '__main__':
    main()

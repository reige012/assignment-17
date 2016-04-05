#!/usr/bin/env python
# encoding: utf-8

"""
Assignment 17
Task 3 Program: Processing chicken mtDNA
Jessie Salter
3 April 2016
"""

import argparse
from Bio import SeqIO
from Bio import Restriction


def parser():
    '''Takes user input'''
    parser = argparse.ArgumentParser(
        description="Gets the input and output file names from the user")
    parser.add_argument(
        "--input",
        required=True,
        help="Enter the input sequence filename.",
        type=str
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Enter the name of the output file you want to create.",
        type=str
    )
    return parser.parse_args()


def insilico(input_file):
    '''Identifies all possible restriction enzymes for the given genome
    available from New England BioLabs.'''
    with open(input_file, 'r') as infile:
        chicken = SeqIO.read(infile, 'fasta')
    NEB_batch = Restriction.RestrictionBatch(first=[], suppliers='N')
    my_batch = []
    for enzyme in NEB_batch:
        # Linear=False is the key to making with work with a circular DNA!
        cutsites = enzyme.search(chicken.seq, linear=False)
        my_batch.append([len(cutsites), enzyme])
    final_batch = []
    for item in my_batch:
        if item[0] > 0:
            final_batch.append(item)
    return sorted(final_batch, reverse=True)


def results(final_batch, output):
    '''Takes the results of the insilico search and writes the most and least
    aggressive enzyme results to a text file.'''
    with open(output, 'w') as results:
        # Most aggressive:
        max_ties = []
        for x in range(len(final_batch)):
            # This will catch any ties and print all results:
            if final_batch[0][0] == final_batch[x][0]:
                max_ties.append(final_batch[x])
        results.write('{0}\n\n{1:<12}{2:<5}\n{3}\n'.format(
            'Most aggressive enzymes:',
            'Enzyme',
            'Cut sites',
            '------------------------'
            )
            )
        for item in max_ties:
            results.write('{0:<12}{1:<5}\n\n'.format(
                str(item[1]),
                str(item[0])
                )
                )
        results.write('\n')
        # Least aggressive:
        min_ties = []
        for x in range(len(final_batch)):
            if final_batch[-1][0] == final_batch[x][0]:
                min_ties.append(final_batch[x])
        results.write('{0}\n\n{1:<12}{2:<5}\n{3}\n'.format(
            'Least aggressive enzymes:',
            'Enzyme',
            'Cut sites',
            '-------------------------'
            )
            )
        for item in min_ties:
            results.write('{0:<12}{1:<5}\n'.format(
                str(item[1]),
                str(item[0])
                )
                )


def main():
    args = parser()
    batch = insilico(args.input)
    results(batch, args.output)

if __name__ == '__main__':
    main()

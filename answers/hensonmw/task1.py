#!/usr/bin/env python
# encoding: utf-8

"""
My 1st program for Assignment 17

Created by Michael Henson on 4 April 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""
import argparse
import os
from Bio import SeqIO


def askingforfiles():
    parser = argparse.ArgumentParser(
        description="Directory for your output folder")
    parser.add_argument(
        "--directory",
        required=True,
        help="Provide the desired directory path please ",
        type=str
    )
    parser.add_argument(
        "--fnq",
        required=True,
        help="Provide the forward .fastq file",
        type=str
    )
    return parser.parse_args()


def makedirectory(directory_file):
    newpath = os.path.join(directory_file, 'Alignment_output')
    print(newpath)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath


def reverse(R_read):
    ''' Because we are working with DNA, we need to take the reverse read from our
    sanger sequences and create the reverse complement (RC). This will allow us
    to align our sequences.
    '''
    sequences = []
    # Creating a list file of the reads
    with open(R_read) as R_read:
        for read in SeqIO.parse(R_read, "fastq"):
            if "n" in read.seq:
                raise IOError("Sequence {} has ambigous bp".format(read.id))
            else:
                x = read.reverse_complement(read.seq)
                sequences.append(x)
    return sequences


def main():
    path = askingforfiles()
    X = makedirectory(path.directory)
    RC = reverse(path.fnq)
    os.chdir(X)
    RC_output = open("RC_seqs.fasta", "w")
    SeqIO.write(RC, RC_output, "fastq")


if __name__ == '__main__':
    main()

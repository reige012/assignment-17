#!/usr/bin/env python
# utf-8

"""
BIOL 7800 Assignment 17, Task 1
Austen T. Webber
2016_4_4
"""
import argparse
import os
from Bio import SeqIO


def askingforfiles():
    parser = argparse.ArgumentParser(
        description="Directory of output folder")
    parser.add_argument(
        "--directory",
        required=True,
        help="Directory path for output fasta file ",
        type=str
    )
    parser.add_argument(
        "--fastq",
        required=True,
        help="Provide the .fastq file",
        type=str
    )
    return parser.parse_args()


def makedirectory(directory_file):
    newdir = os.path.join(directory_file, 'Reverse_Complement')
    print(newdir)
    if not os.path.exists(newdir):
        os.makedirs(newdir)
    return newdir


def reverse(Rev_read):
    ''' Finds reverse compliment of fastq sequence
    '''
    sequences = []
    # Creating a list file of the reads
    with open(Rev_read) as Rev_read:
        for read in SeqIO.parse(Rev_read, "fastq"):
            if "n" in read.seq:
                raise IOError("Sequence {} has ambigous bp".format(read.id))
            else:
                x = read.reverse_complement(read.seq)
                sequences.append(x)
    return sequences


def main():
    path = askingforfiles()
    X = makedirectory(path.directory)
    Revcomp = reverse(path.fastq)
    os.chdir(X)
    Rev_comp_output = open("Rev_comp_seqs.fasta", "w")
    SeqIO.write(Revcomp, Rev_comp_output, "fastq")


if __name__ == '__main__':
    main()

# http://biopython.org/wiki/Seq#Complement_and_reverse_complement
# https://www.biostars.org/p/14614/
# https://www.biostars.org/p/93844/

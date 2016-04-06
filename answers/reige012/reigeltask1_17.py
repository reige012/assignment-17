#!/usr/bin/env python
# encoding: utf-8

"""
This takes a directory path and an output file name as input from the command
line and then searches that directory for any file with *fastq* in the name.
The first of those files is then selected and each sequence record is read into
the script and the reverse complement is determined and written to the output
file in fasta format.

Edited by Alicia Reigel. 4 April 2016.
Copyright Alicia Reigel. Louisiana State University. 4 April 2016. All
rights reserved.

"""


import argparse
import os
import glob
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


def parser_get_args():
    """Collects the path to the directory holding the fastq file"""
    parser = argparse.ArgumentParser(
        description="""Input the full path to the directory of interest"""
        )
    parser.add_argument(
            '--directorypath',
            required=True,
            type=str,
            help='Enter the path to the directory of interest.'
        )
    parser.add_argument(
            '--outputfile',
            required=True,
            type=str,
            help='Enter the desired name for the output file'
        )
    return parser.parse_args()


def open_sequences_get_reverse(an_inputfile, an_outputfile):
    """determines the reverse compliment of the sequence and prints those to
       a new output file"""
    with open(an_inputfile, 'r') as input_file:
        with open(an_outputfile, 'a') as output_file:
            for record in SeqIO.parse(input_file, 'fastq'):
                # iteratively brings in each sequence from the input file
                new_record = SeqRecord(seq=record.seq.reverse_complement(), id=record.id, name=record.name, description="reverse complement")
                # creates a new seq record with the original description info
                # and the reverse complement as the sequence
                output_file.write(new_record.format('fasta'))
                # writes the new sequence in fasta format to the output file


def main():
    args = parser_get_args()
    os.chdir(args.directorypath)
    path_name = os.path.join(args.directorypath, "*fastq*")
    # finds the pathnames for any files that have *fastq* in the directory
    file_path_list = glob.glob(path_name)
    # creates a list of the path names associated with the c-darwin files found
    file_name = os.path.basename(file_path_list[0])
    # finds the basename for the first file path in the list created by glob
    open_sequences_get_reverse(file_name, args.outputfile)


if __name__ == '__main__':
    main()

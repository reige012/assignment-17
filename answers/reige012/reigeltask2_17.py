#!/usr/bin/env python
# encoding: utf-8

"""
Obtains an input directory containing nexus alignments and the name of an
output directory to place the converted alignments into after they are
converted to phylip-relaxed format.

Edited by Alicia Reigel. 4 April 2016.
Copyright Alicia Reigel. Louisiana State University. 4 April 2016. All
rights reserved.

"""


import argparse
import os
import glob
from Bio import AlignIO


def parser_get_args():
    """Collects the path to the directory holding the alignment files"""
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
            '--odirectory',
            required=True,
            type=str,
            help='Enter the desired name for the output directory'
        )
    return parser.parse_args()


def convert_alignments(in_file, out_file, new_type):
    """converts a nexus alignment into a phylip alignment and writes to new file"""
    alignments = AlignIO.parse(open(in_file, 'r'), "nexus")
    for alignment in alignments:
        handle = open(out_file, "a")
        AlignIO.write(alignment, handle, new_type)
        handle.close()


def main():
    args = parser_get_args()
    os.chdir(args.directorypath)
    os.mkdir(os.path.join(args.directorypath, args.odirectory))
    output_path = os.path.abspath(args.odirectory)
    path_name = os.path.join(args.directorypath, "*nexus*")
    # finds the pathnames for any files that have *nexus* in the directory
    file_path_list = glob.glob(path_name)
    # creates a list of the path names associated with the c-darwin files found
    for filepath in file_path_list:
        file_name = os.path.basename(filepath)
        # finds the basename for the file path in the list created by glob
        new_file_name = file_name.replace('.nexus', '')
        # removes the .nexus from the end of the file name
        out_file = os.path.join(output_path, new_file_name + '.phylip')
        # creates an outfile that has the path of the new directory + the name
        # of the original inputfile and ends in .phylip
        convert_alignments(file_name, out_file, 'phylip-relaxed')


if __name__ == '__main__':
    main()

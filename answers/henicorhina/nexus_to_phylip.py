# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 17
Oscar Johnson 3 April 2016

Copyright Oscar Johnson 2016

convert nexus files to phylip-relaxed alignment files
provide input and output directories
"""

import os
import glob
import argparse
from Bio import AlignIO


def get_args():
    parser = argparse.ArgumentParser(
            description="""provide input directory of nexus files""")
    parser.add_argument('--in_dir',
                        type=str,
                        required=True,
                        help="enter a fastq files",
                        )
    parser.add_argument('--out_dir',
                        type=str,
                        required=True,
                        help="enter an output directory for phylip files",
                        )
    return parser.parse_args()


def file_converter(my_files):
    """
    takes list of nexus files in working directory
    converts to phylip files
    writes to output directory
    """
    for file in my_files:
        with open(file, 'r') as in_file:
            name = os.path.basename(file)
            n = name.split('.')
            new_file = n[0] + '.phylip'
            with open(new_file, 'w') as out_file:
                aln_nexus = AlignIO.read(in_file, 'nexus')
                AlignIO.write(aln_nexus, out_file, 'phylip-relaxed')


def main():
    args = get_args()
    files = glob.glob(os.path.join(args.in_dir, '*.nexus'))
    file_converter(files)

if __name__ == '__main__':
    main()

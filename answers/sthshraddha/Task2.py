#!/usr/bin/env python

import os
import glob
import shutil
import argparse
from Bio import AlignIO


def parser():
    """Get directory information from user"""
    parser = argparse.ArgumentParser(
            description="Converting alignment format from nexus to phylip")
    parser.add_argument("-indir", required=True, type=str, help="user's input directory with files, eg: -indir C:xyz\abc")
    parser.add_argument("-outdir", required=True, type=str, help="user's choice of output directory, eg: -outdir C:xyz\abc")
    return parser.parse_args()


def converting_file_format(myfiles, outdir):
    for file in myfiles:
        read_align = AlignIO.parse(file, 'nexus')
        with open("aln_file.phylip", 'w') as outfile:
            convert_form = AlignIO.write(read_align, outfile, 'phylip-relaxed')
            shutil.copy(convert_form, outdir)


def main():
    args = parser()
    myfiles = glob.glob(os.path.join(args.indir, '*.nexus'))
    output_dir = args.outdir
    converting_file_format(myfiles, output_dir)


if __name__ == '__main__':
    main()

# !/usr/bin/env python
# encoding: utf-8

"""
My assignment 17 task2 program
Created by Andre Moncrieff on 4 April 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""

import glob
import os
import argparse
from Bio import AlignIO


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--in_path", required=True,
                        help="Enter path for the NEXUS file directory.",
                        type=str)
    parser.add_argument("--out_path", required=True,
                        help="Enter path for the directory where you want" +
                        " to put all the PHYLIP output files.",
                        type=str)
    args = parser.parse_args()
    return args


def list_of_filenames(in_path):
    os.chdir(in_path)
    list_of_filenames = glob.glob("*.nexus")
    return list_of_filenames


def file_conversion(list_o_filenames, in_path, out_path):
    counter = 1
    for nex_file in list_o_filenames:
        os.chdir(in_path)
        alignment = AlignIO.read(nex_file, 'nexus')
        os.chdir(out_path)
        with open("locus-{}.phylip".format(counter), "w") as outfile:
            AlignIO.write(alignment, outfile, 'phylip-relaxed')
        counter += 1


def main():
    args = parser()
    list_o_filenames = list_of_filenames(args.in_path)
    file_conversion(list_o_filenames, args.in_path, args.out_path)


if __name__ == '__main__':
    main()

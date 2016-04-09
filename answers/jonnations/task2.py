#!/usr/bin/env python
# utf-8

"""
Assignment 17, Task 2
Jon Nations on 3 April 2016
This is a program that uses glob, os, and biopython to read these files and convert each, individual file to the PHYLIP file format.

"""
from Bio import SeqIO
import argparse
import os
import glob
import copy


def file_in():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--indir', required=True, type=str,
                        help="give input directory where nexus files are stored.")
    parser.add_argument('-o', '--outdir', required=True, help="give input directory where Phylip files are going.")
    return parser.parse_args()


def new_files(args):
    nexus_files = []
    os.chdir(args.indir)
    nexuses = glob.glob('*.nexus')
    nexus_files.extend(copy.deepcopy(nexuses))
    return nexus_files


def convert(nexus_files):
    for f in nexus_files:
        SeqIO.convert(f, 'nexus', f.replace(".nexus", ".phylip"), "phylip-relaxed")
        # print(phylip_files)


def output_dir(args, nexus_files):
    os.mkdir(args.outdir)
    my_phylip = glob.glob(os.path.join(args.indir, "*.phylip"))
    # works up to here!
    # the for loop is not doing what I want it to.
    # the files exist, I just need to get them from args,indir into args.outdir
    """for item in nexus_files:
        output_dir.append(os.path.join(args.outdir, item))
    for i in output_dir:
        open(i, 'w')"""
    for file in my_phylip:
        with open(os.path.join(args.indir, os.path.basename(file)), 'r') as infile:
                files = infile.read()
        with open(os.path.join(args.outdir, os.path.basename(file)), 'w') as out:
            out.write(files)
            out.close()


def main():
    file_in()
    args = file_in()
    new_files(args)
    nexus_files = new_files(args)
    """print(nexus_files)""" # debug
    convert(nexus_files)
    """phylip_files = convert(nexus_files)""" # debug
    output_dir(args, nexus_files)

if __name__ == '__main__':
    main()

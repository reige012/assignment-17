#!/usr/bin/env python
# encoding: utf-8

"""
My second task for Assignment 17. Note -- not complete...gave up...

Created by A.J. Turner on April 4, 2016
Copyright 2016 A.J. Turner. All rights reserved. Collaboration/helpful hints
provided by Mikey Henson.

"""
from Bio import Restriction
import argparse
import glob
import os


def get_location():
    """"user to input working directory and ouput directory--easiest to drop
    file path into command line for each"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--in_directory", help="input directory of interest", type=str)
    parser.add_argument("--out_directory", help="output directory of interest", type=str)
    args = parser.parse_args()
    return args


def res_enzyme(name):
    neb = Restriction.RestrictionBatch(first=[], suppliers=["N"])
    print("NOTE: I gave up at this point--task unfinished!")
    # print(neb)


def main():
    path = get_location()
    res_enzyme(path.in_directory)


if __name__ == '__main__':
    main()

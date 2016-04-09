# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Marco
# @Date:   2016-04-05 12:38:05
# @Last Modified by:   Marco
# @Last Modified time: 2016-04-05 15:21:38


import os
import glob
import argparse
from Bio import AlignIO


def arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument('input_folder', type=str, help="""give the
                             entire name of the directory(and path) containing
                             your files""")
        parser.add_argument('out_folder', type=str,
                            help="""give the entire name (and path)
                                 of the directory you want to put your
                                  files, minus the last dash""")
        args = parser.parse_args()
        inp = args.input_folder
        outp = args.out_folder
        return inp, outp


def nexus_to_phylip(in_folder, out_folder):
    for file in glob.glob(os.path.join(in_folder + "\\*.nexus")):
        filename = (file.split("\\")[-1]).split(".")[0]
        with open(file, "r") as my_file:
            my_alig = AlignIO.parse(my_file, "nexus")
            with open(out_folder+"\\"+filename+".phy", 'w') as out_file:
                AlignIO.write(my_alig, out_file, "phylip-relaxed")


def main():
    inp, outp = arguments()
    nexus_to_phylip(inp, outp)

if __name__ == '__main__':
    main()

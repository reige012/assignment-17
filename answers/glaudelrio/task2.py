# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Glaucia
# @Date:   2016-04-05 06:32:02
# @Last Modified by:   Glaucia
# @Last Modified time: 2016-04-05 16:31:31

"""
This code was made in partnership with Marco Rego
"""

import os
import glob
import argparse
from Bio import AlignIO


def arguments():
        """parsing arguments to allow changing input file and output file"""
        parser = argparse.ArgumentParser(description="""my argument parser""")
        parser.add_argument('inputdirectoryname', type=str, help="""give the
                             entire name of the directory(and path) containing
                             your files""")
        parser.add_argument('outputdirectoryname', type=str,
                            help="""give the entire name (and path)
                                 of the directory you want to put your
                                  files, minus the last dash""")
        args = parser.parse_args()
        inp = args.inputdirectoryname
        out = args.outputdirectoryname
        return inp, out


def nexus_to_phylip(in_folder, out_folder):
    list_of_files = glob.glob(os.path.join(in_folder + "\\*.nexus"))
    for file in list_of_files:
        name = (file.split("\\")[-1]).split(".")[0]
        with open(file, "r") as f:
            with open(out_folder+"\\"+name+".phy", 'w') as new:
                alig = AlignIO.parse(f, "nexus")
                AlignIO.write(alig, new, "phylip-relaxed")


def main():
    arg1, arg2 = arguments()
    nexus_to_phylip(arg1, arg2)

if __name__ == '__main__':
    main()

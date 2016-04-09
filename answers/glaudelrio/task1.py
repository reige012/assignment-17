# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Glaucia
# @Date:   2016-04-04 18:20:21
# @Last Modified by:   Glaucia
# @Last Modified time: 2016-04-05 16:31:19

"""
This code was made in partnership with Marco Rego
"""

import argparse
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


def arguments():
    """parsing arguments to have input file"""
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str, help="name of input file FASTQ")
    parser.add_argument('output_name', type=str, help="name of output file FASTA")
    args = parser.parse_args()
    input_file = args.input_file
    output_name = args.output_name
    return input_file, output_name


def fastq_rev_transform(input_file, output_name):
    with open(input_file) as myfile:
        with open(output_name, 'w') as outfile:
            for rec in SeqIO.parse(myfile, 'fastq'):
                new = SeqRecord(seq=rec.seq.reverse_complement(), id=rec.id,
                                name=rec.name, description="reverse complement")
                outfile.write(new.format('fasta'))


def main():
    inp, out = arguments()
    fastq_rev_transform(inp, out)

if __name__ == '__main__':
    main()
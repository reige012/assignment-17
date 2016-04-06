# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Marco
# @Date:   2016-04-04 09:47:13
# @Last Modified by:   Marco
# @Last Modified time: 2016-04-05 15:46:42


'''
I worked with Glaucia Del Rio to write the codes in this task, that
 is the reason why our code is similar
'''

import argparse
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


def parser_function():
    '''
    Function to parse arguments
    '''
    parser = argparse.ArgumentParser(description='''This program provide gets a
         fastq file as input create the reverse complement of the input
         sequences and write then as a fasta file''')
    # Adding an argument to 'parse'
    parser.add_argument('in_file', type=str,
                        help='type the name of the fastq file you wish to '
                             'parse')
    parser.add_argument('out_file', type=str,
                        help='type the name of the fasta file')
    args = parser.parse_args()
    inp = args.in_file
    outp = args.out_file
    return inp, outp


def fastq2fasta_rev_comp(input_file, output_name):
    with open(input_file) as myfile:
        with open(output_name, 'w') as outfile:
            for record in SeqIO.parse(myfile, 'fastq'):
                new = SeqRecord(seq=record.seq.reverse_complement(),
                                id=record.id, name=record.name,
                                description=record.description
                                )
                outfile.write(new.format('fasta'))


def main():
    inp, outp = parser_function()
    fastq2fasta_rev_comp(inp, outp)

if __name__ == '__main__':
    main()

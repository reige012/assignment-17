# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Marco
# @Date:   2016-04-04 22:55:41
# @Last Modified by:   Marco
# @Last Modified time: 2016-04-05 15:46:14


import argparse
from Bio import Seq
from Bio import Restriction
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


'''
I worked with Glaucia Del Rio to write the codes in this task, that
 is the reason why our code is similar
'''


def parser_function():
    '''
    Function to parse arguments
    '''
    parser = argparse.ArgumentParser(description='''Enzyme Query''')
    # Adding an argument to 'parse'
    parser.add_argument('in_file', type=str,
                        help='type the name of the fasta file you wish to '
                             'parse')
    parser.add_argument('out_file', type=str,
                        help='type the name of the text file where you would'
                        ' like')
    args = parser.parse_args()
    inp = args.in_file
    outp = args.out_file
    return inp, outp


def get_sequence(file):
    with open(file, 'r') as my_file:
        for rec in SeqIO.parse(my_file, 'fasta'):
            sequence = rec.seq
        return sequence, rec


def enz_cuts(file):
    '''this function returns a dictionary where the keys are the enzymes
     and the values are their cut places in a particular sequence'''
    mybatch = Restriction.RestrictionBatch(first=[], suppliers="N")
    neb_enz = [str(m) for m in mybatch]
    sequence, record = get_sequence(file)
    mybatch = Restriction.RestrictionBatch(neb_enz)
    enz_dict = mybatch.search(sequence)
    return enz_dict


def dict_counter(enz_dict):
    l = []
    for key, value in enz_dict.items():
        lis = [len(value), key]
        l.append(lis)
    return sorted(l)


def main():
    file, new_file = parser_function()
    enz_dict = enz_cuts(file)
    l = dict_counter(enz_dict)
    with open(new_file, 'w') as f:
        f.write("ENZYM --> CUTS\n")
        for enz in l:
            if enz[0] != 0:
                f.write(str(enz[1])+' --> '+str(enz[0])+'\n')
        f.write('\n\nENZYMES WITH FEWER CUTS\n')
        for enz in l:
            if enz[0] == 1:
                f.write(str(enz[1])+' --> '+str(enz[0])+'\n')
        f.write('\n\nENZYME WITH MORE CUTS\n')
        f.write(str(l[-1][1])+' --> '+str(l[-1][0]))

if __name__ == '__main__':
    main()

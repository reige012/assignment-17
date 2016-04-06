# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Glaucia
# @Date:   2016-04-04 19:34:32
# @Last Modified by:   Glaucia
# @Last Modified time: 2016-04-05 16:32:13

"""
This code was made in partnership with Marco Rego, and I did not consider the
circular nature of mitochondrial DNA
"""


import argparse
from Bio import Seq
from Bio import Restriction
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


def arguments():
    """
    Function to parse arguments
    """
    parser = argparse.ArgumentParser(description='''Enzyme Query''')
    parser.add_argument('in_file', type=str,
                        help='type the name of the fasta file you wish to '
                             'parse')
    parser.add_argument('out_file', type=str,
                        help='type the name of the text file where you would'
                        ' like to save the output')
    args = parser.parse_args()
    inp = args.in_file
    outp = args.out_file
    return inp, outp


def open_sequences(file):
    with open(file, 'r') as my_file:
        for rec in SeqIO.parse(my_file, 'fasta'):
            sequences = rec.seq
        return sequences, rec


def enzime(file):
    '''this function returns a dictionary where the keys are the enzymes
     and the values are their cut places in a particular sequence'''
    mybatch = Restriction.RestrictionBatch(first=[], suppliers="N")
    neb_list = []
    for enz in mybatch:
        neb_list.append(str(enz))
    myseq = open_sequences(file)[0]
    mybatch = Restriction.RestrictionBatch(neb_list)
    enz_dictionary = mybatch.search(myseq)
    return enz_dictionary


def dict_counter(enz_dict):
    mylist = []
    for key, value in enz_dict.items():
        lis = [len(value), key]
        mylist.append(lis)
    ordered_list = sorted(mylist)
    return ordered_list


def main():
    file, new_file = arguments()
    enz_dictionary = enzime(file)
    l = dict_counter(enz_dictionary)
    with open(new_file, 'w') as f:
        f.write("{:10}\t--> {:4}\n".format("Enzymes", "Number of places"))
        for enz in l:
            if enz[0] != 0:
                f.write("{:10}\t--> {:4}\n".format(str(enz[1]), str(enz[0])))
        f.write('\n\nEnzymes cutting chicken mtDNA in fewest places\n')
        for enz in l:
            if enz[0] == 1:
                f.write("{:10}\t--> {:4}\n".format(str(enz[1]), str(enz[0])))
        f.write('\n\nEnzyme cutting chicken mtDNA in the largest number of places\n')
        f.write("{:10}\t--> {:4}\n".format(str(l[-1][1]), str(l[-1][0])))

if __name__ == '__main__':
    main()

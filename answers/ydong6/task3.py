#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
A17.task3
Created on Apr 5, 2016 In the task3-files directory, there is a FASTA formatted
file representing the sequence of the Gallus gallus mtDNA genome. Remembering
that this is a circular genome and assuming that NEB (New Englang Biolabs) is
the only supplier of restriction enzymes in the entire world, write a program
that uses BioPython to determine all possible restriction enzymes from NEB that
cut the chicken mtDNA sequence. Write the number of these enzymes that cut the
chicken mtDNA to a text file that also contains the name of the enzyme cutting
the chicken mtDNA sequence in the fewest places as well as the name of the
enzyme cutting the chicken mtDNA sequence in the largest number of places. Be
sure to also output the exact number(s) of cuts provided by the most and least
agressive restriction enzyme. As above, use argparse to get the input and output
file names from the user. Your program should contain a main loop and an ifmain
statement, and it should be formatted correctly. 
@author: York
'''
                                                                        
import argparse
from Bio import SeqIO
from Bio import Restriction


def parser_file_input():
    """Function takes a file as input and ask for a name for output file"""
    parser = argparse.ArgumentParser(
            description="""Input a file to use and an output file name"""
            )
    parser.add_argument(
                '--input',
                required=True,
                type=str,
                help='Enter the name of the file containing text.'
            )
    return parser.parse_args()  


def main():
    args = parser_file_input()
    with open(args.input,'r') as infile:
        record=SeqIO.read(infile,'fasta')
        print(record)
    f1 = open('restrict.fasta','w+')
    t=Restriction.RestrictionBatch(first=[],suppliers="N").search(record.seq)
    print(t)
     
  
if __name__ == '__main__':
    main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Task 1 
In the task1-files directory, there is a file named 10k-reads-
S100_L004_R1_001.fastq that contains 10,000 FASTQ reads. Write a program that
reads in the FASTQ file, reverse complements each sequence, and writes the
reverse complemented sequences out as a FASTA-formatted file. Use argparse to
get the name of the input file (the FASTQ file) and the name of some output file
name from the user. Use BioPython to read/write/convert the input and output
files. Your program should contain a main loop and an ifmain statement, and it
should be formatted correctly. @author: York
'''
                                                                         
import argparse
from Bio import SeqIO
from Bio.Alphabet import IUPAC

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
    parser.add_argument(
                '--output',
                required=True,
                type=str,
                help='Enter the name of the file containing text.'
            )
    return parser.parse_args()                                                           


def main():
    args = parser_file_input()
    count = SeqIO.convert(args.input, "fastq", "convertq.fasta", "fasta")
    print("Converted %i records" % count)
    f1 = open('convertq.fasta','r')
    f2 = open('result.fasta','w+')
    f3 = open('reverse.fasta','w+')
    
    AI_DICT = {}
    for line in f2:
        AI_DICT[line[:-1]] = 1
    print(AI_DICT)
    
    for line in f1:
        if line[0] == '>':
            _splitline = line.split('|')
            accessorIDWithArrow = _splitline[0]
            accessorID = accessorIDWithArrow[1:-1]
            print("checkID=",accessorID)
            if accessorID in AI_DICT:
                f2.write(line)
        else:
                ready_seq=f2.write(line)
                print("ready=",ready_seq)
                
    with open('reverse.fasta','r') as infile:
        for record in SeqIO.parse(infile,'fasta'):
            result=record.reverse_complement()
            result.description=record.description
            f3.write(result.format('fasta'))
            
                

  
if __name__ == '__main__':
    main()
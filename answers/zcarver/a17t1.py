#! /usr/bin/env python
# encoding UTF-8

'''
Assignment17Task1 biol7800
ZacCarver 04/05/2016
'''

import argparse
#import glob
#import os
from Bio import SeqIO
#from Bio import Seq
from Bio.SeqRecord import SeqRecord


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fastq", type=str,
                        help="provide FASTQ file")
    return parser.parse_args()


def IO(q_file):
    #allseqs = []
    with open(q_file.fastq, 'r') as q:
        with open('revcom.fasta', 'w') as a:
            for record in SeqIO.parse(q, 'fastq'):
                records = SeqRecord(seq=record.seq.reverse_complement(),
                                    id="rc_" + record.id,
                                    description="reverse complement")
                #allseqs.append(records)
                #return allseqs
                a.write(records.format('fasta'))
                #with open('revcom.fasta', 'w') as a:
                    #for records in SeqIO.parse(q, 'fastq'):
                        #a.write(record.format('fasta'))


def main():
    q_file = args()
    #q_file = glob.glob(os.path.join(arg.directory, '*.fastq'))
    IO(q_file)
    #SeqIO.write(record, 'revcom.fasta', 'fasta')
if __name__ == '__main__':
    main()

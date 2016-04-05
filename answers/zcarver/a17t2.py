#! /usr/bin/env python
# encoding UTF-8

'''
Assignment17Task2 biol7800
ZacCarver 04/05/2016
'''
import argparse
import glob
import os
from Bio import AlignIO
#from Bio import SeqIO


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--origin", type=str,
                        help="provide path to files")
    parser.add_argument("--destination", type=str,
                        help="provide path to send files")
    return parser.parse_args()


def nex_phy(origin, destination):
    for f in glob.glob(os.path.join(origin, '*.nexus')):
        if os.path.isfile(f):
            with open(f, 'r') as nex:
                p = AlignIO.read(nex, 'nexus')
                #with open(p, 'w') as phy:
                AlignIO.write(p, 'p.phylip', 'phylip-relaxed')


def main():
        arg = args()
        #map(nex_phy, arg.origin, arg.destination)
        nex_phy(arg.origin, arg.destination)
        #for filename in glob.glob(arg.origin, '*.nexus'):
            #out = nex_phy(filename)
        #in_files = glob.glob(os.path.join(arg.origin, '*.nexus'))
        #out_files = glob.glob(os.path.join(arg.destination, '*.phylip'))
            #if os.path.isfile(out):
                #shutil.copy2(out, arg.destination)
if __name__ == '__main__':
    main()

import argparse
import glob
import os
from Bio import SeqIO
from Bio.Alphabet import IUPAC


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputdir", help='directory to use', type=str)
    parser.add_argument("--outputdir", help='directory to use', type=str)
    args = parser.parse_args()
    return args


def convert(filename):
    return SeqIO.convert(filename, "nexus", filename + '.phylip', "phylip", alphabet=IUPAC.ambiguous_dna)


def main():
    args = get_parser()
    file1 = glob.glob(os.path.join(args.inputdir, "*.nexus"))
    for path, files in os.walk(file1):
        for filename in files:
            fullpath = os.path.join(path, filename)
            with open(fullpath, 'w') as f:
                convert(f)
    print(fullpath)
            
        

if __name__ == '__main__':
    main()
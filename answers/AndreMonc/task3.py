# !/usr/bin/env python
# encoding: utf-8

"""
My assignment 17 task3 program
Created by Andre Moncrieff on 4 April 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.

User must add directory path for task3 files in my answers directory. Sorry!
"""


import os
import glob
import argparse
import os.path
from Bio import SeqIO
from Bio import Restriction


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--in_path", required=True,
                        help="Enter path for the directory containing Gallus"
                        "gallus mtDNA genome FASTA formatted file",
                        type=str)
    parser.add_argument("--out_name", required=True,
                        help="Enter the name you wish for the answer output" +
                        " file",
                        type=str)
    args = parser.parse_args()
    return args


def readin(in_path):
    os.chdir(in_path)
    filename = glob.glob("*.fasta")[0]
    with open(filename, "r") as infile:
        record = SeqIO.read(infile, 'fasta')
    return record


def res_batch():
    new_eng_enz = Restriction.Restriction.RestrictionBatch(first=[],
                                                           suppliers=["N"])
    return new_eng_enz


def enzyme_cut_sites(new_eng_enzymes, record):
    enzyme_cut_sites = []
    list_of_used_enzymes = []
    for enzyme in new_eng_enzymes:
        cut_sites = enzyme.search(record.seq, linear=False)
        if cut_sites == []:
            pass
        else:
            enzyme_cut_sites.append(cut_sites)
            list_of_used_enzymes.append(str(enzyme))
    # print(enzyme_cut_sites)
    # print(len(enzyme_cut_sites))
    # print(list_of_used_enzymes)
    # print(len(list_of_used_enzymes))
    return enzyme_cut_sites, list_of_used_enzymes


def max_cuts(enz_cut_sites, list_of_used_enzymes):
    number_of_cuts = []
    for single_cut_site_list in enz_cut_sites:
        number_of_cuts.append(len(single_cut_site_list))
    maxval_cuts = max(number_of_cuts)
    max_cut_indices = [ind for ind, val in enumerate(number_of_cuts) if val == maxval_cuts]
    elongated_maxval_cuts = [maxval_cuts]*(len(max_cut_indices))
    max_cut_enzymes = []
    for index in max_cut_indices:
        max_cut_enzymes.append(list_of_used_enzymes[index])
    enz_cuts_dict_max = dict(zip(max_cut_enzymes, elongated_maxval_cuts))
    return enz_cuts_dict_max


def min_cuts(enz_cut_sites, list_of_used_enzymes):
    number_of_cuts = []
    for single_cut_site_list in enz_cut_sites:
        number_of_cuts.append(len(single_cut_site_list))
    minval_cuts = min(number_of_cuts)
    min_cut_indices = [ind for ind, val in enumerate(number_of_cuts) if val == minval_cuts]
    elongated_minval_cuts = [minval_cuts]*(len(min_cut_indices))
    min_cut_enzymes = []
    for index in min_cut_indices:
        min_cut_enzymes.append(list_of_used_enzymes[index])
    enz_cuts_dict_min = dict(zip(min_cut_enzymes, elongated_minval_cuts))
    return enz_cuts_dict_min


def write_to_new_file(enzymes, enz_cuts_dict_min, enz_cuts_dict_max):
    os.chdir("/Users/Andre/Documents/aa_LSU_Files/3_Spring_2016/Comp_Prog_for_Biologists/assignment-17/answers/AndreMonc/task3_output")
    with open("answers.txt", "w") as outfile:
        outfile.write("{}\n".format(
                      "All possible restriction enzymes" +
                      " from New England Biolabs that cut the chicken\n" +
                      "mtDNA sequence:\n"))
        counter = 1
        for item in enzymes:
            if counter % 5 == 0:
                outfile.write("{}\n".format(item))
                counter += 1
            else:
                if len(item) > 7:
                    outfile.write("{}\t\t".format(item))
                    counter += 1
                else:
                    outfile.write("{}\t\t\t".format(item))
                    counter += 1
        outfile.write("\n\n{}\n{}\n".format(
                      "The number of restriction" +
                      " enzymes from New England Biolabs that cut" +
                      " the chicken mtDNA\nsequence:", len(enzymes)))
        outfile.write("\n{}\n".format(
                      "The name of the enzymes" +
                      " cutting the chicken mtDNA sequence in the" +
                      " fewest places and \nassociated number of cuts:"))
        jubba = 1
        for e, j in enz_cuts_dict_min.items():
            if jubba % 5 == 0:
                outfile.write("{}:\t{}\n".format(e, j))
                jubba += 1
            else:
                outfile.write("{}:\t{}\t\t".format(e, j))
                jubba += 1
        outfile.write("\n{}\n".format(
                      "\nThe name of the enzymes cutting the" +
                      " chicken mtDNA sequence in the most places and\n" +
                      "associated number of cuts:"))
        for k, v in enz_cuts_dict_max.items():
            outfile.write("{}:\t{}".format(k, v))
            # print(key, values)
            # print(enz_cuts_dict_max)


def main():
    args = parser()
    record = readin(args.in_path)
    new_eng_enzymes = res_batch()
    enz_cut_sites = enzyme_cut_sites(new_eng_enzymes, record)
    # print(enz_cut_sites)
    enz_cuts_dict_max = max_cuts(enz_cut_sites[0], enz_cut_sites[1])
    # print(enz_cuts_dict_max)
    enz_cuts_dict_min = min_cuts(enz_cut_sites[0], enz_cut_sites[1])
    # print(enz_cuts_dict_min)
    write_to_new_file(enz_cut_sites[1], enz_cuts_dict_min, enz_cuts_dict_max)

if __name__ == '__main__':
    main()

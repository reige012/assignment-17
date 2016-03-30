## Task 1

In the `task1-files` directory, there is a file named `10k-reads-S100_L004_R1_001.fastq` that contains 10,000 FASTQ reads. Write a program that reads in the FASTQ file, reverse complements each sequence, and writes the reverse complemented sequences out as a FASTA-formatted file. Use `argparse` to get the name of the input file (the FASTQ file) and the name of some output file name from the user.  Use BioPython to read/write/convert the input and output files.  Your program should contain a main loop and an ifmain statement, and it should be formatted correctly.

- [ ] Program is correctly formatted [PEP8] (1.0 pt)
- [ ] Program functions as requested (4.0 pt)

## Task 2

In the `task2-files` directory, there are 10 alignments that are in NEXUS format.  Write a program that uses `glob`, `os`, and `biopython` to read these files and convert each, individual file to the PHYLIP file format. Use `argparse` to get the name of the input directory that contains the alignments and the name of some output directory where the transformed alignments will be written.  Use BioPython to read/write/convert the input and output alignments, and write the output alignments to the output directory provided by the user.  Be sure to maintain the full species name. Your program should contain a main loop and an ifmain statement, and it should be formatted correctly.

- [ ] Program is correctly formatted [PEP8] (1.0 pt)
- [ ] Program functions as requested (4.0 pt)

## Task 3

In the `task3-files` directory, there is a FASTA formatted file representing the sequence of the _Gallus gallus_ mtDNA genome.  Remembering that this is a circular genome and assuming that NEB (New Englang Biolabs) is the only supplier of restriction enzymes in the entire world, write a program that uses BioPython to determine all possible restriction enzymes from NEB that cut the chicken mtDNA sequence.  Write the number of these enzymes that cut the chicken mtDNA to a text file that also contains the name of the enzyme cutting the chicken mtDNA sequence in the fewest places as well as the name of the enzyme cutting the chicken mtDNA sequence in the largest number of places.  Be sure to also output the exact number(s) of cuts provided by the most and least agressive restriction enzyme.  As above, use `argparse` to get the input and output file names from the user. Your program should contain a main loop and an ifmain statement, and it should be formatted correctly.

- [ ] Program is correctly formatted [PEP8] (1.0 pt)
- [ ] Program functions as requested (4.0 pt)

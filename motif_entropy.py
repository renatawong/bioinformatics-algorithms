'''
(C) Renata Wong

This code calculates the entropy of a set of motifs.

The file to be read consists of 1 line:
Line 1: motif1 motif2 motif3 ...

If no file is specified, 'Motif_entropy.txt' is loaded by default.
'''

import sys
import math





def motif_entropy(motifs):
    
    entropy = 0.0
    num_motifs = len(motifs)
    prob_distr = [[0.0] * len(motifs[0]) for i in range(4)]
    # each row = list storing probability distributions of A, C, G, and T, resp.
    single_prob = 1 / num_motifs

    for motif in motifs:
        for column, base in enumerate(motif):
            if base == 'A':
                prob_distr[0][column] += single_prob
            if base == 'C':
                prob_distr[1][column] += single_prob
            if base == 'G':
                prob_distr[2][column] += single_prob
            if base == 'T':
                prob_distr[3][column] += single_prob
    
    for row in prob_distr:
        for column, value in enumerate(row):
            if value != 0.0:
                entropy += (-1) * value * math.log2(value)

    return entropy




def compute(f):
    motifs = [motif for motif in map(str, f.readline().split())]

    entropy = motif_entropy(motifs)
    print('ENTROPY =', entropy) 

    f.close()



#
# The following code is only for running through the command line interface
#

if __name__ == "__main__":
    def print_usage():
        print("Usage:\n", file=sys.stderr)
        print("python ./moftif_entropy.py [file_name.txt]", file=sys.stderr)

    # For execution from IDE
    if len(sys.argv) == 1:
        with open('Motif_entropy.txt', 'r') as genome_file:
            compute(genome_file)

    # For execution from terminal
    elif len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as genome_file:
            compute(genome_file)

    
    if len(sys.argv) > 2:
        print_usage()
 
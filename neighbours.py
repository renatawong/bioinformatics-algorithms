
'''
(C) Renata Wong

Algorithm for generating the set of all k-mers whose Hamming distance from pattern does not exceed d.

The file to be read consists of 2 lines:
Line 1: Nucleotide sequence
Line 2: d

If no file is specified, the default file Neighbours.txt is loaded.
'''

import sys


NUCLEOTIDES = ['A', 'T', 'G', 'C']


def hamming_distance(p, q):

    hamming_distance = 0

    for p_i, q_i in zip(p, q):
        if p_i != q_i:
            hamming_distance += 1

    return hamming_distance




def get_suffix(pattern):

    return pattern[1:]





def get_neighbours(pattern, d):

    if d == 0:
        return {pattern}
    if len(pattern) == 1: 
        return {'A', 'C', 'G', 'T'}
    
    neighbourhood = set()
    
    suffix_neighbors = get_neighbours(get_suffix(pattern), d)

    for suffix in suffix_neighbors:
        if hamming_distance(get_suffix(pattern), suffix) < d:
            for base in NUCLEOTIDES:
                neighbourhood.add(base+suffix)
        else:
            neighbourhood.add(pattern[0]+suffix)
        
    return neighbourhood





def compute(f):
    kmer = f.readline().strip()
    d = int(f.readline().strip())

    neighbours = get_neighbours(kmer, d)
    print(*neighbours)

    f.close()



#
# The following code is only for running through the command line interface
#

if __name__ == "__main__":
    def print_usage():
        print("Usage:\n", file=sys.stderr)
        print("python ./neighbours.py [file_name.txt]", file=sys.stderr)

    if len(sys.argv) > 2:
        print_usage()
    
    # Run from IDE
    if len(sys.argv) == 1:
        with open('Neighbours.txt', 'r') as genome_file:
            compute(genome_file)

    # Run form terminal
    elif len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as genome_file:
            compute(genome_file)

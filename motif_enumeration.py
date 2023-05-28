'''
(C) Renata Wong

This code finds all (k,d)-motifs in all given DNA sequences. 
(k,d)-motifs are k-mers with a distance of at most d.
The hope is that these motifs correspond to regulatory motifs used by regulatory proteins to bind to in order to control
the expression of different genes (circadian activity). 

This is a brute-force method. 

The file to be read consists of 2 lines:
Line 1: k d
Line 2: sequence1 sequence2 sequence3 ...

If no file is specified, 'Motifs.txt' is loaded by default.
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



def motif_enumeration(sequences, k, d):

    kmer_list = [set() for _ in sequences] 
    
    for index, seq in enumerate(sequences):
        for k_pos in range(len(seq) - k + 1):
            # Generate neighbors for each kmer in a sequence
            kmer = seq[k_pos : k_pos + k]
            kmer_list[index].update(get_neighbours(kmer, d))
    
    motifs = kmer_list[0]
    
    for k_set in kmer_list[1:len(kmer_list)]:
        # Take the intersection of all sets
        motifs = motifs.intersection(k_set)      # the result of intersection() must be stored in a new object. 

    return motifs




def compute(f):
    k, d = map(int, f.readline().split())
    sequences = [seq for seq in map(str, f.readline().split())]

    motifs = motif_enumeration(sequences, k, d)
    print('({},{})-motifs found in all sequences: '.format(k, d)) 
    print(*motifs)

    f.close()



#
# The following code is only for running through the command line interface
#

if __name__ == "__main__":
    def print_usage():
        print("Usage:\n", file=sys.stderr)
        print("python ./moftif_enumeration.py [file_name.txt]", file=sys.stderr)

    # For execution from IDE
    if len(sys.argv) == 1:
        with open('Motifs.txt', 'r') as genome_file:
            compute(genome_file)

    # For execution from terminal
    elif len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as genome_file:
            compute(genome_file)

    
    if len(sys.argv) > 2:
        print_usage()
 
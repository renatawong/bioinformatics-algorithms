'''
(C) Renata Wong

This code finds the most probable k-mer in a sequence given a profile matrix.
A profile matrix consists has dimensions 4 x k, where the rows represent the four nucleotides: A, C, G, T.
Its entries are the probabilities of occurrence of that nucleotide in a given set of sequences at the 
particular position. 

The file to be read consists of 6 lines:
Line 1: sequence
Line 2: k
Lines 3-6: probabilities of observing A, C, G, T in a particular location in a previously established 
set of sequences.

If no file is specified, 'Most_probable_kmer.txt' is loaded by default.
'''


import sys







def find_most_probable_kmer(sequence, k, profile_matrix):

    # generate a list of all k-mers in sequence
    kmer_list = [sequence[i:i+k] for i in range(len(sequence)-k)]

    kmer_probabilities = [1.0] * len(kmer_list)
    
    # calculate probabilities for each k-mer in kmer_list
    for idx1, kmer in enumerate(kmer_list):
        
        for idx2, base in enumerate(kmer):

            if base == 'A':
                kmer_probabilities[idx1] *= profile_matrix[0][idx2]
            if base == 'C':
                kmer_probabilities[idx1] *= profile_matrix[1][idx2]
            if base == 'G':
                kmer_probabilities[idx1] *= profile_matrix[2][idx2]
            if base == 'T':
                kmer_probabilities[idx1] *= profile_matrix[3][idx2]

    # store most probable k-mers in most_probable_kmers
    most_probable_kmers = [kmer for kmer, prob in zip(kmer_list, kmer_probabilities) 
                           if prob == max(kmer_probabilities)]

    return most_probable_kmers




def compute(f):
    sequence = f.readline()
    k = int(f.readline())
    lines = [line.strip() for line in f]
    
    profile_matrix = [list(map(float, line.split(' '))) for line in lines]

    print(profile_matrix)

    most_probable_kmer = find_most_probable_kmer(sequence, k, profile_matrix)
    print('The most probable k-mer is', *most_probable_kmer) 

    f.close()



#
# The following code is only for running through the command line interface
#

if __name__ == "__main__":
    def print_usage():
        print("Usage:\n", file=sys.stderr)
        print("python ./profile_most_probable_kmer.py [file_name.txt]", file=sys.stderr)

    # For execution from IDE
    if len(sys.argv) == 1:
        with open('Most_probable_kmer.txt', 'r') as genome_file:
            compute(genome_file)

    # For execution from terminal
    elif len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as genome_file:
            compute(genome_file)

    
    if len(sys.argv) > 2:
        print_usage()
 
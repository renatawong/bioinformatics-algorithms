'''
(C) Renata Wong

This code finds a collection of best motifs given a set of sequences, and k-mer length.

The file to be read consists of 2 lines:
Line 1: k t
Line 2: sequences separated by spaces

If no file is specified, 'Greedy_motifs.txt' is loaded by default.
'''


import sys



def find_consensus(motifs):
    
    motif_length = len(motifs[0])
    bases = []

    for j in range(motif_length):
        bases.append([motifs[i][j] for i in range(len(motifs))])
    
    max_items = []
    for i in range(motif_length):
        max_items.append(max(bases[i],key=bases[i].count))
    
    consensus = ''.join(max_items)
    
    return consensus




def hamming_distance(p, q):

    hamming_distance = 0

    for p_i, q_i in zip(p, q):
        if p_i != q_i:
            hamming_distance += 1

    return hamming_distance




def score(motifs):
    consensus = find_consensus(motifs)
    score = 0
    for motif in motifs:
        score += hamming_distance(consensus, motif)
    return score




def generate_profile_matrix(motifs):

    # if calcuating with pseudocounts, initialize with 1.0, otherwise with 0.0
    profile_matrix = [[1.0] * len(motifs[0]) for i in range(4)]

    single_prob = 1 / len(motifs)

    for motif in motifs:
        for column, base in enumerate(motif):
            if base == 'A':
                profile_matrix[0][column] += single_prob
            if base == 'C':
                profile_matrix[1][column] += single_prob
            if base == 'G':
                profile_matrix[2][column] += single_prob
            if base == 'T':
                profile_matrix[3][column] += single_prob
    
    return profile_matrix



def greedy_motif_search(k, t, sequences):

    # create motif matrix from the first k-mer in each sequence
    best_motifs = []
    for strand in sequences:
       best_motifs.append(strand[ : k])
       
    # treat the first sequence as the base strand
    base_strand_kmers = [sequences[0][i:i+k] for i in range(len(sequences[0])-k+1)]
    other_strands = sequences[1 : t]

    # generate profile_matrix for each case where the first k-mer is replaced in each step
    # by one of the k-mers in the first sequence
    for kmer in base_strand_kmers:
        
        motifs = [kmer]
        
        for strand in other_strands:
            profile_matrix = generate_profile_matrix(motifs)
            # we want only one k-mer as the next_motif
            next_motif = find_most_probable_kmer(strand, k, profile_matrix)
            motifs.append(next_motif)
        
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    
    return best_motifs




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

    return most_probable_kmers[0]




def compute(f):
    
    k, t = map(int, f.readline().split())
    sequences = f.readline().split()

    best_motifs = greedy_motif_search(k, t, sequences)
    print('The best motifs found')
    print(*best_motifs) 

    f.close()



#
# The following code is only for running through the command line interface
#

if __name__ == "__main__":
    def print_usage():
        print("Usage:\n", file=sys.stderr)
        print("python ./greedy_motif_search.py [file_name.txt]", file=sys.stderr)

    # For execution from IDE
    if len(sys.argv) == 1:
        with open('Greedy_motifs.txt', 'r') as genome_file:
            compute(genome_file)

    # For execution from terminal
    elif len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as genome_file:
            compute(genome_file)

    
    if len(sys.argv) > 2:
        print_usage()
 
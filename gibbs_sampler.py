'''
(C) Renata Wong

This code finds a collection of best motifs given a set of sequences, and k-mer length. 
Gibbs Sampler is a modification of randomized motif search. 
Unlike the latter, it exchanges only one k-mer in each iteration at random. 

The file to be read consists of 2 lines:
Line 1: k t N 
Line 2: sequences separated by spaces
* k = length of k-mer, t = number of sequences, N = number of repeated runs of the algorithm

If no file is specified, 'Gibbs_sampler.txt' is loaded by default.

'''


import sys
import random



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

    # we are calculating with pseudocount, i.e. each base count is incremented by 1
    single_prob = 1 / (len(motifs) + 4)
    profile_matrix = [[single_prob] * len(motifs[0]) for i in range(4)]

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





def get_random_substring(sequence, k):
    idx = random.randrange(0, len(sequence) - k + 1)    
    return sequence[idx : (idx+k)]




def gibbs_sampler(k, t, N, sequences):

    # create motif matrix from randomly selected k-mers, each k-mer from a different sequence
    best_motifs, motifs = [], []

    for strand in sequences:
       motifs.append(get_random_substring(strand, k))

    best_motifs = motifs.copy() 

    for j in range(N):
        # select a random sequence i from the t sequences and the corresponding motif i in motifs
        random_idx = random.randrange(t)
        
        # generate profile matrix for all motifs except the motif at random_idx in motifs
        del motifs[random_idx]
        profile_matrix = generate_profile_matrix(motifs)

        # select the best motif from sequence at random_idx in sequences
        motif_i = find_best_random_kmer(sequences[random_idx], k, profile_matrix)
        
        motifs.insert(random_idx, motif_i)
        
        if score(motifs) < score(best_motifs):
            best_motifs = motifs

    return best_motifs






def find_best_random_kmer(sequence, k, profile_matrix):

    # generate a list of all k-mers in a sequence
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
    most_probable_kmers = random.choices(kmer_list, weights = kmer_probabilities, k = 1)

    return most_probable_kmers[0]





def repeated_gibbs_sampler(k, t, N, sequences):
    best_score = float('inf')
    best_motifs = []
    for i in range(50):
        motifs = gibbs_sampler(k, t, N, sequences)
        current_score = score(motifs)
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs
    print('Best score', best_score)
    return best_motifs



def compute(f):
    
    k, t, N = map(int, f.readline().split())
    sequences = f.readline().split()
    
    best_motifs = repeated_gibbs_sampler(k, t, N, sequences)
    print('The best motifs found')
    print(*best_motifs) 

    f.close()



#
# The following code is only for running through the command line interface
#

if __name__ == "__main__":
    def print_usage():
        print("Usage:\n", file=sys.stderr)
        print("python ./gibbs_sampler.py [file_name.txt]", file=sys.stderr)

    # For execution from IDE
    if len(sys.argv) == 1:
        with open('Gibbs_sampler.txt', 'r') as genome_file:
            compute(genome_file)

    # For execution from terminal
    elif len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as genome_file:
            compute(genome_file)

    
    if len(sys.argv) > 2:
        print_usage()
 
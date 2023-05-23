'''
(C) Renata Wong

Algorithm for finding patterns of length k (k-mers) that occur most frequently in a genome. 
The k-mers are allowed to have a mismatch of magnitude d (Hamming distance). 
Reverse complements and their mismatches are included as well.

The output consists of all k-mers with the highest sum of counts:
max (count(pattern) + count(reverse_complement))

The file to be read consists of 2 lines:
Line 1: Nucleotide sequence
Line 2: k (length k of k-mer) d (Hamming distance measure for level of mismatch)
'''

import sys
from itertools import product




def hamming_distance(p, q):

    hamming_distance = 0

    for p_i, q_i in zip(p, q):
        if p_i != q_i:
            hamming_distance += 1


    return hamming_distance




def approximate_pattern_matching(kmer, genome, d):

    count = 0

    for i in range(len(genome) - len(kmer)+1):
        if hamming_distance(kmer, genome[i : len(kmer)+i]) <= d:
            #kmers.append(i)
            count += 1

    return count






def reverse_complement(text):

    complement = text[::-1]

    reverse_complement = ''

    for char in complement:
        if char == 'A':
            reverse_complement += 'T'
        if char == 'T':
            reverse_complement += 'A'
        if char == 'C':
            reverse_complement += 'G'
        if char == 'G':
            reverse_complement += 'C'

    return reverse_complement





def frequent_kmers_with_mismatches(genome, k, d):
    
    bases = ['A', 'C', 'G', 'T']
    base_combinations = [''.join(base) for base in product(bases, repeat = k)]
    freq_kmers = {}

    for pattern in base_combinations:
        count = approximate_pattern_matching(pattern, genome, d)

        if count not in freq_kmers:
            freq_kmers[count] = [pattern]
        else:
            freq_kmers[count].append(pattern)

        
        # Consider reverse complement of the pattern.
        # Do not add the reverse complement of the pattern to a list.
        # Rather increase the count of occurrences for the pattern itself. 
        rev_complement = reverse_complement(pattern)
        count_rev = approximate_pattern_matching(rev_complement, genome, d)

        # Increase the key value of pattern by count_rev
        update_count = count + count_rev

        # Store the pattern under the new key
        if update_count not in freq_kmers:
            freq_kmers[update_count] = [pattern]
        else:
            freq_kmers[update_count].append(pattern)

    # Output the patterns with highest counts.
    # The count for each pattern include the count for that pattern and its reverse compleemnt.
    return freq_kmers[max(freq_kmers)]




def compute(f):
    genome = f.readline().strip()
    k, d = map(int, f.readline().split())

    kmer_list = frequent_kmers_with_mismatches(genome, k, d)
    print(*kmer_list)

    f.close()



#
# The following code is only for running through the command line interface
#

if __name__ == "__main__":
    def print_usage():
        print("Usage:\n", file=sys.stderr)
        print("python ./frequent_kmers_with_mismatch.py [file_name.txt]", file=sys.stderr)

    if len(sys.argv) > 2:
        print_usage()
    
    # Run from IDE
    if len(sys.argv) == 1:
        with open('Frequent_patterns_with_mismatch.txt', 'r') as genome_file:
            compute(genome_file)

    # Run form terminal
    elif len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as genome_file:
            compute(genome_file)

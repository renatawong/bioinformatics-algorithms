'''
(C) Renata Wong

This code finds a k-mer that minimizes distance(kmer, dna_string) among all possible choices of k-mers.

The file to be read consists of 2 lines:
Line 1: k
Line 2: DNA strings separated by a space

If no file is specified, 'Median_strings.txt' is loaded by default.

This is a brute force method. 
'''

import sys





def calculate_hamming_distance(p, q):

    hamming_distance = 0

    for p_i, q_i in zip(p, q):
        if p_i != q_i:
            hamming_distance += 1


    return hamming_distance




def median_string(k, dna_strings):

    # iterate through each DNA string
    kmerList = []
    for dna in dna_strings:
        for i in range(len(dna) - k+1):
            pattern = dna[i:i+k]
            if pattern not in kmerList:
                kmerList.append(pattern)
        
        # pattern that minimizes hamming distance
        distance = float('inf')
        for kmer in kmerList:
            for i in range(len(dna) - k+1):
                temp_dist = calculate_hamming_distance(kmer, dna[i:i+k])
                if distance > temp_dist:
                    distance = temp_dist
                    median = kmer
    return median




def compute(f):
    k = int(f.readline())
    dna_strings = [dna_string for dna_string in map(str, f.readline().split())]

    median_kmers = median_string(k, dna_strings)
    print('K-mers found =', median_kmers) 

    f.close()



#
# The following code is only for running through the command line interface
#

if __name__ == "__main__":
    def print_usage():
        print("Usage:\n", file=sys.stderr)
        print("python ./median_string_problem.py [file_name.txt]", file=sys.stderr)

    # For execution from IDE
    if len(sys.argv) == 1:
        with open('Median_strings.txt', 'r') as genome_file:
            compute(genome_file)

    # For execution from terminal
    elif len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as genome_file:
            compute(genome_file)

    
    if len(sys.argv) > 2:
        print_usage()
 
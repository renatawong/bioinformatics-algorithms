'''
(C) Renata Wong

This code calculates the Hamming distance between two DNA strands. 

The file to be read consists of two lines:
Line 1: k-mer, e.g. 'TGC'
Line 2: DNA sequence
Line 3: d (maximum allowed distance)

If no file is specified, the file Approx_matching.txt is used for calculation. 
'''


import sys



def hamming_distance(p, q):

    hamming_distance = 0

    for p_i, q_i in zip(p, q):
        if p_i != q_i:
            hamming_distance += 1


    return hamming_distance




def approximate_pattern_matching(pattern, genome, d):

    indices = []
    total_count = 0

    for i in range(len(genome) - len(pattern)+1):
        if hamming_distance(pattern, genome[i : len(pattern)+i]) <= d:
            indices.append(i)
            total_count += 1


    return indices, total_count







def compute(f):

    kmer = f.readline().strip()
    genome = f.readline().strip()
    distance = int(f.readline().strip())

    matched_pattern_indices, total_count = approximate_pattern_matching(kmer, genome, distance)
    print("Indices of approximate pattern matchis with distance at most {}:".format(distance))
    print(*matched_pattern_indices)
    print('Number of occurrences of {} with the given Hamming distance: {}'.format(kmer, total_count))  
    
    f.close()



#
# The following code is only for running through the command line interface
#

if __name__ == "__main__":
    def print_usage():
        print("Usage:\n", file=sys.stderr)
        print("python ./find_kmer_clumps.py [file_name.txt]", file=sys.stderr)

    # For execution from IDE
    if len(sys.argv) == 1:
        with open('Approx_matching.txt', 'r') as genome_file:
            compute(genome_file)

    # For execution from terminal
    elif len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as genome_file:
            compute(genome_file)

    
    if len(sys.argv) > 2:
        print_usage()
 
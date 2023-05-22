'''
(C) Renata Wong

This code calculates the Hamming distance between two DNA strands. 

The file to be read consists of two lines:
Line 1: DNA sequence 1
Line 2: DNA sequence 2

If no file is specified, the file Hamming_distance.txt is used for calculation. 
'''


import sys




def calculate_hamming_distance(p, q):

    hamming_distance = 0

    for p_i, q_i in zip(p, q):
        if p_i != q_i:
            hamming_distance += 1


    return hamming_distance







def compute(f):

    strand_1 = f.readline().strip()
    strand_2 = f.readline().strip()

    hamming_distance = calculate_hamming_distance(strand_1, strand_2)
    print("Hamming distance =", hamming_distance)
    
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
        with open('Hammming_distance.txt', 'r') as genome_file:
            compute(genome_file)

    # For execution from terminal
    elif len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as genome_file:
            compute(genome_file)

    
    if len(sys.argv) > 2:
        print_usage()
 
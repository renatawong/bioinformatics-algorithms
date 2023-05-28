'''
(C) Renata Wong

This code finds all (k,d)-motifs in all given DNA sequences. 
(k,d)-motifs are k-mers with a distance of at most d.
The hope is that these motifs correspond to regulatory motifs used by regulatory proteins to bind to in order to control
the expression of different genes (circadian activity). 

This is a brute-force method. 

The file to be read consists of 2 lines:
Line 1: genome sequence
Line 2: k-mer
Example: Vibrio_cholerae.txt, the DNA sequence of the bacteria that couses cholera.
'''

import sys



def motif_enumeration(sequences, k, d):
    kmer_list = [set(s) for s in sequences] # Creating a list of sets
    
    for index, seq in enumerate(sequences):
        for k_pos in range(len(seq) - k + 1):
            # Generate neighbors for all kmers in all strings and

            # add them to a set() in a kmer_list
    
    motifs = kmer_list[0]
    #for k_set in kmer_list:
        # Use 'AND' on a Python set() to ONLY get kmers from all sets
        # that are in all sets we generated above

    return motifs




def compute(f):
    k, d = map(int, f.readline().split())
    sequences = [seq for seq in map(str, f.readline().split())]
    print(sequences)

    motifs = motif_enumeration(sequences, k, d)
    print('({},{})-motifs found: '.format(k, d)) 
    print(motifs)

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
        with open('Vibrio_cholerae.txt', 'r') as genome_file:
            compute(genome_file)

    # For execution from terminal
    elif len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as genome_file:
            compute(genome_file)

    
    if len(sys.argv) > 2:
        print_usage()
 
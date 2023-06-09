'''
(C) Renata Wong

Algorithm for finding patterns of length k (k-mers) that occur most frequently in a genome.

The file to be read consists of 2 lines:
Line 1: Nucleotide sequence
Line 2: length k of k-mer
'''

import sys


def frequency_table(text, k):

    freq_map = {}
    n = len(text)
    
    for i in range(n - k):
        pattern = text[i : k+i]
        if freq_map.get(pattern) == None:
            freq_map[pattern] = 1
            
        else:
            freq_map[pattern] += 1

    return freq_map



def find_frequent_patterns(text, k):

    freq_map = frequency_table(text, k)
    max_count = max(freq_map.values())

    frequent_patterns = [pattern for pattern in freq_map.keys() if freq_map[pattern] == max_count]
    
    return frequent_patterns




def compute(f):
    text = f.readline().strip()
    pattern_length = int(f.readline().strip())

    pattern_list = find_frequent_patterns(text, pattern_length)
    print(*pattern_list)

    f.close()



#
# The following code is only for running through the command line interface
#

if __name__ == "__main__":
    def print_usage():
        print("Usage:\n", file=sys.stderr)
        print("python ./frequent_kmers.py [file_name.txt]", file=sys.stderr)

    if len(sys.argv) > 2:
        print_usage()
    
    # Run from IDE
    if len(sys.argv) == 1:
        with open('Frequent_patterns.txt', 'r') as genome_file:
            compute(genome_file)

    # Run form terminal
    elif len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as genome_file:
            compute(genome_file)

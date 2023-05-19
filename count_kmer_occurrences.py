'''
(C) Renata Wong

This code counts occurrences of a k-mer in a given genome sequence. 

The file to be read consists of 2 lines:
Line 1: genome sequence
Line 2: k-mer
Example: Vibrio_cholerae.txt, the DNA sequence of the bacteria that couses cholera.
'''

import sys



def pattern_count(text, pattern):
    count = 0
    for i in range(len(text)-len(pattern)):
        if text[i : len(pattern)+i] == pattern:
            count += 1
    return count





#
# The following code is only for running through the command line interface
#

if __name__ == "__main__":
    def print_usage():
        print("Usage:\n", file=sys.stderr)
        print("python ./count_kmer_occurrences.py [file_name.txt]", file=sys.stderr)

    if len(sys.argv) > 2:
        print_usage()
    
    with open(sys.argv[1], 'r') as genome_file:
        text = genome_file.readline().strip()
        pattern = genome_file.readline().strip()

        count = pattern_count(text, pattern)
        print('Number of occurrences of {}-mer {} :  {}'.format(len(pattern), pattern, count))

        genome_file.close()


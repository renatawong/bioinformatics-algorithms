'''
(C) Renata Wong

This code generates the list of indices in a genome that indicate the start of the k-mer. 

The file to be read consists of 2 lines:
Line 1: k-mer, e.g. ACT
Line 2: genome sequence

'''


import sys
import re


def match_kmer_to_genome(pattern, text):

    index_list = [m.start() for m in re.finditer('(?={0})'.format(re.escape(pattern)), text)]

    return index_list



def compute(f):
    pattern = f.readline().strip()
    text = f.readline().strip()

    index_list = match_kmer_to_genome(pattern, text)
    print(*index_list)

    f.close()



#
# The following code is only for running through the command line interface
#

if __name__ == "__main__":
    def print_usage():
        print("Usage:\n", file=sys.stderr)
        print("python ./kmer_genome_match.py [file_name.txt]", file=sys.stderr)

    # For execution from IDE
    if len(sys.argv) == 1:
        with open('Kmer_genome_match.txt', 'r') as genome_file:
            compute(genome_file)

    # For execution from terminal
    elif len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as genome_file:
            compute(genome_file)

    
    if len(sys.argv) > 2:
        print_usage()
 
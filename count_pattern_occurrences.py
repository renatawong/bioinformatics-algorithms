'''
(C) Renata Wong

This code counts occurrences of a DNA pattern in a given DNA sequence. 
This script can be executed either from the terminal or in an editor.

The file to be read consists of 2 lines:
Line 1: DNA sequence
Line 2: DNA pattern
Example: Vibrio_cholerae.txt, the DNA sequence of the bacteria that couses cholera.
'''

import sys

dna_file = open('Vibrio_cholerae.txt', 'r')
text = dna_file.readline().strip()
pattern = dna_file.readline().strip()

def pattern_count(text, pattern):
    count = 0
    for i in range(len(text)-len(pattern)):
        if text[i : len(pattern)+i] == pattern:
            count += 1
    return count

count = pattern_count(text, pattern)
print('Number of pattern occurrences:', count)

dna_file.close()



#
# The following code is only for running through the command line interface
#

if __name__ == "__main__":
    def print_usage():
        print("Usage:\n", file=sys.stderr)
        print("python count_pattern_occurrences.py [file_name.txt]", file=sys.stderr)

    if len(sys.argv) > 2:
        print_usage()
    with open(sys.argv[0]) as f:
        text = f.readline()
        pattern = f.readline()

        count = pattern_count(text, pattern)


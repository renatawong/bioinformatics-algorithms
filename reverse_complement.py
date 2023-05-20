'''
(C) Renata Wong

This code generates the reverse complement of a DNA segment. 

The file to be read consists of 1 single line:
Line 1: genome sequence

'''


import sys


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



def compute(f):
    text = f.readline().strip()

    print(reverse_complement(text))

    f.close()



#
# The following code is only for running through the command line interface
#

if __name__ == "__main__":
    def print_usage():
        print("Usage:\n", file=sys.stderr)
        print("python ./reverse_complement.py [file_name.txt]", file=sys.stderr)

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
 
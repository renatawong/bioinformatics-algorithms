'''
(C) Renata Wong

This code finds the point(s) for which #G - #C is minimal within a genome. 
This minimum could be the original of replication of the genome. 

The file to be read consists of a single line:
Line 1: genome sequence

If no file is specified, the file Vibrio_cholerae.txt is used for calculation. 
It contains the genome of the bacteria causing cholera.

NOTE: Positions are counted from 1 on, not from 0. 
'''


import sys




def find_minimum_skew_position(text):

    skew, minimum_skew = 0, 0
    skew_list = []

    for index, nucleotide in enumerate(text):

        if nucleotide == 'C':
            skew -= 1
        if nucleotide == 'G':
            skew += 1
        
        if minimum_skew > skew or minimum_skew == skew:
            minimum_skew = skew
            skew_list.append((minimum_skew, index+1))

    return minimum_skew, [element[1] for index, element in enumerate(skew_list) 
                      if minimum_skew == element[0]]







def compute(f):

    text = f.readline().strip()

    minimum_skew, min_skew_positions = find_minimum_skew_position(text)
    print("Positions of minimum skew {} are".format(minimum_skew))
    print(*min_skew_positions)

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
        with open('Vibrio_cholerae.txt', 'r') as genome_file:
            compute(genome_file)

    # For execution from terminal
    elif len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as genome_file:
            compute(genome_file)

    
    if len(sys.argv) > 2:
        print_usage()
 
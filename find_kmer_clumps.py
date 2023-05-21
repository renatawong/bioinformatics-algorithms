'''
(C) Renata Wong

This code finds all k-mers that occur t times within a window of length L. 

The file to be read consists of 2 lines:
Line 1: genome sequence
Line 2: k [space] L [space] t

If no file is specified, the file E-coli_kmer_clumps.txt is used for calculation. 
It contains the genome of E.coli.
'''


import sys




def find_kmer_clumps(text, k, L, t):

    # Building a dictionary over all possible k-mers and list of their indices
    kmer_dict = {}
    
    for index, _ in enumerate(text):
        
        pattern = text[index : k+index]

        # create new key and value if key not present in the dictionary
        if pattern not in kmer_dict:
            kmer_dict.update({pattern : []})
        
        # update the value by appending elements to it
        kmer_dict[pattern].append(index)
 

    kmer_set = set()

    for key, index_list in kmer_dict.items():
        
        for i in range(len(index_list) - t+1):

            if (index_list[i+t-1] + k) - index_list[i] < L + 1:
                
                kmer_set.add(key)


    return kmer_set






def compute(f):

    text = f.readline().strip()
    k, L, t = map(int, f.readline().split())

    kmer_list = find_kmer_clumps(text, k, L, t)
    print('Number of k-mers', len(kmer_list))
    print('Different k-mers', *kmer_list)

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
        with open('E-coli_kmer_clumps.txt', 'r') as genome_file:
            compute(genome_file)

    # For execution from terminal
    elif len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as genome_file:
            compute(genome_file)

    
    if len(sys.argv) > 2:
        print_usage()
 
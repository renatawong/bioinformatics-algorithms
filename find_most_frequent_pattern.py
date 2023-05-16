'''
(C) Renata Wong

Algorithm for finding the DNA patterns of length k that occur most frequently in a DNA sequence.

The file to be read consists of 2 lines:
Line 1: DNA sequence
Line 2: length k
'''

import sys
import numpy as np


dna_file = open('Frequent_patterns.txt', 'r')
text = dna_file.readline().strip()
pattern_length = int(dna_file.readline().strip())


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

pattern_list = find_frequent_patterns(text, pattern_length)
print(*pattern_list)

dna_file.close()
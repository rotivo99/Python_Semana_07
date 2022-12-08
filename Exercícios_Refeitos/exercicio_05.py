#!/usr/bin/env python3

import re

dictionary = {}
dictionary[item] = []

with open('Python_07.fasta', 'r') as seq_read:
    for line in seq_read:
        if line[0] == '>':
            item = line.rstrip()
        else:
            dictionary[item] = dictionary[item].extend(line)
print(dictionary)

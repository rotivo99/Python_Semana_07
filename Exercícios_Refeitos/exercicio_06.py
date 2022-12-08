#!/usr/bin/env python3

import re

with open('Python_07_ApoI.fasta', 'r') as apoI_read:
    for line in re.finditer(r'([AG]AATT[TC])', apoI_read):
        print(f'The site R^AATTY is present in the informed sequence and starts at nucleotide {line.start()} and ends at nucleotide {line.end()}')


#ith open('Python_07_ApoI.fasta', 'r') as apoI_read:
#    for line in apoI_read:
#        for nt in re.finditer(r'([AG]AATT[TC])', line)
#            print(f'The site R^AATTY is present in the informed sequence and starts at nucleotide {nt.start()} and ends at nucleotide {nt.end()}')

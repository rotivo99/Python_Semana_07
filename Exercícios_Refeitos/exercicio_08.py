#!/usr/bin/env python3

import re
cut_seq_list = []

with open('Python_07_ApoI.fasta', 'r') as apoI_read:
    for line in apoI_read:
        substitution = re.sub(r'([GA])(AATT[CT])', r'\1^\2', line)
        if line[0] != '>':
            cut_seq_list += substitution.rstrip().split('^')
print(sorted(cut_seq_list, key=len))

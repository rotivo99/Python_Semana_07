#!/usr/bin/env python3

import re

line_count = 0

with open('Python_07.fasta', 'r') as fasta_read:
    for line in fasta_read:
        line_count += 1
        finding = re.findall(r'>', line)
        if finding != []:
            print(f'Line {line_count} is a header: {line}'.rstrip())

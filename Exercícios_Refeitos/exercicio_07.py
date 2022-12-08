#!/usr/bin/env python3

import re

with open('Python_07_ApoI.fasta', 'r') as apoI_read:
    for line in apoI_read:
        substitution = re.sub(r'([GA])(AATT[CT])', r'\1^\2', line)
        print(substitution.rstrip())

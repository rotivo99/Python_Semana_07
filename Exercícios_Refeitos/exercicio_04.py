#!/usr/bin/env python3

import re

line_count = 0

with open('Python_07.fasta', 'r') as fasta_read:
    for line in fasta_read:
        line_count += 1
        if line[0] == '>':
#            finding = re.findall(r'(^\S*$)', line)
#            finding = re.findall(r'(>.{30,32})', line)
            for i in re.finditer('((^>.{23,30})\s(.{30}))', line):
                print(f'{i.group(0)}\t{i.group(1)}')


#for i in re.finditer('(nobody) (\w+s)', line2):                                                                                                                             print(f'{count_line}\t{i.group(1)}\t{i.start(1) + 1 }\t{i.end(1)}\t{line}')      
                  #  for i in re.finditer('(nobody) (\w+s)', line2):
#            finding = re.findall(r'(>.{30,32})', line)
#            try:
#                finding = re.search(r'(.{30})\s(.{50})', line)
#                print(finding.group(0))
#            except AttributeError:
#                print('')

#( r"(.{50})TATTAT(.{25})"
#       if finding != []:
#            print(f'Line {line_count} is a header: {line}'.rstrip())

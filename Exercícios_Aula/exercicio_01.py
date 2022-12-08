#!/usr/bin/env python3

import re

texto = 'Nobody by Shel Silverstein                                                                                                                                                                                                                                                                                                                      Nobody loves me,                                                                                                                                                        Nobody cares,                                                                                                                                                           Nobody picks me peaches and pears.                                                                                                                                      Nobody offers me candy and Cokes,                                                                                                                                       Nobody listens and laughs at me jokes.'

variavel = re.findall('Nobody', texto)
print(variavel)

variavel = re.sub(r'Nobody', r'Vitor', texto)
print(variavel)

#with open('Python_07_nobody.txt', 'r') as nobody_read:
#    find = re.findall(r'Nodoby', nobody_read)

import sys
import re

count_line = 0

with open(sys.argv[1], 'r') as file_hd:
    for line in file_hd:
        count_line += 1
        line2 = line.rstrip().lower()
        line = line.rstrip()
###MÉTODO 1
#        for i in re.finditer('nobody', line2):
#            print(f'{count_line}\t{i.group()}\t{i.start(0) + 1 }\t{line}')
###MÉTODO 2
#        for i in re.findall('nobody', line2):
#            print(f'{count_line}\t{i}\t{line}')

#for i in re.finditer('nobody', line2):
#    print(f'{count_line}\t{ii.group()}\t{i.start(0) + 1 }\t{line}')


count_line = 0

with open(sys.argv[1], 'r') as file_hd:
    for line in file_hd:
        count_line += 1
        line2 = line.rstrip().lower()
        line = line.rstrip()
        for i in re.finditer('(nobody) (\w+s)', line2):
            print(f'{count_line}\t{i.group(1)}\t{i.start(1) + 1 }\t{i.end(1)}\t{line}')
            print(f'{count_line}\t{i.group(2)}\t{i.start(2) + 1 }\t{i.end(2)}\t{line}') 

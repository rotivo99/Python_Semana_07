#!/usr/bin/env python3

import re

dictionary = {}

with open('bionet.txt', 'r') as bionet_read:
    for i, line in enumerate(bionet_read):
        if i > 9:


            blank_space = r' {2,}'
            #print(blank_space)
            line = line.split(blank_space)
            print(line)


#            blank_space = re.fidall(r') *?[ATGCRYN^].*?', line)

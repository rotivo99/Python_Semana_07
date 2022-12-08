#!/usr/bin/env python3

import re

with open('Python_07_nobody.txt', 'r') as nobody_read:
    for line in nobody_read:
        replacing = re.sub(r'[Nn]obody', r'Pikachu', line)
        print(replacing.rstrip())


        #variavel = re.sub(r'Nobody', r'Vitor', texto) 
        #print(variavel)                                                                                                                                                                           

       # line = line.rstrip()

       # print(line.rstrip().re.sub(r'[Nn]obody', 'Pikachu'))

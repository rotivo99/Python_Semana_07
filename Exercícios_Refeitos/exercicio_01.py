#!/usr/bin/env python3

import re

with open('Python_07_nobody.txt', 'r') as nobody_read: #Abrindo o arquivo de entrada
    for line in nobody_read: #Para cada linha no arquivo
        for found in re.finditer(r'([Nn]obody)', line): #Para cada encontro do re.finditer de [Nn]obody em line
            print(f'{found.group(0)}\t{found.start() + 1}\t{found.end()}') #Imprimir a palavra encontrada bem como sua posição inicial e final

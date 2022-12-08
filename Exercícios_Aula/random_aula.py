#!/usr/bin/env python3

import re

dna = "ACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAGGAATTCACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGATATTATCCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAGGAATTCACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGATATTATCCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGG"

for found in re.finditer(r"(.{50})TATTAT(.{25})"  , dna):
    whole    = found.group(0) #Esse 0 imprime a sequência inteira
    up       = found.group(1) #Esse 1 imprime só o primeiro colchetes, o de 50 caracteres
    down     = found.group(2) #Esse 2 imprime só o segundo colchetes, o de 25 caracteres
    up_start = found.start(1) + 1   # need to convert from 0 to 1 notation 
    up_end   = found.end(1) 
    dn_start = found.start(2) + 1
    dn_end   = found.end(2)

print(whole, up, up_start, up_end, down, dn_start, dn_end, sep="\t")

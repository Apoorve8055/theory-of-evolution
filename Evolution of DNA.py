# -*- coding: utf-8 -*-
"""
@program: Evolution of DNA
@author: APOORVE KUMAR VERMA
"""

import random as rand

def evolution(dna):
    index = rand.randint(0,len(dna)-1)
    n = rand.randint(1,1000)
    if n == 1:
        if dna[index] == '0':
            dna[index] = '1'
        else:
            dna[index] = '0'
    return dna

def main():
    with open("dna_data_bits.txt") as dna:
        d = dna.read()
        d = list(d)
        print(d)
        for i in range(1,1000):
            r = evolution(d)
        print(r)
    return

if __name__ == "__main__":
    main()
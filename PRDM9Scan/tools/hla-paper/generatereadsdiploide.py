#!/usr/bin/env python3
# -*- coding: utf-8 -*

import sys
from random import randint


fileIn=sys.argv[1]
couverture=sys.argv[2]
fileout=sys.argv[3]

f=open(fileIn,'r')
seq=''
identifiant=f.readline()
sequence=f.readlines()
for line in sequence:
    seq+=line.strip()
f.close()
i=0
f2=open(fileout,'a')
while i<int(couverture)*len(seq):
    position=randint(0,len(seq)-75)
    f2.write(identifiant)
    f2.write(seq[position:position+60]+'\n')
    f2.write('+\n')
    f2.write('hhhhhhhhhhghhghhhhhfhhhhhfffffe`ee[`X]b[d[ed`[Y[^Yhhhhhhhhhh\n')
    f2.write(identifiant)
    f2.write(seq[position+61:position+75]+'\n')
    f2.write('+\n')
    f2.write('ghhghhhhhfhhhhh'+'\n')
    i=i+1
f2.close()

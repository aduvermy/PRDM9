#!/usr/bin/env python3
# -*- coding: utf-8 -*

import sys
from random import randint


filePRDM9=sys.argv[1]
couverture=sys.argv[2]
fileout=sys.argv[3]
#randint(2,9)

f=open(filePRDM9,'r')
seq=''
identifiant=f.readline()
sequence=f.readlines()
for line in sequence:
    seq+=line.strip()
f.close()
i=0
f2=open(fileout,'a')
while i<float(couverture)*len(seq):
    position=randint(0,len(seq)-100)
    f2.write(identifiant)
    f2.write(seq[position:position+100]+'\n')
    f2.write('+\n')
    f2.write('hhhhhhhhhhghhghhhhhfhhhhhfffffe`ee[`X]b[d[ed`[Y[^Yhhhhhhhhhhghhghhhhhfhhhhhhhhhhhhhhhghhghhhhhfhhhhh\n')
    i=i+1
f2.close()

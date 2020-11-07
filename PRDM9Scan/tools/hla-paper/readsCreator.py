#!/usr/bin/env python3
# -*- coding: utf-8 -*

import sys
from random import randint

print ('je suis dans le script')
filePRDM9=sys.argv[1]
couverture=sys.argv[2]
fileout=sys.argv[3]
f=open(filePRDM9,'r')
seq=''
identifiant=f.readline()
identifiant=identifiant.strip()
sequence=f.readlines()
for line in sequence:
    seq+=line.strip()
f.close()
print (seq)
i=0
name1=fileout+'1.fa'
name2=fileout+'2.fa'
print (name2)
f2=open(name1,'a')
f3=open(name2,'a')
while i<int(couverture)*len(seq)/2:
    position=randint(0,len(seq)-75)
    position1=position
    position2=position+75
    read1=seq[position1:position2]
    f2.write('>read'+str(i)+'\n')
    f2.write(read1[:60]+'\n')
    f2.write(read1[61:]+'\n')
    f3.write('>read'+str(i)+'\n')
    position1_2=len(seq)-position1
    position2_2=len(seq)-position2
    read2=seq[position2_2:position1_2]
    f3.write(read2[:60]+'\n')
    f3.write(read2[61:]+'\n')
    i=i+1
f2.close()
f3.close()

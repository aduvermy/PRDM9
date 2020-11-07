 #!/bin/bash

listeAllele=(a b c d e L1 L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13 L14 L15 L16 L17 L18 L19 L20 L21 L22 L23 L24)
cpteur=0
for i in ${listeAllele[*]}
  do
    for j in ${listeAllele[*]}
      do
        echo $i
        echo $j
        diploide=$i$j
        ./readsCreatorSingle.py ../hla-ref-5gene/IMGT_HLA/PRDM9/$i.fa 30 readsdiploide/$diploide.fq
        ./readsCreatorSingle.py ../hla-ref-5gene/IMGT_HLA/PRDM9/$j.fa 30 readsdiploide/$diploide.fq
        unset listeAllele[$cpteur]
      done
    cpteur=$cpteur+1
  done

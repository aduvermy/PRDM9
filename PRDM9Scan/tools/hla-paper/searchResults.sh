#!/bin/bash

header='individu\tcoverage\tpopulation\tgene\tallele1\tindice1\tallele2\tindice2'
echo -e "$header" >EUR_results.tsv
for resultfile in results/EUR/*/*/*/Report
do
  while read line
  do
  echo "$line" >>EUR_results.tsv
  done < $resultfile
done

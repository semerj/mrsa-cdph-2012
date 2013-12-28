#!/bin/bash

wget http://www.cdph.ca.gov/programs/hai/Documents/2012-MRSA-BSI-T1-T4.pdf

for f in *.pdf
do
  qpdf --password= --decrypt $f out-$f
  pdftotext -layout out-$f
done

python mrsa2012.py

rm -r *.pdf *.txt

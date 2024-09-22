#!/bin/bash

# step 2
curl -s https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz > compressed

# step 3
tar -xzvf compressed > myfile.tsv

# step 4
cat myfile.tsv | tr -s '\n' > my_new_file.tsv

# step 5
tr '\t' ',' < myfile.tsv > file.csv

# step 6
count_lines=$(wc -l < file.csv)
echo $((count_lines - 1))

# step 7
touch converted-archive.tar.gz < file.csv

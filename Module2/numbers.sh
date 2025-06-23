#!/bin/bash

rm -f file1.txt

for i in {1..1000}; do
  echo $RANDOM >> file1.txt
done


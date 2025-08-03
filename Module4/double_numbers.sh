#!/bin/bash

rm -f newfile1.txt

echo "Start: $(date)"
start_time=$SECONDS

# Read input from file1.txt
while read -r number
do
  # Double the number read from file1.txt
  let "number *= 2"
  # Write the doubled nubmer to newfile1.txt
  echo "$number" >> newfile1.txt
done < file1.txt

end_time=$SECONDS
echo "End: $(date)"

duration=$((end_time - start_time))
echo "Total execution time: $duration seconds"


#!/bin/bash

rm -f hugefile1.txt
rm -f hugefile2.txt

echo "Start: $(date)"
start_time=$SECONDS

for i in {1..1000}; do
  cat file1.txt >> hugefile1.txt
  cat file2.txt >> hugefile2.txt
done

end_time=$SECONDS
echo "End: $(date)"

duration=$((end_time - start_time))
echo "Total execution time: $duration seconds"


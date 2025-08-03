#!/bin/bash

rm -f file1.txt

echo "Start: $(date)"
start_time=$SECONDS

for i in {1..1000000}; do
  echo $RANDOM >> file1.txt
done

end_time=$SECONDS
echo "End: $(date)"

duration=$((end_time - start_time))
echo "Total execution time: $duration seconds"


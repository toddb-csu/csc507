#!/bin/bash

rm -f part1.txt
rm -f part2.txt
rm -f totalfile_twoprocesses.txt

echo "Start: $(date)"
start_time=$SECONDS

n=1000000000
half=$((n/2))

python3 process_half.py 0 $half part1.txt &
python3 process_half.py $half $half part2.txt &
wait
cat part1.txt part2.txt >> totalfile_twoprocesses.txt

end_time=$SECONDS
echo "End: $(date)"

duration=$((end_time - start_time))
echo "Total execution time: $duration seconds"


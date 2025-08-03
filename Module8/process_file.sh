#!/bin/bash

for i in {0..9}
do
  rm -f part0$((i)).txt
done

rm -f totalfile_tenprocesses.txt

echo "Start: $(date)"
start_time=$SECONDS

n=1000000000
half=$((n/2))

for i in {0..9}
do
  python3 process_file.py hugefile1_part0$((i)).txt hugefile2_part0$((i)).txt part0$((i)).txt &
done

wait
cat part00.txt part01.txt part02.txt part03.txt part04.txt part05.txt part06.txt part07.txt part08.txt part09.txt >> totalfile_tenprocesses.txt

end_time=$SECONDS
echo "End: $(date)"

duration=$((end_time - start_time))
echo "Total execution time: $duration seconds"


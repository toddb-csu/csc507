import random
import time

start_time = time.time()
print(f"Start baseline Python script: {start_time}")

with open('file2.txt', 'w') as f:
  for _ in range(1000000):
    f.write(str(random.randint(0, 32767)) + '\n')

end_time = time.time()
print(f"End baseline Python script: {end_time}")
duration = end_time - start_time
print(f"Baseline Duration: {duration:.2f} seconds.")


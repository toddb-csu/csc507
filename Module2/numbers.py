import random

with open('file2.txt', 'w') as f:
  for _ in range(1000):
    f.write(str(random.randint(0, 32767)) + '\n')

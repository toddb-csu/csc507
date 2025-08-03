import random
import time
from multiprocessing import Process, Lock

def random_numbers_segment(lock, total, start_index, num_processes):
	with lock:
		with open('file4.txt', 'a') as f:
			for i in range(start_index, start_index + (total // num_processes)):
				f.write(f"{random.randint(0, 32767)}\n")

start_time = time.time()
print(f"Start multiprocessed Python script: {start_time}")

with open('file4.txt', 'w') as f:
	pass

lock = Lock()

processes = []

for i in range(4):
	p = Process(target=random_numbers_segment, args=(lock, 1000000, i*250000, 4))
	p.start()
	processes.append(p)

for p in processes:
	p.join()

end_time = time.time()
print(f"End multiprocessed Python script: {end_time}")
duration = end_time - start_time
print(f"Multiprocessed Duration: {duration:.2f} seconds.")


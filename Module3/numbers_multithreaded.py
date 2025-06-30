import random
import time
import threading

num_threads = 4
results = []
lock = threading.Lock()

def random_numbers_segment(num_lines):
	segment = [str(random.randint(0, 32767)) for _ in range(num_lines)]
	with lock:
		results.extend(segment)

start_time = time.time()
print(f"Start multithreaded Python script: {start_time}")

with open('file3.txt', 'w') as f:
	pass

threads = []
num_lines = 1000000 // num_threads

for _ in range(num_threads):
	thread = threading.Thread(target=random_numbers_segment, args=(num_lines,))
	threads.append(thread)
	thread.start()

for thread in threads:
	thread.join()

with open('file3.txt', 'w') as f:
	f.write("\n".join(results))

end_time = time.time()
print(f"End multithreaded Python script: {end_time}")
duration = end_time - start_time
print(f"Multithreaded Duration: {duration:.2f} seconds.")


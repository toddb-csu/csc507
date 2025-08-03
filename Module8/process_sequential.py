import time

start_time = time.time()
print(f"Start baseline Python script: {start_time}")

with open('hugefile1.txt', 'r') as f1, open('hugefile2.txt', 'r') as f2, open('totalfile.txt', 'w') as fout:
	for line1, line2 in zip(f1, f2):
		num1 = int(line1.strip())
		num2 = int(line2.strip())
		fout.write(f"{num1 + num2}\n")

end_time = time.time()
print(f"End baseline Python script: {end_time}")

duration = end_time - start_time
print(f"Baseline Duration: {duration:.2f} seconds.")

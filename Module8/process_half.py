import time, sys

if __name__=="__main__":
	_, start, line_count, out_file = sys.argv

	start_time = time.time()
	print(f"Start Half Python script: {start_time}")

	with open('hugefile1.txt', 'r') as f1, open('hugefile2.txt', 'r') as f2, open(out_file, 'w') as fout:
		f1.seek(int(start))
		f2.seek(int(start))
		for _ in range(int(line_count)):
			num1 = int(f1.readline().strip())
			num2 = int(f2.readline().strip())
			fout.write(f"{num1 + num2}\n")

	end_time = time.time()
	print(f"End Half Python script: {end_time}")

	duration = end_time - start_time
	print(f"Half Duration: {duration:.2f} seconds.")

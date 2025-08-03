import time, sys

if __name__ == "__main__":
	_, f1_name, f2_name, out_file = sys.argv
	
	start_time = time.time()
	print(f"Start Python script for {out_file}: {start_time}")

	with open(f1_name, 'r') as f1, open(f2_name, 'r') as f2, open(out_file, 'w') as fout:
		for line1, line2 in zip(f1, f2):
			num1 = int(line1.strip())
			num2 = int(line2.strip())
			fout.write(f"{num1 + num2}\n")

	end_time = time.time()
	print(f"End Python script for {out_file}: {end_time}")

	duration = end_time - start_time
	print(f"{out_file} Duration: {duration:.2f} seconds.")

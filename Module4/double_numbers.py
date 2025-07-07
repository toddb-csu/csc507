import time

input_file = "file1.txt"
output_file_prefix = "newfileMethod"

######################################################
# Method 1: Read the entire contents of file1.txt into memory, then process each row.
start_time = time.time()
print(f"Start Method 1 Python script: {start_time}")

# Read the entire contents of file1.txt into memory
with open(input_file, 'r') as file_in:
	lines = file_in.readlines()

# Process each row
with open(output_file_prefix + "1.txt", 'w') as file_out:
	for line in lines:
		number_doubled = int(line.strip()) * 2
		file_out.write(f"{number_doubled}\n")

end_time = time.time()
print(f"End Method 1 Python script: {end_time}")
duration = end_time - start_time
print(f"Method 1 Python script Duration: {duration:.2f} seconds.\n")

######################################################
# Method 2: Read one row of file1.txt at a time and process it.
start_time = time.time()
print(f"Start Method 2 Python script: {start_time}")

with open(input_file, 'r') as file_in, open(output_file_prefix + "2.txt", 'w') as file_out:
	for line in file_in:
		number_doubled = int(line.strip()) * 2
		file_out.write(f"{number_doubled}\n")

end_time = time.time()
print(f"End Method 2 Python script: {end_time}")
duration = end_time - start_time
print(f"Method 2 Python script Duration: {duration:.2f} seconds.\n")

######################################################
# Method 3: Split file1.txt into 2 parts and read each part into memory separately.
start_time = time.time()
print(f"Start Method 3 Python script: {start_time}")

split_point = 0
with open(input_file, 'r') as file_in:
	lines = file_in.readlines()
split_point = len(lines) // 2

# Split file1 into 2 parts
with open('temp_file1.txt', 'w') as out_file1:
	out_file1.writelines(lines[:split_point])
with open('temp_file2.txt', 'w') as out_file2:
	out_file2.writelines(lines[split_point:])

# Process first file part
with open('temp_file1.txt', 'r') as in_file1:
	lines_part1 = in_file1.readlines()

with open(output_file_prefix + "3.txt", 'w') as file_out:
	for line in lines_part1:
		number_doubled = int(line.strip()) * 2
		file_out.write(f"{number_doubled}\n")

# Process second file part
with open('temp_file2.txt', 'r') as in_file2:
	lines_part2 = in_file2.readlines()

with open(output_file_prefix + "3.txt", 'a') as file_out:
	for line in lines_part2:
		number_doubled = int(line.strip()) * 2
		file_out.write(f"{number_doubled}\n")

end_time = time.time()
print(f"End Method 3 Python script: {end_time}")
duration = end_time - start_time
print(f"Method 3 Python script Duration: {duration:.2f} seconds.")


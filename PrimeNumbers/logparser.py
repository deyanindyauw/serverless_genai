import csv
import re

# Define the regex pattern to extract the required values
pattern = re.compile(
    r"Duration: (\d+\.\d+) ms\s+Billed Duration: (\d+) ms\s+Memory Size: (\d+) MB\s+Max Memory Used: (\d+) MB\s+Init Duration: (\d+\.\d+) ms|"
    r"Duration: (\d+\.\d+) ms\s+Billed Duration: (\d+) ms\s+Memory Size: (\d+) MB\s+Max Memory Used: (\d+) MB"
)

# Define a function to parse the log file and extract the values
def parse_log_file(input_file_path, output_file_path):
    extracted_data = []

    # Open and read the CSV file
    with open(input_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        # Iterate through each row in the CSV file
        for row in reader:
            timestamp, message = row
            match = pattern.search(message)
            if match:
                if match.group(1):  # If Init Duration is present
                    duration = float(match.group(1))
                    billed_duration = int(match.group(2))
                    memory_size = int(match.group(3))
                    max_memory_used = int(match.group(4))
                    init_duration = float(match.group(5))
                else:  # If Init Duration is not present
                    duration = float(match.group(6))
                    billed_duration = int(match.group(7))
                    memory_size = int(match.group(8))
                    max_memory_used = int(match.group(9))
                    init_duration = None

                extracted_data.append({
                    'Timestamp': timestamp,
                    'Duration': duration,
                    'Billed Duration': billed_duration,
                    'Memory Size': memory_size,
                    'Max Memory Used': max_memory_used,
                    'Init Duration': init_duration
                })

    # Write the extracted data to a new CSV file
    with open(output_file_path, 'w', newline='') as csvfile:
        fieldnames = ['Timestamp', 'Duration', 'Billed Duration', 'Memory Size', 'Max Memory Used', 'Init Duration']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for data in extracted_data:
            writer.writerow(data)

# Define the path to the input log file and the output CSV file
input_file_path = 'logs_python.csv'
output_file_path = 'extracted_python.csv'
# input_file_path = 'logs_ruby.csv'
# output_file_path = 'extracted_ruby.csv'
# input_file_path = 'logs_node.csv'
# output_file_path = 'extracted_node.csv'

# Call the function to parse the log file and store the extracted data in a CSV file
parse_log_file(input_file_path, output_file_path)
print(f'Extracted data has been written to {output_file_path}')

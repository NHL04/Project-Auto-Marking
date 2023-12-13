import os
import subprocess
import csv

def run_flake8_on_files(folder_path):
    # Get a list of all Python files in the folder and its subdirectories
    python_files = [f for f in os.listdir(folder_path) if f.endswith('.py')]

    # Initialize counters
    file_counts = []

    for file in python_files:
        file_path = os.path.join(folder_path, file)
        print(f"Running Flake8 on {file_path}...")

        # Run Flake8 using subprocess
        result = subprocess.run(['flake8', file_path], capture_output=True, text=True)

        # Get the full output of Flake8
        full_output = result.stdout.strip()

        # Print the full output
        # print(full_output)

        # Count occurrences of E, W, and F
        error_count = full_output.count('E')
        warning_count = full_output.count('W')
        failure_count = full_output.count('F')

        # Append counts to the list
        file_counts.append({
            'file_name': file,
            'Failure': failure_count,
            'Error': error_count,
            'Warning': warning_count
        })

    return file_counts

def write_counts_to_csv(csv_folder, file_counts):
    # Create the CSV folder if it doesn't exist
    os.makedirs(csv_folder, exist_ok=True)

    # Define the CSV file path
    csv_file_path = os.path.join(csv_folder, 'flake8_result.csv')

    # Write counts to the CSV file
    with open(csv_file_path, 'w', newline='') as csv_file:
        fieldnames = ['file_name', 'Failure', 'Error', 'Warning']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(file_counts)

def flake8_program():
    # Specify the folder path where your Python scripts are located
    scripts_folder = 'Correct'

    # Specify the CSV folder path
    csv_folder = 'csv'

    # Run Flake8 on files in the specified folder
    file_counts = run_flake8_on_files(scripts_folder)

    # Write counts to a CSV file
    write_counts_to_csv(csv_folder, file_counts)

    print(f"Flake8 counts written to {csv_folder}/flake8_counts.csv")

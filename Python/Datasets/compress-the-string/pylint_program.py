import csv
from pylint import lint
from pylint.reporters import CollectingReporter
import os

def count_messages(messages, category):
    return sum(1 for msg in messages if msg.C == category)

def pylint_program():
    # Path to the folder containing the files
    folder_path = "Correct"
    output_folder = "csv"
    os.makedirs(output_folder, exist_ok=True)

    # CSV file path
    csv_file_path = os.path.join(output_folder, "pylint_results.csv")

    # Open CSV file for writing
    with open(csv_file_path, mode='w', newline='') as csv_file:
        fieldnames = ['file_name', 'E_pylint', 'R_pylint', 'pylint_score']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write CSV header
        writer.writeheader()

        # Get a list of all Python files in the folder
        files = [f for f in os.listdir(folder_path) if f.endswith(".py")]

        for file in files:
            file_path = os.path.join(folder_path, file)

            # Run pylint to collect messages
            reporter = CollectingReporter()
            pylint_obj = lint.Run([file_path], reporter=reporter, exit=False)

            # Extract the score from pylint_obj.linter.stats
            score = pylint_obj.linter.stats.global_note

            # Count the total number of 'E' and 'R' messages
            total_errors = count_messages(reporter.messages, 'E')
            total_refactors = count_messages(reporter.messages, 'R')

            # Write to CSV
            writer.writerow({
                'file_name': file,
                'E_pylint': total_errors,
                'R_pylint': total_refactors,
                'pylint_score': score
            })

    print(f"CSV file created: {csv_file_path}")



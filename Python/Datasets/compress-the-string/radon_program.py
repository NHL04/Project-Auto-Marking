# import os
# import csv
# from radon.raw import analyze
# from radon.metrics import mi_visit
# from radon.complexity import cc_visit
# from radon.cli.tools import iter_filenames

# # Specify the path of the folder containing the files to analyze
# folder_path = "submit_code"

# # Specify the path of the folder to save CSV files
# csv_folder = "csv"

# # Create the CSV folder if it doesn't exist
# os.makedirs(csv_folder, exist_ok=True)

# # Specify the CSV file path
# csv_file_path = os.path.join(csv_folder, "radon_result.csv")

# # Open the CSV file in write mode
# with open(csv_file_path, mode='w', newline='') as csvfile:
#     # Define the CSV fieldnames
#     fieldnames = ["file_name", "num_of_func", "total_complexity", "maintainability_index", "loc", "lloc", "sloc", "num_of_comments", "num_of_blank"]

#     # Create a CSV writer object
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     # Write the header row
#     writer.writeheader()

#     # iter through filenames in the specified folder
#     for filename in iter_filenames([folder_path]):
#         with open(filename) as fobj:
#             source = fobj.read()

#         # get cc blocks
#         blocks = cc_visit(source)
#         # get MI score
#         mi = mi_visit(source, True)
#         # get raw metrics
#         raw = analyze(source)

#         # Extract relevant metrics
#         file_name = os.path.basename(filename)
#         num_of_func = len(blocks)
#         total_complexity = sum(block.complexity for block in blocks)
#         loc = raw.loc
#         lloc = raw.lloc
#         sloc = raw.sloc
#         num_of_comments = raw.comments
#         num_of_blank = raw.blank

#         # Write the metrics to the CSV file
#         writer.writerow({
#             "file_name": file_name,
#             "num_of_func": num_of_func,
#             "total_complexity": total_complexity,
#             "maintainability_index": mi,
#             "loc": loc,
#             "lloc": lloc,
#             "sloc": sloc,
#             "num_of_comments": num_of_comments,
#             "num_of_blank": num_of_blank
#         })

# print(f"Metrics saved to: {csv_file_path}")

import os
import csv
from radon.raw import analyze
from radon.metrics import mi_visit
from radon.complexity import cc_visit
from radon.cli.tools import iter_filenames
from radon.metrics import h_visit

# Specify the path of the folder containing the files to analyze
folder_path = "submit_code"

# Specify the path of the folder to save CSV files
csv_folder = "csv"

# Create the CSV folder if it doesn't exist
os.makedirs(csv_folder, exist_ok=True)

# Specify the CSV file path
csv_file_path = os.path.join(csv_folder, "radon_result.csv")

# Open the CSV file in write mode
with open(csv_file_path, mode='w', newline='') as csvfile:
    # Define the CSV fieldnames
    fieldnames = ["file_name", "num_of_func", "total_complexity", "maintainability_index",
                  "loc", "lloc", "sloc", "num_of_comments", "num_of_blank",
                  "h1", "h2", "N1", "N2", "vocabulary", "length", "calculated_length",
                  "volume", "difficulty", "effort", "time", "bugs"]

    # Create a CSV writer object
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header row
    writer.writeheader()

    # iter through filenames in the specified folder
    for filename in iter_filenames([folder_path]):
        with open(filename) as fobj:
            source = fobj.read()

            # get cc blocks
            blocks = cc_visit(source)
            # get MI score
            mi = mi_visit(source, True)
            # get raw metrics
            raw = analyze(source)

            # get Halstead metrics
            halstead_metrics = h_visit(source)

            # Extract relevant metrics
            file_name = os.path.basename(filename)
            num_of_func = len(blocks)
            total_complexity = sum(block.complexity for block in blocks)
            loc = raw.loc
            lloc = raw.lloc
            sloc = raw.sloc
            num_of_comments = raw.comments
            num_of_blank = raw.blank

            # Access Halstead metrics using attributes
            h1 = halstead_metrics.total.h1
            h2 = halstead_metrics.total.h2
            N1 = halstead_metrics.total.N1
            N2 = halstead_metrics.total.N2
            vocabulary = halstead_metrics.total.vocabulary
            length = halstead_metrics.total.length
            calculated_length = halstead_metrics.total.calculated_length
            volume = halstead_metrics.total.volume
            difficulty = halstead_metrics.total.difficulty
            effort = halstead_metrics.total.effort
            time = halstead_metrics.total.time
            bugs = halstead_metrics.total.bugs

            # Write the metrics to the CSV file
            writer.writerow({
                "file_name": file_name,
                "num_of_func": num_of_func,
                "total_complexity": total_complexity,
                "maintainability_index": mi,
                "loc": loc,
                "lloc": lloc,
                "sloc": sloc,
                "num_of_comments": num_of_comments,
                "num_of_blank": num_of_blank,
                "h1": h1,
                "h2": h2,
                "N1": N1,
                "N2": N2,
                "vocabulary": vocabulary,
                "length": length,
                "calculated_length": calculated_length,
                "volume": volume,
                "difficulty": difficulty,
                "effort": effort,
                "time": time,
                "bugs": bugs
            })


print(f"Metrics saved to: {csv_file_path}")

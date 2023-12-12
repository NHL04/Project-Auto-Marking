import os
import subprocess
import csv
from Test_program import winnowing
from io import StringIO
import pandas as pd

program1 = 'program1'
program2 = 'program2'


def write_csv(row):
    csv_filename = "csv/Similarity.csv"
    with open(csv_filename, "a", newline='') as file:
        fieldnames = ['Ref Program', 'input_filename', 'Total Score Winnowing', 'Similarity Score', 'Score by num of failure', 'Score by num of error', 'Score by num of warning']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        if file.tell() == 0:
            writer.writeheader()

        csvwriter = csv.writer(file)
        csvwriter.writerow(row)
        print(f'Results written to {csv_filename}')

def generate_ast(file_name, numeric_value, file_path):
    try:
        subprocess.run(['python',file_name , numeric_value, file_path], check = True)
        print(f"Script executed successfully for file: {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error running the script for file: {file_path}")
        print(f"Return code: {e.returncode}")

def process_directory(ref_file_path, directory_path):
    generate_ast_file_path = 'Test_program/generate_ast.py'
    numeric_value = ['1','2']
    generate_ast(generate_ast_file_path,numeric_value[0], ref_file_path)
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".py"):
            file_path = os.path.join(directory_path, file_name)
            print(f"Running tests for {file_path}")
            command = f"pytest --input-filename={file_name} --tb=no"
            try:
                subprocess.run(command, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error while running tests for {file_path}: {e}")
            generate_ast(generate_ast_file_path,numeric_value[1], file_path)
            row = winnowing.result_winnowing()
            write_csv(row)

process_directory('ref.py','Correct')




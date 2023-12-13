from flake8_program import *
from pylint_program import *
from radon_program  import *
from simi_unit_program import *
import pandas as pd


def main():
    flake8_program()
    pylint_program()
    radon_program()
    process_directory()

    directory_path = 'csv'
    csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]
    print(csv_files)
    dfs = [pd.read_csv(os.path.join(directory_path, file)) for file in csv_files]
    merged_df = dfs[0]

    for df in dfs[1:]:
        merged_df = pd.merge(merged_df, df, on='file_name', how='inner')
    merged_df.to_csv('csv/final_result.csv', index=False)

if __name__ =='__main__':
    main() 
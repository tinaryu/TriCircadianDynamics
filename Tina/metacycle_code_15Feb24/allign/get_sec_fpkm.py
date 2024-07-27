import pandas as pd

def extract_second_column(file_prefix):
    # Read the FPKM file into a Pandas DataFrame
    df = pd.read_csv(file_prefix + '_new_fpkm.txt', sep='\t')

    # Extract the second column
    second_col = df.iloc[:, 1]

    # Write the second column to a new text file
    second_col.to_csv(file_prefix + '.txt', index=False, header=True)

# Call the function for each of your files
for i in range(1, 5):
    for j in range(1, 3):
        file_prefix = f'GFRNA{i}_rep{j}'
        extract_second_column(file_prefix)


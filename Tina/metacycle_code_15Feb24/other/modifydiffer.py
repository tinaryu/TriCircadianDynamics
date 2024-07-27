# modifydiffer is run after difference.py
#it is used to modify the difference.txt file to make the phase difference between 0 and 12

import pandas as pd

gene = ["hdac3", "nfil3", "nr1d1"]

for g in gene:
    # Load the datat
    file_path = g+'_difference_div.txt'
    df = pd.read_csv(file_path, sep='\t')  # Adjust the separator if needed

    # Modify the 'meta2d_phase_diff' column based on the condition
    df['meta2d_phase_diff'] = df['meta2d_phase_diff'].apply(lambda x: abs(24 - x) if x > 12 else x)

    # Save the modified DataFrame to a new file
    output_file_path = g+'_difference_modify_div.txt'
    df.to_csv(output_file_path, sep='\t', index=False)

    output_file_path




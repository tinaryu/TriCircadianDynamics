import os

def update_column_names(file_path):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Extract column names
    columns = lines[0].split()

    numcols = len(columns)
    halfcols = int((numcols-1)/2)

    for i in range(1, halfcols + 1):
        columns[i+halfcols] = columns[i] + "r"

    # Write the updated column names back to the file
    lines[0] = '\t'.join(columns) + '\n'

    with open(file_path, 'w') as file:
        file.writelines(lines)

    print(f"Updated column names in {file_path}")

def update_column_names_in_folder(folder_path):
    # Iterate over all files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            update_column_names(file_path)

# Example usage:
folder_path = 'repR'
update_column_names_in_folder(folder_path)
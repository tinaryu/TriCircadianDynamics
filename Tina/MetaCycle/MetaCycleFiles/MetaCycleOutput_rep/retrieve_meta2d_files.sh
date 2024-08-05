#!/bin/bash

# Directory containing folders with meta2d*.txt files
source_dir="/path/to/source_directory"

# Destination directory to save meta2d*.txt files
destination_dir="/path/to/destination_directory/meta2d_only"

# Create the destination directory if it doesn't exist
mkdir -p "$destination_dir"

# Loop through each folder in the source directory
for folder in "$source_dir"/*; do
    # Check if it's a directory
    if [ -d "$folder" ]; then
        # Loop through files in the current folder
        for file in "$folder"/meta2d*.txt; do
            # Check if meta2d*.txt file exists
            if [ -f "$file" ]; then
                # Copy meta2d*.txt file to the destination directory
                cp "$file" "$destination_dir"
            fi
        done
    fi
done

echo "All meta2d*.txt files have been copied to $destination_dir"
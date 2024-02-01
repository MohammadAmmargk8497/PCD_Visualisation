#!/bin/bash

# Check if three arguments are provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 fetch_path store_path num"
    exit 1
fi

# Extract the arguments 
path_arg1=$1
path_arg2=$2
num_arg=$3

# Run the Python script with the provided arguments
python3 open.py "$path_arg1" "$path_arg2" "$num_arg"  
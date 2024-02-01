#!/bin/bash

# Check if three arguments are provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 fetch_path "
    exit 1
fi

# Extract the arguments 
path_arg1=$1


# Run the Python script with the provided arguments
python3 visualise.py "$path_arg1"
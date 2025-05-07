#!/bin/bash

# Usage: ./run_all_py.sh [optional_directory]

BASE_DIR=${1:-.}
ORIGINAL_DIR=$(pwd)

find "$BASE_DIR" -type f -name "*.py" | sort | while read -r file; do
    DIR=$(dirname "$file")
    BASENAME=$(basename "$file")

    echo -e "\nRunning: $file"

    cd "$DIR" || continue

    python "$BASENAME"

    cd "$ORIGINAL_DIR" || exit
done

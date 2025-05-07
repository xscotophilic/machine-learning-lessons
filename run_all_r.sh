#!/bin/bash

# Usage: ./run_all_r.sh [optional_directory]

BASE_DIR=${1:-.}
ORIGINAL_DIR=$(pwd)

find "$BASE_DIR" -type f -name "*.R" | sort | while read -r file; do
    DIR=$(dirname "$file")
    BASENAME=$(basename "$file")

    echo -e "\nRunning: $file"

    cd "$DIR" || continue

    Rscript "$BASENAME"

    cd "$ORIGINAL_DIR" || exit
done

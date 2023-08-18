#!/bin/bash

for file in *.py; do
    # Using grep to filter out lines that start with a '#'
    grep -v '^#' "$file" > "$file.tmp"
    # Replace the original file with the filtered content
    mv "$file.tmp" "$file"
done


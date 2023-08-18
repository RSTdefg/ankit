for file in *; do
  # Extract the second portion of the filename split by '.'
  new_name=$(echo "$file" | awk -F'.' '{print $2".py"}')
  mv "$file" "$new_name"
done

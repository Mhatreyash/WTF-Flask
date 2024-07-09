project_dir=$(pwd)

output_file="${project_dir}/code_context.txt"

if [ -f "$output_file" ]; then
  rm "$output_file"
fi

include_extensions=(".py" ".js" ".jsx" ".ts" ".tsx" ".html" ".css" ".json")

ignore_patterns=("*.ico" "*.png" "*.jpg" "*.jpeg" "*.gif" "*.svg" "*.pyc" "__pycache__" "env")

read_files() {
  for entry in "$1"/*
  do
    should_ignore=false
    for ignore_pattern in "${ignore_patterns[@]}"; do
      if [[ "$entry" == *"$ignore_pattern" ]]; then
        should_ignore=true
        break
      fi
    done

    if $should_ignore; then
      continue
    fi

    if [ -d "$entry" ]; then
      read_files "$entry"
    elif [ -f "$entry" ]; then
      should_include=false
      for ext in "${include_extensions[@]}"; do
        if [[ "$entry" == *"$ext" ]]; then
          should_include=true
          break
        fi
      done

      if $should_include; then
        relative_path=${entry#"$project_dir/"}
        echo "// File: $relative_path" >> "$output_file"
        cat "$entry" >> "$output_file"
        echo "" >> "$output_file"
      fi
    fi
  done
}

read_files "${project_dir}"

echo "Code context has been saved to ${output_file}"
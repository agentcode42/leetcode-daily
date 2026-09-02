#!/usr/bin/env bash

set -e

PROBLEM="$*"

if [ -z "$PROBLEM" ]; then
    echo "Usage:"
    echo '  ./new-problem.sh "3568. Minimum Moves to Clean the Classroom"'
    exit 1
fi

# Extract problem number
NUMBER="${PROBLEM%%.*}"

# Remove number and dot from the problem name
NAME="${PROBLEM#*. }"

# Convert problem name to lowercase kebab-case
SLUG=$(echo "$NAME" \
    | tr '[:upper:]' '[:lower:]' \
    | sed 's/[^a-z0-9]/-/g' \
    | sed 's/-\+/-/g' \
    | sed 's/^-//' \
    | sed 's/-$//')

FOLDER="${NUMBER}-${SLUG}"

echo "========================================"
echo " Creating LeetCode Problem"
echo "========================================"
echo "Number : $NUMBER"
echo "Name   : $NAME"
echo "Folder : $FOLDER"
echo

# Prevent accidental overwrite
if [ -e "$FOLDER" ]; then
    echo "ERROR: Folder already exists:"
    echo "$FOLDER"
    exit 1
fi

# Create structure
mkdir -p "$FOLDER/python"

# Create README
cat > "$FOLDER/README.md" <<EOF
# LeetCode $NUMBER — $NAME

EOF

# Create empty Python solution
touch "$FOLDER/python/solution.py"

echo "Created:"
echo
echo "$FOLDER/"
echo "├── README.md"
echo "└── python/"
echo "    └── solution.py"
echo
echo "✓ Done"

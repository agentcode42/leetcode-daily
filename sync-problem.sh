#!/usr/bin/env bash

set -e

PUBLIC_REPO="$(cd "$(dirname "$0")" && pwd)"
PERSONAL_REPO="$PUBLIC_REPO/../leetcode_daily_personal"

DRY_RUN=false

if [ "$1" = "--dry-run" ]; then
    DRY_RUN=true
    shift
fi

PROBLEM="$1"

if [ -z "$PROBLEM" ]; then
    echo "Usage:"
    echo "  ./sync-problem.sh --dry-run <problem-folder>"
    echo "  ./sync-problem.sh <problem-folder>"
    exit 1
fi

SOURCE="$PUBLIC_REPO/$PROBLEM"
DEST="$PERSONAL_REPO/$PROBLEM"

echo "========================================"
echo " LeetCode Problem Sync"
echo "========================================"
echo "Problem:       $PROBLEM"
echo

# --------------------------------------------------
# Verify repositories
# --------------------------------------------------

if [ ! -d "$SOURCE" ]; then
    echo "ERROR: Problem folder does not exist:"
    echo "$SOURCE"
    exit 1
fi

if [ ! -d "$PUBLIC_REPO/.git" ]; then
    echo "ERROR: Public repository not found."
    exit 1
fi

if [ ! -d "$PERSONAL_REPO/.git" ]; then
    echo "ERROR: Personal repository not found:"
    echo "$PERSONAL_REPO"
    exit 1
fi

# --------------------------------------------------
# Show identities and remotes
# --------------------------------------------------

echo "Public Git identity:"
git -C "$PUBLIC_REPO" config user.name
git -C "$PUBLIC_REPO" config user.email
echo

echo "Personal Git identity:"
git -C "$PERSONAL_REPO" config user.name
git -C "$PERSONAL_REPO" config user.email
echo

echo "Public remote:"
git -C "$PUBLIC_REPO" remote get-url origin
echo

echo "Personal remote:"
git -C "$PERSONAL_REPO" remote get-url origin
echo

# --------------------------------------------------
# Check working trees
# --------------------------------------------------

if [ -n "$(git -C "$PUBLIC_REPO" status --porcelain)" ]; then
    echo "ERROR: Public repository has uncommitted changes."
    echo
    git -C "$PUBLIC_REPO" status --short
    exit 1
fi

if [ -n "$(git -C "$PERSONAL_REPO" status --porcelain)" ]; then
    echo "ERROR: Personal repository has uncommitted changes."
    echo
    git -C "$PERSONAL_REPO" status --short
    exit 1
fi

# --------------------------------------------------
# Dry run
# --------------------------------------------------

if [ "$DRY_RUN" = true ]; then

    echo "----------------------------------------"
    echo "DRY RUN"
    echo "----------------------------------------"

    if [ -d "$DEST" ]; then

        echo
        echo "Personal copy already exists."
        echo "Comparing files..."

        if diff -qr "$SOURCE" "$DEST" > /dev/null; then
            echo "✓ Both folders are identical."
        else
            echo "⚠ The folders are different."
            diff -qr "$SOURCE" "$DEST" || true
        fi

    else

        echo
        echo "Personal copy does not exist."
        echo "Would create:"
        echo "$DEST"

    fi

    echo
    echo "No files were changed."
    echo "No commits were created."
    echo "No pushes were performed."

    exit 0
fi

# --------------------------------------------------
# Protect existing personal folder
# --------------------------------------------------

if [ -d "$DEST" ]; then

    echo
    echo "ERROR: Problem already exists in personal repository:"
    echo "$DEST"
    echo
    echo "Nothing was changed."
    echo "If you intentionally want to update it, handle that separately."
    exit 1

fi

# --------------------------------------------------
# Copy problem
# --------------------------------------------------

echo
echo "----------------------------------------"
echo "Copying problem..."
echo "----------------------------------------"

cp -r "$SOURCE" "$DEST"

echo "✓ Problem copied to personal repository."

# --------------------------------------------------
# Public repository
# --------------------------------------------------

echo
echo "----------------------------------------"
echo "Public repository"
echo "----------------------------------------"

git -C "$PUBLIC_REPO" add "$PROBLEM"

git -C "$PUBLIC_REPO" commit \
    -m "Add solution for LeetCode ${PROBLEM%%-*}"

git -C "$PUBLIC_REPO" push origin main

echo "✓ Public repository pushed."

# --------------------------------------------------
# Personal repository
# --------------------------------------------------

echo
echo "----------------------------------------"
echo "Personal repository"
echo "----------------------------------------"

git -C "$PERSONAL_REPO" add "$PROBLEM"

git -C "$PERSONAL_REPO" commit \
    -m "Add solution for LeetCode ${PROBLEM%%-*}"

git -C "$PERSONAL_REPO" push origin main

echo "✓ Personal repository pushed."

echo
echo "========================================"
echo "✓ Sync complete"
echo "========================================"

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
echo "Problem: $PROBLEM"
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
# Check personal repository
# --------------------------------------------------

if [ -n "$(git -C "$PERSONAL_REPO" status --porcelain)" ]; then
    echo "ERROR: Personal repository has uncommitted changes."
    echo
    git -C "$PERSONAL_REPO" status --short
    exit 1
fi

# --------------------------------------------------
# Check public repository changes
# Only the target problem may be uncommitted
# --------------------------------------------------

PUBLIC_CHANGES=$(git -C "$PUBLIC_REPO" status --porcelain)

OTHER_CHANGES=$(echo "$PUBLIC_CHANGES" | grep -v "^[?MADRCU ][?MADRCU ] $PROBLEM/" || true)

if [ -n "$OTHER_CHANGES" ]; then
    echo "ERROR: Public repository has changes outside the target problem."
    echo
    echo "$PUBLIC_CHANGES"
    echo
    echo "Commit or remove those changes first."
    exit 1
fi

# --------------------------------------------------
# Check personal destination
# --------------------------------------------------

if [ -d "$DEST" ]; then
    echo "ERROR: Problem already exists in personal repository:"
    echo "$DEST"
    echo
    echo "Nothing was changed."
    exit 1
fi

# --------------------------------------------------
# DRY RUN
# --------------------------------------------------

if [ "$DRY_RUN" = true ]; then

    echo "----------------------------------------"
    echo "DRY RUN"
    echo "----------------------------------------"
    echo

    echo "Public repository:"
    echo "  $PUBLIC_REPO"
    echo

    echo "Personal repository:"
    echo "  $PERSONAL_REPO"
    echo

    echo "Problem:"
    echo "  $PROBLEM"
    echo

    echo "Files in problem:"
    find "$SOURCE" -type f | sed "s|$SOURCE/|  |"
    echo

    echo "Public repository changes:"
    if [ -n "$PUBLIC_CHANGES" ]; then
        echo "$PUBLIC_CHANGES"
    else
        echo "  No uncommitted changes."
    fi
    echo

    echo "Personal destination:"
    echo "  Does not exist — ready for sync."
    echo

    echo "The real run would:"
    echo "  1. Commit the problem to the public repository."
    echo "  2. Push public repository."
    echo "  3. Copy the problem to the personal repository."
    echo "  4. Commit the problem to the personal repository."
    echo "  5. Push personal repository."
    echo

    echo "========================================"
    echo "✓ Dry run complete"
    echo "========================================"

    exit 0
fi

# --------------------------------------------------
# PUBLIC REPOSITORY
# --------------------------------------------------

echo "----------------------------------------"
echo "Public repository"
echo "----------------------------------------"

git -C "$PUBLIC_REPO" add "$PROBLEM"

if git -C "$PUBLIC_REPO" diff --cached --quiet; then
    echo "ERROR: No changes found for $PROBLEM."
    exit 1
fi

git -C "$PUBLIC_REPO" commit \
    -m "Add solution for LeetCode ${PROBLEM%%-*}"

git -C "$PUBLIC_REPO" push origin main

echo "✓ Public repository pushed."
echo

# --------------------------------------------------
# PERSONAL REPOSITORY
# --------------------------------------------------

echo "----------------------------------------"
echo "Copying to personal repository"
echo "----------------------------------------"

cp -r "$SOURCE" "$DEST"

echo "✓ Problem copied."
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

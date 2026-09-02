# LeetCode 3568 — Minimum Moves to Clean the Classroom

## Approach

This problem can be modeled as a shortest-path problem on a grid.

A state is determined by:

- Current position
- Current energy
- Which litter pieces have already been collected

Since every move costs exactly one step, BFS can be used to find the minimum number of moves.

A bitmask represents the collected litter. Each litter position is assigned one bit.

To reduce unnecessary states, for each position and litter mask we store the maximum energy reached so far. If we reach the same position with the same mask but less or equal energy, that state is not useful.

## Key Idea

The BFS state is:

`(row, column, energy, litter_mask)`

The bitmask allows us to track up to 10 litter pieces efficiently.

For every reachable state:

1. Try all four directions.
2. Ignore walls and positions outside the grid.
3. Decrease energy after moving.
4. Recharge to the original energy when landing on `R`.
5. Add newly collected litter to the bitmask.
6. Keep the state only if it reaches that position and mask with more energy than before.

The first state that contains all litter is the answer because BFS explores states in increasing order of steps.

## Complexity

Let:

- `R` = number of rows
- `C` = number of columns
- `L` = number of litter pieces
- `E` = maximum energy

The state space contains at most:

`O(R × C × 2^L × E)`

states.

Therefore:

- Time: `O(R × C × 2^L × E)`
- Space: `O(R × C × 2^L)`

The `max_energy` array provides state dominance: for a given position and litter mask, only the state with the greatest remaining energy needs to be explored.

## Solutions

- [Python](python/solution.py)
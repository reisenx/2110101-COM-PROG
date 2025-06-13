# --------------------------------------------------
# File Name : 09_Nested_25.py
# Problem   : Tiling Puzzle
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


# Get the row number of num in the tiles which is a 2D list.
def row_number(tiles: list, num: int) -> int:
    for idx in range(len(tiles)):
        if num in tiles[idx]:
            return idx
    return -1


# Flatten the 2D list of tiles into a 1D list, ignoring zeros.
def flatten(tiles: list) -> list:
    flat_tiles = []
    for row in tiles:
        for tile in row:
            if tile > 0:
                flat_tiles.append(tile)
    return flat_tiles


# Count the number of inversions in a list.
# An inversion is a pair of indices (i, j) such that i < j and x[i] > x[j].
def inversions(flat_tiles: list) -> int:
    inv_count = 0
    for i in range(len(flat_tiles)):
        for j in range(i + 1, len(flat_tiles)):
            if flat_tiles[i] > flat_tiles[j]:
                inv_count += 1
    return inv_count


# Check if the 15 puzzle is solvable
def solvable(tiles: list) -> bool:
    # Tiles information
    rows = len(tiles)
    inv_count = inversions(flatten(tiles))
    empty_row = row_number(tiles, 0)
    # Condition for solvability
    c1 = rows % 2 == 1 and inv_count % 2 == 0
    c2 = rows % 2 == 0 and (inv_count + empty_row) % 2 == 1
    return c1 or c2


# Execute an input string as code
exec(input().strip())

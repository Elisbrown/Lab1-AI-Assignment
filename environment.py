# environment.py
# Define the 2D grid environment where:
# 0 = open space, 1 = obstacle, 2 = target

grid = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 2, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]  # Target is at position (2, 3)
]

# Function to print the grid in a readable format
def print_grid(grid):
    for row in grid:
        print(row)

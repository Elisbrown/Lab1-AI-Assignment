# search_algorithms.py
from collections import deque  # BFS uses a queue

# Breadth-First Search (BFS) Algorithm
def bfs(agent, target_value):
    # Start BFS from the agent's current position
    start = agent.position
    queue = deque([start])
    visited = set()  # Keep track of visited positions
    visited.add(start)
    
    while queue:
        x, y = queue.popleft()  # Get the current position
        
        # Check if the agent has reached the target
        if agent.grid[x][y] == target_value:
            return (x, y)  # Return the target's position
        
        # Explore all possible moves (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            # Ensure the move is within the grid and not an obstacle
            if 0 <= nx < len(agent.grid) and 0 <= ny < len(agent.grid[0]) and (nx, ny) not in visited:
                if agent.grid[nx][ny] != 1:  # Skip obstacles
                    queue.append((nx, ny))  # Add to queue for further exploration
                    visited.add((nx, ny))
    
    return None  # Return None if no path to the target is found

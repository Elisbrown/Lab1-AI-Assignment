# agent_class.py
# Agent class to handle movement and sensing the environment

class Agent:
    def __init__(self, start_pos, grid):
        self.position = start_pos  # Agent starts at this position
        self.grid = grid  # The environment grid the agent will navigate
    
    # Function to sense the surroundings (up, down, left, right)
    def sense(self):
        x, y = self.position
        # Check adjacent cells (up, down, left, right)
        surroundings = {
            'up': self.grid[x-1][y] if x > 0 else None,  # Cell above
            'down': self.grid[x+1][y] if x < len(self.grid)-1 else None,  # Cell below
            'left': self.grid[x][y-1] if y > 0 else None,  # Cell to the left
            'right': self.grid[x][y+1] if y < len(self.grid[0])-1 else None  # Cell to the right
        }
        return surroundings
    
    # Function to move the agent in a specific direction (up, down, left, right)
    def move(self, direction):
        x, y = self.position
        if direction == 'up' and x > 0 and self.grid[x-1][y] != 1:
            self.position = (x-1, y)  # Move up
        elif direction == 'down' and x < len(self.grid)-1 and self.grid[x+1][y] != 1:
            self.position = (x+1, y)  # Move down
        elif direction == 'left' and y > 0 and self.grid[x][y-1] != 1:
            self.position = (x, y-1)  # Move left
        elif direction == 'right' and y < len(self.grid[0])-1 and self.grid[x][y+1] != 1:
            self.position = (x, y+1)  # Move right

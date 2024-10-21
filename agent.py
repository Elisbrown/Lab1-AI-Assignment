# agent.py
from environment import grid, print_grid  # Import the environment setup
from search_algorithms import bfs  # Import the BFS algorithm
from agent_class import Agent  # Import the Agent class

# Initialize the grid and agent
print("Initial Grid:")
print_grid(grid)

# Initialize the agent at the starting position (0, 0)
agent = Agent(start_pos=(0, 0), grid=grid)

# Run BFS to find the target
target_pos = bfs(agent, 2)

if target_pos:
    print(f"Target found at: {target_pos}")
    # Simulate the agent's movement towards the target
    def simulate_agent_movement(agent, target_pos):
        print("Agent Initial Position:", agent.position)
        while agent.position != target_pos:
            surroundings = agent.sense()  # Sense surroundings
            # Decision: Move down if possible, otherwise rig

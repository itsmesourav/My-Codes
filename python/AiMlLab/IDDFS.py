# Depth-limited DFS function
def dls(graph, start, goal, depth):
    if start == goal:
        print(start, end=" ")
        return True
    if depth <= 0:
        return False
    print(start, end=" ")
    for neighbor in graph.get(start, []):
        if dls(graph, neighbor, goal, depth-1):
            return True
    return False

# IDDFS main function
def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"\nDepth Level: {depth}")
        if dls(graph, start, goal, depth):
            print("\nGoal found!")
            return
    print("\nGoal not found within depth limit.")

# User input
n = int(input("Enter number of nodes: "))
graph = {}

for i in range(n):
    node = input(f"Enter node {i+1} name: ")
    neighbors = input(f"Enter neighbors of {node} separated by space: ").split()
    graph[node] = neighbors

start_node = input("Enter start node: ")
goal_node = input("Enter goal node: ")
max_depth = int(input("Enter max depth limit: "))

iddfs(graph, start_node, goal_node, max_depth)


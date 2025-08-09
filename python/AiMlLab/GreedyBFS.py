import heapq

# Best First Search using Priority Queue (Min Heap)
def best_first_search(graph, heuristics, start, goal):
    visited = set()
    queue = [(heuristics[start], start)]

    while queue:
        cost, node = heapq.heappop(queue)
        if node in visited:
            continue
        print(node, end=" ")
        visited.add(node)

        if node == goal:
            print("\nGoal reached!")
            return

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (heuristics[neighbor], neighbor))
    print("\nGoal not reachable.")

# User input
n = int(input("Enter number of nodes: "))
graph = {}
heuristics = {}

for i in range(n):
    node = input(f"Enter node {i+1} name: ")
    neighbors = input(f"Enter neighbors of {node} separated by space: ").split()
    graph[node] = neighbors
    heuristics[node] = int(input(f"Enter heuristic value for {node}: "))

start_node = input("Enter start node: ")
goal_node = input("Enter goal node: ")

print("Best First Search Path:")
best_first_search(graph, heuristics, start_node, goal_node)

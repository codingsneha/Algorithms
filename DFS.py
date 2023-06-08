def dfs(graph, start):
    visited = set()               # Set to keep track of visited nodes
    stack = [start]               # Initialize the stack with the start node
    
    while stack:                  # Loop until the stack is empty
        node = stack.pop()        # Pop a node from the top of the stack
        
        if node not in visited:
            visited.add(node)     # Mark the node as visited
            print(node, end=" ")  # Print the visited node
            
            for neighbor in reversed(graph[node]):
                stack.append(neighbor) # Add the neighbor to the top of the stack
graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
dfs(graph, 2)

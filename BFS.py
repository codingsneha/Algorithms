def bfs(graph, start):
    visited = set()               # Set to keep track of visited nodes
    queue = [start]               # Initialize the queue with the start node
    visited.add(start)            # Mark the start node as visited
    
    while queue:                  # Loop until the queue is empty
        node = queue.pop(0)       # Dequeue a node from the queue
        print(node, end=" ")      # Print the visited node
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor) # Mark the neighbor as visited
                queue.append(neighbor) # Add the neighbor to the queue
graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
bfs(graph, 2)

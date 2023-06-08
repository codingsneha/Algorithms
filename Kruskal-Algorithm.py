def kruskal(graph):
    mst = []
    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            edges.append((weight, vertex, neighbor))
    edges.sort()
    parent = {vertex: vertex for vertex in graph}
    for weight, u, v in edges:
        if find(u, parent) != find(v, parent):
            mst.append((weight, u, v))
            parent[find(u, parent)] = find(v, parent)
    return mst

def find(vertex, parent):
    while parent[vertex] != vertex:
        vertex = parent[vertex]
    return vertex

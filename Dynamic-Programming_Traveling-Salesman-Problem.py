"""Minimum cost of tour from city S (starting node)
    visiting all cities available in the graph
    and return to home town S"""

"""Also called minimum weight Hamiltonian Cycle Problem"""

"""Recursive equation:
        T(i, S) = min( (i, j) + T(j, S - {j} )  ;     s != 0
        
        where,  i is starting node
        S is set of remaining nodes"""

"""graph G = (V, E), V and E are set of vertices and edges
    Dist(i, j) denotes the non-negative distance between two vertices, i and j"""

"""Time complexity: O(N2 * 2^N)
    Space complexity: O(2^N)"""

from sys import maxsize
from itertools import permutations
V = 4
def tsp(graph, s):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
    
    min_cost = maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
        current_cost = 0
        k = s
        for j in i:
            current_cost += graph[k][j]
            k = j
        current_cost += graph[k][s]
        min_cost = min(min_cost, current_cost)
        return min_cost
graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
s = 0
print(tsp(graph, s))
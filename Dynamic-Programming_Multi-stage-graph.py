#Python3 program for multistage graph (shortest path).  
import sys
#function for finding shortest distance   
def Source_to_Sink(MG):
#list for storing shortest distance from particular node to N-1 node  
    Distance=[0]*n
#finding the shortest paths  
    for x in range(n-2, -1, -1): 
        Distance[x]=infinity  
#Checking nodes from next stages 
        for y in range(n): 
#condition when no edge exists  
            if MG[x][y]==infinity: 
                continue
#finding minimum distances
            Distance[x]=min(MG[x][y]+Distance[y],Distance[x]) 
    return Distance[0] 
  
# Driver code  
n=9
infinity=sys.maxsize
  
#Adjacency matrix for graph
MG=[[infinity, 10, 5, infinity, infinity, infinity, infinity, infinity, infinity],  
    [infinity, infinity, infinity, 1, infinity, 2, infinity, infinity, infinity],  
    [infinity, infinity, infinity, 8, 4, 7,infinity, infinity, infinity],  
    [infinity, infinity, infinity, infinity, infinity, infinity, 5, 3, infinity],  
    [infinity, infinity, infinity, infinity, infinity, infinity, 6, 9, infinity], 
    [infinity, infinity, infinity, infinity, infinity, infinity, 11, 15, infinity],  
    [infinity, infinity, infinity, infinity, infinity, infinity, infinity, infinity, 4],
    [infinity, infinity, infinity, infinity, infinity, infinity, infinity, infinity, 7]]  
D=Source_to_Sink(MG)  
print("SHORTEST PATH FROM SOURCE TO SINK IS :", D)
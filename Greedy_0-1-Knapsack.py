#Knapsack 0-1 problem
"""Problem statement: A sack or bag can contain maximum W unit weight.
Given some objects each having their respective profits and weights
you must put the objects in the sack in such a way that weight is not more than W.
and profit is maximum.

Note: Profit is maximum when we are greedy about profit/weight ratio
not greedy about only profit, neither greedy about only less weight."""

#naive approach (recursion)
def knapSack(W, weight, profit, n):
    if n == 0 or W == 0:
        return 0
    if (weight[n - 1] > W):
        return knapSack(W, weight, profit, n - 1)
    else:
        return max(profit[n - 1] + knapSack(W - weight[n - 1], weight, profit, n - 1), knapSack(W, weight, profit, n - 1))

n = int(input("\nEnter number of objects: "))
profit = [int(input("\nEnter profit of object %d: "%(i + 1))) for i in range(n)]
weight = [int(input("\nEnter weight of object %d: "%(i + 1))) for i in range(n)]
W = int(input("\nEnter maximum capacity of sack: "))
print (knapSack(W, weight, profit, n))
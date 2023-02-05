'''
Name : Muhammad Hazim Bin Zaharuddin
Matric No: 2016579
CSCI 3302 Section 02 DATA STRUCTURES AND ALGORITHMS II

Basic Dijkstra Algorithm with Example Graph
'''

import heapq
import math

def Dijkstra(Graph, source):
    wt = [math.inf for _ in range(len(Graph))] # initialize the load from the source to the source
    previous = [None for _ in range(len(Graph))] # track the previous node from source
    wt[source] = 0 # initialize the load for the source node
    heap = []
    heapq.heappush(heap, (0, source))
    
    while heap:
        (wt_u, u) = heapq.heappop(heap)
        if wt_u == math.inf:
            break
        for v, weight in enumerate(Graph[u]):
            if weight == 0:
                continue
            if wt[v] > wt[u] + weight:
                wt[v] = wt[u] + weight
                previous[v] = u
                heapq.heappush(heap, (wt[v], v))
                
    min_path = []

    for i in range(2):
      min_distance = wt[i]
      if wt[i] < min_distance:
        min_distance = wt[i]

    for i, distance in enumerate(wt):
        if distance == min_distance:
            min_path.append(i)
            
    return wt, previous, min_distance, min_path

# Example Graph
Graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]]
source = 0

wt, previous, min_distance, min_path = Dijkstra(Graph, source)

print("Vertex Distance from Source") 
for i, d in enumerate(wt):
    print("{0} \t\t {1}".format(i, d))

print("Weight from source to each vertex: ", wt)
print("Previous node from source for each vertex: ", previous)
print("Minimum distance: ", min_distance)
print("Vertices with minimum distance: ", min_path)

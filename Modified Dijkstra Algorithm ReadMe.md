Name : Muhammad Hazim Bin Zaharuddin Matric No: 2016579 CSCI 3302
Section 02 DATA STRUCTURES AND ALGORITHMS II

A Modified Dijkstra's Algorithm for Solving the Problem of Finding the
Maximum Load Path

A modified version of Dijkstra's algorithm can be used to find the
maximum load path in a graph. An example of an application for the
modified Dijkstra's algorithm for finding the maximum load path is to
find a path that maximizes the load capacity of the vehicle according to
the starting and destination locations on a road map that indicates the
road load limit between each pair of adjacent road intersections. The
main modification made to the original Dijkstra's algorithm to find the
maximum load path is the use of the "wt" array to keep track of the load
on the path from the source vertex to each vertex.

function ModifiedDijkstra(Graph, source): wt\[source\] := 0 //
Initialize the load from the source to the source for each vertex v in
Graph: //Initialize the load for all other vertices if v ≠ source:
wt\[v\] := -infinity previous\[v\] := undefined //Previous node from
source create empty priority queue Q // Q will be used to track vertices
for each edge (u,v) in Graph: if wt\[u\] + weight(u,v) \> wt\[v\]:
wt\[v\] = wt\[u\] + weight(u,v) previous\[v\] = u add v to Q with
priority wt\[v\] while Q is not empty: u := vertex in Q with max wt\[u\]
remove u from Q for each neighbor v of u: if wt\[u\] + weight(u, v) \>
wt\[v\]: wt\[v\] = wt\[u\] + weight(u, v) previous\[v\] = u if v is not
in Q: add v to Q with priority wt\[v\] return wt, previous

From the pseudocode, The priority of a vertex in the priority queue is
also based on the value in the "wt" array, where the vertex with the
highest value in the "wt" array has the highest priority with all
elements of the "wt" array are initialized to -infinity. Moreover, the
modified Dijkstra's algorithm uses a for loop to iterate through all
edges in the graph, and check if the load on the path to the destination
vertex can be increased by traversing this edge. If the load can be
increased, the value in the "wt" array is updated, the "previous" array
is updated and the destination vertex is added to the priority queue.

Performance The modified Dijkstra's algorithm totally takes O((n+m)log
n) time, where n is the number of nodes in graph G and m is the number
of edges in graph G. This is because the algorithm needs to examine all
the vertices and edges once, and perform logarithmic time operations on
the priority queue.

Advantages: 1. It has an efficient performance with a time complexity of
O((n+m)log n) which is efficient for sparse graphs with relatively few
edges compared to the number of vertices. 2. It has versatility. It can
handle graphs with both positive and negative weights, and it can find
the maximum load path on them. 3. It has simplicity because it is
relatively simple to implement.

Disadvantages: 1. It is limited to unweighted graphs and you need to
find the maximum load path on it. 2. It is not efficient for dense
graphs. As the number of edges increases, the time complexity of the
algorithm increases as well. 3. It uses a priority queue which requires
additional space.

How to use the code The code can be used by following these steps:

1.  Import the heapq module.
2.  Define the ModifiedDijkstra function.
3.  Create an adjacency matrix representing the weighted graph.
4.  Specify the source node (the starting node from which the longest
    path should be found).
5.  Call the ModifiedDijkstra function and pass the graph and source
    node as arguments.
6.  The function will return four values: the weight from the source
    node to each vertex, the previous node from the source for each
    vertex, the maximum distance, and the vertices with the maximum
    distance.
7.  You can print these values or use them for other purposes.

Wei, K., Gao, Y., Zhang, W., & Lin, S. (2019, March). A modified
Dijkstra's algorithm for solving the problem of finding the maximum load
path. In 2019 IEEE 2nd International Conference on Information and
Computer Technologies (ICICT) (pp. 10-13). IEEE.

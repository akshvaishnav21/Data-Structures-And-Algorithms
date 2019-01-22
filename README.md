# Data-Structures-And-Algorithms
Data Structures And Algorithms using Python
----------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------
BFS And DFS --------------------------------------------------------------

You can use a graph search algorithm to traverse the entirety of a graph data structure to locate a specific value
Vertices in a graph search include a "visited" list to keep track of whether or not each vertex has been checked
Depth-first search (DFS) and breadth-first search (BFS) are two common approaches to graph search
The runtime for graph search algorithms is O(vertices + edges)
DFS, which employs either recursion or a stack data structure, is useful for determining whether a path exists between two points
BFS, which generally relies on a queue data structure, is helpful in finding the shortest path between two points
There are three common traversal orders which you can apply with DFS to generate a list of all values in a graph: pre-order, post-order, and reverse post-order

Pusedo Code for DFS recursion -

loop through each neighbor of the current vertex in the graph:

  if neighbor has not been visited:

    recursively call dfs on neighbor

    if a path exists:

      return the path

DFS Psuedo Code -
  loop through queue while the queue is not empty:

    set current_vertex & path equal to first vertex & path on queue

    add current_vertex to visited set

    loop through each neighbor of current_vertex in graph

      if neighbor has not been visited:

        if neighbor is equal to target_value:

          return path including neighbor

        else:

           add neighbor and its path to the queue

Dijkstra’s Algorithm -----------------------------------------------------

Dijkstra’s Algorithm works like the following:

1. Instantiate a dictionary that will eventually map vertices to their distance from the start vertex
2. Assign the start vertex a distance of 0 in a min heap
3. Assign every other vertex a distance of infinity in a min heap
4. Remove the vertex with the smallest distance from the min heap and set that to the current vertex
5. For the current vertex, consider all of its adjacent vertices and calculate the distance to them as (distance to the current vertex) + (edge weight of current vertex to adjacent vertex).
6. If this new distance is less than the current distance, replace the current distance.
7. Repeat 4 and 5 until the heap is empty
8. After the heap is empty, return the distances

Using a heap will allow removing the minimum from the heap to be efficient. In python, there is a library called heapq which we will use to do all of our dirty work for us!

The heapq method has two critical methods we will use in Dijkstra's Algorithm: heappush and heappop.

heappush will add a value to the heap and adjust the heap accordingly
heappop will remove and return the smallest value from the heap

Psuedo Code - 
create dictionary to map vertices to their distance from start vertex

assign start vertex a distance of 0 in min heap

assign every other vertex a distance of infinity in min heap

remove the vertex with the minimum distance from the min heap and set it to the current vertex

while min heap is not empty:
  for each current vertex:
    for each neighbor in neighbors:
    new distance = (distance to current vertex) + (edge weight of current vertex to neighbor)

    if new distance is less than its current distance:
      current distance = new distance

return distances

A* ------------------------------------------------------------------------
#manhatten-graoh.py and Euclidian_graph.py needed for input.

To build out an A* implementation in Python.

There are only a few important changes:

1. Include a target for the search to find. No more searching in all directions for all destinations.
2. Collect and return the shortest path. A dictionary of distances is cool and all, but A* is on a mission to get you to your target destination and tell you how to get there.
3. Build a heuristic that calculates the estimated distance between two points. This is the crucial point of difference between Dijkstra's and A*; A* has a real sense of direction.

The A* algorithm is a greedy graph search algorithm that optimizes looking for a target vertex.
A* is a modification of Dijkstra’s done by adding the estimated distance of each vertex to the goal vertex when searching.

The runtime of A* is O(b^d) where b is the branching factor of the graph and d is the depth of the goal vertex from the start vertex.

# Data-Structures-And-Algorithms
Data Structures And Algorithms using Python
----------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------

Linear Search ------------------------------------------------------------

The linear search, or sequential search, algorithm sequentially checks whether a given value is an element of a specified list by scanning the elements of a list one-by-one. It checks every item in the list in order from the beginning to end until it finds a target value.

If it finds the target value in the list, the linear search algorithm stops and returns the position in the list corresponding to the target value. If it does not find the value, the linear search algorithm returns a message stating that the target value is not in the list.

The steps are:

1. Examine the first element of the list.
2. If the first element is equal to the target value, stop.
3. If the first element is not equal to the target value, check the next element in the list.
4. Continue steps 1-3 until the element is found or the end of the list is reached.

The best case performance for linear search occurs when the target value exists in the list and is in the first position of the list. In this case, the linear search algorithm will only be required to make one comparison. The time complexity for linear search in its best case is O(1).

There are two worst cases for linear search.

Case 1: when the target value at the end of the list. 

Case 2: when the target value does not exist in the list. 

In both cases, the linear search algorithm is required to scan the entire list of N elements and, therefore, makes N comparisons.

For this reason, the time complexity for linear search in its worst case is O(N).

The time complexity for linear search is O(N), but its performance is dependent on its input:

    Best Case: The algorithm requires only 1 comparison to find the target value in the first position of the list.
    Worst Case: The algorithm requires only n comparison to find the target value in the last position of the list or does not exist in the list.
    Average Case: The algorithm makes N/2 comparisons.
    
Linear search is a good choice for a search algorithm when:

  You expect the target value to be positioned near the beginning of the list.

  A search needs to be performed on an unsorted list because linear search traverses the entire list from beginning to end, regardless of its order.

Binary Search ------------------------------------------------------------

Binary search requires a sorted data-set. We then take the following steps:

  1. Check the middle value of the dataset.

  2. If this value matches our target we can return the index.
  3. If the middle value is less than our target

  4. Start at step 1 using the right half of the list.
  If the middle value is greater than our target

  Start at step 1 using the left half of the list.
We eventually run out of values in the list, or find the target value.

Time Complexity
In each iteration, we are cutting the list in half. The time complexity is O(log N).

A sorted list of 64 elements will take at most log2(64) = 6 comparisons.

In the worst case:

Comparison 1: We look at the middle of all 64 elements

Comparison 2: If the middle is not equal to our search value, we would look at 32 elements

Comparison 3: If the new middle is not equal to our search value, we would look at 16 elements

Comparison 4: If the new middle is not equal to our search value, we would look at 8 elements

Comparison 5: If the new middle is not equal to our search value, we would look at 4 elements

Comparison 6: If the new middle is not equal to our search value, we would look at 2 elements

When there's 2 elements, the search value is either one or the other, and thus, there is at most 6 comparisons in a sorted list of size 64.

BFS And DFS --------------------------------------------------------------

You can use a graph search algorithm to traverse the entirety of a graph data structure to locate a specific value
Vertices in a graph search include a "visited" list to keep track of whether or not each vertex has been checked
Depth-first search (DFS) and breadth-first search (BFS) are two common approaches to graph search
The runtime for graph search algorithms is O(vertices + edges)
DFS, which employs either recursion or a stack data structure, is useful for determining whether a path exists between two points
BFS, which generally relies on a queue data structure, is helpful in finding the shortest path between two points
There are three common traversal orders which you can apply with DFS to generate a list of all values in a graph: pre-order, post-order, and reverse post-order

Pusedo Code for DFS -

def dfs(graph, current_vertex, target_value, visited): 

  set visited to empty list if not yet set

  add current_vertex to visited

  # base case:
  if current_vertex is equal to target_value:

    return visited list

  loop through each neighbor of the current vertex in the graph:

    if neighbor has not been visited:

      recursively call dfs on neighbor

      if a path exists:

        return the path

DFS Psuedo Code -

def bfs(graph, start_vertex, target_value):

  set path to a list containing the start_vertex

  create a queue to hold vertices and their corresponding paths

  define an empty visited set
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

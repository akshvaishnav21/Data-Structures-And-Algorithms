# Data-Structures-And-Algorithms
Data Structures And Algorithms using Python
----------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------

Bubble Sort --------------------------------------------------------------
Bubble sort is an introductory sorting algorithm that iterates through a list and compares pairings of adjacent elements.

According to the sorting criteria, the algorithm swaps elements to shift elements towards the beginning or end of the list.

By default, a list is sorted if for any element e and position 1 through N:

e1 <= e2 <= e3 ... eN, where N is the number of elements in the list.

For example, bubble sort transforms a list:

[5, 2, 9, 1, 5]
to an ascending order, from lowest to highest:

[1, 2, 5, 5, 9]
We implement the algorithm with two loops.

The first loop iterates as long as the list is unsorted and we assume it's unsorted to start.

Within this loop, another iteration moves through the list. For each pairing, the algorithm asks:

In comparison, is the first element larger than the second element?

If it is, we swap the position of the elements. The larger element is now at a greater index than the smaller element.

When a swap is made, we know the list is still unsorted. The outer loop will run again when the inner loop concludes.

The process repeats until the largest element makes its way to the last index of the list. The outer loop runs until no swaps are made within the inner loop.

Runtime - 
        bubble sort requires multiple passes through the input before producing a sorted list. Each pass through the list will place the next largest value in its proper place.

    We are performing n-1 comparisons for our inner loop. Then, we must go through the list n times in order to ensure that each item in our list has been placed in its proper order.

    The n signifies the number of elements in the list. In a worst case scenario, the inner loop does n-1 comparisons for each n element in the list.

    Therefore we calculate the algorithm's efficiency as:

    \mathcal{O}(n(n-1)) = \mathcal{O}(n(n)) = \mathcal{O}(n^2)O(n(n−1))=O(n(n))=O(n 
    2
     )
    The diagram analyzes the pseudocode implementation of bubble sort to show how we draw this conclusion.

    When calculating the run-time efficiency of an algorithm, we drop the constant (-1), which simplifies our inner loop comparisons to n.

    This is how we arrive at the algorithm's runtime: O(n^2).
    
  Psuedo Code - 
  for each pair(elem1, elem2):
  if elem1 > elem2:
    swap(elem1, elem2)
  else:
    # analyze next set of pairs
    
 Bubble Sort: Compare
Now that we know how to swap items in an array, we need to set up the loops which check whether a swap is necessary.

Recall that Bubble Sort compares neighboring items and if they are out of order, they are swapped.

What does it mean to be "out of order"? Since bubble sort is a comparison sort, we'll use a comparison operator: <.

We'll have two loops:

One loop will iterate through each element in the list.

Within the first loop, we'll have another loop for each element in the list.

Inside the second loop, we'll take the index of the loop and compare the element at that index with the element at the next index. If they're out of order, we'll make a swap!



Merge Sort ---------------------------------------------------------------
Merging
When merging larger pre-sorted lists we build the list similarly to how we did with single-element lists.

    Let's call the two lists left and right. Bothleft and right are already sorted. We want to combine them (to merge them) into a larger sorted list, let's call it both. To accomplish this we'll need to iterate through both with two indices, left_index and right_index.

    At first left_index and right_index both point to the start of their respective lists. left_index points to the smallest element of left (its first element) and right_index points to the smallest element of right.

    Compare the elements at left_index and right_index. The smaller of these two elements should be the first element of both because it's the smallest of both! It's the smallest of the two smallest values.

    Let's say that smallest value was in left. We continue by incrementing left_index to point to the next-smallest value in left. Then we compare the 2nd smallest value in left against the smallest value of right. Whichever is smaller of these two is now the 2nd smallest value of both.

    This process of "look at the two next-smallest elements of each list and add the smaller one to our resulting list" continues on for as long as both lists have elements to compare. Once one list is exhausted, say every element from left has been added to the result, then we know that all the elements of the other list, right, should go at the end of the resulting list (they're larger than every element we've added so far).

the best, worst, and average time complexity are all the same: Θ(N*log(N)). This means an almost-sorted list will take the same amount of time as a completely out-of-order list. This is acceptable because the worst-case scenario, where a sort could stand to take the most time, is as fast as a sorting algorithm can be.

The whole sort takes up two functions:

merge_sort() which is called recursively breaks down an input list to smaller, more manageable pieces. merge() which is a helper function built to help combine those broken-down lists into ordered combination lists.

merge_sort() continues to break down an input list until it only has one element and then it joins that with other single element lists to create sorted 2-element lists. Then it combines 2-element sorted lists into 4-element sorted lists. It continues that way until all the items of the lists are sorted!

Quick Sort ---------------------------------------------------------------

break the array into sub-arrays containing at most one element. One element is sorted by default!

    We choose a single pivot element from the list. Every other element is compared with the pivot, which partitions the array into three groups.

    A sub-array of elements smaller than the pivot.
    The pivot itself.
    A sub-array of elements greater than the pivot.
    The process is repeated on the sub-arrays until they contain zero or one element. Elements in the "smaller than" group are never compared with elements in the "greater than" group. If the smaller and greater groupings are roughly equal, this cuts the problem in half with each partition step!

Quicksort is an unusual algorithm in that the worst case runtime is O(N^2), but the average case is O(N * logN).

We typically only discuss the worst case when talking about an algorithm's runtime, but for Quicksort it's so uncommon that we generally refer to it as O(N * logN).
Steps - 
We established a base case where the algorithm will complete when the start and end pointers indicate a list with one or zero elements
If we haven't hit the base case, we randomly selected an element as the pivot and swapped it to the end of the list
We then iterate through that list and track all the "lesser than" elements by swapping them with the iteration index and incrementing a lesser_than_pointer.
Once we've iterated through the list, we swap the pivot element with the element located at lesser_than_pointer.
With the list partitioned into two sub-lists, we repeat the process on both halves until base cases are met.

We need to partition our list into two sub-lists of greater than or smaller than elements, and we're going to do this "in-place" without creating new lists. Strap in, this is the most complex portion of the algorithm!
 
In Place Quick Sort - 

Because we're doing this in-place, we'll need two pointers. One pointer will keep track of the "lesser than" elements. We can think of it as the border where all values at a lower index are lower in value to the pivot. The other pointer will track our progress through the list.

Let's explore how this will work in an example:

[5, 6, 2, 3, 1, 4]
# we randomly select "3" and swap with the last element
[5, 6, 2, 4, 1, 3]

# We'll use () to mark our "lesser than" pointer
# We'll use {} to mark our progress through the list

[{(5)}, 6, 2, 4, 1, 3]
# {5} is not less than 3, so the "lesser than" pointer doesn't move

[(5), {6}, 2, 4, 1, 3]
# {6} is not less than 3, so the "lesser than" pointer doesn't move

[(5), 6, {2}, 4, 1, 3]
# {2} is less than 3, so we SWAP the values...
[(2), 6, {5}, 4, 1, 3]
# Then we increment the "lesser than" pointer
[2, (6), {5}, 4, 1, 3]

[2, (6), 5, {4}, 1, 3]
# {4} is not less than 3, so the "lesser than" pointer doesn't move

[2, (6), 5, 4, {1}, 3]
# {1} is less than 3, so we SWAP the values...
[2, (1), 5, 4, {6}, 3]
# Then we increment the "lesser than" pointer
[2, 1, (5), 4, {6}, 3]

# We've reached the end of the non-pivot values
[2, 1, (5), 4, 6, {3}]
# Swap the "lesser than" pointer with the pivot...
[2, 1, (3), 4, 6, {5}]
We have successfully partitioned this list. Note that the "sub-lists" are not necessarily sorted, we'll need to recursively run the algorithm on each sub-list, but the pivot has arrived at the correct location within the list.

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
  
  Psuedo Code - 
    # For each element in the search_list
        # if element equal target value then
           # return its index
    # if element is not found then 
    # raise a ValueError
    
 Psuedo Code for Finding Duplicates using linear Search - 
    # For each element in the searchList
    # if element equal target value then
        # Add its index to a list of occurrences
    # if the list of occurrences is empty
        # raise ValueError
    # otherwise
        # return the list occurrences

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

Algorithm - 
    Check the middle value of the dataset.

    If this value matches our target we return the target value index.
    If the middle value is greater than our target

        Begin at step 1 using the left half of the list.
    If the middle value is less than our target

        Begin at step 1 using the right half of the list.

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

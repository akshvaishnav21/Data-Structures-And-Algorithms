# Data-Structures-And-Algorithms
Data Structures And Algorithms using Python
----------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------

Nodes --------------------------------------------------------------------

Nodes Introduction
Nodes are the fundamental building block of many computer science data structures. They form the basis for linked lists, stacks, queues, trees, and more.

An individual node contains data and links to other nodes. Each data structure adds additional constraints or behavior to these features to create the desired structure.

Nodes:

        Contain data, which can be a variety of data types
        Contain links to other nodes. If a node has no links, or they are all None, you have reached the end of the path you were following.
        Can be orphaned if there are no existing links to them

Linked Lists -------------------------------------------------------------

Linked List Introduction
Linked lists are one of the basic data structures used in computer science. They have many direct applications and serve as the foundation for more complex data structures.

The list is comprised of a series of nodes as shown in the diagram. The head node is the node at the beginning of the list. Each node contains data and a link (or pointer) to the next node in the list. The list is terminated when a node's link is null. This is called the tail node.

Since the nodes use links to denote the next node in the sequence, the nodes are not required to be sequentially located in memory. These links also allow for quick insertion and removal of nodes as you will see in future exercises.

Common operations on a linked list may include:

adding nodes
removing nodes
finding a node
traversing (or travelling through) the linked list
Linked lists typically contain unidirectional links (next node), but some implementations make use of bidirectional links (next and previous nodes).

Adding a new node
Adding a new node to the beginning of the list requires you to link your new node to the current head node. This way, you maintain your connection with the following nodes in the list.

Removing a node
If you accidentally remove the single link to a node, that node's data and any following nodes could be lost to your application, leaving you with orphaned nodes.

To properly maintain the list when removing a node from the middle of a linked list, you need to be sure to adjust the link on the previous node so that it points to the following node.

Linked Lists:

        Are comprised of nodes
        The nodes contain a link to the next node (and also the previous node for bidirectional linked lists)
        Can be unidirectional or bidirectional
        Are a basic data structure, and form the basis for many other data structures
        Have a single head node, which serves as the first node in the list
        Require some maintenance in order to add or remove nodes
        The methods we used are an example and depend on the exact use case and/or programming language being used
        
node contains two elements:
        data
        a link to the next node
        


Stacks -------------------------------------------------------------------
# stack.py and stack_node.py
Stacks Introduction
A stack is a data structure which contains an ordered set of data.

Stacks provide three methods for interaction:

Push - adds data to the "top" of the stack
Pop - returns and removes data from the "top" of the stack
Peek - returns data from the "top" of the stack without removing it
Stacks mimic a physical "stack" of objects. Consider a set of gym weights.

Each plate has a weight (the data). The first plate you add, or push, onto the floor is both the bottom and top of the stack. Each weight added becomes the new top of the stack.

At any point, the only weight you can remove, or pop, from the stack is the top one. You can peek and read the top weight without removing it from the stack.

The last plate that you put down becomes the first, and only, one that you can access. This is a Last In, First Out or LIFO structure. A less frequently used term is First In, Last Out, or FILO.

Stacks Implementation
Stacks can be implemented using a linked list as the underlying data structure because it's more efficient than a list or array.

Depending on the implementation, the top of the stack is equivalent to the head node of a linked list and the bottom of the stack is equivalent to the tail node.

A constraint that may be placed on a stack is its size. This is done to limit and quantify the resources the data structure will take up when it is "full".

Attempting to push data onto an already full stack will result in a stack overflow. Similarly, if you attempt to pop data from an empty stack, it will result in a stack underflow.

Stacks:

        Contain data nodes
        Support three main operations
        Push adds data to the top of the stack
        Pop removes and provides data from the top of the stack
        Peek reveals data on the top of the stack
        Implementations include a linked list or array
        Can have a limited size
        Pushing data onto a full stack results in a stack overflow
        Stacks process data Last In, First Out (LIFO)
 a Stack class that can:

        add a new item to the top via a push() method
        remove an item from the top and returns its value with a pop() method
        return the value of the top item using a peek() method
        allows a stack instance to maintain an awareness of its size to prevent stack "overflow"
  
Queues -------------------------------------------------------------------

Queues Introduction
A queue is a data structure which contains an ordered set of data.

Queues provide three methods for interaction:

Enqueue - adds data to the "back" or end of the queue
Dequeue - provides and removes data from the "front" or beginning of the queue
Peek - reveals data from the "front" of the queue without removing it
This data structure mimics a physical queue of objects like a line of people buying movie tickets. Each person has a name (the data). The first person to enqueue, or get into line, is both at the front and back of the line. As each new person enqueues, they become the new back of the line.

When the cashier serves someone, they begin at the front of the line (or people would get very mad!). Each person served is dequeued from the front of the line, they purchase a ticket and leave.

If they just want to know who is next in line, they can peek and get their name without removing them from the queue.

The first person in the queue is the first to be served. Queues are a First In, First Out or FIFO structure.

Queues Implementation - 

Queues can be implemented using a linked list as the underlying data structure. The front of the queue is equivalent to the head node of a linked list and the back of the queue is equivalent to the tail node.

Since operations are only allowed affecting the front or back of the queue, any traversal or modification to other nodes within the linked list is disallowed. Since both ends of the queue must be accessible, a reference to both the head node and the tail node must be maintained.

One last constraint that may be placed on a queue is its length. If a queue has a limit on the amount of data that can be placed into it, it is considered a bounded queue.

Similar to stacks, attempting to enqueue data onto an already full queue will result in a queue overflow. If you attempt to dequeue data from an empty queue, it will result in a queue underflow.

Queues:

        Contain data nodes
        Support three main operations:
        Enqueue adds data to the back of the queue
        Dequeue removes and provides data from the front of the queue
        Peek provides data on the front of the queue
        Can be implemented using a linked list or array
        Bounded queues have a limited size.
        Enqueueing onto a full queue causes a queue overflow
        Queues process data First In, First Out (FIFO)
        
enqueue() method - 

There are three scenarios that we are concerned with when adding a node to the queue:

The queue is empty, so the node we're adding is both the head and tail of the queue
The queue has at least one other node, so the added node becomes the new tail
The queue is full, so the node will not get added because we don't want queue "overflow"

For dequeue, there are three scenarios that we will take into account:

The queue is empty, so we cannot remove or return any nodes lest we run into queue "underflow"
The queue has one node, so when we remove it, the queue will be empty and we need to reset the queue's head and tail to None
The queue has more than one node, and we just remove the head node and reset the head to the following node.



Hash Map -----------------------------------------------------------------

A hash map is:

Built on top of an array using a special indexing system.
A key-value storage with fast assignments and lookup.
A table that represents a map from a set of keys to a set of values.
Hash maps accomplish all this by using a hash function, which turns a key into an index into the underlying array.

A hash collision is when a hash function returns the same index for two different keys.

There are different hash collision strategies. Two important ones are separate chaining, where each array index points to a different data structure, and open addressing, where a collision triggers a probing sequence to find where to store the value for a given key.

Hash maps are efficient key-value stores. They are capable of assigning and retrieving data in the fastest way possible for a data structure. This is because the underlying data structure that they use is an array. A value is stored at an array index determined by plugging the key into a hash function.

In Python we don’t have an array data structure that uses a contiguous block of memory. We are going to simulate an array by creating a list and keeping track of the size of the list with an additional integer variable. This will allow us to design something that resembles a hash map. This is somewhat elaborate for the actual storage of a key-value pair, but it helps to remember that the purpose of this lesson is to gain a deeper understanding of the structure as it is constructed. For real-world use cases in which a key-value store is needed, Python offers a built-in hash table implementation with dictionaries.



Hash Functions - 

A hash function takes a string (or some other type of data) as input and returns an array index as output. In order for it to return an array index, our hash map implementation needs to know the size of our array. If the array we are saving values into only has 4 slots, our hash map's hashing method should not return an index bigger than that.

In order for our hash map implementation to guarantee that it returns an index that fits into the underlying array, the hash function will first compute a value using some scoring metric: this is the hash value, hash code, or just the hash. Our hash map implementation then takes that hash value mod the size of the array. This guarantees that the value returned by the hash function can be used as an index into the array we're using.

It is actually a defining feature of all hash functions that they greatly reduce any possible inputs (any string you can imagine) into a much smaller range of potential outputs (an integer smaller than the size of our array). For this reason hash functions are also known as compression functions.

Much like an image that has been shrunk to a lower resolution, the output of a hash function contains less data than the input. Because of this hashing is not a reversible process. With just a hash value it is impossible to know for sure the key that was plugged into the hashing function.

Open Addressing: Linear Probing
        Another popular hash collision strategy is called open addressing. In open addressing we stick to the array as our underlying data structure, but we continue looking for a new index to save our data if the first result of our hash function has a different key's data.

        A common open method of open addressing is called probing. Probing means continuing to find new array indices in a fixed sequence until an empty index is found.

        Suppose we want to associate famous horses with their owners. We want our first key, “Bucephalus”, to store our first value, “Alexander the Great”. Our hash function returns an array index 3 and so we save “Alexander the Great”, along with our key “Bucephalus”, into the array at index 3.

        After that, we want to store “Seabiscuit"s owner "Charles Howard". Unfortunately “Seabiscuit” also has a hash value of 3. Our probing method adds one to the hash value and tells us to continue looking at index 4. Since index 4 is open we store "Charles Howard" into the array at index 4. Because "Seabiscuit" has a hash of 3 but "Charles Howard" is located at index 4, we must also save "Seabiscuit" into the array at that index.

        When we attempt to look up "Seabiscuit" in our Horse Owner's Hash Map, we first check the array at index 3. Upon noticing that our key (Seabiscuit) is different from the key sitting in index 3 (Bucephalus), we realize that this can't be the value we were looking for at all. Only by continuing to the next index do we check the key and notice that at index 4 our key matches the key saved into the index 4 bucket. Realizing that index 4 has the key "Seabiscuit" means we can retrieve the information at that location, Seabiscuit's owner's name: Charles Howard.
        


Trees - ------------------------------------------------------------------

Trees Introduction
Trees are an essential data structure for storing hierarchical data with a directed flow.

Similar to linked lists and graphs, trees are composed of nodes which hold data. 
Nodes also store references to zero or more other tree nodes. Data moves down from node to node. We depict those references as lines drawn between circles.

Trees are often displayed with a single node at the top and connected nodes branching downwards.

Binary Search Tree - 

Constraints are placed on the data or node arrangement of a tree to solve difficult problems like efficient search.

A binary tree is a type of tree where each parent can have no more than two children, known as the left child and right child.

Further constraints make a binary search tree:

Left child values must be lesser than their parent.
Right child values must be greater than their parent.
The constraints of a binary search tree allow us to search the tree efficiently. At each node, we can discard half of the remaining possible values!

Trees are useful for modeling data that has a hierarchical relationship which moves in the direction from parent to child. No child node will have more than one parent.

To recap some terms:

root: A node which has no parent. One per tree.
parent: A node which references other nodes.
child: Nodes referenced by other nodes.
sibling: Nodes which have the same parent.
leaf: Nodes which have no children.
level: The height or depth of the tree. Root nodes are at level 1, their children are at level 2, and so on.

Class TreeNodes:

        have a value
        have a reference to zero or more other TreeNodes
        can add a node as a child
        can remove a child
        can traverse (or travel through) connected nodes

in our implementation:

        Trees are a Python class called TreeNode.
        A TreeNode has two properties, value and children.
        Nodes hold any type of data inside value.
        children is a list, which can be empty or hold other instances of TreeNode.
        We add to children by using the list method .append.
        We remove from children by filtering the list.
        
 


Heaps --------------------------------------------------------------------

Heaps are used to maintain a maximum or minimum value in a dataset. Heaps tracking the maximum or minimum value are max-heaps or min-heaps. Think of the min-heap as a binary tree with two qualities:

        The root is the minimum value of the dataset.
        Every child's value is greater than its parent.
        
These two properties are the defining characteristics of the min-heap. By maintaining these two properties, we can efficiently retrieve and update the minimum value.

We can picture min-heaps as binary trees, where each node has at most two children. As we add elements to the heap, they're added from left to right until we've filled the entire level.

Conceptually, the tree representation is beneficial for understanding. Practically, we implement heaps in a sequential data structure like an array or list for efficiency.

Notice how by filling the tree from left to right; we're leaving no gaps in the array. The location of each child or parent derives from a formula using the index.

        left child: (index * 2) + 1
        right child: (index * 2) + 2
        parent: (index - 1) / 2 — not used on the root!
       
Defining Min-Heap
Our MinHeap class will store two pieces of information:

A Python list of the elements within the heap.
A count of the elements within the heap.

Adding an Element: Heapify Up I
The min-heap is no good if all it ever contains is None. Let's build the functionality to add elements while maintaining the heap properties.

Our MinHeap will abide by two principles:

The element at index 1 is the minimum value in the entire list.
Every "child" element in the list must be larger than their "parent".
The first element we add to the list will be the minimum because there are no other elements. We'll tackle the trickier aspects of maintaining these principles in the coming lessons.

We need to make sure that every child is greater in value than their parent. Say we add an element to the following heap:

print(heap.heap_list)
# [None, 10, 13, 21, 61, 22, 23, 99]
heap.add(12)

# ( new_element )
# { parent_element }
# [None, 10, 13, 21, {61}, 22, 23, 99, (12)]
Oh no! We've violated the heap property: 12's parent is 61, the parent element is greater than the child.
we can fix this. We'll exchange the parent and the child elements.

# [None, 10, 13, 21, {61}, 22, 23, 99, (12)]
# SWAP 12 and 61
# [None, 10, 13, 21, (12), 22, 23, 99, {61}]
12's parent is now 13, they're close but the parent element is still greater than the child. Keep on swappin'!

# [None, 10, {13}, 21, (12), 22, 23, 99, 61]
# SWAP 12 and 13
# [None, 10, (12), 21, {13}, 22, 23, 99, 61]
Okay, you can let out that sigh of relief. We've restored the heap properties!

# [None, {10}, (12), 21, 13, 22, 23, 99, 61]
# The child, 12, is greater than the parent, 10!
Let's recap our strategy for .heapify_up():

        # start at the last element of the list
        # while there's a parent element available:
          # if the parent element is greater:
            # swap the elements
          # set the target element index to be the parent's index

.heapify_down(), Here's the general shape of the method:

 # starting with our first element...
 # while there's at least one child present:
   # get the smallest child's index
   # compare the smallest child with our element
     # if our element is larger, swap with child
   # regardless, set our element index to be the child
   
 
 To recap: MinHeap tracks the minimum element as the element at index 1 within an internal Python list.

        When adding elements, we use .heapify_up() to compare the new element with its parent, making swaps if it violates the heap property: children must be greater than their parents.

        When removing the minimum element, we swap it with the last element in the list. Then we use .heapify_down() to compare the new root with its children, swapping with the smaller child if necessary.

        Heaps are so useful because they're efficient in maintaining their heap properties. 
        
        

Graphs -------------------------------------------------------------------
#vertex.py, graphs and graph.py

Representing Graphs
We typically represent the vertex-edge relationship of a graph in two ways: an adjacency list or an adjacency matrix.

An adjacency matrix is a spreadsheet. Across the top, every vertex in the graph appears as a column. Down the side, every vertex appears again as a row. Edges can be bi-directional, so each vertex is listed twice.

To find an edge between B and P, we would look for the B row and then trace across to the P column. The contents of this cell represent a possible edge.

Our diagram uses 1 to mark an edge, 0 for the absence of an edge. In a weighted graph, the cell contains the cost of that edge.

In an adjacency list, each vertex contains a list of the vertices where an edge exists. To find an edge, one looks through the list for the desired vertex.

Graphs are an essential data structure in computer science for modeling networks. Let's review some key terms:

vertex: A node in a graph.
edge: A connection between two vertices.
adjacent: When an edge exists between vertices.
path: A sequence of one or more edges between vertices.
disconnected: Graph where at least two vertices have no path connecting them.
weighted: Graph where edges have an associated cost.
directed: Graph where travel between vertices can be restricted to a single direction.
cycle: A path which begins and ends at the same vertex.
adjacency matrix: Graph representation where vertices are both the rows and the columns. Each cell represents a possible edge.
adjacency list: Graph representation where each vertex has a list of all the vertices it shares an edge with.

two classes, Vertex and Graph,functionality we require from these classes:

Vertex stores some data.
Vertex stores the edges to connected vertices and their weight.
Vertex can add a new edge to its collection.
Graph stores all the vertices.
Graph knows if it is directed or undirected.
Graph can add a new vertex to its collection.
Graph can add a new edge between stored vertices.
Graph can tell whether a path exists between stored vertices.



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


Counting Sort-------------------------------------------------------------

In Counting sort, the frequencies of distinct elements of the array to be sorted is counted and stored in an auxiliary array, by mapping its value as an index of the auxiliary array.

Algorithm:

Let's assume that, array  of size  needs to be sorted.

Initialize the auxillary array  as . 
Note: The size of this array should be .
Traverse array  and store the count of occurrence of each element in the appropriate index of the  array, which means, execute Aux[A[i]]++ for each , where  ranges from .
Initialize the empty array 
Traverse array  and copy  into  for  number of times where .
Note: The array  can be sorted by using this algorithm only if the maximum value in array  is less than the maximum size of the array . Usually, it is possible to allocate memory up to the order of a million . If the maximum value of  exceeds the maximum memory- allocation size, it is recommended that you do not use this algorithm. Use either the quick sort or merge sort algorithm.

Bucket Sort --------------------------------------------------------------

Bucket sort is a comparison sort algorithm that operates on elements by dividing them into different buckets and then sorting these buckets individually. Each bucket is sorted individually using a separate sorting algorithm or by applying the bucket sort algorithm recursively. Bucket sort is mainly useful when the input is uniformly distributed over a range.

Assume one has the following problem in front of them:

One has been given a large array of floating point integers lying uniformly between the lower and upper bound. This array now needs to be sorted. A simple way to solve this problem would be to use another sorting algorithm such as Merge sort, Heap Sort or Quick Sort. However, these algorithms guarantee a best case time complexity of . However, using bucket sort, the above task can be completed in O(n) time. Let's have a closer look at it.

Consider one needs to create an array of lists, i.e of buckets. Elements now need to be inserted into these buckets on the basis of their properties. Each of these buckets can then be sorted individually using Insertion Sort. Consider the pseudo code to do so:

void bucketSort(float[] a,int n)
{
    for(each floating integer 'x' in n)
    {
        insert x into bucket[n*x]; 
    }
    for(each bucket)
    {
        sort(bucket);
    }
}
Time Complexity:

If one assumes that insertion in a bucket takes O(1) time, then steps 1 and 2 of the above algorithm take O(n) time.

divide the elements of this array into buckets on the basis of the number of set bits in its binary representation.

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


Radix Sort ------------------------------------------------------------------

RADIX SORT: 
What Is A Radix
Quick, which number is bigger: 1489012 or 54? It’s 1489012, but how can you tell? It has more digits so it has to be larger, but why exactly is that the case?

Our number system was developed by 8th century Arabic mathematicians and was successful because it made arithmetic operations more sensible and larger numbers easier to write and comprehend.

The breakthrough those mathematicians made required defining a set of rules for how to depict every number. First we decide on an alphabet: different glyphs, or digits, that we’ll use to write our numbers with. The alphabet that we use to depict numbers in this system are the ten digits 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9. We call the length of this alphabet our radix (or base). So for our decimal system, we have a radix of 10.

Next we need to understand what those digits mean in different positions. In our system we have a ones place, a tens place, a hundreds place and so on. So what do digits mean in each of those places?

This is where explaining gets a little complicated because the actual knowledge might feel very fundamental. There’s a difference, for instance, between the digit '6' and the actual number six that we represent with the digit '6'. This difference is similar to the difference between the letter 'a' (which we can use in lots of words) and the word 'a'.

But the core of the idea is that we use these digits to represent different values when they're used in different positions. The digit 6 in the number 26 represents the value 6, but the digit 6 used in the number 86452 represents the value 6000.

Base Numbering Systems
The value of different positions in a number increases by a multiplier of 10 in increasing positions. This means that a digit '8' in the rightmost place of a number is equal to the value 8, but that same digit when shifted left one position (i.e., in 80) is equal to 10 * 8. If you shift it again one position you get 800, which is 10 * 10 * 8.

This is where it's useful to incorporate the shorthand of exponential notation. It's important to note that 100 is equal to 1. Each position corresponds to a different exponent of 10.

So why 10? It's a consequence of how many digits are in our alphabet for numbering. Since we have 10 digits (0-9) we can count all the way up to 9 before we need to use a different position. This system that we used is called base-10 because of that.

Sorting By Radix
So how does a radix sort use this base numbering system to sort integers? First, there are two different kinds of radix sort: most significant digit, or MSD, and least significant digit, or LSD.

Both radix sorts organize the input list into ten "buckets", one for each digit. The numbers are placed into the buckets based on the MSD (left-most digit) or LSD (right-most digit). For example, the number 2367 would be placed into the bucket "2" for MSD and into "7" for LSD.

This bucketing process is repeated over and over again until all digits in the longest number have been considered. The order within buckets for each iteration is preserved. For example, the numbers 23, 25 and 126 are placed in the "3", "5", and "6" buckets for an initial LSD bucketing. On the second iteration of the algorithm, they are all placed into the "2" bucket, but the order is preserved as 23, 25, 126.

Radix Sort Performance
The most amazing feature of radix sort is that it manages to sort a list of integers without performing any comparisons whatsoever. We call this a non-comparison sort.

This makes its performance a little difficult to compare to most other comparison-based sorts. Consider a list of length n. For each iteration of the algorithm, we are deciding which bucket to place each of the n entries into.

How many iterations do we have? Remember that we continue iterating until we examine each digit. This means we need to iterate for how ever many digits we have. We'll call this average number of digits the word-size or w.

This means the complexity of radix sort is O(wn). Assuming the length of the list is much larger than the number of digits, we can consider w a constant factor and this can be reduced to O(n).

radix sort:

        A radix is the base of a number system. For the decimal number system, the radix is 10.
        Radix sort has two variants - MSD and LSD
        Numbers are bucketed based on the value of digits moving left to right (for MSD) or right to left (for LSD)
        Radix sort is considered a non-comparison sort
        The performance of radix sort is O(n)
        
Finding the Max Exponent
In our version of least significant digit radix sort, we're going to utilize the string representation of each integer. This, combined with negative indexing, will allow us to count each digit in a number from right-to-left.

Some other implementations utilize integer division and modular arithmetic to find each digit in a radix sort, but our goal here is to build an intuition for how the sort works.

Our first step is going to be finding the max_exponent, which is the number of digits long the largest number is. We're going to find the largest number, cast it to a string, and take the length of that string.

Setting Up For Sorting
In this implementation, we're going to build the radix sort naturally, from the inside out. The first step we're going to take is going to be our inner-most loop, so that we know we'll be solid when we're iterating through each of the exponents.

Bucketing Numbers
The least significant digit radix sort algorithm takes each number in the input list, looks at the digits of that number in order from right to left, and incrementally stuffs each number into the bucket corresponding to the value of that digit.

First we're going to write this logic for the least significant digit, then we're going to loop over the code we write to do that for every digit.

Rendering the List
For every iteration, radix sort renders a version of the input list that is sorted based on the digit that was just looked at. At first pass, only the ones digit is sorted. At the second pass, the tens and the ones are sorted. This goes on until the digits in the largest position of the largest number in the list are all sorted, and the list is sorted at that time.

Here we'll be rendering the list, at first, it will just return the list sorted so just the ones digit is sorted.

Iterating through Exponents
We have the interior of our radix sort, which right now goes through a list and sorts it by the first digit in each number. That's a pretty great start actually. It won't be hard for us to go over every digit in a number now that we can already sort by a given digit.

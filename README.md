# This repo is for DSA problem and it's solution.

# 1. Singly Linked List :

-- The 1st program or code is for implementation of singly linked list using Python.
-- I have created two different class in this, 1 for creating a Node and another 1 for managing node using some function.
-- Functions are
-- 1. insertionAtBeg(value) :- this function is used to add node at the begining of linked list.
--- eg. insertionAtBeg(10) >>> 10
-- 2. insertionAtEnd(value) :- this function is used to add node at the end of linked list.
--- eg. insertionAtEnd(20) >>> 10 20
-- 3. insertionAtMid(value, location) :- this function is used to add node at the middle of linked list based on the given location(value of a node already present in linked list) else it add the node at the end of linked list by default.
--- eg. insertionAtMid(15,30) >>> 10 20 15
-- 4. deleteNode(value) :- this function is used to delete a node based on the value of the node from the linked list.
--- eg. deleteNode(20) >>> 10 15
-- 5. printNode() :- this function is used to print the nodes of linked list.

# 2. Doubly Linked List :

-- The 2nd program or code is for implementation of doubly linked list using Python.
-- I have created two different class in this, 1 for creating a Node and another 1 for managing node using some function.
-- Functions are
-- 1. insertionAtBeg(value) :- this function is used to add node at the begining of linked list.
--- eg. insertionAtBeg(10) >>> 10
-- 2. insertionAtEnd(value) :- this function is used to add node at the end of linked list.
--- eg. insertionAtEnd(20) >>> 10 20
-- 3. insertionAtMid(value, location) :- this function is used to add node at the middle of linked list based on the given location(value of a node already present in linked list) else it add the node at the end of linked list by default.
--- eg. insertionAtMid(15,30) >>> 10 20 15
-- 4. deleteNode(value) :- this function is used to delete a node based on the value of the node from the linked list.
--- eg. deleteNode(20) >>> 10 15
-- 5. printNode() :- this function is used to print the nodes of linked list.

# 3. Circular Singly Linked List :

-- The 3rd program or code is for implementation of circular singly linked list using Python.
-- I have created two different class in this, 1 for creating a Node and another 1 for managing node using some function.
-- Functions are
-- 1. insertionAtBeg(value) :- this function is used to add node at the begining of linked list.
--- eg. insertionAtBeg(10) >>> 10
-- 2. insertionAtEnd(value) :- this function is used to add node at the end of linked list.
--- eg. insertionAtEnd(20) >>> 10 20
-- 3. insertionAtMid(value, location) :- this function is used to add node at the middle of linked list based on the given location(value of a node already present in linked list) else it add the node at the end of linked list by default.
--- eg. insertionAtMid(15,30) >>> 10 20 15
-- 4. deleteNode(value) :- this function is used to delete a node based on the value of the node from the linked list.
--- eg. deleteNode(20) >>> 10 15
-- 5. printNode() :- this function is used to print the nodes of linked list.

# 4. Circular Doubly Linked List :

-- The 4th program or code is for implementation of circular doubly linked list using Python.
-- I have created two different class in this, 1 for creating a Node and another 1 for managing node using some function.
-- Functions are
-- 1. insertionAtBeg(value) :- this function is used to add node at the begining of linked list.
--- eg. insertionAtBeg(10) >>> 10
-- 2. insertionAtEnd(value) :- this function is used to add node at the end of linked list.
--- eg. insertionAtEnd(20) >>> 10 20
-- 3. insertionAtMid(value, location) :- this function is used to add node at the middle of linked list based on the given location(value of a node already present in linked list) else it add the node at the end of linked list by default.
--- eg. insertionAtMid(15,30) >>> 10 20 15
-- 4. deleteNode(value) :- this function is used to delete a node based on the value of the node from the linked list.
--- eg. deleteNode(20) >>> 10 15
-- 5. printNode() :- this function is used to print the nodes of linked list.

# Definition

1. Singly Linked List :-
   -- SLL nodes contains 2 field -data field and next link field.
   -- In SLL, the traversal can be done using the next node link only. Thus traversal is possible in one direction only.
   -- Supports lesser number of operations in constant time
   -- The SLL occupies less memory than DLL as it has only 2 fields.
   -- Complexity of deletion with a given node is O(n), because the previous node needs to be known, and traversal takes O(n)
   -- A singly linked list consumes less memory as compared to the doubly linked list.

2. Doubly Linked List :-
   -- DLL nodes contains 3 fields -data field, a previous link field and a next link field.
   -- In DLL, the traversal can be done using the previous node link or the next node link. Thus traversal is possible in both directions
   (forward and backward).
   -- Supports additional operations like insert before, delete previous, delete current node and delete last in O(1) time. Since it supports delete last, it is used to efficiently implement Deque.
   -- The DLL occupies more memory than SLL as it has 3 fields.
   -- Complexity of deletion with a given node is O(1) because the previous node can be accessed easily
   -- The doubly linked list consumes more memory as compared to the singly linked list.

3. Circular Linked List :-

   (a.) Circular Singly Linked List :-
   -- In Circular Singly Linked List, each node has just one pointer called the "next" pointer. The next pointer of the last node points back to the first node and this results in forming a circle. In this type of Linked list, we can only move through the list in one direction.

   (b.) Circular Doubly Linked List :-
   -- In circular doubly linked list, each node has two pointers prev and next, similar to doubly linked list. The prev pointer points to the previous node and the next points to the next node. Here, in addition to the last node storing the address of the first node, the first node will also store the address of the last node.

   Advantage :-
   -- Efficient Traversal
   -- No Null Pointers / References
   -- Useful for Repetitive Tasks
   -- Insertion at Beginning or End is O(1)
   -- Uniform Traversal
   -- Efficient Memory Utilization

   Disadvantage :-
   -- Complex Implementation
   -- Infinite Loop Risk
   -- Harder to Debug
   -- Deletion Complexity
   -- Memory Overhead (for Doubly Circular LL)
   -- Not Cache Friendly

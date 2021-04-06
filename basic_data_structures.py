# 4.1 ----------------- OBJECTIVES

'''
To understand the abstract data types stack, queue, deque, and list.

To be able to implement the ADTs stack, queue, and deque using Python lists.

To understand the performance of the implementations of basic linear data structures.

To understand prefix, infix, and postfix expression formats.

To use stacks to evaluate postfix expressions.

To use stacks to convert expressions from infix to postfix.

To use queues for basic timing simulations.

To be able to recognize problem properties where stacks, queues, and deques are appropriate data structures.

To be able to implement the abstract data type list as a linked list using the node and reference pattern.

To be able to compare the performance of our linked list implementation with Python’s list implementation.
'''

# 4.2 ----------------- WHAT ARE LINEAR STRUCTURES?

'''
Linear Data Structures: 
- Data collections whose items are ordered depending on how they are add or removed.
  Once an item is added, it stays in that position relative to the other elements that came before or after it.

  - Stacks
  - Queues
  - Deques
  - Lists

- Can be thought of as having two ends. Sometimes these ends are referred to as the...
  "left" & "right" or "front" & "rear" or "top" & "bottom". 
  The names given to the ends aren't significant. 

- What distinguishes one linear structure from another is the way in which items are added and removed.
  In particular, the location where these additions and removals occur. 
  Example: 
  Some structures might only allow new items to be added at only one end.
  Some structures might allow items to be removed from either end. Just depends. 
'''
# 4.3 ----------------- WHAT IS A STACK?

'''
Stack:
- An ordered collection of items where the addition of new items and the removal of existing items always takes place at the same end.
  This end is commonly referred to as the "top".
  The end opposite of the top is known as the "base".
  Example: 
  Think of a stack of books.

- The base of the stack is significant since items stored in the stack that are closer to the base represent those that have beeen in 
the stack the longest.

- LIFO: Last-in first-out
  - The most recently added item is the one that is in position to be removed first.
  - This principle provides an ordering based on length of time in the collection. 
  - Newer items are near the top, while older items are near the base. 
  


'''



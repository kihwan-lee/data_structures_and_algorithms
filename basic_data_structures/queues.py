# 4.10 ----------------- WHAT IS A QUEUE?

'''
Queue:
  - An ordered collection of items where the addition of new items happens at one end, called the "rear".
  - The removal of existing items occurs at the other end, commonly called the "front".
  - As an element enters the queue it starts at the rear and makes its way toward the front, waiting until that time when it is the next element to be removed.
  - There is no jumping in the middle and no leaving before you have waited the necessary amount of time to get to the front.


FIFO: First In, First Out
  - The most recently added item in the queue must wait at the end of the collection. 
  - The item that has been in the collection the longest is at the front. 
  - Also known as "first come, first served".

Examples:
  - Waiting in line for a movie, check-out line at a grocery store, waiting in a cafeteria line

Strength of Queues:
  - If you, your friend, and your roommate all send information to the printer, it will print out the information it received first
  - Also commonly used in multi-threading and concurrency situations to keep track of what tasks are waiting to be performed and making sure we take them in that order. 
'''

# 4.11 ----------------- THE QUEUE ABSTRACT DATA TYPE

'''
Queue() : Creates a new queue that is empty. It needs no parameters and returns an empty queue.

enqueue(item) : Adds a new item to the rear of the queue. It needs the item and returns nothing.

dequeue() : Removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.

isEmpty() : Tests to see whether the queue is empty. It needs no parameters and returns a boolean value.

size() : Returns the number of items in the queue. It needs no parameters and returns an integer.
'''

# 4.12 ----------------- IMPLEMENTING A QUEUE IN PYTHON

# class Queue:
#   def __init__(self):
#     self.items = []

#   def is_empty(self):
#     return self.items == []

#   def enqueue(self, item):
#     self.items.insert(0, item)

#   def dequeue(self):
#     return self.items.pop()

#   def size(self):
#     return len(self.items)

# q=Queue()	
# q.enqueue(4)
# q.enqueue('dog')
# print(q.size())
# q.enqueue(True)
# print(q.size())
# print(q.is_empty())
# q.dequeue()
# print(q.size())

# 4.13 ----------------- SIMULATION: HOT POTATO


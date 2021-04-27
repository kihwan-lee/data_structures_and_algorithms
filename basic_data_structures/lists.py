# 4.19 ----------------- LISTS

'''
List:
- Two Types: Unordered & Ordered
  - Unordered List:
    - Collection of items where each item holds a relative position with respect to the others. 
- 

Strength of Lists:

'''

# 4.20 ----------------- THE UNORDERED LIST ABSTRACT DATA TYPE

'''
List() : Creates a new list that is empty. It needs no parameters and returns an empty list.

add(item) : Adds a new item to the list. It needs the item and returns nothing. Assume the item is not already in the list.

remove(item) : Removes the item from the list. It needs the item and modifies the list. Assume the item is present in the list.

search(item) : Searches for the item in the list. It needs the item and returns a boolean value.

isEmpty() : Tests to see whether the list is empty. It needs no parameters and returns a boolean value.

size() : Returns the number of items in the list. It needs no parameters and returns an integer.

append(item) : Adds a new item to the end of the list making it the last item in the collection. It needs the item and returns nothing. Assume the item is not already in the list.

index(item) : Returns the position of item in the list. It needs the item and returns the index. Assume the item is in the list.

insert(pos,item) : Adds a new item to the list at position pos. It needs the item and returns nothing. Assume the item is not already in the list and there are enough existing items to have position pos.

pop() : Removes and returns the last item in the list. It needs nothing and returns an item. Assume the list has at least one item.

pop(pos) : Removes and returns the item at position pos. It needs the position and returns the item. Assume the item is in the list.
'''

# 4.21 ----------------- IMPLEMENTING AN UNORDERED LIST: LINKED LISTS

'''
In order to implement an unordered list, we will construct what is commonly known as a LINKED LIST.
- If we can maintain some explicit information in each item, namely the location of the next item, then the relative position of each item can be expressed by simply following the link from one item to the next.
- It is important to note that the location of the first item of the list must be explicitly specified. 
- Once we know where the first item is, the first item can tell us where the second is, and so on. 
- The external reference is often referred to as the head of the list. Similarly, the last item needs to know that there is no next item.
'''

# 4.21.1 ----------------- THE NODE CLASS

'''
Node:
- Basic building block for the linked list implementation
- Each node object must hold at least two pieces of information
  - First, the node must contain the list item itself a.k.a the data field of the node
  - Second, each node must hold a reference to the next node
'''


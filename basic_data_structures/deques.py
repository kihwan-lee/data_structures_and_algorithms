from pythonds.basic import Deque
# 4.15 ----------------- WHAT IS A DEQUE?

'''
Deque:
- Also known as a double-ended queue, is an ordered collection of items similar to the queue. 
- It has two ends, a front an a rear, and the items remain positioned in the collection. 
- Main difference is the unrestrictive nature of adding and removing items.
  - New items can be added at either the front of the rear. 
  - Likewise, existing items can be removed from either end.


Strength of Deques:
- In a sense, it provides all the capabilites of stacks and queues in a single data structure.
'''

# 4.16 ----------------- THE DEQUE ABSTRACT DATA TYPE

'''
Deque() : Creates a new deque that is empty. It needs no parameters and returns an empty deque.

addFront(item) : Adds a new item to the front of the deque. It needs the item and returns nothing.

addRear(item) : Adds a new item to the rear of the deque. It needs the item and returns nothing.

removeFront() : Removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.

removeRear() : Removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.

isEmpty() : Tests to see whether the deque is empty. It needs no parameters and returns a boolean value.

size() : Returns the number of items in the deque. It needs no parameters and returns an integer.
'''

# 4.17 ----------------- IMPLEMENTING A DEQUE IN PYTHON

class Deque:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def addFront(self, item):
    self.items.append(item)

  def addRear(self, item):
    self.items.insert(0,item)

  def removeFront(self):
    return self.items.pop()

  def removeRear(self):
    return self.items.pop(0)

  def size(self):
    return len(self.items)

# 4.18 ----------------- PALINDROME - CHECKER

'''
Palindrome:
- A string that reads the same forward and backward.
- Write an algorithm to input a string of characters and check whether it is a palindrome.

Example:
radar
toot
madam
'''

def pal_checker(a_string):
  char_deque = Deque()

  # Store the characters of the string into a Deque
  for ch in a_string:
    # Process the string from left to right and add each character to the rear of the deque
    char_deque.addRear(ch)

  still_Equal = True

  # Checks if deque is down to one character and is true
  while char_deque.size() > 1 and still_Equal:
    # Remove both front and rear, compare them, and continue only if they match. Keep matching first and last items, until we either run out of characters or be left with size = 1 depending on whether the length of string was even or odd. 
    first = char_deque.removeFront()
    last = char_deque.removeRear()
    if first != last:
      still_Equal = False
    
  return still_Equal

print(pal_checker("lsdkjfskf"))
print(pal_checker("radar"))

from pythonds.basic import Stack
# 4.3 ----------------- WHAT IS A STACK?

'''
Stack:
- An ordered collection of items where the addition of new items and the removal of existing items always takes place at the same end.
  This end is commonly referred to as the "top".
  The end opposite of the top is known as the "base".
  Example: 
  Think of a stack of books.
  If we want to add one, we add it to the top, because it is much easier (and faster) than lifting the whole stack of books up and adding one to the bottom.

- The base of the stack is significant since items stored in the stack that are closer to the base represent those that have beeen in 
the stack the longest.

- LIFO: Last-in first-out
  - The most recently added item is the one that is in position to be removed first.
  - This principle provides an ordering based on length of time in the collection. 
  - Newer items are near the top, while older items are near the base. 

Strength of Stacks:
- GREAT for reversing the order of items. 
- Keeping track of state or when things have occured. 
'''

# 4.4 ----------------- THE STACK ABSTRACT DATA TYPE

'''
Stack() : Creates a new stack that is empty. It needs no parameters and returns an empty stack.

push(item) : Adds a new item to the top of the stack. It needs the item and returns nothing.

pop() : Removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.

peek() : Returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.

isEmpty() : Tests to see whether the stack is empty. It needs no parameters and returns a boolean value.

size() : Returns the number of items on the stack. It needs no parameters and returns an integer.
'''

# 4.5 ----------------- IMPLEMENTATING A STACK IN PYTHON

class Stack:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[len(self.items)-1]

  def size(self):
    return len(self.items)


def reverse_string(mystr):
  s = list(mystr)
  n = []
  print(s)
  while len(s) > 0:
    item = s.pop()
    n.append(item)

  print(n)

reverse_string('apple')

# Didn't really implement it but it doesn't seem too important because I just learn how to use a list effectively.

# 4.6 ----------------- SIMPLE BALANCED PARENTHESES

'''
Balanced Parentheses:
- Means that each opening symbol has a corresponding closing symbol and the pairs of parentheses are properly nested.

Balanced Example:
(()()()())
(((())))
(()((())()))

Not Balanced Example:
(((((())
()))
(()()(()
'''

'''
Challenge:
  - Write an algorithm that will read a string of parentheses from left to right and decide whether the symbols are balanced. 
    - As you process symbols from left to right, the most recent opening parenthesis must match the next closing symbol. 
    - Also, the first opening symbol processed may have to wait until the very last symbol for its match. 
    - Closing symbols match opening symbols in the reverse order of their appearance; they match from the inside out. 
'''
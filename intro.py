#1.2 ----------------- GETTING STARTED 

#1.3 ----------------- WHAT IS COMPUTER SCIENCE?

'''
Computer science is the study of problems, problem-solving, and the solutions that come out of the problem-solving process. 

We say that a problem is computable if an algorithm exists for solving it.

Algorithm:
- Step by step list of instructions for solving and unstrance of the problem that might arise
- Finite processes taht if followed will solve the problem
- Algorithms are solutions

Abstraction:
- Allows us to view the problem and solution in such a way as to separate the so-called logical and physical perspectives
- Logical Perspective: Interface, The User
- Physical Perspective: "Under the Hood", The Programmer

- Procedural Abstraction:
  - We do not necessarily know how an operation is being performed but we know what the function is called and how to use it.
  - We describe the interface: the name of the funciton, what is needed(the parameters), and what will be returned. The details of the actual operation is hidden inside. 
'''

#1.4 ----------------- WHAT IS PROGRAMMING?

'''
Programming:
- Process of taking an algorithm and executing it by a computer
- Without an algorithm there can be no program

Data Types:
- Provide an interpretation for binary data so that we can think about the data in terms that make sense
- Primitive data types provide the building blocks for algorithm development
'''
#1.5 ----------------- WHY STUDY DATA STRUCTURES & ABSTRACT DATA TYPES?

'''
To manage the complexity of problems and the problem-solving process, computer scientists use abstractions to allow them to focus on the “big picture” without getting lost in the details.

Information Hiding: 
- By encapsulating the details of the implementation, we are hiding them from the user’s view

How an abstract data type operates:
- The user interacts with the interface, using the operations that have been specified by the abstract data type
- The abstract data type is the shell that the user interacts with
- The implementation is hidden one level deeper
- The user is not concerned with the details of the implementation

Data Structure: 
- The implementation of an abstract data type
- Requires a physical view of the data using some collection of programming constructs and primitive data types
'''

#1.6 ----------------- WHY STUDY ALGORITHMS?

'''
- We learn analysis techniques that allow us to compare and contrast solutions based solely on their own characteristics
- By considering a number of different algorithms, we can begin to develop pattern recognition so that the next time a similar problem arises, we are better able to solve it
- In the end, there are often many ways to solve a problem. Finding a solution and then deciding whether it is a good one are tasks that we will do over and over again
'''

#1.7 ----------------- REVIEW OF BASIC PYTHON

'''
Relational and Logical Operators

  less than < 
  greater than >
  less than or equal <=
  greater than or equal >=
  equal ==
  not equal !=
  and: Both operands True for result to be True
  or: One of the other operand is True for the result to be True
  not: Negates the truth value, False beomces True, True becomes False

Operations on Any Sequence

  indexing [] Access an element of a sequence
  concatenation + Combine sequences together
  repetition * Concatenate a repeated number of times
  membership in Ask whether an item is in a sequence
  length len Ask the number of items in the sequence
  slicing [:] Extract a part of a sequence
'''

'''Input and Output'''
# Example
user_radius = input("Please enter the radius of the circle ")
radius = float(user_radius)
diameter = 2 * radius
print(diameter)

'''Control Structures'''
'''
Algorithms require two important control structures: iteration and selection.
- Iteration: Python provides a standard WHILE statement and a very powerful FOR statement.
  - The While Statement: Repeats a body of code as long as a condition is true.
  - The For Statement: Used to iterate over the members of a colleciton, so long as the collection is a sequence
- Selection: Allow programmers to ask questions and then, based on the result, perform differenct actions.
  - if
  - else
  - elif
'''
# While Loop Example
counter = 1 
while counter <= 5:
  print("Hello, world")
  counter = counter + 1 
'''
Explanation: 
- The condition on the while statement is evaluated at the start of each repetition.
- If the condition is True, the body of the statement will execute. 
'''
# For Loop Example
for item in [1,3,6,2,5]:
  print(item)
'''
Explanation: 
- The variable iteam is assigned to be each successive value in the list [1,3,6,2,5]. 
- The body of the iteration is then executed
'''
# For Loop Example: Over a range of values
for item in range(5):
  print(item ** 2)
'''
Explanation:
- The statement will perfrom the print function five times. 
- The range funciton will return a range object representing the sequence 0,1,2,3,4 and each value will be assigned to the variable item.
- This value is then squared and printed
'''
# For Loop Example: Process each character of a string
word_list = ['cat', 'dog', 'fish']
letter_list = []
for a_word in word_list:
  for a_letter in a_word:
    letter_list.append(a_letter)
print(letter_list)
'''
Explanation:
- Iterates over a list of strings and for each string processes each character by appending it to a list.
- The result is a list of all the letters in all of the words.
'''
import timeit
import random
# 3.1 ----------------- OBJECTIVES

'''
To understand why algorithm analysis is important.

To be able to use “Big-O” to describe execution time.

To understand the “Big-O” execution time of common operations on Python lists and dictionaries.

To understand how the implementation of Python data impacts algorithm analysis.

To understand how to benchmark simple Python programs.
'''

# 3.2 ----------------- WHAT IS ALGORITHM ANALYSIS?

# def sumOfN(n):
#   theSum = 0
#   for i in range(1, n+1):
#     theSum = theSum + i
#     print(theSum)
#   return theSum

# print(sumOfN(10))

'''
Algorithm analysis is concerned with comparing algorithms based upon the amount of computing resources that each algorithm uses. 

We want to be able to consider two algorithms and say that one is better than the other because it is more efficient in its use of those resources or perhaps because it simply uses fewer. 


What does computing resources even mean??
  One way is to consider the amount of space or memory an algorithm requires to solve the problem.

  Another way is the “execution time” or “running time” of the algorithm.
'''

# 3.3 ----------------- BIG-O NOTATION

'''
When trying to characterize an algorithm’s efficiency in terms of execution time, independent of any particular program or computer, it is important to quantify the number of operations or steps that the algorithm will require. If each of these steps is considered to be a basic unit of computation, then the execution time for an algorithm can be expressed as the number of steps required to solve the problem. Deciding on an appropriate basic unit of computation can be a complicated problem and will depend on how the algorithm is implemented.


Order of Magnitude is better known as the Big-O Notation.


We characterize an algorithm's performance in terms of best case, worst case, or average case performance.

The worst case performance refers to a particular data set where the algorithm performs especially poorly. 
Whereas a different data set for the exact same algorithm might have extraordinarily good performance. 

However, in most cases the algorithm performs somewhere in between these two extremes (average case).
'''

# Big O Example

# a=5
# b=6
# c=10
# for i in range(n):
#   for j in range(n):
#       x = i * i
#       y = j * j
#       z = i * j
# for k in range(n):
#   w = a*k + 45
#   v = b*b
# d = 33

'''
Explanation:

The number of assignment operations is the sum of four terms. The first term is the constant 3, representing the three assignment statements at the start of the fragment. 

The second term is 3𝑛2, since there are three statements that are performed 𝑛2 times due to the nested iteration. 

The third term is 2𝑛, two statements iterated n times. 

Finally, the fourth term is the constant 1, representing the final assignment statement. 

This gives us 𝑇(𝑛)=3+3𝑛^2+2𝑛+1=3𝑛^2+2𝑛+4. 

By looking at the exponents, we can easily see that the 𝑛2 term will be dominant and therefore this fragment of code is 𝑂(𝑛2). 
Note that all of the other terms as well as the coefficient on the dominant term can be ignored as n grows larger.
'''

# 3.4 ----------------- AN ANAGRAM DETECTION EXAMPLE

# Our goal is to write a boolean function that will take two strings and return whether they are anagrams.

# 3.4.1 Solution 1: Checking Off

# def anagram_solution(s1, s2):
#   still_ok = True
#   if len(s1) != len(s2):
#     still_ok = False

  
#   a_list = list(s2)
#   pos1 = 0

#   while pos1 < len(s1) and still_ok:
#     pos2 = 0
#     found = False
#     while pos2 < len(a_list) and not found:
#       if s1[pos1] == a_list[pos2]:
#         found = True
#       else:
#         pos2 = pos2 + 1

#     if found:
#       a_list[pos2] = None
#     else:
#       still_ok = False

#     pos1 = pos1 + 1

#   return still_ok

# print(anagram_solution('nar', 'ran'))

'''
Explanation: 

Our first solution to the anagram problem will check the lengths of the strings and then to see that each character in the first string actually occurs in the second. 

If it is possible to “checkoff” each character, then the two strings must be anagrams. 

Checking off a character will be accomplished by replacing it with the special Python value None. 

However, since strings in Python are immutable, the first step in the process will be to convert the second string to a list. 

Each character from the first string can be checked against the characters in the list and if found, checked off by replacement.
'''

# 3.4.2 Solution 2: Sort and Change

# def anagram_solution_2(s1, s2):
#   a_list_1 = list(s1)
#   a_list_2 = list(s2)

#   a_list_1.sort()
#   a_list_2.sort()

#   pos = 0
#   matches = True

#   while pos < len(s1) and matches: 
#     if a_list_1[pos] == a_list_2[pos]:
#       pos = pos + 1
    
#     else:
#       matches = False
  
#   return matches

#   if len(a_list_1) == len(a_list_2):
#       return True
  
#   else:
#     return False

# print(anagram_solution_2('abcde', 'edcba'))

'''
Explanation: 
Another solution to the anagram problem will make use of the fact that even though s1 and s2 are different, they are anagrams only if they consist of exactly the same characters. 

So, if we begin by sorting each string alphabetically, from a to z, we will end up with the same string if the original two strings are anagrams

We use the built-in sort method on lists by simply converting each string to a list at the start.

Sorting is typically either 𝑂(𝑛2) or 𝑂(𝑛log𝑛), so the sorting operations dominate the iteration. In the end, this algorithm will have the same order of magnitude as that of the sorting process.
'''

# 3.4.3 Solution 3: Brute Force

'''
A brute force technique for solving a probelm typically tries to exhaust all possibilities.
'''

# 3.4.4 Solution 4: Count and Compare

def final_anagram_solution(s1, s2):
  c1 = [0] * 26
  c2 = [0] * 26

  for i in range(len(s1)):
    pos = ord(s1[i]) - ord('a')
    c1[pos] = c1[pos] + 1

  for i in range(len(s2)):
    pos = ord(s2[i]) - ord('a')
    c2[pos] = c2[pos] + 1

  j = 0
  still_ok = True

  while j < 26 and still_ok:
    if c1[j] == c2[j]:
      j = j + 1
    
    else:
      still_ok = False
  
  return still_ok

print(final_anagram_solution('apple', 'elapp'))


'''
Explanation:
This solution has a number of iterations. However, unlike the first solution, none of them are nested. 

The first two iterations (the for loops) used to count the characters are both based on n. 

The third iteration (the while loop), comparing the two lists of counts, always takes 26 steps since there are 26 possible characters in the strings. Adding it all up gives us 𝑇(𝑛)=2𝑛+26 steps. 

That is 𝑂(𝑛). We have found a linear order of magnitude algorithm for solving this problem.

---------------------------

Before leaving this example, we need to say something about space requirements. Although the last solution was able to run in linear time, it could only do so by using additional storage to keep the two lists of character counts. In other words, this algorithm sacrificed space in order to gain time.

This is a common occurrence. On many occasions you will need to make decisions between time and space trade-offs. In this case, the amount of extra space is not significant. However, if the underlying alphabet had millions of characters, there would be more concern. As a computer scientist, when given a choice of algorithms, it will be up to you to determine the best use of computing resources given a particular problem.
'''

# 3.5 ----------------- PERFORMANCE OF PYTHON DATA STRUCTURES

#  -----------------------------------------

# 3.6 ----------------- LISTS


# Time Complexity Example: Concatenation, Append, List Comprehension, Range Function Inside List Constructor

def test1():
  l = []
  for i in range(1000):
      l = l + [i]

def test2():
  l = []
  for i in range(1000):
      l.append(i)

def test3():
  l = [i for i in range(1000)]

def test4():
  l = list(range(1000))


t1 = timeit.Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = timeit.Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")
t3 = timeit.Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = timeit.Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")

'''
Name:             Time Complexity

Constant Time:    0(1)

Logarithmic Time: 0(log n)

Linear Time:      0(n)

Quasilinear Time: 0(n log n)

Quadratic Time:   0(n^2)

Exponential Time: 0(2^n)

Factorial Time:   0(n!)
'''

'''
Operation:         Big-O Efficiency

index[]:           O(1)
index assignment:  O(1)
append:            O(1)
pop():             O(1)
pop(i):            O(n)
insert(i, item):   O(n)
del operator:      O(n)
iteration:         O(n)
contains (in):     O(n)
get slice [x:y]:   O(k)
del slice:         O(n)
set slice:         O(n + k)
reverse:           O(n)
concatenate:       O(k)
sort:              O(n log n)
multiply:          O(nk)
'''

# 3.6 ----------------- DICTIONARIES

'''
Operation:        Big-O Efficiency

copy:             O(n)
get item:         O(1)
set item:         O(1)
delete item:      O(1)
contains (in):    O(1)
iteration:        O(n)
'''

# Comparing the performance of the contains operation between lists and dictionaries

for i in range(10000,1000001,20000):
  t = timeit.Timer("random.randrange(%d) in x"%i,
                  "from __main__ import random,x")
  # list
  x = list(range(i))       
  lst_time = t.timeit(number=1000)

  # dictionary
  x = {j:None for j in range(i)}
  d_time = t.timeit(number=1000)
  print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))

'''
Explanation:
List Time Complexity: O(n) 
Dictionary Time Complexity: O(1)

The bigger the list, the longer it takes to determine if any one number is contained in the list.
That does not apply for Dictionary 
'''

# 3.7 ----------------- SUMMARY

'''
Algorithm analysis is an implementation-independent way of measuring an algorithm.

Big-O notation allows algorithms to be classified by their dominant process with respect to the size of the problem.
'''
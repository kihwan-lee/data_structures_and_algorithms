#3.1 ----------------- OBJECTIVES

'''
To understand why algorithm analysis is important.

To be able to use “Big-O” to describe execution time.

To understand the “Big-O” execution time of common operations on Python lists and dictionaries.

To understand how the implementation of Python data impacts algorithm analysis.

To understand how to benchmark simple Python programs.
'''

#3.2 ----------------- WHAT IS ALGORITHM ANALYSIS?

def sumOfN(n):
  theSum = 0
  for i in range(1, n+1):
    theSum = theSum + i
    print(theSum)
  return theSum

print(sumOfN(10))

'''
Algorithm analysis is concerned with comparing algorithms based upon the amount of computing resources that each algorithm uses. 

We want to be able to consider two algorithms and say that one is better than the other because it is more efficient in its use of those resources or perhaps because it simply uses fewer. 


What does computing resources even mean??
  One way is to consider the amount of space or memory an algorithm requires to solve the problem.

  Another way is the “execution time” or “running time” of the algorithm.
'''

#3.3 ----------------- WHAT IS ALGORITHM ANALYSIS?

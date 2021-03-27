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

#3.3 ----------------- BIG-O NOTATION

'''
When trying to characterize an algorithm’s efficiency in terms of execution time, independent of any particular program or computer, it is important to quantify the number of operations or steps that the algorithm will require. If each of these steps is considered to be a basic unit of computation, then the execution time for an algorithm can be expressed as the number of steps required to solve the problem. Deciding on an appropriate basic unit of computation can be a complicated problem and will depend on how the algorithm is implemented.


Order of Magnitude is better known as the Big-O Notation.


We characterize an algorithm's performance in terms of best case, worst case, or average case performance.

The worst case performance refers to a particular data set where the algorithm performs especially poorly. 
Whereas a different data set for the exact same algorithm might have extraordinarily good performance. 

However, in most cases the algorithm performs somewhere in between these two extremes (average case).
'''

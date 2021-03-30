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

def anagram_solution_2(s1, s2):
  a_list_1 = list(s1)
  a_list_2 = list(s2)

  a_list_1.sort()
  a_list_2.sort()

  pos = 0
  matches = True

  while pos < len(s1) and matches: 
    if a_list_1[pos] == a_list_2[pos]:
      pos = pos + 1
    
    else:
      matches = False
  
  return matches

  # if len(a_list_1) == len(a_list_2):
  #     return True
  
  # else:
  #   return False

print(anagram_solution_2('abcde', 'edcba'))

'''
Explanation: 
Another solution to the anagram problem will make use of the fact that even though s1 and s2 are different, they are anagrams only if they consist of exactly the same characters. 

So, if we begin by sorting each string alphabetically, from a to z, we will end up with the same string if the original two strings are anagrams

We use the built-in sort method on lists by simply converting each string to a list at the start.

Sorting is typically either 𝑂(𝑛2) or 𝑂(𝑛log𝑛), so the sorting operations dominate the iteration. In the end, this algorithm will have the same order of magnitude as that of the sorting process.
'''
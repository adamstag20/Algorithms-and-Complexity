# CS 350: Homework 1
# Due: Week of 4/4
# Name: Adam Stagner 

# This homework is largely review, and to make sure you have a working version of python.

############################################################################
#
# Problem 1
# Find the largest two elements in a list.
# Return your answer in a tuple as (largest, secondLargest)
#
# Running Time: O(n)
#
############################################################################
import math
from pickle import TRUE
from re import A
import sys
from tkinter import W

def largest2(l):
    """
    >>> largest2([1, 2, 3, 4, 5, 6, 7])
    (7, 6)
    >>> largest2([7, 6, 9, 4, 9, 2, 1])
    (9, 7)
    """
    first = 0
    second = 0
    for i in range(len(l)):
        if ( first < l[i]):
            first = l[i]
    for i in range(len(l)):
        if ( second < l[i] and l[i] != first):
            second = l[i]
    mytuple = (first,second)
    print(mytuple)

    

############################################################################
#
# Problem 2
# Reverse a list in place,
# and returned the reversed list.
#
# Running Time: O(log(n))
############################################################################

def reverse(l):
    """
    >>> l = [1, 2, 3, 4, 5]
    >>> reverse(l)
    [5, 4, 3, 2, 1]
    >>> l
    [5, 4, 3, 2, 1]
    """
    front = 0
    end = len(l) - 1
    while ( front < end):
        temp = l[end]
        l[end] = l[front]
        l[front] = temp
        front = front + 1
        end = end - 1
    print(l)

############################################################################
#
# Problem 3
# Compute the transpose of a matrix in place.
#
# What is the input size measuring?
# Running Time: O(n^2)
############################################################################

def transpose(m):
    """
    >>> m = [[1,2,3],[4,5,6],[7,8,9]]
    >>> transpose(m)
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    >>> m
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    """
    size = len(m[0])

    for i in range(size):
        for j in range(i, size):
            hold = m[j][i]
            m[j][i] = m[i][j]
            m[i][j] = hold

    print(m)

############################################################################
#
# Problem 4
# Given a list of points, return the distance between the two closest points.
# The distance between two points (x1,y1) and (x2,y2) is:
# d = sqrt((x2-x1)^2 + (y2-y1)^2)
#
# Running Time: O(n^2) 
############################################################################

def pointDist(points):
    """
    >>> pointDist([(1,1), (4,5), (13,6)])
    5.0
    """
    """
    >>> pointDist([(1,1),(3,5),(3,2),(11,9),(11,2)])
    3.0
    """
    val = sys.maxsize
    for i in range(len(points)):
        for j in range(i+1,len(points)) :
                x = (points[j][0] - points[i][0])**2
                y = (points[j][1] - points[i][1])**2
                num = math.sqrt(x+y)
                if (val > num) :
                    val = num
    print(val)
        



############################################################################
#
# Problem 5
# multiply two matrices A and B.
# For the running time A is an m*n matrix, and B is an n*l matrix.
#
# what is the size of the output? ?*?
# Running Time: O(n^3 + n^2) ->  O(n^3)
############################################################################

def matMul(A,B):
    """
    >>> matMul([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
    [[58, 64], [139, 154]]
    """
    result = []

    for i in range(len(B[0])):
        mytuple = []
        for j in range(len(B[0])):
                mytuple = mytuple + [0,]
        result += [mytuple,]

    for m in range(len(A)):
        for n in range(len(B[0])):
           for l in range(len(B)):
               result[m][n] += A[m][l] * B[l][n]

    print(result)


############################################################################
#
# Problem 6
# Compute the number of 1s that would be in the binary representation of x
# for example: 30 = 11110 in base 2, and it has 4 1s.
#
# For full credit, you should assume that 
# arithmetic operations are *not* constant time.
# bitwise operations are constant time though.
#
# What is the input size?
# Running Time: O(n) 
############################################################################

def popcount(x):
    """
    >>> popcount(7)
    3
    >>> popcount(30)
    4
    >>> popcount(256)
    1
    """
    count = 0
    while (x):
        count += x & 1
        x >>= 1
    print(count)

############################################################################
#
# Problem 7
# compute the integer square root of x.
# This is the largest number s such that s^2 <= x.
#
# You can assume that arithmetic operations are constant time for this algorithm.
#
# What is the input size?
# Running Time: O(n)
############################################################################

def isqrt(x):
    """
    >>> isqrt(6)
    2
    >>> isqrt(121)
    11
    >>> isqrt(64)
    8
    """
    count = 0
    go = True 
    while (go == True ):
        if ( count ** 2 <= x):
            count += 1
        else :
            go = False
    print(count - 1)

############################################################################
#
# Problem 8: Word Search
#
# determine if string s is any where in the word grid g.
#
# for example s = "bats"
# g = ["abrql",
#      "exayi",
#      "postn",
#      "cbkrs"]
#
# Then s is in the word grid
#     [" b   ",
#      "  a  ",
#      "   t ",
#      "    s"]
#
# what is your input size?
# Running Time: O(n^3)
############################################################################

def wordSearch(word,grid):
    """
    >>> s = "bats"
    >>> g = ["abrql", "exayi", "postn", "cbkrs"]
    >>> wordSearch(s,g)
    True
    """
    columns = len(grid[0])
    rows = len(grid)
    for i in range(rows):
        for j in range(columns):
            if (grid[i][j] == word[0]):

                if (j >= len(word)-1):
                    count = 1
                    for k in range(1,len(word)): # check going left
                        if ( grid[i][j-k] != word[k]):
                            break
                        if ( grid[i][j-k] == word[k]):
                            count += 1
                        if (count == len(word)):
                            return True

                if ( i >= len(word)-1 and j >= len(word)-1):
                    count = 1
                    for k in range(1,len(word)): # check diagonal going left
                        if ( grid[i-k][j-k] != word[k]):
                            break
                        if ( grid[i-k][j-k] == word[k]):
                            count += 1
                        if (count == len(word)):
                            return True
                if ( i < len(word)-1 and j < len(word)-1):
                    count = 1
                    for k in range(1,len(word)): # check diagonal going down/right
                        if (grid[i+k][j+k] != word[k]):
                            break
                        if ( grid[i+k][j+k] == word[k]):
                            count += 1
                        if ( count == len(word)):
                            return True
                    count = 1
                    for k in range(count,len(word)): # check same row going right
                        if ( grid[i][j+k] != word[k]):
                            break
                        if ( grid[i][j+k] == word[k]):
                            count += 1
                        if (count == len(word)) :
                            return True
                    count = 1 
                    for k in range(count,len(word)): # check same column going down
                        if (grid[i+k][j] != word[k]):
                            break
                        if ( grid[i+k][j] == word[k]):
                            count += 1
                        if (count == len(word)) :
                            return True
                if ( i >= len(word)-1 and j < len(word)-1):
                    count = 1
                    for k in range(1,len(word)): # check diagonal going up/right
                        if (grid[i-k][j+k] != word[k]):
                            break
                        elif ( grid[i-k][j+k] == word[k]):
                            count += 1
                        if ( count == len(word)):
                            return True
                    count = 1
                    for k in range(1,len(word)): # check going up
                        if (grid[i-k][j] != word[k]):
                            break
                        elif ( grid[i-k][j] == word[k]):
                            count += 1
                        if ( count == len(word)):
                            return True
                    count = 1
                    for k in range(1,len(word)): # check going right
                        if (grid[i][j+k] != word[k]):
                            break
                        elif ( grid[i][j+k] == word[k]):
                            count += 1
                        if ( count == len(word)):
                            return True
            
    return False
                    
                    
                    



############################################################################
#
# Problem 9: Convex Hull
#
# In class we learned about the convex hull problem.
# We also learned that for any line segment on the convex hull,
# every other point will we on the same side of that line.
#
# Use this fact to write an algorithm to find all of the points in the convex hull.
#
# for example: [(1,1), (4,2), (4,5), (7,1)] are the points shown below
#
#    *
#
#    *
# *     *
#
# The convex hull is [(1,1), (4,5), (7,1)]
#    *
#   / \
#  /   \
# *-----*
#
# Running Time:  
# n^2 + n + 6
# O(n^2)
############################################################################

def convexHull(points):
    """
    >>> convexHull([(1,1),(4,2), (4,5), (7,1)])
    [(1, 1), (4, 5), (7, 1)]
    """
    holder = sys.maxsize
    position = 0
    hull = []
    for i in range(len(points)):
        if ( holder > points[i][1]):
            holder = points[i][1]
            position = i
        if (holder == points[i][1]):
            if (points[position][0] > points[i][0]):
                holder = points[i][0]
                position = i
    hull += [points[position],]



    decide = True
    for j in range(len(points)):
        decide = True
        a = points[j][1] - points[position][1]
        b = points[position][0] - points[j][0]
        c = (points[position][0]*points[j][1]) - (points[j][0]*points[position][1]) 
        for k in range(len(points)):
            if ( position != k and j != k):
                val = (a*points[k][0] ) + (b*points[k][1])
                if ( val <= c):
                    decide = False
        if (decide == True):
            position = j
            hull += [points[position],]
    print(hull)




############################################################################
#
# Problem 10: Running time
#
# Find the Theta time complexity for the following functions.
# If the problem is a summation, give a closed form first.
#
# 1. f(n) = n^2 + 2n + 1
#          O(n^2)


# 2. f(n) = sum(i=0, n, sum(j=0, i, 1) )
# 0, 1, 2, 3, 4,..,n
# f(n) =  n(n+1)/2 = n^2/2 + n/2 
#           O(n^2) 


# 3. f(n) = (n+1)! = n! + 1! 
#       O(n!)


# 4.  f(n) = sum(i=1, n, log(i))
#       f(n) = log(n!) 
        # O(n * log(n))
       

# 5. f(n) = log(n!)
        # O(n * log(n))

############################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()

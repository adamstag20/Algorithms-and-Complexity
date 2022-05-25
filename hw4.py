# CS 350: Homework 4
# Due: Week of 4/4
# Name: Adam Stagner

import sys

############################################################################
# Problem 1: Quicksort
# 
# implement quicksort described in class.
#
# Recurrence worst case:  2T (n/2) + n 
# Recurrence average case: T(n −1) + 1 + n
# Running time worst case: Theta(n^2)
# Running time average case: Theta(n*log(n))
# 
# When does the worst case happen? if our list is sorted in descending order and we
#sort it in ascending order or vice versa
############################################################################



def quicksort(l):
    """
    >>> quicksort([3,2,6,1,4])
    [1,2,3,4,6]
    >>> quicksort([5,4,3,2,1])
    [5,4,3,2,1]
    """
    low = 0
    high = len(l) -1
    sort(l, low, high)
    print(l)
    
def sort(l, low, high):
   
    if  low < high:
        pivot = swap(l, low, high)
        sort(l,low, pivot-1)
        sort(l,pivot+1,high)
    
    

def swap(l, low, high):
    
    pivot = l[high]
    key = low -1
    
    for i in range(low,high):
        if ( l[i] <= pivot) :
            key += 1
            (l[key],l[i]) = (l[i], l[key])
    (l[key+1],l[high]) = (l[high], l[key+1])
    return key+1
            
            
    
    

############################################################################
# Problem 2: maximum sublist sum
# 
# A sublist is a contiguous piece of a list
# [1,2,1] is a sublist of [4,1,2,1,3]
# but [1,2,3] isn't.
#
# the sum of a list is just adding all of the elements.
#
# compute the maximum sum of any sublist.
# For example:  [-2,1,-3,4,-1,2,1,-5,4]
# the maximum sublist is [4,-1,2,1] with a sum of 6
# 
# Running time: Theta(n)
############################################################################
def maxSublist(l):
    """
    >>> maxSublist([-2,1,-3,4,-1,2,1,-5,4])
    [4,-1,2,1]
    """
    total_max = 0
    start_max = 0
    position = 0
    start = 0
    end = 0
    
    for i in range(len(l)):
        #running total
        total_max += l[i]
        # if my start_max is less than total then start_max must be switched 
        if (start_max < total_max):
            start = position
            end = i # increment end so we know our ending point
            start_max = total_max
        # if total sum is negative we reset it and look for next max
        if total_max < 0:
            total_max = 0
            position = i +1
    list = []
    for i in range(start,end+1):
        list.append(l[i])
    print(list)


############################################################################
# Problem 3: Parenthesizing matrices.
# 
# If I multiply and m*l matrix A by an l*n matrix B
# That will take O(n*l*m) time to compute.
#
# If I include a n*o matrix C in this product
# Then I have the m*o matrix A*B*C.
# This is perfectly well defined, but I have a choice.
# Do I multiply (A*B)*C (giving a running time of:w
# n*l*m + n*m*o)
# or do i multiply A*(B*C) (giving a running time of l*m*o + n*l*o)
#
# Since matrix multiplication is associative, We will get the same answer.
#
# So, given a list of dimensions of matrices
# (for example [(n,l), (l,m), (m,o)])
# compute the fastest running time that we can do matrix multiplication in. 
#
# example [(3,5), (5,4), (4,7)]
# is 3*5*4 + 3*4*7 = 144
# 
# Running time: Theta(n^3)
############################################################################
def matrixParens(sizes):
    """
    >>> matrixParens([(3,5), (5,4), (4,7)])
    144
    """
    n = len(sizes)
    M = [[0 for x in range(n)] for y in range(n)]
    d = [0] * (n+1)   
    
    # Saving our multiplying values
    for i in range(0,n):
        if i == n-1:
            d[i] = sizes[i][0]
            d[i+1] = sizes[i][1]
        else:
            d[i] = sizes[i][0]
    n = len(d)
    M = [[0 for x in range(n)] for y in range(n)]
    #loop through range in d values       
    for i in range(1,n):
        #restricts range each time we go to new i value
        for j in range(0, n-i+1):
            f = j + i -1
            for k in range(i,f):
                # formula for finding different multplication values ref -> https://www.youtube.com/watch?v=prx1psByp7U
                current = M[i][k] + M[k+1][f] + d[i-1]*d[k]*d[f]
                M[i][j] = current
    min = sys.maxsize         
    for i in range(n):
        if ( M[i][n-1] < min and M[i][n-1] != 0):
            min = M[i][n-1]
        
    print(min)
            
            

############################################################################
# Problem 4: Convex Hull again!
# 
# Use the Divide and Conquer algorithm described in class to compute
# the convex hull of a set of points.
#
# Recurrence worst case:
# Recurrence average case:
# Running time worst case:
# Running time average case:
# 
# When does the worst case happen?
############################################################################

def convexHull(l):
    """
    >>> convexHull([(1,1), (4,2), (4,5), (7,1)])
    [(1, 1), (4, 5), (7, 1)]""
    """
    leftmost = l[0] #P1
    rightmost = l[len(l)-1] #P2
    top = []
    bottom = []
    a = rightmost[1] - leftmost[1]
    b = leftmost[0] - rightmost[0]
    c = leftmost[0]*rightmost[1] - rightmost[0]*leftmost[1]
    
    for i in range(1,len(l)-1):
       answer = a*l[i][0] + b*l[i][1]
       if (answer > c):
           bottom.append(l[i])
       else:
           top.append(l[i])
    convex = [leftmost,rightmost]
    add1 = solve_hull(top, leftmost,rightmost, True)
    add2 = solve_hull(bottom, leftmost,rightmost, False)
    convex += add1 + add2
    convex.sort()
    print(convex)

def solve_hull(l,l_most,r_most,boo):
    # t = x1y2 + x2y3 + x3y1 −(x2y1 + x3y2 + x1y3)
    to_return = [] 
    # Determine the farthest  point
    if (len(l) == 0):
        return []
    furthest = []
    if (boo == True):
        furthest = l[len(l)-1]
    else:
        furthest = l[0]
    #a = y2 −y1
    #b = x1 −x2
    #c = x1y2 −x2y1
    #p1p3 calculation
    a = furthest[1] - l_most[1]
    b = l_most[0] - furthest[0]
    c = l_most[0]*furthest[1] - furthest[0]*l_most[1]
    for i in range(len(l)):
        if a*l[i][0] + b*l[i][1] <= c:
            to_return.append(l[i])
            
    #p3p2 calculation
    a = r_most[1] - furthest[1]
    b = furthest[0] - r_most[0]
    c = furthest[0]*r_most[1] - r_most[0]*furthest[1]
    for i in range(len(l)):
       if a*l[i][0] + b*l[i][1] <= c:
            to_return.append(l[i])
    to_return = list(set(to_return))
    return to_return
            
        
         
        
             

############################################################################
# Problem 5: Recurrence relations
# 
# Give a closed form, and bit Theta for the following recurrence relations.
# If it's a divide and conquer relation, then you only need to give the Theta.
#
# a. Give the recurrence relation for Karatsuba's algorithm, and solve it.
#  We do 3 multiplcations taking half of n each time so...
#   T(n) = 3T(n/2) + O(n)
#   Theta(n*log(n))
# b. Give the recurrence relation for Strassen's algorithm, and solve it.
#  Involves 7 different multiplications which is 7T(n/2) being a divide and conquer problem
#  Theta(7log(n))
# c.
# T(1) = 1
# T(n) = T(n-1) + n
#      = T(n-2) + n-1 + n
#      = T(n-3) + n-2 + n-1 + n
#      = T(n-k) + kn - n
#       k = n - 1
#       n(n-1) - n
#       n^2 -n - n -> n^2 biggest term
#  Theta(n^2)
#  
# d. 
# T(1) = 1
# T(n) = 2T(n-2) + 1
#       = 2T(2T(n-3)-2) + 1
#       = 2T(2T(2T(n-4)+ 1) +1)+ 1
#       = 2^3T
# T(2) = 2 + 1 = 3
# T(3) = 6 + 1 = 7
# T(4) = 14 + 1 = 15
# CLOSED FORM  = 2^n - 1
# Theta(2^n)
############################################################################
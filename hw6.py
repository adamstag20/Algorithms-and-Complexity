
# CS 350: Homework 6
# Due: Week of 6/16
# Name:  Adam Stagner

import math
import sys

def machine(data, code):
    i = 0
    value = 0
    for instruction in code:
        if i >= len(data):
            raise Exception("Ran out of numbers")
        if instruction == "ADD":
            value += data[i]
            i += 1
        elif instruction == "MUL":
            value += data[i] * data[i+1]
            i += 2
        else:
            raise Exception("Illegal Instruction: " + instruction)
    if i < len(data):
        raise Exception("has leftover numbers")
    return value

###########################################################################
# Problem 1:
#
# I've constructed a new data processing language that I call addmul.
# It is a very simple language, programs in addmul consist of two instructions.
# ADD take a value from the data stream and adds it to the current total
# MUL takes the next two number from the current data stream, multiplies them together,
# and adds them to the total.
# That's it.
#
# Your job is to take the data stream (just a list of numbers), and determine
# the program that will produce the largest value.
#
# example:
# largetstProgram([2,3,5])
# should return
# ["ADD","MUL"]
# because this will return 17
# where ["MUL","ADD"] will return 11
# and ["ADD","ADD","ADD"] will return 10
#
# You can run your program by calling 
# machine([2,3,4], ["ADD","MULL]) 
# to run your program
#
# you can use
# machine(numbers, largestProgram(numbers))
# to test your algorithm on any list of numbers.
#
# running time:  Theta(n)
###########################################################################

def largestProgram(data):
    """
    >>> largestProgram([2,3,5])
    ["ADD", "MUL"]
    """
    result = []
    i = 0
    while i < len(data)-1:
        
        if i+2 == len(data)-1:
            hold1 = (data[i] * data[i+1]) + data[i+2]
            hold2 = data[i] + (data[i+1] * data[i+2])
            if hold1 > hold2:
                result.append("MUL")
                result.append("ADD")
                return result
            if hold2 > hold1:
                result.append("ADD")
                result.append("MUL")
                return result
            else:
                result.append("ADD")
                result.append("ADD")
                result.append("ADD")
                return result
        if data[i] * data[i+1] > data[i] + data[i+1]:
            result.append("MUL")
            i += 2
        else:
            result.append("ADD")
            i += 1
    if i + 1 == len(data):
        result.append("ADD")
    return result
            
        


###########################################################################
# Problem 2
#
# Implemnt the Floyd-Warshal algorithm from class
#
# For example, the adjacency matrix:
#    [ [  0, inf,  -2, inf], 
#      [  4,   0,   3, inf], 
#      [inf, inf,   0,   2], 
#      [inf,  -1, inf,   0] ]
# should give the distance matrix:
#    [ [  0,  -1,  -2,   0], 
#      [  4,   0,   2,   4], 
#      [  5,   1,   0,   2], 
#      [  3,  -1,   1,   0] ]
# 
#
# Running Time: Theta(n^3)
###########################################################################

def floyd(g):
    """
    >>> floyd([ [0, math.inf, -2, math.inf], [4, 0, 3, math.inf], [math.inf, math.inf, 0, 2], [math.inf, -1, math.inf, 0]])
    [ [  0,  -1,  -2,   0], [  4,   0,   2,   4], [  5,   1,   0,   2], [  3,  -1,   1,   0] ]
    """
    for w in range(len(g)):
        for u in range(len(g)):
            for v in range(len(g)):
                if (g[u][v] > g[u][w] + g[w][v]) and g[u][w] != math.inf and g[w][v] != math.inf:
                    g[u][v] = g[u][w] + g[w][v]
    for i in g:
        print(i)


###########################################################################
# Problem 3
#
# Congratulations! You know own a factory that cuts rods.
# Customers will pay a certain value for a length of rods
# for example
# rod length:  3  4  5  6   7
# price:       2  3  6  8  11
#
# You just received a rod of length d, 
# Write a function to determine the most efficient way to cut the rod
# to maximize the profit.
# You should return the maximum profit you can make.
#
# Running Time: Theta(n)
###########################################################################

def rods(weights, prices, d):
    """
    >>> rods([3,4,5,6,7], [2,3,6,8,11], 20)
    30
    """
    for i in range(len(weights)):
        if weights[i] == d:
            print(prices[i])
            return prices[i]
    
    amounts = [0] * len(weights)
    x = len(weights) -1
    while x >= 0:
        if d != 0 and d < weights[x]:
            d += weights[x+1]
            amounts[x+1] -= 1
            
        pos = d // weights[x]
        d = d - pos*weights[x]
        amounts[x] = pos
        x -= 1
    max_price = 0
    for i in range(len(amounts)):
        max_price += amounts[i] * prices[i]
        
    return max_price

############################################################################
# Problem 4: Parenthesizing matrices.
#
# This is the same problem as homework 4, problem 3,
# but this time I want you to do it in polynomial time using dynamic programmign.
# 
# If I multiply and m*l matrix A by an l*n matrix B
# That will take O(n*l*m) time to compute.
#
# If I include a n*o matrix C in this product
# Then I have the m*o matrix A*B*C.
# This is perfectly well defined, but I have a choice.
# Do I multiply (A*B)*C (giving a running time of n*l*m + n*m*o)
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

if __name__ == "__main__":
  import doctest
  doctest.testmod()
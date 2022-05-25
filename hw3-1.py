
# CS 350: Homework 3
# Due: Week of 4/18
# Name: ADAM STAGNER  

# for this homework, unless I'm asking you to sort a list,
# you are allowed to use the sorted function in Python.
# sorted takes a list, and returns a sorted copy of the list in Theta(n*log(n)) time.

############################################################################
#
# Problem 1
# Compute the largest gap between two numbers in a list.
#
# for example: gap([1,6,2,4,9]) == 3 because the gap between 6 and 9 is 3.
# The gap isn't 8 because even thought 9-1 is 8, there is a 4 in the middle
# of those numbers.
############################################################################
import sys


def gap(l):
    """
    >>> gap([1,6,2,4,9])
    3
    """
    pos = 0
    previous = 0
    
    # orders list smallest to largest O(n^2)
    for i in range(len(l)):
        hold = sys.maxsize
        for j in range(i,len(l)):
            if ( hold > l[j] and previous != l[j]):
                hold = l[j]
                pos = j
        previous = l[pos]
        l[pos],l[i] = l[i],l[pos]
    largest = 0
    for i in range(len(l) -1):
        hold = l[i+1]-l[i]
        if (hold > largest):
            largest = hold
    print(largest)

############################################################################
#
# Problem 2
# We can concatenate two numbers together to get a new number.
# for example: 44 concatenated with 55 = 4455
# We can concatenate a list of numbers by concatenating all the numbers.
# concat([1,2,55,3]) = 12553
#
# If we rearrange the list, we can get a different number.
# concat([2,55,1,3]) = 25513
#
# Write a function to find the largest value we can get from concatenating a list.
#
# Running Time: Theta(n^2) 
############################################################################
def concatenate(l):
    out = ""
    for x in l:
        out = out + str(x)
    return int(out)

def largestConcat(l):
    """
    >>> largestConcat([1,2,55,3])
    55321
    """
    cat = 0
    for i in range(len(l)):
        for j in range(i,len(l)):
            if l[i] < l[j]:
                l[i],l[j] = l[j], l[i]
    for i in range(len(l)):
        cat = int(str(cat) + str(l[i]))
    print(cat)


############################################################################
#
# Problem 3
# Write a function to return the number of unique elements in an array.
# for example the list [3,6,2,3,2,7,4] has 3 unique elements, 6, 7, and 4.
#
# Running Time: Theta(n) 
############################################################################
def numberUnique(l):
    """
    >>> numberUnique([3,6,2,3,2,7,4])
    3
    """
    l.sort()
    i = 0
    count = 0
    while i < len(l):
        
        if i == 0:
            if l[i] != l[i+1]:
                count += 1
                i += 1
            i += 1
        elif i + 1 == len(l):
            if l[i] != l[i-1]:
                count += 1
                i += 1
            i += 1
        elif l[i] != l[i-1] and l[i] != l[i+1]:
            count += 1
            i += 1
        else:
         i += 1
    print(count)
        
        
        
            
        
        

############################################################################
#
# Problem 4
# Implement insertion sort from class.
#
# Running Time: Theta(n^2) 
############################################################################
def insertionSort(l):
    """
    >>> insertionSort([3,6,2,5,1])
    [1,2,3,5,6]
    """
    for i in range(1, len(l)):
        check = l[i]
        for j in range((i -1), -1, -1):
            if (check < l[j]):
                l[j+1] = l[j]
                l[j] = check
    print(l)
        
            
        

############################################################################
#
# Problem 5
# Use the heap from last homework to sort an array.
#
# Running Time: 
# for each item in list we have to use O(log(n)) for either pushing or popping this would 
# mean we would have n* log(n)

# Theta(n*log(n))
############################################################################
def heapSort(n):
    """
    >>> heapSort([3,6,2,5,1])
    [1,2,3,5,6]
    """
    myHeap = Heap()
    for i in range(len(n)):
        myHeap.push(n[i])
    for i in range(len(n)):
        n[i] = myHeap.pop()
    print(n)
    
    
class Heap():
    def __init__(self):
        self.pos = 0
        self.arr = [0]

    def bubbleUp(self, value):

        while value // 2 > 0:
            #swap
            if self.arr[value] < self.arr[value // 2] :
                self.arr[value], self.arr[value // 2 ] =  self.arr[value // 2],self.arr[value]
            value = value // 2
    
    def bubbleDown(self, value):

        while (value * 2)<= self.pos:
            minimum = 0 # holds minimum child for swap comparison

            if (value * 2)+1 > self.pos: #no other child
                minimum = value * 2
            else:
                if self.arr[value*2] < self.arr[(value*2)+1]: #find smallest child
                    minimum = value * 2
                else:
                    minimum = (value * 2) +1
            #swap
            if self.arr[value] > self.arr[minimum]:
                self.arr[value], self.arr[minimum] =  self.arr[minimum],self.arr[value]

            value = minimum



    def push(self, x):
        
        self.arr.append(x)
        self.pos += 1
        self.bubbleUp(self.pos)
        

    def pop(self):
        root = self.arr[1]
        self.arr[1] = self.arr[self.pos]
        del self.arr[-1]
        self.pos -= 1
        self.bubbleDown(1)
        return(root)


if __name__ == "__main__":
    import doctest
    doctest.testmod()    
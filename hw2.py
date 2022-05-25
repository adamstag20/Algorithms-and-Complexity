
import copy
from ctypes import resize
from re import A
# CS 350: Homework 2
# Due: Week of 4/11
# Name: Adam Stagner 



#########################################3
# Problem 1:
#
# Find a pair with a given sum.
#
# input: a list of integers l, an integer s
# return None if this sum doesn't exist in the array.
# output: a pair of numbers (a,b) where a,b are in l, and a + b == s
# findSum([1,3,5], 8) returns (3, 5)
# 
# What data structure did you use?

# I used a Tuple because all I need to store is two numbers which is 
# easily done with a simple tuple data structure

# Running Time: 

# O(n^2)

#########################################3



def findSum(l, s):
    """
    >>> findSum([1,3,5], 8)
    (3, 5)
    >>> findSum([1,2,5], 8)
    None
    """
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if ( j != i):
                if ( l[i]+ l[j] == s):
                    summation = (l[i],l[j])
                    return summation
    print(None)


#########################################3
# Problem 2:
#
# Find the mode of a list of numbers.
# The mode of a list is the most commonly occurring number in the list.
#
# input: a list of integers l
# output: the mode of l.
# mode([1,2,3,3,4,5]) returns 3
# 
# What data structure did you use?

# I used a hash map for the first attempt giving me n^2 time
# I decided fot my final answer to use a list insteas which cut my time down

# Running Time: O(n)
#########################################3

def mode(l):
    """
    >>> mode([1,2,3,3,4,5])
    3
    """
    """ 
    class Number:
        def __init__(self, id, amount): 
            self.id = id
            self.amount = amount
    list = []
    for i in range(len(l)):
        list.append(Number(0,0))

    position = 0
    
    for i in range(len(l)):
        hit = 0
        for j in range(position):
            if (list[j].id == l[i]):
                list[j].amount += 1
                hit = 1
        if (hit == 0):
            list[position].id = l[i]
            list[position].amount += 1
            position += 1
    most = 0
    key = 0
    for i in range(position):
        if ( most < list[i].amount):
            most = list[i].amount
            key = list[i].id
    return key

    """
    highest = 0
    for i in range(len(l)):
        if (highest < l[i]):
            highest = l[i]
    
    list = []
    for i in range(highest+1):
        list.append(0)
    for i in range(len(l)):
        list[l[i]] += 1
    amount = 0
    key = 0
    for i in range(len(list)):
        if (amount < list[i]):
            amount = list[i]
            key = i
    return key

    
            

    






#########################################3
# Problem 3:
#
# We talked about a ring buffer in class
# A ring buffer has four methods
# pushFront(x)
# pushBack(x)
# popFront()
# popBack()
#
# Your job is to implement these four methods.
# We can't just use the list append method to resize the ring buffer.
# we might have front and back in the middle of the buffer,
# and append only adds new space at the end.
# for that reason, you're going to have to copy
# the array over to a bigger one manually.
#
# I've provided a malloc function to allocate a new array.
# You need to copy the old array into the new one
# but be sure to keep elements in the correct position
#
# For example if we have the buffer :
#
#     v back
# [3, 4, 1, 2]
#        ^ front
#
# and we were to resize it, then the new buffer should be
#     v back
# [3, 4, None, None, None, None, 1, 2]
#                                ^ front
#    
# pushFront Running Time: 
# O(n+n) for worst case because I would have to use copyleft and copyright if
# my array is full

# O(n)

# pushBack Running Time: 
# Again worst case I have to run both copy functions
# O(n)

# popFront Running Time: 
# O(1) direct access

# popBack Running Time: 
# O(n)
#########################################3

def malloc(size):
    return [None] * size

class RingBuffer():
    """
    >>> r = RingBuffer()
    >>> r.pushBack(3)
    >>> r.pushBack(4)
    >>> r.pushBack(5)
    >>> r.pushFront(2)
    >>> r.pushFront(1)
    >>> r.popFront()
    1
    >>> r.popBack()
    5
    >>> r.popBack()
    4
    >>> r.popBack()
    3
    >>> r.popBack()
    2

    """

    def __init__(self):
        self.size = 0
        self.body = []
        self.front = 0
        self.back = 0

    # This method isn't mandatory,
    # but I suggest you implement it anyway.
    # It will help to test this method on it's own.
    # Think carefully about what cases you can have with front and back.
    def resize(self):
        if (self.size == 0):
            self.size = 4
            self.body = malloc(self.size)
            return
        self.size *= 2
        self.body = malloc(self.size)
        self.front = self.size-self.front

    def copyleft(self,old_copy, position):

        hold = copy.deepcopy(self.front)
        for i in range(hold,len(self.body)):
            self.body[i] = old_copy[i-position]
        return

    def copyright(self,old_copy):

        for i in range(self.back):
            self.body[i] = old_copy[i]
        return 





    def pushFront(self, x):
        # Just beginning
        if (self.size == 0):
            self.resize()
            self.front = self.size - 1
            self.body[self.front] = x
            return
        
        #Front is full
        holder = copy.deepcopy(self.body)
        val = copy.deepcopy(self.front)
        if (self.front  == self.back):
            self.resize()
            spot = len(holder)-val
            self.front = len(self.body) - spot
            spot += val
            self.copyleft(holder, spot)
            self.copyright(holder)


        
        self.front -= 1
        self.body[self.front] = x
        
    def pushBack(self, x):

        if (self.size == 0):
            self.resize()
            self.body[self.back] = x
            self.back += 1
            self.front = self.size
            return

        old_copy = copy.deepcopy(self.body)
        old_front = copy.deepcopy(self.front)
        spot = len(old_copy) - old_front
        if ( self.back == self.front):
            self.resize()
            self.front = len(self.body) - spot
            spot += 2
            self.copyleft(old_copy,spot)
            self.copyright(old_copy)
        self.body[self.back] = x
        self.back += 1
            


    def popFront(self):
        value = None
        if ( self.front == self.size - 1 and self.body[self.front] == None ):
            value = copy.deepcopy(self.body[0])
            self.body[0] = None
            for i in range(0, self.back):
                self.body[i-1] = self.body[i]
                self.body[i]=None
            self.back -= 1
            return value
        value = copy.deepcopy(self.body[self.front])
        self.body[self.front] = None
        if(self.front == self.size-1):
            return value
        self.front += 1
        return value
        
    def popBack(self):
        value = None
        if ( self.back == 0 and self.body[self.back] == None):
            if (self.back == self.front):
                self.front += 1
            if (self.front == len(self.body)-1 and self.body[self.front] != None):
                value = copy.deepcopy(self.body[self.front])
                self.body[self.front] = None
                return value
                
            value = copy.deepcopy(self.body[self.front])
            self.body[self.front] = None
        if (self.back == 0):
            value = copy.deepcopy(self.body[self.back])
            self.body[self.back] = None
            return value
        self.back -= 1
        value = copy.deepcopy(self.body[self.back])
        self.body[self.back] = None
        return value
#########################################3
# Problem 4:
#
# We talked about a heap in class
# A heap is a data structure that has a constructor,
# a push method, and a pop method.
# Your job is to implement these methods in Python.
# I've given you the skeleton for the class,
# you need to fill it in.
# 
# 
# push Running Time: 
# worse case we switch up whole height of tree
# O(h) where h equals height of tree

# pop Running Time:   O(log n) because when we delete and traverse down we only compare 
# to the smallest child moving downward. Don't have to check every node
#########################################3

class Heap():
    """
    >>> h = Heap()
    >>> h.push(3)
    >>> h.push(2)
    >>> h.push(4)
    >>> h.push(1)
    >>> h.push(5)
    >>> h.pop()
    1
    >>> h.pop()
    2
    >>> h.pop()
    3
    >>> h.pop()
    4
    >>> h.pop()
    5
    """
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

# CS 350: Homework 5
# Due: Week of 5/9
# Name: Adam Stagner

# You should not assume anything about the data for these problems
# other than it's valid.
# Adjacency lists might not be in any particular order
# and graphs may not be connected.

############################################################################
#
# Problem 1
#
# write a function that returns the set of connected components 
# of an undirected graph g.
# g is represented as an adjacency list
# you should return a list of components, where each component is a list of vertices.
# Example g = [[1,2], [0,2], [0,1], [4], [3]]
# Should return a list of two components [[0,1,2],[3,4]]
#
# Running time?
# Theta(n^4)
############################################################################
from collections import deque
from re import A


def components(g):
    """
    >>> components([[1,2], [0,2], [0,1], [4], [3]])
    [[0, 1, 2], [3, 4]]
    """
    connected = []
    pos = 0
    for i in range(len(g)):
        connected,pos = search(g[i],i,connected,pos, g)
    print(connected)
        
def search(point, i, connected,pos,g):
    if ( i == 0 and point != None):
        connected = [[0]]
        for p in point:
            if p not in connected[pos]:
                connected[pos].append(p)
        return connected, pos
    else :
        check = 0
        for p in range(len(connected)):
            for w in point:
                if w in connected[p]:
                    check = 1
        if (check == 0):
            pos += 1
            connected.append([i])
        for p in point:
            if p not in connected[pos]:
                connected[pos].append(p)
    return connected, pos
                
        
        
        

############################################################################
#
# Problem 2
#
# write a function the returns True if, and only if, graph g is bipartite
# g is represented as an adjacency list
#
# Running time?
# Theta(n^2)
############################################################################
def bipartite(g):
    """
    >>> bipartite([[3,4,7], [3,5,6], [4,5,7], [0,1], [0,2], [1,2], [1], [0,2]])
    True
    """
    # Holds level of each node in the graph
    levels = [None] * len(g)
    parents = []
    pos = 0
    q = deque()
    # Load all vertices into a queue 
    for i in g:
         q.append(i)
    while q:
        v = q.popleft()
        for i in v:
            if i not in parents:
                parents.append(i)
                levels[i] = pos + 1
            else:
                if levels[i] == levels[pos]:
                    print(False)
                    return False
        pos += 1
    
    print(True)


############################################################################
#
# Problem 3
#
# write a function the returns True if, and only if, graph g is a forrest
# g is represented by a adjacency list.
#
# Running time?
# Theta(n^3)
############################################################################
def isForrest(g):
    """
    >>> isForrest([[1,2], [3,4], [5,6], [], [], [], []])
    True
    >>> isForrest([[1,2], [3,4], [5,4], [], [], []])
    False
    """
    stack = []
    parent = []
    pos = 0
    if g[0] != None:
        stack.append(pos)
        parent.append(0)
        
    while stack:
        w = stack.pop()
        for x in g[w]:
            if x not in parent:
                parent.append(x)
                stack.append(x)
            else:
                    print(False)
                    return False
    print(True)            
    return True

############################################################################
#
# Problem 4
#
# write a function to topologically sort the vertices of a directed graph d
# Assume d is an adjacency list.
#
# Running time?
# Theta(n^2) 
############################################################################
def topsort(d):
    """
    >>> topsort([[1, 2], [3], [3], []])
    [0, 1, 2, 3]
    """
    seen = [0] * len(d)
    stack = []
   
    # Loop through each vertex 
    for i in range(len(d)):
        if (seen[i] == 0):
            cont_top(i, seen,d,stack)
    # reverses order of stack because we want topological order
    stack = stack[::-1]
    print(stack)

def cont_top(i, seen, d, stack):
    
    seen[i] = 1
    #DFS 
    for x in d[i]:
        if seen[x] == 0:
            cont_top(x, seen, d,stack)
    stack.append(i) 
    
    
                    
            
    

############################################################################
#
# Problem 5
#
# write a function to determine the strongly connected components of digraph d.
# Just like the components example, you should return a list of strongly connected components.
#
# Running time?
# Theta(V+E)
############################################################################
def scc(d):
    """
    >>> scc([[1], [2], [0,3], [1,2], [3,5,6], [4], [7], [8], [6]])
    [[0, 1, 2, 3], [4, 5], [6, 7, 8]]
    """
    seen = [False] * len(d)
    stack = []
    scc = []
    
    #DFS search to set up Stack 
    for i in range(len(d)):
        if (seen[i] == False):
            cont_top(i, seen, d,stack)
    
    seen = [False] * len(d) # reset seen for DFS again
    
    #Reverse the graph
    d = reverse(d)
    while stack:
      w = stack.pop()
      if seen[w] == False:
            hold = []
            traverse(d,w, seen,hold)
            scc.append(hold)
    
    #Sort scc for eyeball appeal
    for i in range(len(scc)):
        scc[i].sort()       
    scc.sort()
    
    #ANSWER
    print(scc)
               
# Perform DFS on reversed graph for strong connections 
def traverse(d,x, seen,hold):
    seen[x] = True 
    for i in d[x]:
        if seen[i] == False:
            traverse(d,i,seen,hold)
    hold.append(x)
    
    
# Reverses the direction of the graph
def reverse(d):
        ans = [[] for _ in d]
        for i, l in enumerate(d):
            for x in l:
                ans[x].append(i)
        return ans 
                
            
            


############################################################################
#
# Problem 6
#
# a. What doe we need to change about BFS/DFS if we use an adjacency matrix?
#    how we track the parent node when we traverse through the graph. 
# b. What is the running time for BFS/DFS if we use and adjacency matrix?
#  Theta(V+E)
#
# c. Give an example of a weighted graph where BFS doesn't return the shortes path.
#  An example would be if a graph  had a path with fewer edges but super large weights
# the BFS algo would go down that path with the least amount of edges but it would create a big weighted
# sum making that traversal more expensive. But with a wieghted graph you want the LEAST expensive path. 
############################################################################
import math

################################################################
# Problem 1
# 
# We're going to take the job scheduling problem from class,
# but this time, I want to make sure every job is scheduled.
# If I have a set of n jobs where each job is represented
# by a tuple (s,f),
# Give a greedy algorithm to schdule the jobs on the fewest
# number of processors total
#
# Running Time:
# Theta(n^2)
################################################################



def schedule(jobs):
    """
    >>> schedule([(5,40), (30,35), (6,20), (19, 31), (23, 29), (28, 32)])
    [[(6, 20), (23, 29), (30, 35)], [(19, 31)], [(28, 32)], [(5, 40)]]
    """
    fewest = []
    seen = [False] * len(jobs)
    jobs.sort()
    for i in range(len(jobs)):
        concat = []
        if seen[i] == False:
            concat.append(jobs[i])
        for j in range(len(jobs)):
            if seen[i] == False and i != j:
                if jobs[j][0] > jobs[i][1]:
                        if seen[j] != True and concat[len(concat)-1][1] < jobs[j][0]:
                            concat.append(jobs[j])
                            seen[j] = True
        if len(concat) > 0:
            fewest.append(concat)
        seen[i] = True
    print(fewest)
        

################################################################
# Problem 2
# 
# Given a list of string (strings)
# Find s short string (bigstring) that 
# for every s in string, s is a substring of bigstring.
#
# Use the approximation algorithm we gave in class.
#
# Running Time: 
#
################################################################

def superstring(strings):
    """
    >>> superstring(["CADBC", "CDAABD", "BCDA", "DDCA", "ADBCADC"])
    'BCDAABDDCADBCADC'
    """
    counter = len(strings)
    while (counter != 1):
        max = 0
        pos1 = 0 # holds position of word in i loop
        pos2 = 0 # holds position of word in j loop
        resultant = []
        #loop through each word doing comparisons
        for i in range(counter):
            for j in range(i+1,counter):
                hold = []
                pot_max,hold = findOverlap(strings[0],strings[1],hold)
                if max < pot_max:
                    max = pot_max
                    resultant = hold
                    pos1 = i
                    pos2 = j
        counter -= 1
        # strings[0] is going to hold our superstring
        if max == 0:
            strings[0] = strings[0] + strings[counter]
        else:
            # move the words around for evaluation
            strings[pos1] = resultant
            strings[pos2] = strings[counter]
    print(strings[0])

def findOverlap(x,y,resultant):
    max = 0
    #checks slices of prefix of x to suffix of y
    for i in range(1,min(len(x),len(y))):
        if x[len(x)-i:] == y[:i]:
            if max < i:
                max = i
                resultant = x + y[i:]

    #checks slices of suffix of x to prefix of y
    for i in range(1,min(len(x),len(y))):
        if x[:i] == y[len(y)-i:]:
            if max < i:
                max = i
                resultant = y + x[i:]
    return max,resultant


################################################################
# Problem 3
# 
# Find the shortest path from a to b
# in a weighted graph g that is represented by an adjacency matrix.
# You can assume all edge weights are positive.
#
# Running time: Theta(n lg n + m),
################################################################


def dijkstra(g, a, b):
    """
    >>> g = [ [(1,3), (2,6)], \
              [(0,3), (4,4)], \
              [(0,6), (3,2), (5,7)], \
              [(2,2), (4,4), (8,1)], \
              [(1,4), (3,4), (6,9)], \
              [(2,7), (6,2), (7,8)], \
              [(4,9), (5,2), (9,4)], \
              [(5,8), (8,3)], \
              [(3,1), (7,3), (9,2)], \
              [(6,4), (8,2)] ]
    >>> dijkstra(g,0,9)
    [0, 2, 3, 8, 9]
    """
    seen = [False] * len(g)
    confirmed = []
    shortest = [math.inf] * len(g)
    previous = [0] * len(g)
    q = []

    shortest[a] = 0 # starting location

    #load in nodes to look at from starting node
    for i in g[a]:
        shortest[i[0]] = shortest[a] + i[1]
        previous[i[0]] = a
        q.append(i[0])
    seen[a] = True
    shortest[a] = 0 # starting location

    while q:
        pos = q.pop(0)
        if seen[pos] == False:
            find_short(g,pos, shortest, previous,q)
        seen[pos] = True
    print(shortest)
    print(previous)
    
    location = b
    while location != a:
        confirmed.append(previous[location])
        location = previous[location]
    confirmed.append(b)
    confirmed.sort()
    print(confirmed)
    
def find_short(g,position, shortest, previous,q):
    for i in g[position]:
        if shortest[i[0]] > shortest[position] + i[1]:
            shortest[i[0]] =shortest[position] + i[1] 
            previous[i[0]] = position
        q.append(i[0])





#if __name__ == "__main__":
  #  import doctest
   # doctest.testmod()
superstring(["CADBC", "CDAABD", "BCDA", "DDCA", "ADBCADC"])
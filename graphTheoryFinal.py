# wes ostlund
# MA430 Final Project

## connected - path from any vertex to any other vertex

# euler cycle - all vertices have even degree, graph is connected
# & contains all edges and vertices of graph

# Euler trail - graph must have exactly two odd degree vertices, 
# vetices may be repeated, edges may not be repeated, graph is connected
# doesn't have to start and end at the same vertex


#  Write a program that takes an adjacency matrix for a graph and does the following:
# a. Checks to see if the graph is connected
# b. Checks to see if the graph has an Euler cycle
# c. If it has an Euler cycle, find the actual cycle
# d. If it doesn’t have an Euler cycle, check to see if it has an Euler trail
# e. If it has an Euler trail, find the actual trail


# 0 - n vertices

# not connected
matrix = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
]

matrix2 = [ # square 
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 0]
]

matrix3 = [
    [0, ]
]

def is_connected(matrix): # DONE 
    n = len(matrix)
    visited = [False] * n

    # depth first search recursive function
    # argument: vertex to start from
    def dfs(v):
        visited[v] = True # add vertex to visited list
        for i in range(n): # iterate through all vertices
            if matrix[v][i] == 1 and not visited[i]: # if there is an edge between the current vertex and another vertex...
                dfs(i) # ...make recursive call, the next vertex is now added and the process continues

    dfs(0)  # Start DFS from the first vertex

    return all(visited) # built-in all function checks if all elements in the list are true - in which case the graph is connected

def has_euler_cycle(matrix): # DONE 
    oddDegreeCount = 0 # if a graph has any odd degree vertices, it does not have an euler cycle
    for row in matrix: # sum up degree of each vertex
        degree = sum(row)
        if degree % 2 != 0: # if degree is odd increment oddDegreeCount
            oddDegreeCount += 1
    return oddDegreeCount == 0 # if there are no odd degree vertices, the graph has an euler cycle

def has_euler_trail(matrix): # DONE
    oddDegreeCount = 0
    for row in matrix:
        degree = sum(row) # sum up degree of each vertex
        if degree % 2 != 0: # keep track of number of odd degree vertices
            oddDegreeCount += 1
    return oddDegreeCount == 2 # will return true if there are exactly two odd degree vertices

def find_euler_trail(matrix): # DONE
    n = len(matrix)
    stack = []
    trail = []

    def dfs(v):
        for i in range(n): # for every vertex
            if matrix[v][i] == 1: # if there is an edge between the current vertex and another vertex...
                matrix[v][i] = 0 # remove edge from graph
                matrix[i][v] = 0 # remove edge from other side of graph
                dfs(i)
        stack.append(v)

    # Start DFS from a vertex with odd degree
    start_vertex = next(i for i in range(n) if sum(matrix[i]) % 2 != 0)
    dfs(start_vertex)
    while stack:
        trail.append(stack.pop())
        
    return trail
    
        
def find_euler_cycle(matrix): # DONE 
    n = len(matrix)
    stack = [] # temporary stack to hold vertices during dfs
    cycle = [] # store final euler cycle

    def dfs(v):
        for i in range(n):
            if matrix[v][i] == 1:
                matrix[v][i] = 0
                matrix[i][v] = 0
                dfs(i)
        stack.append(v) # v is added to stack when all edges from v are used

    dfs(0)  # Start DFS from the first vertex

    while stack:
        cycle.append(stack.pop()) # stack contains vertices in reverse order, pop them off to get correct order from start to finish

    return cycle    # return final cycle


print("Connected: ", is_connected(matrix2))
print("Contains euler cycle:", has_euler_cycle(matrix2))
print("Euler cycle:", find_euler_cycle(matrix2))
print("contains euler trail:", has_euler_trail(matrix))
print("euler trail:", find_euler_trail(matrix))


## if graph is connected
## if graph has euler cycle, find cycle
## if no cycle, check for trail
# if has trail, find trail
## if no trail, print no euler cycle or trail
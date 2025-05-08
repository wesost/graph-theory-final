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



matrix = [ # e trail
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
]

matrix2 = [ # e cycle
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 0]
]

matrix3 = [ # no cycle no trail - not connected
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0]
]

matrix4 = [ # no cycle no trail - connected
    [0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
]

# list of matrices to iterate over and analyze
matrices = [matrix, matrix2, matrix3, matrix4]

# prints matrix out for conveinence
def print_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        print(matrix[i]) # print row
    print("\n") # go next line
            

# takes matrix, returns True if connected, False if not 
def is_connected(matrix): 
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

# takes a matrix and returns True if it has an euler cycle, False otherwise
def has_euler_cycle(matrix):
    oddDegreeCount = 0 # if a graph has any odd degree vertices, it does not have an euler cycle
    for row in matrix: # sum up degree of each vertex
        degree = sum(row)
        if degree % 2 != 0: # if degree is odd increment oddDegreeCount
            oddDegreeCount += 1
    return oddDegreeCount == 0 # if there are no odd degree vertices, the graph has an euler cycle

# takes matrix, return True if euler trail present, False otherwise
def has_euler_trail(matrix):
    oddDegreeCount = 0
    for row in matrix:
        degree = sum(row) # sum up degree of each vertex
        if degree % 2 != 0: # keep track of number of odd degree vertices
            oddDegreeCount += 1
    return oddDegreeCount == 2 # will return true if there are exactly two odd degree vertices

# Takes matrix, returns a list of vertices in order of euler trail
def find_euler_trail(matrix):
    n = len(matrix)
    stack = []
    trail = []

    def dfs(v):
        for i in range(n): # for every column (representing another vertex in relation to vertex v)
            if matrix[v][i] == 1: # if there is an edge between the current vertex (v) and another vertex (i)...
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
    
# takes matrix and returns list representing vertices in euler cycle
# uses recursive depth-first search starting from vertex 0 to construct stack
# which holds correct order of the vertices in the cycle
def find_euler_cycle(matrix):
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
        cycle.append(stack.pop()) # stack contains vertices in reverse order, pop them off to get correct order from where you started to finished
                                # (Order doesn't really matter here, cycle is valid either way)
    return cycle    # return final cycle

# given a matrix, print information on that matrix
# i.e. connected, has cycle or trail, print cycle or trail as case may be
def process_graph(matrix):
    print_matrix(matrix)
    if (is_connected(matrix)):
        print("Graph is connected")
        if has_euler_cycle(matrix):
            print("Graph has Euler cycle!")
            print("Cycle: ", find_euler_cycle(matrix), "")
        elif (has_euler_trail(matrix)):
            print("Graph has Euler trail!")
            print("Trail: ", find_euler_trail(matrix), "")
        else:
            print("Graph is connected but has neither Euler cycle nor Euler trail,")
            print("it must have exactly one, or more than two vertices with odd degree!")
            
    else: 
        print("Graph is not connected, so it does not have an Euler cycle or trail")
    print("-------------\n")

    
# test out all matrices
for m in matrices:
    process_graph(m)
    
# print_matrix(matrix3)
# print(find_euler_trail(matrix3))



# Old pseudocode
## if graph is connected
## if graph has euler cycle, find cycle
## if no cycle, check for trail
# if has trail, find trail
## if no trail, print no euler cycle or trail


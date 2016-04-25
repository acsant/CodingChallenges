# Enter your code here. Read input from STDIN. Print output to STDOUT
# read in the size of the NxN matrix
N = int(raw_input());
# G is the friends adjacency matrix
G = [];
# keep track of all the visited nodes
visited = [];
# of disjoin components
count = 0;

def explore(v):
    if not v in visited:
        visited.append(v);
        for u in range(N):
            if G[v][u] == 'Y':
                explore(u);

for i in range(N):
    # read each row of the matrix
    row = list(raw_input());
    # add the row to the graph
    G.append(row);
    
# now that we have the adjacency matrix, we treat each numnber as a node and the Y entries are the edges
# go through each node to find a component
for v in range(N):
    if not v in visited:
        explore(v);
        count += 1;
        
# final answer => number of disjoint components in the graph is the number of independent friend circles
print count;
           
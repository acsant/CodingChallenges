# Initialize infinity - used for the distance from node i to j where i and j are not connected
INF = float("infinity")
# Enter your code here. Read input from STDIN. Print output to STDOUT
NMCOUNT = raw_input().split(' ')
# Node count
N = int(NMCOUNT[0])
# Edge count
M = int(NMCOUNT[1])

# Node is a vertex in the graph. 
# A node can have 0 to N neighbors and there is a weight associated with each edge connecting the parent vertex to neighbors
class Node:
	def __init__(self, node):
		self.name = node
		self.neighbors = {}

	# Append a neighbor to the vertex
	def append_neighbor(self, neighbor, weight):
		self.neighbors[neighbor] = weight

	# Given a source vertex and its neighbor, figure out the weight
	def weight(self, neighbor):
		if neighbor in self.neighbors:
			return int(self.neighbors[neighbor])
		return INF

	# Print information about the node: For test purposes only
	def print_node(self):
		print self.name + ":"
		for node in self.neighbors:
			print node

# Graph is used to creating a directed graph with weights by adding vertices and edges that have a weight associated with them
class Graph:
	def __init__(self):
		self.nodes = {}

	# Add a vertex to the graph
	def add_node(self, node):
		if node not in self.nodes:
			to_add = Node(node)
			self.nodes[node] = to_add

	# Given two nodes and a weight, connect the nodes and attach the weight
	def build_from_nodes(self, nodes_weight):
		source = nodes_weight[0]
		to_dest = nodes_weight[1]
		weight = nodes_weight[2]
		# Add source
		self.add_node(source)
		# Add destination
		self.add_node(to_dest)
		# Connect the two
		self.nodes[source].append_neighbor(to_dest, weight)

	# Get the weight of an edge between a source and destination node given that there exists and edge between the two
	# and that edge should have a weight associated to it
	def weight(self, source, dest):
		return self.nodes[source].weight(dest)

	# Print the graph: For testing purposes only
	def test_graph(self):
		for node in self.nodes:
			self.nodes[node].print_node()

# Create a new graph
G = Graph()
# Go through the input and construct the graph from the input
for i in range(int(M)):
	# Read in the node a and node b along with the weight
	nodes_weight = raw_input().split(' ')
	# Add the two nodes and an edge with the given weight to the graph
	G.build_from_nodes(nodes_weight)

# Initialize the dist array
dist = [[INF for i in range(N+1)] for j in range(N+1)]
for i in range(1, int(N+1)):
	for j in range(1, int(N+1)):
		# For every vertex i and j, if there exists an edge between i and j, update the distacenace between i,j with the edge weight
		dist[i][j] = G.weight(str(i), str(j))

# Distance from a node to itself is always 0
for i in range(1, int(N+1)):
	dist[i][i] = 0

# Calculate the shortest distance from node i to node j using k intermediate vertices
# Given a vertex i and j, if we want to use DP to figure out the disatance between i and j, we assume
# that we have already calculated the solution for i,k where k < j. The we use that result and calculate the distance
# from node k to j. If the sum of the two is less than the distance between node i,j, update the distance.
for k in range(1, int(N+1)):
	for i in range(1, int(N+1)):
		for j in range(1, int(N+1)):
			# The explanation above gives us the following recurrence
			if dist[i][k] + dist[k][j] < dist[i][j]:
				dist[i][j] = dist[i][k] + dist[k][j]

# Now that we have a dynamically calculated distance array, we know the shortest distance from any given source vertex to any given
# destination vertex. Now any of the queries can be answered in O(1) time.
Q = int(raw_input())

for i in range(Q):
	# Read in the querried vertices
	vertices = raw_input().split(' ')
	# Extract the source vertex and the destination vertex from the querried vertices
	source = int(vertices[0])
	destination = int(vertices[1])
	# Use the calculated distance array to get the shortest distance from the source vertex to the destination vertex
	distance = dist[source][destination]
	# If there is no way to get from node i to j, then we print -1
	if distance == INF:
		print -1
	else:
		print distance

# The overall time complexity of this algorithm is dominated by the 
# preprocessing step (Dynamically calculating the distance array). This is
# done in O(N^3). Querying the distance is then done in constant time. So, N
# queries can be answered in O(N). So, the overall time complexity is O(N^3).

#include <iostream>
#include <sstream>
#include <map>
#include <vector>

// Initialize infinity - used for the distance from node i to j where i and j are not connected
// Max weight = max weight for one edge times the number of edges.  Max # of edges is in O(N^2) in complete graphs
#define INF 350*400*400
// Testing flag
//#define TESTING

using namespace std;

// Number of edges
int N;
// Number of nodes
int M;
// Distance array to store the dynamically calculated solutions
int** dist;
// Number of performed queries
int Q;
// Length of shortest path
int _distance;

// This is the structure of the graph
map<int, vector<pair<int, int>>> _graph = map<int, vector<pair<int, int>>>();

// Testing purposes - Prints the graph
void printGraph() {
    for(map<int, vector<pair<int, int>>>::iterator it = _graph.begin(); it != _graph.end(); it++) {
        cout << it->first << ": " << endl;
        vector<pair<int, int>> neighbor = it->second;
        for (int i = 0; i < neighbor.size(); i++) {
            cout << neighbor[i].first << endl;
        }
    }
}

int main(int argc, char *argv[]) {
    string inputLine;
    stringstream inputStream;
    int source, destination, weight;

    // Read in the number of nodes and edges
    getline(cin, inputLine);
    inputStream << inputLine;
    inputStream >> N;
    inputStream >> M;

    // Initialize the dist array
    dist = new int*[N+1];
    for (int i = 0; i < N+1; i++) {
        dist[i] = new int[N+1];
        for (int j = 0; j < N+1; j++) {
            // Distance from a vertex to itself is always 0 else INF (assume not reachable in beginning)
            dist[i][j] = i == j ? 0 : INF;
        }
    }

    // Go through the input and construct the graph from the input
    for (int i = 0; i < M; i++) {
        inputStream.clear();
        // Read in the source and destination node with the edge weight
        getline(cin, inputLine);
        inputStream << inputLine;
#ifdef TESTING
        cout << "Read in: " << inputLine << endl;
#endif
        inputStream >> source;
        inputStream >> destination;
        inputStream >> weight;

        // If the vertex is already added, attach the neighbor and assign the corresponding weight to it
        if (_graph.find(source) != _graph.end()) {
            _graph[source].push_back(pair<int, int>(destination, weight));
        } else {
            vector<pair<int, int>> elem = vector<pair<int, int>>();
            elem.push_back(pair<int, int>(destination, weight));
            _graph[source] =  elem;
        }
        // Store the weight as distance from source to destination since there exists an edge from source
        // to destination with weight (weight)
        dist[source][destination] = weight;
    }

#ifdef TESTING
    printGraph();
#endif

    // Calculate the shortest distance from node i to node j using k intermediate vertices
    // Given a vertex i and j, if we want to use DP to figure out the disatance between i and j, we assume
    // that we have already calculated the solution for i,k where k < j. The we use that result and calculate the distance
    // from node k to j. If the sum of the two is less than the distance between node i,j, update the distance.

    for (int k = 1; k <= N; k++) {
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                // The explanation above gives us the following recurrence
                if (dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }

    inputStream.clear();
    getline(cin, inputLine);
    inputStream << inputLine;
    inputStream >> Q;
    // Go through all the queries
    while (Q > 0) {
        inputStream.clear();
        getline(cin, inputLine);
        inputStream << inputLine;
        // Get start vertex
        inputStream >> source;
        // Get ending vertex
        inputStream >> destination;
        // Query the distance
        // Print -1 if not reachable
        _distance = dist[source][destination] == INF ? -1 : dist[source][destination];
        cout << _distance << endl;
        Q--;
    }

    return 0;
}
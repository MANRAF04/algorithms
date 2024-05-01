#include <fstream>
#include <iostream>
#include <list>
#include <queue>
#include <vector>

using namespace std;

class Graph {
public:
  int V;
  vector<list<int>> adjList;

  Graph(int vertices) {
    V = vertices;
    adjList.resize(V);
  }

  void addEdge(int u, int v) {
    // Add edge in both directions for non-directed graph
    cout << u << " " << v << endl;
    adjList[u].push_back(v);
    adjList[v].push_back(u);
  }

  void printGraph() {
    cout << "Adjacency List:" << endl;
    for (int i = 0; i < V; i++) {
      cout << "Vertex " << i << ": ";
      for (int neighbor : adjList[i]) {
        cout << neighbor << " ";
      }
      cout << endl;
    }
  }

  bool isConnected() {
    vector<bool> visited(V, false);

    // Find a non-visited vertex and start DFS from it
    int start;
    for (int v = 0; v < V; v++) {
      if (!visited[v]) {
        start = v;
        break;
      }
    }

    DFS(start, visited);

    // Check if all vertices were visited
    for (int v = 0; v < V; v++) {
      if (!visited[v]) {
        return false;
      }
    }

    return true;
  }

  void DFS(int u, vector<bool> &visited) {
    visited[u] = true;
    for (int neighbor : adjList[u]) {
      if (!visited[neighbor]) {
        DFS(neighbor, visited);
      }
    }
  }

  int BFS(int start, int end) {
    vector<bool> visited(V, false);
    vector<int> parent(V, -1);
    int length = 0;

    queue<int> q;
    q.push(start);
    visited[start] = true;

    while (!q.empty()) {
      int u = q.front();
      q.pop();

      if (u == end) {
        // Path found, backtrack to reconstruct
        // cout << "Shortest Path: ";
        int v = u;
        while (v != -1) {
          // cout << v << " -> ";
          v = parent[v];
          length++;
        }
        // cout << endl;
        return length;
      }

      for (int neighbor : adjList[u]) {
        if (!visited[neighbor]) {
          visited[neighbor] = true;
          parent[neighbor] = u;
          q.push(neighbor);
        }
      }
    }

    cout << "No path found between " << start << " and " << end << endl;
    return -1;
  }
};

int main(int argc, char **argv) {
  Graph g(1);

  if (argc != 2) {
    cout << "Wrong number of arguements!\n./main [edgefile]\n";
    return 1;
  }
  ifstream inputFile("/home/manraf/Desktop/HMMY/algorithms/project/src/" +
                     string(argv[1]));
  int u, v;
  int maxVertex = 0;
  while (inputFile >> u >> v) {
    // cout << u << " " << v << endl;
    maxVertex = max(maxVertex, max(u, v));
  }
  g.V = maxVertex;
  g.adjList.resize(g.V);

  inputFile.clear();
  inputFile.seekg(0, ios::beg);

  while (inputFile >> u >> v) {
    g.addEdge(static_cast<int>(u) - 1, static_cast<int>(v) - 1);
  }
  inputFile.close();

  g.printGraph();
  // if (g.isConnected()) {
  //   cout << "The graph is connected" << endl;
  // } else {
  //   cout << "The graph is not connected" << endl;
  // }

  // cout << "Lenght is:\t" << g.BFS(1, 4) << endl;

  return 0;
}

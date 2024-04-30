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
    adjList[u].push_back(v);
    adjList[v].push_back(u);    // Add edge in both directions for non-directed graph
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

  void BFS(int start, int end) {
    vector<bool> visited(V, false);
    vector<int> parent(V, -1);

    queue<int> q;
    q.push(start);
    visited[start] = true;

    while (!q.empty()) {
      int u = q.front();
      q.pop();

      if (u == end) {
        // Path found, backtrack to reconstruct
        cout << "Shortest Path: ";
        int v = u;
        while (v != -1) {
          cout << v << " -> ";
          v = parent[v];
        }
        cout << endl;
        return;
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
  }
};

int main() {
  int V = 6;
  Graph g(V);
  g.addEdge(0, 1);
  g.addEdge(0, 2);
  g.addEdge(1, 2);
  g.addEdge(1, 3);
  g.addEdge(2, 4);
  // Comment out the line below to create a disconnected graph
  // g.addEdge(3, 4);
  // g.addEdge(3, 5);

  if (g.isConnected()) {
    cout << "The graph is connected" << endl;
  } else {
    cout << "The graph is not connected" << endl;
  }

  g.BFS(0, 5);

  return 0;
}

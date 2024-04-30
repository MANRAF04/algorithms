import networkx as nx
import matplotlib.pyplot as plt

edges = [(1, 2), (2, 3), (3, 1), (3,4), (1,5)]

def getNetworkEdges(filename):
  value_counts = {}  # Dictionary to store value counts
  tuples = []
  try:
    with open(filename, 'r') as file:
      lines = file.readlines()
      for line in lines:
        # Split the line into words and remove trailing whitespace
        words = line.strip().split()
        edge = tuple(words)
        tuples.append(edge)
        
        # Update value counts for each element in the edge
        value_counts[int(edge[0])] = value_counts.get(int(edge[0]), 0) + 1
        value_counts[int(edge[1])] = value_counts.get(int(edge[1]), 0) + 1
  except FileNotFoundError:
    print(f"Error: File {filename} not found.")
  return tuples,value_counts

filename0 = "my_edges.txt"
testEdges,testNodeCounts =  getNetworkEdges(filename0)
filename1 = "karateedges.txt"
karateEdges,karateNodeCounts =  getNetworkEdges(filename1)
filename2 = "erdos_coauthors.txt"
erdosEdges,erdosNodeCounts =  getNetworkEdges(filename2)
filename3 = "USA.txt"
usaEdges,usaNodeCounts =  getNetworkEdges(filename2)

print(karateNodeCounts)
# print(edgeMap)
G = nx.Graph()
G.add_edges_from(karateEdges)

def analyzeGraph(G):
  global karateNodeCounts
  
  edges = G.edges()
  S = [G]
  
  #if G.number_of_nodes() == 1:
  #  return
  
  while len(S) == 1:
    edgeMap = dict((edge,0) for edge in edges)
    cpl = nx.average_shortest_path_length(G)
    print("This is the cpl:", cpl)
    print(karateNodeCounts)
    for edge in edgeMap:
        edgeMap[edge] = karateNodeCounts[int(edge[0])] + karateNodeCounts[int(edge[1])]
    
    # print(edgeMap)
    # sp = dict(nx.shortest_path(G))
    # print(sp)
    # for node in sp:
    # #   print(sp[node])
    #   for target in sp[node]:
    #     if target == node:
    #       # print("yeah!")
    #       continue
    #     pairs = []
    #     for i in range(0, len(sp[node][target]) - 1):
    #         # Access elements with a step of 2 to create pairs
    #         pairs.append((sp[node][target][i], sp[node][target][i + 1]))
    #     # print(pairs)
    #     for edge in pairs:
    #       if edge in edgeMap:
    #         edgeMap[edge] += 1
    #       else:
    #         edgeMap[edge[::-1]] += 1
        
    # Sort edges by their responding value in edgeMap without saving the value
    sortedEdges = sorted(edgeMap, key=edgeMap.get, reverse=True)
    mostcomedge = sortedEdges[0]
    karateNodeCounts[int(mostcomedge[0])] -= 1
    karateNodeCounts[int(mostcomedge[1])] -= 1
    edges = sortedEdges[1::]
    G.remove_edge(*mostcomedge)
    # G.remove_edge(2,3)
    print("most common connection",mostcomedge)

    S = [G.subgraph(c).copy() for c in nx.connected_components(G)]
  # print("The resulted edgemap", edgeMap, "\nThe resulted edges", edges)
  for graph in S:
    # print("\nWe use this graph:",graph)
    if graph.number_of_nodes() == 1:
      continue
    nx.draw(graph, with_labels=True, font_weight='bold')
    plt.show()
    analyzeGraph(graph)
  
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
analyzeGraph(G)
